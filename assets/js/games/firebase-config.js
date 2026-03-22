/**
 * Firebase Configuration — RKoots Games
 *
 * SETUP INSTRUCTIONS:
 * 1. Go to https://console.firebase.google.com/
 * 2. Open project "games-rkoots" (or create it)
 * 3. Go to Project Settings → Your Apps → Web App
 * 4. Copy the firebaseConfig values and replace the placeholders below
 * 5. In Firebase Console → Authentication → Sign-in method → Enable Google
 * 6. Add "rkoots.github.io" to Authorized domains
 * 7. In Realtime Database → Rules, set:
 *    { "rules": { ".read": true, ".write": "auth != null" } }
 */
window.FIREBASE_CONFIG = {
  apiKey: "AIzaSyBz_RAvcwDpvyH5_UXTGXWZJ5DmQ1RsvIU",
  authDomain: "games-rkoots.firebaseapp.com",
  databaseURL: "https://games-rkoots-default-rtdb.firebaseio.com",
  projectId: "games-rkoots",
  storageBucket: "games-rkoots.firebasestorage.app",
  messagingSenderId: "644089913016",
  appId: "1:644089913016:web:34ea6f83d1dc4891909e4d",
  measurementId: "G-MW4P84QQJY"
};

window.FIREBASE_DB_URL = "https://games-rkoots-default-rtdb.firebaseio.com";
