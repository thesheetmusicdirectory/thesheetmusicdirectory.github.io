# Firebase Setup Guide

To complete the integration of "Sign in with Google" and cloud storage, you need to set up a Firebase project and update the configuration file.

## Step 1: Create a Firebase Project
1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Click **"Add project"**.
3. Enter a name (e.g., "Sheet Music Directory") and follow the steps.
4. You can disable Google Analytics for this project if you want to keep it simple.

## Step 2: Register Your App
1. In the project overview page, click the **Web icon** (</>) to add a web app.
2. Give it a nickname (e.g., "Web App").
3. Click **"Register app"**.
4. You will see a code block with `firebaseConfig`. **Keep this page open** or copy the config object.

## Step 3: Enable Authentication
1. In the left sidebar, click **"Build"** > **"Authentication"**.
2. Click **"Get started"**.
3. Select **"Google"** from the Sign-in method list.
4. Click **"Enable"**.
5. Select a support email for the project.
6. Click **"Save"**.

## Step 4: Enable Firestore Database
1. In the left sidebar, click **"Build"** > **"Firestore Database"**.
2. Click **"Create database"**.
3. Choose a location (e.g., `nam5 (us-central)` or one close to you).
4. Start in **Test mode** (for development) or **Production mode**.
   - **Recommended for now:** Start in **Test mode** so you can write data without complex rules immediately. You can update rules later.
5. Click **"Create"**.

## Step 5: Update Configuration
1. Open the file `js/firebase-config.js` in your project.
2. Replace the placeholder values with the keys from **Step 2**.

It should look like this:
```javascript
const firebaseConfig = {
    apiKey: "AIzaSy...",
    authDomain: "your-project.firebaseapp.com",
    projectId: "your-project",
    storageBucket: "your-project.appspot.com",
    messagingSenderId: "123456...",
    appId: "1:123456..."
};
```

## Step 6: Test It
1. Open `account.html` in your browser.
2. Click **"Sign in with Google"**.
3. Once signed in, try adding a favorite song on any song page.
4. Refresh the page or open it on another device (if deployed) to see your favorites sync!
