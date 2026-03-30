/**
 * RKoots Learning Platform — certificate.js
 * Handles: certificate generation, license number, Firebase storage, PDF download
 */
console.log('[Cert] certificate.js starting to load...');
(function () {
  'use strict';
  console.log('[Cert] certificate.js IIFE started...');

  var _certData = null;

  window.LearnCert = {

    generate: function (result) {
      var user = GameAuth.getCurrentUser();
      if (!user) { LearnApp.toast('Sign in required', 'error'); return; }
      var course = LearnApp.getActiveCourse();
      if (!course) return;

      var now = new Date();
      var licenseNumber = _generateLicense(user.email, user.uid, now.getTime());
      var certificateId = _generateCertificateId(user.email, user.uid, now.getTime(), course.title);
      var examDate = now.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
      var issueDate = examDate;

      _certData = {
        name: user.displayName || 'Learner',
        email: user.email,
        course: course.title,
        courseId: course.id,  // Add course ID for proper storage
        certificateId: certificateId,  // Add unique certificate ID
        score: result.score,
        correct: result.correct,
        total: result.total,
        licenseNumber: licenseNumber,
        examDate: examDate,
        issueDate: issueDate,
        uid: user.uid
      };

      var certHTML = _buildCertHTML(_certData);
      _certData.certificateHTML = certHTML;

      var paper = document.getElementById('certificatePaper');
      if (paper) paper.innerHTML = certHTML;

      document.getElementById('certModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';

      _storeCertificate(_certData, user);
    },

    close: function () {
      document.getElementById('certModal').classList.add('hidden');
      document.body.style.overflow = '';
    },

    download: function () {
      if (!_certData) return;
      var html = _buildFullPageCertHTML(_certData);
      var blob = new Blob([html], { type: 'text/html' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'RKoots-Certificate-' + _certData.course.replace(/\s+/g, '-') + '-' + _certData.licenseNumber + '.html';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      LearnApp.toast('Certificate downloaded!', 'success');
    },

    share: function () {
      if (!_certData) return;
      var certificateUrl = _getCertificateUrl(_certData);
      var text = 'I just earned a free certificate in "' + _certData.course + '" on RKoots Learning Platform! 🎓 Score: ' + _certData.score + '% | License: ' + _certData.licenseNumber + '\n\nView my certificate: ' + certificateUrl;
      if (navigator.share) {
        navigator.share({ 
          title: 'RKoots Certificate', 
          text: text, 
          url: certificateUrl 
        })
          .catch(function () {});
      } else {
        _copyToClipboard(text);
        LearnApp.toast('Certificate info copied to clipboard!', 'success');
      }
    },

    viewFromDash: function (certData) {
      _certData = certData;
      var paper = document.getElementById('certificatePaper');
      if (paper) {
        if (certData.certificateHTML) {
          paper.innerHTML = certData.certificateHTML;
        } else {
          paper.innerHTML = _buildCertHTML(certData);
        }
      }
      document.getElementById('certModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    },

    viewInNewWindow: function () {
      if (!_certData) return;
      var html = _buildFullPageCertHTML(_certData);
      var newWindow = window.open('', '_blank');
      newWindow.document.write(html);
      newWindow.document.close();
      LearnApp.toast('Certificate opened in new window!', 'success');
    },

    syncLocalCertificates: function() {
      var user = GameAuth.getCurrentUser();
      if (!user) return;
      
      var localCerts = JSON.parse(localStorage.getItem('rkoots_certificates') || '{}');
      var emailKey = user.email.replace(/[.#$\[\]]/g, '_');
      var userLocalCerts = localCerts[emailKey];
      
      if (!userLocalCerts || Object.keys(userLocalCerts).length === 0) return;
      
      console.log('[Cert] Syncing local certificates to Firebase...');
      var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
      
      Object.keys(userLocalCerts).forEach(function(courseKey) {
        var certData = userLocalCerts[courseKey];
        // Try to find the actual course ID from courses data
        var courses = window.LEARN_COURSES || [];
        var matchingCourse = courses.find(function(c) { return c.title === certData.course; });
        var actualCourseKey = matchingCourse ? matchingCourse.id : courseKey;
        
        var path = DB_URL + '/certificates/' + emailKey + '/' + actualCourseKey + '.json';
        
        user.getIdToken().then(function(token) {
          return fetch(path + '?auth=' + token, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(certData)
          });
        }).then(function(response) {
          if (response.ok) {
            console.log('[Cert] Synced certificate for course:', actualCourseKey);
            // Remove from localStorage after successful sync
            delete localCerts[emailKey][courseKey];
            localStorage.setItem('rkoots_certificates', JSON.stringify(localCerts));
          }
        }).catch(function(e) {
          console.warn('[Cert] Sync failed for course:', actualCourseKey, e);
        });
      });
    }
  };

  /* ── Certificate HTML Builder ── */
  function _buildCertHTML(d) {
    return [
      '<div class="cert-watermark"><i class="fas fa-graduation-cap"></i></div>',
      '<div class="cert-header-line">Certificate of Achievement</div>',
      '<div class="cert-logo-area">',
        '<div class="cert-logo-icon"><i class="fas fa-graduation-cap"></i></div>',
        '<div class="cert-org">RKoots Learning Platform</div>',
      '</div>',
      '<div class="cert-divider"></div>',
      '<div class="cert-title-block">',
        '<div class="cert-main-title">Certificate of Achievement</div>',
        '<div class="cert-subtitle">This is to certify that</div>',
      '</div>',
      '<div class="cert-presented-to">Presented to</div>',
      '<div class="cert-name">' + _escHtml(d.name) + '</div>',
      '<div class="cert-body-text">',
        'has been certified as',
        '<span class="cert-course-name">' + _escHtml(d.course) + '</span>',
        'by undergoing the training and demonstrating through examination the required competency ',
        'in the internationally recognized title, achieving a',
      '</div>',
      '<div class="cert-seal"><i class="fas fa-award"></i> Seal of Excellence</div>',
      '<div class="cert-body-text" style="font-size:0.85rem;color:#475569">',
        'based on a high score of <strong>' + d.score + '%</strong> (' + d.correct + '/' + d.total + ' correct)',
      '</div>',
      '<div class="cert-divider"></div>',
      '<div class="cert-meta-grid">',
        '<div class="cert-meta-item"><strong>Exam Date</strong>' + _escHtml(d.examDate) + '</div>',
        '<div class="cert-meta-item"><strong>Issue Date</strong>' + _escHtml(d.issueDate) + '</div>',
        '<div class="cert-meta-item"><strong>Score</strong>' + d.score + '% (' + d.correct + '/' + d.total + ')</div>',
      '</div>',
      '<div class="cert-signatures">',
        '<div class="cert-sig-block">',
          '<div class="cert-sig-line"></div>',
          '<div class="cert-sig-name">' +
            '<svg width="120" height="40" viewBox="0 0 120 40" style="font-family:Brush Script MT,cursive;font-size:24px;fill:#1e293b;">' +
              '<path d="M10,25 Q15,10 25,20 T35,15 Q40,10 45,25 T55,20 Q60,15 65,25 T75,20" stroke="#1e293b" stroke-width="1.5" fill="none"/>' +
              '<text x="80" y="25" font-style="italic" font-weight="600">Raj</text>' +
            '</svg>' +
          '</div>',
          '<div class="cert-sig-title">Course Director, rkoots</div>',
        '</div>',
        '<div class="cert-sig-block">',
          '<div class="cert-sig-line"></div>',
          '<div class="cert-sig-name">' + _escHtml(d.name) + '</div>',
          '<div class="cert-sig-title">Certificate Holder</div>',
        '</div>',
      '</div>',
      '<div class="cert-license-bar">License No: ' + _escHtml(d.licenseNumber) + '</div>'
    ].join('');
  }

  /* ── Standalone downloadable HTML ── */
  function _buildFullPageCertHTML(d) {
    var body = _buildCertHTML(d);
    return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Certificate – ' + _escHtml(d.course) + '</title>' +
      '<link rel="preconnect" href="https://fonts.googleapis.com">' +
      '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Georgia&display=swap" rel="stylesheet">' +
      '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">' +
      '<style>' +
      '*{box-sizing:border-box;margin:0;padding:0}' +
      'body{font-family:Inter,sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh;background:#f8f9fc;padding:20px}' +
      /* Certificate Paper - Exact same as preview CSS */
      '.certificate-paper{background:#fff;border:8px solid transparent;border-image:linear-gradient(135deg,#c8a96e,#f0d080,#c8a96e,#a0784a) 1;padding:48px 52px;font-family:Georgia,serif;text-align:center;position:relative;box-shadow:inset 0 0 40px rgba(200,169,110,0.12);max-width:780px;width:100%}' +
      '.cert-watermark{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:8rem;color:rgba(102,126,234,0.05);pointer-events:none;user-select:none}' +
      '.cert-header-line{font-size:.75rem;letter-spacing:4px;text-transform:uppercase;color:#8b6914;margin-bottom:12px;font-family:Inter,sans-serif}' +
      '.cert-logo-area{margin-bottom:16px}' +
      '.cert-logo-icon{font-size:2.4rem;color:#c8a96e}' +
      '.cert-org{font-size:.9rem;font-weight:700;color:#667eea;letter-spacing:2px;text-transform:uppercase;font-family:Inter,sans-serif}' +
      '.cert-title-block{margin:20px 0}' +
      '.cert-main-title{font-size:2.2rem;color:#1e293b;font-weight:700;margin-bottom:4px}' +
      '.cert-subtitle{font-size:.75rem;letter-spacing:3px;text-transform:uppercase;color:#8b6914;font-family:Inter,sans-serif}' +
      '.cert-divider{height:2px;background:linear-gradient(90deg,transparent,#c8a96e,#f0d080,#c8a96e,transparent);margin:20px auto;width:80%}' +
      '.cert-presented-to{font-size:.85rem;color:#64748b;font-family:Inter,sans-serif;margin-bottom:4px}' +
      '.cert-name{font-size:2rem;font-weight:700;color:#1e293b;font-style:italic;margin-bottom:16px}' +
      '.cert-body-text{font-size:.9rem;color:#475569;line-height:1.7;max-width:560px;margin:0 auto 20px;font-family:Inter,sans-serif}' +
      '.cert-course-name{font-size:1.15rem;font-weight:700;color:#667eea;display:block;margin:4px 0 10px;font-family:Inter,sans-serif;font-style:normal}' +
      '.cert-seal{display:inline-flex;align-items:center;gap:6px;background:linear-gradient(135deg,#f59e0b,#d97706);color:white;padding:6px 16px;border-radius:20px;font-size:.75rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;font-family:Inter,sans-serif;margin-bottom:20px}' +
      '.cert-meta-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;font-family:Inter,sans-serif;font-size:.78rem;border-top:1px solid rgba(200,169,110,0.3);border-bottom:1px solid rgba(200,169,110,0.3);padding:14px 0;margin:16px 0;color:#64748b}' +
      '.cert-meta-item strong{display:block;font-size:.7rem;text-transform:uppercase;letter-spacing:1px;color:#8b6914;margin-bottom:2px}' +
      '.cert-signatures{display:flex;justify-content:space-around;margin-top:28px;font-family:Inter,sans-serif}' +
      '.cert-sig-block{text-align:center}' +
      '.cert-sig-line{width:140px;height:1px;background:#1e293b;margin:0 auto 6px}' +
      '.cert-sig-name{font-size:.8rem;font-weight:700;color:#1e293b}' +
      '.cert-sig-title{font-size:.7rem;color:#64748b}' +
      '.cert-license-bar{margin-top:16px;font-family:JetBrains Mono,monospace;font-size:.7rem;color:#94a3b8;letter-spacing:.5px}' +
      '@media print{body{background:white;padding:0}.certificate-paper{border-image:none;border:8px solid #c8a96e;box-shadow:none}}' +
      '@media (max-width:768px){.cert-meta-grid{grid-template-columns:1fr 1fr}.certificate-paper{padding:28px 20px}.cert-main-title{font-size:1.5rem}.cert-name{font-size:1.4rem}}' +
      '</style></head><body>' +
      '<div class="certificate-paper">' + body + '</div>' +
      '<script>window.onload=function(){window.print();}<\/script>' +
      '</body></html>';
  }

  /* ── License Number Generator ── */
  function _generateLicense(email, uid, timestamp) {
    var hash = _hashString((email || '') + (uid || '') + timestamp.toString());
    var prefix = 'RKL';
    var year = new Date().getFullYear();
    var hex = Math.abs(hash).toString(16).toUpperCase().padStart(8, '0').slice(0, 8);
    return prefix + '-' + year + '-' + hex;
  }

  /* ── Certificate ID Generator ── */
  function _generateCertificateId(email, uid, timestamp, courseTitle) {
    var hash = _hashString((email || '') + (uid || '') + timestamp.toString() + (courseTitle || ''));
    var prefix = 'CERT';
    var year = new Date().getFullYear();
    var hex = Math.abs(hash).toString(16).toUpperCase().padStart(12, '0').slice(0, 12);
    return prefix + '-' + year + '-' + hex;
  }

  /* ── Get Unique Certificate URL ── */
  function _getCertificateUrl(certData) {
    var emailKey = (certData.email || '').replace(/[.#$\[\]]/g, '_');
    var baseUrl = window.location.origin + '/learn/certificate.html';
    var certUrl = baseUrl + '?id=' + encodeURIComponent(certData.certificateId || certData.courseId || 'unknown') + 
                  '&user=' + encodeURIComponent(emailKey) +
                  '&utm_source=share&utm_medium=social&utm_campaign=certificate';
    return certUrl;
  }

  function _hashString(str) {
    var hash = 0x811c9dc5;
    for (var i = 0; i < str.length; i++) {
      hash ^= str.charCodeAt(i);
      hash = ((hash >>> 0) * 0x01000193) >>> 0;
    }
    return hash >>> 0;
  }

  /* ── Firebase Storage ── */
  function _storeCertificate(data, user) {
    var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
    var emailKey = data.email.replace(/[.#$\[\]]/g, '_');
    // Use certificate ID as the key for unique URLs
    var courseKey = data.certificateId || data.courseId || (window.LearnApp && LearnApp.getActiveCourse ? LearnApp.getActiveCourse()?.id : null) || data.course.replace(/[^a-zA-Z0-9]/g, '_').toLowerCase();
    var path = DB_URL + '/certificates/' + emailKey + '/' + courseKey + '.json';

    console.log('[Cert] Storage path:', path);

    if (!user || !user.getIdToken) {
      console.error('[Cert] No user or getIdToken method');
      _storeCertificateLocally(data);
      LearnApp.toast('Certificate generated (saved locally)', 'warning');
      return;
    }

    user.getIdToken().then(function (token) {
      return fetch(path + '?auth=' + token, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: data.name,
          email: data.email,
          course: data.course,
          courseId: data.courseId,
          certificateId: data.certificateId,
          score: data.score,
          correct: data.correct,
          total: data.total,
          licenseNumber: data.licenseNumber,
          examDate: data.examDate,
          issueDate: data.issueDate,
          uid: data.uid,
          certificateHTML: data.certificateHTML
        })
      });
    }).then(function () {
      LearnApp.toast('Certificate saved to your profile!', 'success');
    }).catch(function (e) {
      console.warn('[Cert] Storage failed:', e);
      LearnApp.toast('Certificate generated (offline save failed)', '');
    });
  }

  /* ── Local Storage Fallback ── */
  function _storeCertificateLocally(data) {
    try {
      var localCerts = JSON.parse(localStorage.getItem('rkoots_certificates') || '{}');
      var emailKey = data.email.replace(/[.#$\[\]]/g, '_');
      if (!localCerts[emailKey]) localCerts[emailKey] = {};
      // Use certificate ID as the key for unique URLs
      var courseKey = data.certificateId || data.courseId || (window.LearnApp && LearnApp.getActiveCourse ? LearnApp.getActiveCourse()?.id : null) || data.course.replace(/[^a-zA-Z0-9]/g, '_').toLowerCase();
      localCerts[emailKey][courseKey] = data;
      localStorage.setItem('rkoots_certificates', JSON.stringify(localCerts));
      console.log('[Cert] Certificate saved to localStorage');
      
      // Try to sync after a short delay
      setTimeout(function() {
        if (window.LearnCert && LearnCert.syncLocalCertificates) {
          LearnCert.syncLocalCertificates();
        }
      }, 2000);
    } catch (e) {
      console.error('[Cert] Local storage failed:', e);
    }
  }

  function _escHtml(str) {
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function _copyToClipboard(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
  }

}());