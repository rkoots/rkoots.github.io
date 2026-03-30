/**
 * RKoots Learning Platform — exam.js
 * Handles: exam lifecycle, timer, question rendering, scoring, auto-submit
 */
(function () {
  'use strict';

  var EXAM_DURATION = 45 * 60; // 45 minutes in seconds
  var PASS_THRESHOLD = 70;     // percentage

  var _course = null;
  var _questions = [];
  var _answers = {};
  var _currentQ = 0;
  var _timerInterval = null;
  var _timeLeft = EXAM_DURATION;
  var _submitted = false;

  function $(id) { return document.getElementById(id); }

  window.LearnExam = {

    start: function () {
      console.log('[Exam] LearnExam.start() called');
      console.log('[Exam] LearnApp available:', !!window.LearnApp);
      console.log('[Exam] LearnApp.getActiveCourse available:', !!(window.LearnApp && LearnApp.getActiveCourse));
      
      var course = null;
      if (window.LearnApp && LearnApp.getActiveCourse) {
        course = LearnApp.getActiveCourse();
      }
      
      // Fallback: try to get course from URL hash
      if (!course && window.location.hash) {
        var courseId = window.location.hash.substring(1); // Remove #
        console.log('[Exam] Trying to load course from hash:', courseId);
        if (window.LearnApp && LearnApp.loadCourse) {
          LearnApp.loadCourse(courseId);
          course = LearnApp.getActiveCourse();
        }
      }
      
      console.log('[Exam] Active course:', course);
      
      if (!course) {
        console.error('[Exam] No active course found. Cannot start exam.');
        console.log('[Exam] Current URL hash:', window.location.hash);
        if (window.LearnApp && LearnApp.toast) {
          LearnApp.toast('Please select a course first.', 'error');
        } else {
          alert('Please select a course first.');
        }
        return;
      }
      console.log('[Exam] Starting exam for course:', course.title);
      _course = course;
      _questions = _shuffle(course.questions.slice());
      if (_questions.length > 25) _questions = _questions.slice(0, 25);
      _answers = {};
      _currentQ = 0;
      _timeLeft = EXAM_DURATION;
      _submitted = false;

      /* Reset screens */
      _showScreen('examStart');
      $('examStartTitle').textContent = 'Exam: ' + course.title + ' (25 Questions, 45 Minutes)';

      /* Sync auth gate */
      var user = GameAuth.getCurrentUser();
      var gate = $('examAuthGate');
      var startBtn = $('examStartBtn');
      if (gate) gate.style.display = user ? 'none' : 'block';
      if (startBtn) startBtn.style.display = user ? 'flex' : 'none';

      $('examModal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    },

    begin: function () {
      var user = GameAuth.getCurrentUser();
      if (!user) {
        LearnApp.toast('Please sign in to take the exam.', 'error');
        return;
      }
      _showScreen('examActive');
      _buildDots();
      _renderQuestion();
      _startTimer();
    },

    close: function () {
      _stopTimer();
      $('examModal').classList.add('hidden');
      document.body.style.overflow = '';
    },

    nextQuestion: function () {
      if (_currentQ < _questions.length - 1) {
        _currentQ++;
        _renderQuestion();
      }
    },

    prevQuestion: function () {
      if (_currentQ > 0) {
        _currentQ--;
        _renderQuestion();
      }
    },

    selectAnswer: function (qIdx, optIdx) {
      _answers[qIdx] = optIdx;
      _renderQuestion();
      _updateDots();
    },

    submit: function (autoSubmit) {
      if (_submitted) return;
      if (!autoSubmit) {
        var answered = Object.keys(_answers).length;
        var remaining = _questions.length - answered;
        if (remaining > 0) {
          if (!confirm(remaining + ' question(s) unanswered. Submit anyway?')) return;
        }
      }
      _stopTimer();
      _submitted = true;
      _calculateAndShowResult();
    }
  };

  /* ── Timer ── */
  function _startTimer() {
    _timerInterval = setInterval(function () {
      _timeLeft--;
      _updateTimerDisplay();
      if (_timeLeft <= 0) {
        LearnExam.submit(true);
      }
    }, 1000);
  }

  function _stopTimer() {
    if (_timerInterval) {
      clearInterval(_timerInterval);
      _timerInterval = null;
    }
  }

  function _updateTimerDisplay() {
    var mins = Math.floor(_timeLeft / 60);
    var secs = _timeLeft % 60;
    var display = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
    var el = $('timerDisplay');
    if (el) el.textContent = display;
    var timerEl = $('examTimer');
    if (timerEl) {
      if (_timeLeft <= 300) {
        timerEl.classList.add('urgent');
      } else {
        timerEl.classList.remove('urgent');
      }
    }
  }

  /* ── Question Rendering ── */
  function _renderQuestion() {
    var q = _questions[_currentQ];
    if (!q) return;

    /* Counter */
    var counter = $('examQCounter');
    if (counter) counter.textContent = 'Q ' + (_currentQ + 1) + ' / ' + _questions.length;

    /* Progress bar */
    var fill = $('examProgressFill');
    if (fill) fill.style.width = ((_currentQ + 1) / _questions.length * 100) + '%';

    /* Question area */
    var area = $('questionArea');
    if (!area) return;

    var selected = _answers[_currentQ];
    var labels = ['A', 'B', 'C', 'D'];
    var optHtml = q.o.map(function (opt, idx) {
      var cls = 'option-btn' + (selected === idx ? ' selected' : '');
      return '<button class="' + cls + '" onclick="LearnExam.selectAnswer(' + _currentQ + ',' + idx + ')">' +
        '<span class="option-label">' + labels[idx] + '</span>' +
        '<span class="option-text">' + _escHtml(opt) + '</span>' +
        '</button>';
    }).join('');

    area.innerHTML =
      '<p class="question-text">' + (_currentQ + 1) + '. ' + _escHtml(q.q) + '</p>' +
      '<div class="question-options">' + optHtml + '</div>';

    /* Nav buttons */
    var prev = $('btnPrevQ');
    var next = $('btnNextQ');
    if (prev) prev.disabled = (_currentQ === 0);
    if (next) {
      if (_currentQ === _questions.length - 1) {
        next.textContent = '';
        next.innerHTML = 'Last <i class="fas fa-flag-checkered"></i>';
        next.disabled = true;
      } else {
        next.innerHTML = 'Next <i class="fas fa-chevron-right"></i>';
        next.disabled = false;
      }
    }

    _updateDots();
  }

  function _buildDots() {
    var container = $('questionDots');
    if (!container) return;
    var html = '';
    for (var i = 0; i < _questions.length; i++) {
      html += '<span class="qdot" data-idx="' + i + '" onclick="LearnExam._jumpTo(' + i + ')"></span>';
    }
    container.innerHTML = html;
    _updateDots();
  }

  LearnExam._jumpTo = function (idx) {
    _currentQ = idx;
    _renderQuestion();
  };

  function _updateDots() {
    var dots = document.querySelectorAll('.qdot');
    dots.forEach(function (dot) {
      var idx = parseInt(dot.getAttribute('data-idx'), 10);
      dot.className = 'qdot';
      if (idx === _currentQ) dot.classList.add('current');
      else if (_answers[idx] !== undefined) dot.classList.add('answered');
    });
  }

  /* ── Scoring ── */
  function _calculateAndShowResult() {
    var correct = 0;
    var wrong = 0;
    var skipped = 0;

    _questions.forEach(function (q, idx) {
      if (_answers[idx] === undefined) {
        skipped++;
      } else if (_answers[idx] === q.a) {
        correct++;
      } else {
        wrong++;
      }
    });

    var total = _questions.length;
    var score = Math.round((correct / total) * 100);
    var passed = score >= PASS_THRESHOLD;

    /* Animate score ring */
    _showScreen('examResult');

    var iconEl = $('resultIcon');
    if (iconEl) {
      iconEl.innerHTML = passed ? '<i class="fas fa-trophy"></i>' : '<i class="fas fa-times-circle"></i>';
      iconEl.className = 'result-icon ' + (passed ? 'pass' : 'fail');
    }
    var titleEl = $('resultTitle');
    if (titleEl) titleEl.textContent = passed ? '🎉 Congratulations! You Passed!' : 'Keep Practicing!';

    var scoreNum = $('scoreNumber');
    if (scoreNum) scoreNum.textContent = score + '%';

    var arc = $('scoreArc');
    if (arc) {
      var circumference = 339.3;
      var offset = circumference - (score / 100) * circumference;
      arc.style.strokeDashoffset = offset;
      arc.style.stroke = passed ? '#28a745' : '#dc3545';
    }

    if ($('sbCorrect')) $('sbCorrect').textContent = correct + ' Correct';
    if ($('sbWrong')) $('sbWrong').textContent = wrong + ' Wrong';
    if ($('sbSkipped')) $('sbSkipped').textContent = skipped + ' Skipped';

    var msg = $('resultMessage');
    if (msg) {
      msg.textContent = passed
        ? 'Excellent! You scored ' + score + '% and have earned your certificate.'
        : 'You scored ' + score + '%. You need ' + PASS_THRESHOLD + '% to pass. Review the material and try again!';
    }

    var actions = $('resultActions');
    if (actions) {
      if (passed) {
        actions.innerHTML =
          '<button class="btn-cert" onclick="LearnExam.close();LearnCert.generate(' + JSON.stringify({ score: score, correct: correct, total: total }) + ')"><i class="fas fa-certificate"></i> View My Certificate</button>' +
          '<button class="btn-ghost" onclick="LearnExam.close()"><i class="fas fa-home"></i> Back to Course</button>';
      } else {
        actions.innerHTML =
          '<button class="btn-primary-lg" onclick="LearnExam.close();setTimeout(function(){LearnExam.start();},200)"><i class="fas fa-redo"></i> Try Again</button>' +
          '<button class="btn-ghost-lg" onclick="LearnExam.close()"><i class="fas fa-book"></i> Review Material</button>';
      }
    }

    /* Save attempt to Firebase */
    _saveAttempt(score, passed, correct, total);
    
    /* Auto-generate and save certificate if passed */
    if (passed && window.LearnCert) {
      console.log('[Exam] Auto-generating certificate for passed exam...');
      try {
        // Generate certificate data without showing modal
        var user = GameAuth.getCurrentUser();
        var course = LearnApp.getActiveCourse();
        
        if (user && course) {
          var now = new Date();
          var licenseNumber = _generateLicense(user.email, user.uid, now.getTime());
          var examDate = now.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
          var issueDate = examDate;
          
          var certData = {
            name: user.displayName || 'Learner',
            email: user.email,
            course: course.title,
            score: score,
            correct: correct,
            total: total,
            licenseNumber: licenseNumber,
            examDate: examDate,
            issueDate: issueDate,
            uid: user.uid
          };
          
          // Build certificate HTML
          certData.certificateHTML = _buildCertHTML(certData);
          
          // Store certificate to Firebase
          _storeCertificate(certData, user);
          
          console.log('[Exam] Certificate auto-generated and saved');
        }
      } catch (e) {
        console.error('[Exam] Failed to auto-generate certificate:', e);
      }
    }
  }

  function _saveAttempt(score, passed, correct, total) {
    var user = GameAuth.getCurrentUser();
    if (!user || !_course) return;
    var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
    var emailKey = user.email.replace(/[.#$\[\]]/g, '_');
    var path = DB_URL + '/attempts/' + emailKey + '/' + _course.id + '.json';
    user.getIdToken().then(function (token) {
      return fetch(path + '?auth=' + token, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          score: score,
          passed: passed,
          correct: correct,
          total: total,
          lastAttempt: new Date().toISOString(),
          courseName: _course.title
        })
      });
    }).catch(function (e) { console.warn('[Exam] Save attempt failed:', e); });
  }

  /* ── Certificate Helpers ── */
  function _generateLicense(email, uid, timestamp) {
    var hash = _hashString((email || '') + (uid || '') + timestamp.toString());
    var prefix = 'RKL';
    var year = new Date().getFullYear();
    var hex = Math.abs(hash).toString(16).toUpperCase().padStart(8, '0').slice(0, 8);
    return prefix + '-' + year + '-' + hex;
  }

  function _hashString(str) {
    var hash = 0x811c9dc5;
    for (var i = 0; i < str.length; i++) {
      hash ^= str.charCodeAt(i);
      hash = ((hash >>> 0) * 0x01000193) >>> 0;
    }
    return hash >>> 0;
  }

  function _buildCertHTML(data) {
    // Simple certificate HTML generation
    return '<div style="padding:40px;text-align:center;font-family:Georgia,serif">' +
      '<h1 style="font-size:36px;color:#667eea">Certificate of Completion</h1>' +
      '<p style="font-size:20px;margin:20px 0">This is to certify that</p>' +
      '<h2 style="font-size:28px;color:#333">' + data.name + '</h2>' +
      '<p style="font-size:20px;margin:20px 0">has successfully completed the course</p>' +
      '<h3 style="font-size:24px;color:#667eea">' + data.course + '</h3>' +
      '<p style="font-size:18px;margin:20px 0">with a score of ' + data.score + '%</p>' +
      '<p style="font-size:16px;color:#666">License: ' + data.licenseNumber + '</p>' +
      '<p style="font-size:16px;color:#666">Date: ' + data.examDate + '</p>' +
      '</div>';
  }

  function _storeCertificate(data, user) {
    var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
    var emailKey = data.email.replace(/[.#$\[\]]/g, '_');
    var courseKey = data.course.replace(/[^a-zA-Z0-9]/g, '_').toLowerCase();
    var path = DB_URL + '/certificates/' + emailKey + '/' + courseKey + '.json';

    if (!user || !user.getIdToken) {
      console.error('[Exam] No user or getIdToken method for certificate storage');
      _storeCertificateLocally(data);
      return;
    }

    user.getIdToken().then(function (token) {
      var certData = {
        name: data.name,
        email: data.email,
        course: data.course,
        score: data.score,
        correct: data.correct,
        total: data.total,
        licenseNumber: data.licenseNumber,
        examDate: data.examDate,
        issueDate: data.issueDate,
        uid: data.uid,
        certificateHTML: data.certificateHTML,
        createdAt: new Date().toISOString()
      };
      
      return fetch(path + '?auth=' + token, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(certData)
      });
    }).then(function (response) {
      if (response.ok) {
        console.log('[Exam] Certificate saved to Firebase successfully');
        // Show success message
        if (window.LearnApp && LearnApp.toast) {
          LearnApp.toast('Certificate saved to your profile!', 'success');
<<<<<<< D:/VirtualMachines/vagrant-boxes/sbox/projects/Personal/rkoots.github.io/assets/js/learn/exam.js
<<<<<<< D:/VirtualMachines/vagrant-boxes/sbox/projects/Personal/rkoots.github.io/assets/js/learn/exam.js
=======
        } else {
          console.log('[Exam] Certificate saved to your profile!');
>>>>>>> C:/Users/RajkumarV/.windsurf/worktrees/rkoots.github.io/rkoots.github.io-d0327794/assets/js/learn/exam.js
=======
        } else {
          console.log('[Exam] Certificate saved to your profile!');
>>>>>>> C:/Users/RajkumarV/.windsurf/worktrees/rkoots.github.io/rkoots.github.io-d0327794/assets/js/learn/exam.js
        }
      } else {
        throw new Error('HTTP ' + response.status);
      }
    }).catch(function (e) {
      console.error('[Exam] Certificate storage failed:', e);
      _storeCertificateLocally(data);
      if (window.LearnApp && LearnApp.toast) {
        LearnApp.toast('Certificate saved locally (cloud sync failed)', 'warning');
<<<<<<< D:/VirtualMachines/vagrant-boxes/sbox/projects/Personal/rkoots.github.io/assets/js/learn/exam.js
<<<<<<< D:/VirtualMachines/vagrant-boxes/sbox/projects/Personal/rkoots.github.io/assets/js/learn/exam.js
=======
      } else {
        console.log('[Exam] Certificate saved locally (cloud sync failed)');
>>>>>>> C:/Users/RajkumarV/.windsurf/worktrees/rkoots.github.io/rkoots.github.io-d0327794/assets/js/learn/exam.js
=======
      } else {
        console.log('[Exam] Certificate saved locally (cloud sync failed)');
>>>>>>> C:/Users/RajkumarV/.windsurf/worktrees/rkoots.github.io/rkoots.github.io-d0327794/assets/js/learn/exam.js
      }
    });
  }

  function _storeCertificateLocally(data) {
    try {
      var localCerts = JSON.parse(localStorage.getItem('rkoots_certificates') || '{}');
      var emailKey = data.email.replace(/[.#$\[\]]/g, '_');
      if (!localCerts[emailKey]) localCerts[emailKey] = {};
      var courseKey = data.course.replace(/[^a-zA-Z0-9]/g, '_').toLowerCase();
      localCerts[emailKey][courseKey] = data;
      localStorage.setItem('rkoots_certificates', JSON.stringify(localCerts));
      console.log('[Exam] Certificate saved to localStorage');
    } catch (e) {
      console.error('[Exam] Local storage failed:', e);
    }
  }

  /* ── Helpers ── */
  function _showScreen(screenId) {
    ['examStart', 'examActive', 'examResult'].forEach(function (id) {
      var el = $(id);
      if (el) el.classList.add('hidden');
    });
    var target = $(screenId);
    if (target) target.classList.remove('hidden');
  }

  function _shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
    return arr;
  }

  function _escHtml(str) {
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

}());
