// Authentication and Data Management

// DOM Elements
const authBtn = document.getElementById('authBtn'); // Login/Logout button
const userAvatar = document.getElementById('userAvatar'); // Avatar image element
const userName = document.getElementById('userName'); // User name element

// State
let currentUser = null;
let userFavorites = [];

// Auth State Observer
auth.onAuthStateChanged(async (user) => {
    if (user) {
        // User is signed in
        currentUser = user;
        console.log("User signed in:", user.displayName);

        // Update UI
        if (authBtn) {
            authBtn.innerHTML = '<span class="material-icons">logout</span> Sign Out';
            authBtn.onclick = signOut;
        }

        if (userAvatar) {
            userAvatar.src = user.photoURL || 'https://via.placeholder.com/100';
            userAvatar.parentElement.style.display = 'flex'; // Ensure it's visible
        }

        if (userName) {
            userName.textContent = user.displayName || 'User';
        }

        // Load Favorites from Firestore
        await loadFavoritesFromFirestore();

        // Refresh UI if on account page or song page
        updateUI();

    } else {
        // User is signed out
        currentUser = null;
        console.log("User signed out");

        // Update UI
        if (authBtn) {
            authBtn.innerHTML = '<span class="material-icons">login</span> Sign in with Google';
            authBtn.onclick = signInWithGoogle;
        }

        if (userAvatar) {
            userAvatar.src = '';
            // Optional: Hide avatar or show default
        }

        if (userName) {
            userName.textContent = 'Guest';
        }

        // Fallback to LocalStorage
        loadFavoritesFromLocalStorage();
        updateUI();
    }
});

// Sign In
function signInWithGoogle() {
    const provider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(provider)
        .then((result) => {
            // Successful sign in
            // We could merge local storage favorites here if we wanted
        }).catch((error) => {
            console.error("Error signing in:", error);
            alert("Sign in failed: " + error.message);
        });
}

// Sign Out
function signOut() {
    auth.signOut().then(() => {
        // Sign-out successful.
        // Clear data or reload
        location.reload();
    }).catch((error) => {
        console.error("Error signing out:", error);
    });
}

// Data Management
async function loadFavoritesFromFirestore() {
    if (!currentUser) return;

    try {
        const doc = await db.collection('users').doc(currentUser.uid).get();
        if (doc.exists) {
            userFavorites = doc.data().favorites || [];
            // Sync to local storage for offline/faster access? 
            // For now, let's keep them separate or just use memory.
        } else {
            // Create user doc if not exists
            await db.collection('users').doc(currentUser.uid).set({
                favorites: [],
                email: currentUser.email
            });
            userFavorites = [];
        }
    } catch (error) {
        console.error("Error loading favorites:", error);
    }
}

function loadFavoritesFromLocalStorage() {
    try {
        userFavorites = JSON.parse(localStorage.getItem('favorites') || '[]');
    } catch (e) {
        userFavorites = [];
    }
}

async function toggleFavorite(songId) {
    if (userFavorites.includes(songId)) {
        userFavorites = userFavorites.filter(id => id !== songId);
    } else {
        userFavorites.push(songId);
    }

    // Update UI immediately for responsiveness
    updateUI();

    // Persist
    if (currentUser) {
        try {
            await db.collection('users').doc(currentUser.uid).update({
                favorites: userFavorites
            });
        } catch (error) {
            console.error("Error updating favorites in cloud:", error);
            // Revert on error?
        }
    } else {
        localStorage.setItem('favorites', JSON.stringify(userFavorites));
    }
}

// UI Updates
function updateUI() {
    // 1. Update Favorite Button on Song Pages
    const favBtn = document.getElementById('favoriteBtn');
    if (favBtn && typeof songId !== 'undefined') {
        const isFav = userFavorites.includes(songId);
        favBtn.innerHTML = isFav
            ? '<span class="material-icons">favorite</span> Favorite'
            : '<span class="material-icons">favorite_border</span> Favorite';

        // Update onclick handler to use our new function
        favBtn.onclick = () => toggleFavorite(songId);
    }

    // 2. Update Favorites Grid on Account Page
    const favoritesGrid = document.querySelector('.favorites-grid');
    if (favoritesGrid && typeof songDatabase !== 'undefined') {
        renderAccountFavorites();
    }
}

function renderAccountFavorites() {
    const favoritesGrid = document.querySelector('.favorites-grid');
    const favoriteCount = document.getElementById('fav-count');
    const noFavsMsg = document.getElementById('no-favs-msg');

    if (favoriteCount) favoriteCount.textContent = userFavorites.length;

    // Filter valid songs
    const validFavorites = userFavorites.filter(id => songDatabase[id]);

    if (validFavorites.length === 0) {
        if (favoritesGrid) favoritesGrid.innerHTML = '';
        if (noFavsMsg) noFavsMsg.style.display = 'block';
    } else {
        if (noFavsMsg) noFavsMsg.style.display = 'none';
        if (favoritesGrid) {
            favoritesGrid.innerHTML = validFavorites.map(id => {
                const song = songDatabase[id];
                return `
                    <div class="favorite-card">
                        <a href="${song.filename}" class="card-link"></a>
                        <div class="favorite-header">
                            <span class="material-icons favorite-icon" style="font-style: normal;">${song.icon}</span>
                            <div class="favorite-info">
                                <h3>${song.title}</h3>
                                <p>${song.artist}</p>
                            </div>
                        </div>
                        <button onclick="toggleFavorite('${id}')" class="remove-btn">
                            <span class="material-icons" style="font-size: 18px;">delete</span> Remove
                        </button>
                    </div>
                `;
            }).join('');
        }
    }
}
