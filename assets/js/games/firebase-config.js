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
  apiKey: "REPLACE_WITH_YOUR_API_KEY",
  authDomain: "games-rkoots.firebaseapp.com",
  databaseURL: "https://games-rkoots-default-rtdb.firebaseio.com",
  projectId: "games-rkoots",
  storageBucket: "games-rkoots.appspot.com",
  messagingSenderId: "REPLACE_WITH_SENDER_ID",
  appId: "REPLACE_WITH_APP_ID"
};

window.FIREBASE_DB_URL = "https://games-rkoots-default-rtdb.firebaseio.com";
