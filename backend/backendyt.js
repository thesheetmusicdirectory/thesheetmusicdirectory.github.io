// Load environment variables from .env file
require('dotenv').config();

const express = require('express');
const fetch = require('node-fetch');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const cors = require('cors'); // NEW: Import CORS middleware
const path = require('path'); // Added for express.static

// Retrieve sensitive information from environment variables
const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;
const EMAIL_PASS = process.env.EMAIL_PASS; // Your Gmail App Password
const EMAIL_USER = 'mattialobrano@gmail.com'; // This email should be configured for app passwords if using Gmail
const EMAIL_TO = 'theguitardirectory@gmail.com';
const EMAIL_SUBJECT = 'New YouTube Submission';
const EMAIL_HTML_TEMPLATE = `
  <h2>New YouTube Submission</h2>
  <p><b>Title:</b> {{title}}</p>
  <p><b>Description:</b> {{description}}</p>
  <p><b>Video Link:</b> <a href="{{videoLink}}">{{videoLink}}</a></p>
  <p><b>BPM:</b> {{bpm}}</p>
  <p><b>Total Beats:</b> {{totalBeats}}</p>
`;

const app = express();

// NEW: Configure CORS to allow requests from your GitHub Pages domain
app.use(cors({
    origin: 'https://theguitardirectory.github.io' // IMPORTANT: This must be your exact GitHub Pages domain
}));

app.use(bodyParser.json());

// Serve static files from the current directory (though not used for the backend API directly)
app.use(express.static(path.join(__dirname)));

// Helper: Get YouTube video details
async function getYouTubeDetails(videoId) {
  // Ensure API key is available
  if (!YOUTUBE_API_KEY) {
    console.error("YOUTUBE_API_KEY is not defined in environment variables.");
    return null;
  }
  const url = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${YOUTUBE_API_KEY}`;
  try {
    const res = await fetch(url);
    const data = await res.json();
    if (data.items && data.items.length > 0) {
      return data.items[0].snippet;
    }
  } catch (error) {
    console.error("Error fetching YouTube details:", error);
  }
  return null;
}

// Helper: Send email
async function sendEmail(subject, html) {
  // Ensure email credentials are available
  if (!EMAIL_USER || !EMAIL_PASS || !EMAIL_TO) {
    console.error("Email credentials (EMAIL_USER, EMAIL_PASS, EMAIL_TO) are not fully defined.");
    return;
  }

  let transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: EMAIL_USER,
      pass: EMAIL_PASS, // This is your Gmail App Password
    },
  });

  try {
    await transporter.sendMail({
      from: EMAIL_USER,
      to: EMAIL_TO,
      subject,
      html,
    });
    console.log("Email sent successfully!");
  } catch (error) {
    console.error("Error sending email:", error);
    // Log more details for debugging Nodemailer errors
    if (error.responseCode) {
        console.error("Nodemailer response code:", error.responseCode);
        console.error("Nodemailer response:", error.response);
    }
  }
}

// NEW: Root GET route for checking if the backend is alive
app.get('/', (req, res) => {
    res.send('YouTube Submission Backend API is running!');
});

// API endpoint for YouTube video submission
app.post('/submit', async (req, res) => {
  try {
    const { youtubeUrl, bpm, totalBeats } = req.body;

    // Basic URL validation and video ID extraction
    const videoIdMatch = youtubeUrl.match(/(?:https?:\/\/)?(?:www\.)?(?:m\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=|embed\/|v\/|)([\w-]{11})(?:\S+)?/);
    const videoId = videoIdMatch ? videoIdMatch[1] : null;

    if (!videoId) {
      return res.status(400).send('Invalid YouTube URL provided.');
    }

    const details = await getYouTubeDetails(videoId);
    if (!details) {
      return res.status(404).send('Video details not found for the provided URL.');
    }

    const html = EMAIL_HTML_TEMPLATE
      .replace('{{title}}', details.title || 'No Title')
      .replace('{{description}}', details.description || 'No Description')
      .replace(/{{videoLink}}/g, youtubeUrl)
      .replace('{{bpm}}', bpm || 'Not provided')
      .replace('{{totalBeats}}', totalBeats || 'Not provided');

    await sendEmail(EMAIL_SUBJECT, html);

    res.send('Submission received and email sent successfully!');
  } catch (err) {
    console.error("Error in /submit endpoint:", err);
    res.status(500).send('An internal server error occurred during submission.');
  }
});

// Use the PORT environment variable provided by Render, or default to 3000
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
