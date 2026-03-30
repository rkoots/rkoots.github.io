/**
 * RKoots Learning Platform — app.js
 * Handles: navigation, sidebar, search, course/topic rendering, auth UI sync
 */
(function () {
  'use strict';

  /* ── State ── */
  var _activeCourseId = null;
  var _searchIndex = [];

  /* ── DOM refs ── */
  function $(id) { return document.getElementById(id); }

  /* ── Init ── */
  window.LearnApp = {

    init: function () {
      _buildSearchIndex();
      _buildSidebar();
      _buildCourseGrid();
      _initSearch();
      _initSidebarToggle();
      _syncAuthUI();
      _routeFromHash();
      window.addEventListener('hashchange', _routeFromHash);
    },

    showView: function (viewId) {
      document.querySelectorAll('.learn-view').forEach(function (el) {
        el.classList.add('hidden');
      });
      var el = $(viewId);
      if (el) el.classList.remove('hidden');
    },

    showCourseGrid: function () {
      LearnApp.showView('view-home');
      var grid = $('homeCourseGrid');
      if (grid) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
    },

    loadCourse: function (courseId) {
      console.log('[App] Loading course:', courseId);
      var course = _getCourse(courseId);
      if (!course) {
        console.error('[App] Course not found:', courseId);
        return;
      }
      console.log('[App] Found course:', course.title);
      _activeCourseId = courseId;

      LearnApp.showView('view-topic');
      window.location.hash = '#' + courseId;

      /* Breadcrumb */
      $('topicBreadcrumb').innerHTML =
        '<a href="/learn/">Home</a><span class="sep">›</span>' +
        '<span>' + _escHtml(course.category) + '</span><span class="sep">›</span>' +
        '<span>' + _escHtml(course.title) + '</span>';

      /* Icon */
      $('topicIcon').innerHTML = '<i class="' + course.icon + '"></i>';
      $('topicIcon').style.background = 'linear-gradient(135deg,' + course.color + ',#764ba2)';

      /* Title & Meta */
      $('topicTitle').textContent = course.title;
      $('topicTags').innerHTML = course.tags.map(function (t) {
        return '<span class="topic-tag">' + _escHtml(t) + '</span>';
      }).join('');
      $('topicDifficulty').innerHTML = '<i class="fas fa-signal"></i> ' + _ucFirst(course.difficulty);
      $('topicDuration').innerHTML = '<i class="fas fa-clock"></i> ' + course.duration;
      $('topicQuestions').innerHTML = '<i class="fas fa-question-circle"></i> 25 exam questions';

      /* Content */
      $('topicBody').innerHTML = course.content;

      /* Progress bar (if user has a previous score) */
      _loadProgress(courseId);

      /* Highlight active in sidebar */
      document.querySelectorAll('.sb-course').forEach(function (el) {
        el.classList.remove('active');
      });
      var activeLink = document.querySelector('.sb-course[data-id="' + courseId + '"]');
      if (activeLink) {
        activeLink.classList.add('active');
        /* Expand parent category */
        var cat = activeLink.closest('.sb-category');
        if (cat) cat.classList.add('open');
      }

      /* Sync exam button visibility with auth state */
      _syncExamButton();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },

    getActiveCourse: function () {
      console.log('[App] Getting active course. Current ID:', _activeCourseId);
      var course = _activeCourseId ? _getCourse(_activeCourseId) : null;
      console.log('[App] Found course:', course);
      return course;
    },

    toast: function (msg, type) {
      var t = $('learnToast');
      if (!t) return;
      t.textContent = msg;
      t.className = 'learn-toast' + (type ? ' ' + type : '');
      requestAnimationFrame(function () {
        t.classList.add('show');
        setTimeout(function () { t.classList.remove('show'); }, 2800);
      });
    }
  };

  /* ── Private helpers ── */

  function _getCourse(id) {
    var courses = window.LEARN_COURSES || [];
    for (var i = 0; i < courses.length; i++) {
      if (courses[i].id === id) return courses[i];
    }
    return null;
  }

  function _buildSidebar() {
    var courses = window.LEARN_COURSES || [];
    var categories = {};
    courses.forEach(function (c) {
      if (!categories[c.category]) categories[c.category] = [];
      categories[c.category].push(c);
    });

    var nav = $('sidebarNav');
    if (!nav) return;
    var html = '';
    Object.keys(categories).forEach(function (cat) {
      html += '<div class="sb-category open">';
      html += '<div class="sb-cat-header" onclick="this.parentElement.classList.toggle(\'open\')">';
      html += '<span>' + _escHtml(cat) + '</span>';
      html += '<i class="fas fa-chevron-right sb-cat-arrow"></i>';
      html += '</div><div class="sb-cat-courses">';
      categories[cat].forEach(function (c) {
        html += '<a class="sb-course" data-id="' + c.id + '" href="#' + c.id + '" onclick="LearnApp.loadCourse(\'' + c.id + '\');return false;">';
        html += '<i class="' + c.icon + ' sb-course-icon"></i>';
        html += '<span>' + _escHtml(c.title) + '</span>';
        html += '<span class="sb-course-tag">25Q</span>';
        html += '</a>';
      });
      html += '</div></div>';
    });
    nav.innerHTML = html;

    var count = $('courseCount');
    if (count) count.textContent = courses.length + ' courses';
    var stat = $('statCourses');
    if (stat) stat.textContent = courses.length;
  }

  function _buildCourseGrid() {
    var courses = window.LEARN_COURSES || [];
    var grid = $('courseCardGrid');
    if (!grid) return;
    var html = '';
    courses.forEach(function (c) {
      html += '<div class="course-card" onclick="LearnApp.loadCourse(\'' + c.id + '\')">';
      html += '<div class="cc-icon" style="background:linear-gradient(135deg,' + c.color + ',#764ba2)"><i class="' + c.icon + '"></i></div>';
      html += '<div class="cc-title">' + _escHtml(c.title) + '</div>';
      html += '<div class="cc-desc">' + _escHtml(c.description) + '</div>';
      html += '<div class="cc-meta">';
      html += '<span class="cc-difficulty ' + c.difficulty + '">' + _ucFirst(c.difficulty) + '</span>';
      html += '<span class="cc-questions"><i class="fas fa-list-ol"></i> 25 Q</span>';
      html += '</div></div>';
    });
    grid.innerHTML = html;
  }

  function _buildSearchIndex() {
    var courses = window.LEARN_COURSES || [];
    _searchIndex = [];
    courses.forEach(function (c) {
      _searchIndex.push({ type: 'course', id: c.id, title: c.title, sub: c.category, icon: c.icon });
      c.tags.forEach(function (tag) {
        _searchIndex.push({ type: 'tag', id: c.id, title: c.title + ' — ' + tag, sub: 'Tag: ' + tag + ' (25Q)', icon: c.icon });
      });
    });
  }

  function _initSearch() {
    var input = $('globalSearch');
    var results = $('searchResults');
    if (!input || !results) return;

    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      if (q.length < 2) { results.classList.remove('open'); return; }

      var matches = _searchIndex.filter(function (item) {
        return item.title.toLowerCase().indexOf(q) !== -1 || item.sub.toLowerCase().indexOf(q) !== -1;
      }).slice(0, 8);

      if (!matches.length) { results.classList.remove('open'); return; }

      results.innerHTML = matches.map(function (m) {
        return '<a class="sr-item" href="#' + m.id + '" onclick="LearnApp.loadCourse(\'' + m.id + '\');document.getElementById(\'globalSearch\').value=\'\';document.getElementById(\'searchResults\').classList.remove(\'open\');return false;">' +
          '<i class="' + m.icon + ' sr-item-icon"></i>' +
          '<div class="sr-item-text"><strong>' + _escHtml(m.title) + '</strong><small>' + _escHtml(m.sub) + '</small></div>' +
          '</a>';
      }).join('');
      results.classList.add('open');
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest('.learn-search-wrap')) {
        results.classList.remove('open');
      }
    });
  }

  function _initSidebarToggle() {
    var btn = $('sidebarToggle');
    var sidebar = $('learnSidebar');
    if (!btn || !sidebar) return;

    var overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    document.body.appendChild(overlay);

    btn.addEventListener('click', function () {
      sidebar.classList.toggle('open');
      overlay.classList.toggle('show');
    });
    overlay.addEventListener('click', function () {
      sidebar.classList.remove('open');
      overlay.classList.remove('show');
    });
  }

  function _syncAuthUI() {
    GameAuth.onAuthChange(function (user) {
      var signedIn = document.querySelectorAll('.auth-signed-in');
      var signedOut = document.querySelectorAll('.auth-signed-out');
      signedIn.forEach(function (el) { el.style.display = user ? 'flex' : 'none'; });
      signedOut.forEach(function (el) { el.style.display = user ? 'none' : 'flex'; });
      if (user) {
        document.querySelectorAll('.auth-name').forEach(function (el) { el.textContent = user.displayName || 'Learner'; });
        document.querySelectorAll('.auth-avatar-img').forEach(function (el) {
          el.innerHTML = user.photoURL
            ? '<img src="' + user.photoURL + '" alt="avatar">'
            : (user.displayName || 'L').charAt(0).toUpperCase();
        });
      }
      _syncExamButton();
      if (user && _activeCourseId) _loadProgress(_activeCourseId);
    });
  }

  function _syncExamButton() {
    var user = GameAuth.getCurrentUser ? GameAuth.getCurrentUser() : null;
    var authGate = $('examAuthGate');
    var startBtn = $('examStartBtn');
    if (authGate) authGate.style.display = user ? 'none' : 'block';
    if (startBtn) startBtn.style.display = user ? 'flex' : 'none';
  }

  function _loadProgress(courseId) {
    var user = GameAuth.getCurrentUser ? GameAuth.getCurrentUser() : null;
    if (!user) { var pb = $('topicProgressBar'); if (pb) pb.style.display = 'none'; return; }

    var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';
    var path = DB_URL + '/certificates/' + _safeKey(user.email) + '/' + courseId + '.json';
    fetch(path)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        var pb = $('topicProgressBar');
        if (data && data.score != null) {
          if (pb) pb.style.display = 'flex';
          var fill = $('progressFill');
          var val = $('progressValue');
          if (fill) fill.style.width = data.score + '%';
          if (val) val.textContent = data.score + '%';
        } else {
          if (pb) pb.style.display = 'none';
        }
      })
      .catch(function () {});
  }

  function _routeFromHash() {
    var hash = window.location.hash.replace('#', '');
    if (hash && _getCourse(hash)) {
      LearnApp.loadCourse(hash);
    } else {
      LearnApp.showView('view-home');
    }
  }

  function _escHtml(str) {
    return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }

  function _ucFirst(str) {
    return str ? str.charAt(0).toUpperCase() + str.slice(1) : '';
  }

  function _safeKey(email) {
    return (email || '').replace(/[.#$\[\]]/g, '_');
  }

  /* ── Bootstrap ── */
  document.addEventListener('DOMContentLoaded', function () {
    GameAuth.init();
    LearnApp.init();
  });

}());
