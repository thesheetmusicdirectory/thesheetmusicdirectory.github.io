// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBhxOdAM-H60JHZDPc0dQsusi2MFwfJAYA",
    authDomain: "the-sheet-music-directory.firebaseapp.com",
    projectId: "the-sheet-music-directory",
    storageBucket: "the-sheet-music-directory.firebasestorage.app",
    messagingSenderId: "234404899204",
    appId: "1:234404899204:web:0f0ff67287b26d01ab15d1",
    measurementId: "G-1T2PKFCRXX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);