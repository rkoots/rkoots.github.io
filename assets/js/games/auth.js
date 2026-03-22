/**
 * Firebase Google Auth — RKoots Games
 * Requires: firebase-app-compat, firebase-auth-compat, firebase-config.js
 */
(function () {
  'use strict';

  let _app = null;
  let _auth = null;
  let _currentUser = null;
  let _authCallbacks = [];

  function _initFirebase() {
    if (_app) return;
    const cfg = window.FIREBASE_CONFIG;
    if (!cfg || cfg.apiKey === 'REPLACE_WITH_YOUR_API_KEY') {
      console.warn('[Games Auth] Firebase not configured. Set values in firebase-config.js');
      return;
    }
    try {
      _app = firebase.initializeApp(cfg);
      _auth = firebase.auth();
      _auth.onAuthStateChanged(function (user) {
        _currentUser = user;
        _authCallbacks.forEach(function (cb) { cb(user); });
        _updateAuthUI(user);
      });
    } catch (e) {
      console.error('[Games Auth] Init error:', e);
    }
  }

  function _updateAuthUI(user) {
    const signedInEl = document.querySelectorAll('.auth-signed-in');
    const signedOutEl = document.querySelectorAll('.auth-signed-out');
    const nameEl = document.querySelectorAll('.auth-name');
    const avatarEl = document.querySelectorAll('.auth-avatar-img');

    signedInEl.forEach(function (el) { el.style.display = user ? 'flex' : 'none'; });
    signedOutEl.forEach(function (el) { el.style.display = user ? 'none' : 'flex'; });
    if (user) {
      nameEl.forEach(function (el) { el.textContent = user.displayName || 'Player'; });
      avatarEl.forEach(function (el) {
        if (user.photoURL) {
          el.innerHTML = '<img src="' + user.photoURL + '" alt="avatar">';
        } else {
          el.textContent = (user.displayName || 'P').charAt(0).toUpperCase();
        }
      });
    }
  }

  window.GameAuth = {
    init: function () { _initFirebase(); },

    signIn: function () {
      if (!_auth) { _initFirebase(); }
      if (!_auth) {
        GameAuth.showToast('Firebase not configured. Check firebase-config.js', 'error');
        return Promise.reject(new Error('Firebase not configured'));
      }
      const provider = new firebase.auth.GoogleAuthProvider();
      return _auth.signInWithPopup(provider).catch(function (err) {
        console.error('[Games Auth] Sign-in error:', err);
        GameAuth.showToast('Sign-in failed: ' + err.message, 'error');
        throw err;
      });
    },

    signOut: function () {
      if (_auth) {
        return _auth.signOut().then(function () {
          GameAuth.showToast('Signed out', 'success');
        });
      }
      return Promise.resolve();
    },

    getCurrentUser: function () { return _currentUser; },

    isSignedIn: function () { return !!_currentUser; },

    onAuthChange: function (cb) {
      _authCallbacks.push(cb);
      if (_currentUser !== undefined) { cb(_currentUser); }
    },

    getIdToken: function () {
      if (!_currentUser) return Promise.resolve(null);
      return _currentUser.getIdToken();
    },

    showToast: function (msg, type) {
      let toast = document.getElementById('game-toast');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'game-toast';
        toast.className = 'game-toast';
        document.body.appendChild(toast);
      }
      toast.textContent = msg;
      toast.className = 'game-toast' + (type ? ' ' + type : '');
      requestAnimationFrame(function () {
        toast.classList.add('show');
        setTimeout(function () { toast.classList.remove('show'); }, 2800);
      });
    }
  };

  document.addEventListener('DOMContentLoaded', function () {
    GameAuth.init();

    document.addEventListener('click', function (e) {
      if (e.target.closest('.btn-google-signin')) { GameAuth.signIn(); }
      if (e.target.closest('.btn-signout')) { GameAuth.signOut(); }
    });
  });
}());
