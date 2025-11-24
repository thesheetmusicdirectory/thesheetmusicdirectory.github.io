// Firebase Configuration (v8 SDK - Namespaced)
// This matches the Firebase SDK version loaded in the HTML files
const firebaseConfig = {
    apiKey: "AIzaSyBhxOdAM-H60JHZDPc0dQsusi2MFwfJAYA",
    authDomain: "the-sheet-music-directory.firebaseapp.com",
    projectId: "the-sheet-music-directory",
    storageBucket: "the-sheet-music-directory.firebasestorage.app",
    messagingSenderId: "234404899204",
    appId: "1:234404899204:web:0f0ff67287b26d01ab15d1",
    measurementId: "G-1T2PKFCRXX"
};

// Initialize Firebase (v8 syntax)
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();
