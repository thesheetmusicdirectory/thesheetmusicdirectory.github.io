const express = require('express');
const fetch = require('node-fetch');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const YOUTUBE_API_KEY = 'AIzaSyCkfS4m8Vc_KRosj3uvbn3-xQhU12dSA1U';
const EMAIL_USER = 'mattialobrano@gmail.com';
const EMAIL_PASS = 'sbti ymaz mgwb obew'; // Your app password
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
app.use(bodyParser.json());
const path = require('path');
app.use(express.static(path.join(__dirname)));

// Helper: Get YouTube video details
async function getYouTubeDetails(videoId) {
  const url = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${YOUTUBE_API_KEY}`;
  const res = await fetch(url);
  const data = await res.json();
  if (data.items && data.items.length > 0) {
    return data.items[0].snippet;
  }
  return null;
}

// Helper: Send email
async function sendEmail(subject, html) {
  let transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: EMAIL_USER,
      pass: EMAIL_PASS,
    },
  });

  await transporter.sendMail({
    from: EMAIL_USER,
    to: EMAIL_TO,
    subject,
    html,
  });
}

// API endpoint
app.post('/submit', async (req, res) => {
  try {
    const { youtubeUrl, bpm, totalBeats } = req.body;
    const videoId = youtubeUrl.split('v=')[1]?.split('&')[0];
    if (!videoId) return res.status(400).send('Invalid YouTube URL');

    const details = await getYouTubeDetails(videoId);
    if (!details) return res.status(404).send('Video not found');

    const html = EMAIL_HTML_TEMPLATE
      .replace('{{title}}', details.title)
      .replace('{{description}}', details.description)
      .replace(/{{videoLink}}/g, youtubeUrl)
      .replace('{{bpm}}', bpm || 'Not provided')
      .replace('{{totalBeats}}', totalBeats || 'Not provided');

    await sendEmail(EMAIL_SUBJECT, html);

    res.send('Submission received!');
  } catch (err) {
    console.error(err);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));