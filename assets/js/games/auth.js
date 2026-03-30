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
    if (!cfg || !cfg.apiKey) {
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
        if (user) { _saveToUserbase(user); }
      });
    } catch (e) {
      console.error('[Games Auth] Init error:', e);
    }
  }

  function _saveToUserbase(user) {
    var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
    var path = DB_URL + '/userbase/' + user.uid + '.json';
    fetch(path)
      .then(function (r) { return r.json(); })
      .then(function (existing) {
        var payload = {
          username: user.displayName || 'Player',
          email: user.email || '',
          consent: true,
          lastSeen: new Date().toISOString()
        };
        if (!existing || !existing.consentDate) {
          payload.consentDate = new Date().toISOString();
        }
        // Preserve existing certificate name if already set
        if (existing && existing.certificateName) {
          payload.certificateName = existing.certificateName;
        }
        return user.getIdToken().then(function (token) {
          return fetch(path + '?auth=' + token, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
        });
      })
      .then(function () {
        // Check if user needs to provide certificate name
        _checkCertificateName(user);
      })
      .catch(function (e) { console.warn('[GameAuth] Userbase save failed:', e); });
  }

  function _checkCertificateName(user) {
    var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
    var path = DB_URL + '/userbase/' + user.uid + '/certificateName.json';
    fetch(path)
      .then(function (r) { return r.json(); })
      .then(function (certificateName) {
        if (!certificateName) {
          _showCertificateNameModal(user);
        }
      })
      .catch(function (e) { 
        // If certificate name doesn't exist, show modal
        _showCertificateNameModal(user);
      });
  }

  function _showCertificateNameModal(user) {
    // Check if modal already exists
    if (document.getElementById('certificate-name-modal')) return;

    var modal = document.createElement('div');
    modal.id = 'certificate-name-modal';
    modal.innerHTML = `
      <div class="certificate-modal-overlay">
        <div class="certificate-modal-content">
          <div class="certificate-modal-header">
            <h3>🏆 Professional Certificate Name</h3>
            <button class="certificate-modal-close">&times;</button>
          </div>
          <div class="certificate-modal-body">
            <p>Your Google account name (<strong>${user.displayName || 'Player'}</strong>) will be used for leaderboards.</p>
            <p>For certificates, please provide your professional name as you'd like it to appear:</p>
            <input type="text" id="certificate-name-input" placeholder="Enter your professional name" maxlength="50">
            <div class="certificate-modal-examples">
              <small>Examples: John Smith, Dr. Jane Doe, Sarah Johnson, PMP</small>
            </div>
          </div>
          <div class="certificate-modal-footer">
            <button id="certificate-name-save" class="btn-primary">Save Certificate Name</button>
            <button id="certificate-name-skip" class="btn-secondary">Use Google Name</button>
          </div>
        </div>
      </div>
    `;

    // Add styles
    var style = document.createElement('style');
    style.textContent = `
      .certificate-modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.7);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        animation: fadeIn 0.3s ease;
      }
      .certificate-modal-content {
        background: white;
        border-radius: 12px;
        max-width: 450px;
        width: 90%;
        max-height: 90vh;
        overflow-y: auto;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        animation: slideUp 0.3s ease;
      }
      .certificate-modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 24px;
        border-bottom: 1px solid #e5e7eb;
      }
      .certificate-modal-header h3 {
        margin: 0;
        color: #1f2937;
        font-size: 1.25rem;
        font-weight: 600;
      }
      .certificate-modal-close {
        background: none;
        border: none;
        font-size: 1.5rem;
        color: #6b7280;
        cursor: pointer;
        padding: 4px;
        border-radius: 4px;
        transition: all 0.2s;
      }
      .certificate-modal-close:hover {
        background: #f3f4f6;
        color: #374151;
      }
      .certificate-modal-body {
        padding: 24px;
      }
      .certificate-modal-body p {
        margin: 0 0 16px 0;
        color: #4b5563;
        line-height: 1.5;
      }
      .certificate-modal-body p strong {
        color: #1f2937;
      }
      #certificate-name-input {
        width: 100%;
        padding: 12px 16px;
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        font-size: 1rem;
        transition: border-color 0.2s;
        box-sizing: border-box;
      }
      #certificate-name-input:focus {
        outline: none;
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
      }
      .certificate-modal-examples {
        margin-top: 8px;
      }
      .certificate-modal-examples small {
        color: #6b7280;
        font-style: italic;
      }
      .certificate-modal-footer {
        display: flex;
        gap: 12px;
        padding: 20px 24px;
        border-top: 1px solid #e5e7eb;
        background: #f9fafb;
        border-radius: 0 0 12px 12px;
      }
      .btn-primary {
        flex: 1;
        background: #3b82f6;
        color: white;
        border: none;
        padding: 12px 20px;
        border-radius: 8px;
        font-size: 0.95rem;
        font-weight: 500;
        cursor: pointer;
        transition: background 0.2s;
      }
      .btn-primary:hover {
        background: #2563eb;
      }
      .btn-primary:disabled {
        background: #9ca3af;
        cursor: not-allowed;
      }
      .btn-secondary {
        background: white;
        color: #6b7280;
        border: 1px solid #d1d5db;
        padding: 12px 20px;
        border-radius: 8px;
        font-size: 0.95rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s;
      }
      .btn-secondary:hover {
        background: #f9fafb;
        border-color: #9ca3af;
        color: #4b5563;
      }
      @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
      }
      @keyframes slideUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
      }
      @media (max-width: 480px) {
        .certificate-modal-content {
          width: 95%;
          margin: 10px;
        }
        .certificate-modal-footer {
          flex-direction: column;
        }
        .btn-primary, .btn-secondary {
          width: 100%;
        }
      }
    `;
    document.head.appendChild(style);
    document.body.appendChild(modal);

    // Focus input
    setTimeout(function() {
      document.getElementById('certificate-name-input').focus();
    }, 100);

    // Event handlers
    var closeBtn = modal.querySelector('.certificate-modal-close');
    var saveBtn = document.getElementById('certificate-name-save');
    var skipBtn = document.getElementById('certificate-name-skip');
    var input = document.getElementById('certificate-name-input');

    function closeModal() {
      modal.remove();
      style.remove();
    }

    function saveCertificateName() {
      var certificateName = input.value.trim();
      if (!certificateName) {
        input.style.borderColor = '#ef4444';
        input.focus();
        return;
      }

      saveBtn.disabled = true;
      saveBtn.textContent = 'Saving...';

      var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
      var path = DB_URL + '/userbase/' + user.uid + '.json';
      
      user.getIdToken().then(function(token) {
        return fetch(path + '?auth=' + token, {
          method: 'PATCH',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ certificateName: certificateName })
        });
      }).then(function() {
        GameAuth.showToast('Certificate name saved successfully!', 'success');
        closeModal();
      }).catch(function(e) {
        console.error('[GameAuth] Certificate name save failed:', e);
        GameAuth.showToast('Failed to save certificate name', 'error');
        saveBtn.disabled = false;
        saveBtn.textContent = 'Save Certificate Name';
      });
    }

    function skipCertificateName() {
      closeModal();
    }

    closeBtn.addEventListener('click', closeModal);
    saveBtn.addEventListener('click', saveCertificateName);
    skipBtn.addEventListener('click', skipCertificateName);
    
    input.addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        saveCertificateName();
      }
    });

    // Close on overlay click
    modal.querySelector('.certificate-modal-overlay').addEventListener('click', function(e) {
      if (e.target === this) {
        closeModal();
      }
    });
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
    },

    getCertificateName: function () {
      if (!_currentUser) return Promise.resolve(null);
      var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
      var path = DB_URL + '/userbase/' + _currentUser.uid + '/certificateName.json';
      return fetch(path)
        .then(function (r) { return r.json(); })
        .then(function (certificateName) {
          return certificateName || _currentUser.displayName || 'Player';
        })
        .catch(function () {
          return _currentUser.displayName || 'Player';
        });
    },

    updateCertificateName: function () {
      if (_currentUser) {
        _showCertificateNameModal(_currentUser);
      }
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
