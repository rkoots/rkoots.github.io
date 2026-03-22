/**
 * Leaderboard Component — RKoots Games
 * Uses Firebase Realtime Database REST API.
 * Schema: /scorecard/{challenge}/{userId} → { name, score, timestamp }
 */
(function () {
  'use strict';

  var DB_URL = window.FIREBASE_DB_URL || 'https://games-rkoots-default-rtdb.firebaseio.com';

  /* ---- REST helpers ---- */
  function dbGet(path) {
    return fetch(DB_URL + path + '.json')
      .then(function (r) { return r.json(); })
      .catch(function (e) { console.error('[Leaderboard] GET error', e); return null; });
  }

  function dbPatch(path, data, idToken) {
    var headers = { 'Content-Type': 'application/json' };
    var url = DB_URL + path + '.json';
    if (idToken) url += '?auth=' + idToken;
    return fetch(url, { method: 'PATCH', headers: headers, body: JSON.stringify(data) })
      .then(function (r) { return r.json(); });
  }

  /* ---- Seed helpers (for initial data population) ---- */
  var SEED_NAMES = [
    'AcePlayer99','Ninja_Coder','TurboTyper','ClickMaster','SpeedDemon',
    'QuizKing','ByteRunner','ProGamer42','FlashFinger','MemoryWiz'
  ];

  window.GameLeaderboard = {

    /**
     * Fetch scores for a challenge, return sorted array.
     * @param {string} challengeId
     * @returns {Promise<Array>}
     */
    fetchScores: function (challengeId) {
      return dbGet('/scorecard/' + challengeId).then(function (data) {
        if (!data) return [];
        return Object.entries(data).map(function (entry) {
          return Object.assign({ userId: entry[0] }, entry[1]);
        }).sort(function (a, b) { return b.score - a.score; });
      });
    },

    /**
     * Submit a score. Only updates if new score > existing score.
     * @param {string} challengeId
     * @param {string} userId
     * @param {string} name
     * @param {number} score
     * @param {string|null} idToken
     * @returns {Promise<{updated:boolean, reason:string}>}
     */
    submitScore: function (challengeId, userId, name, score, idToken) {
      return dbGet('/scorecard/' + challengeId + '/' + userId)
        .then(function (existing) {
          if (existing && existing.score >= score) {
            return { updated: false, reason: 'Score not higher than existing (' + existing.score + ')' };
          }
          var payload = { name: name, score: score, timestamp: Date.now() };
          return dbPatch('/scorecard/' + challengeId + '/' + userId, payload, idToken)
            .then(function () { return { updated: true, reason: 'Score saved!' }; });
        });
    },

    /**
     * Render leaderboard into a container element.
     * @param {string} containerId  - DOM element id
     * @param {Array}  scores       - sorted scores array
     * @param {string|null} currentUserId
     */
    render: function (containerId, scores, currentUserId) {
      var el = document.getElementById(containerId);
      if (!el) return;

      if (!scores || scores.length === 0) {
        el.innerHTML = '<div class="lb-loading">No scores yet. Be the first!</div>';
        return;
      }

      var top10 = scores.slice(0, 10);
      var userRank = currentUserId
        ? scores.findIndex(function (s) { return s.userId === currentUserId; }) + 1
        : -1;
      var userInTop10 = userRank > 0 && userRank <= 10;

      var medals = ['🥇', '🥈', '🥉'];
      var medalClass = ['gold', 'silver', 'bronze'];

      var html = '';
      top10.forEach(function (s, i) {
        var rank = i + 1;
        var rankHtml = rank <= 3
          ? '<span class="lb-rank ' + medalClass[i] + '">' + medals[i] + '</span>'
          : '<span class="lb-rank">#' + rank + '</span>';

        var rowClass = 'leaderboard-row';
        if (rank === 1) rowClass += ' top-1';
        else if (rank === 2) rowClass += ' top-2';
        else if (rank === 3) rowClass += ' top-3';
        if (s.userId === currentUserId) rowClass += ' current-user';

        html += '<div class="' + rowClass + '">';
        html += rankHtml;
        html += '<span class="lb-name">' + _escHtml(s.name) + (s.userId === currentUserId ? ' (You)' : '') + '</span>';
        html += '<span class="lb-score">' + s.score + '</span>';
        html += '</div>';
      });

      if (currentUserId && !userInTop10 && userRank > 0) {
        var userScore = scores[userRank - 1];
        html += '<div class="lb-divider"></div>';
        html += '<div class="leaderboard-row current-user">';
        html += '<span class="lb-rank">#' + userRank + '</span>';
        html += '<span class="lb-name">' + _escHtml(userScore.name) + ' (You)</span>';
        html += '<span class="lb-score">' + userScore.score + '</span>';
        html += '</div>';
      }

      el.innerHTML = html;

      if (currentUserId && userRank > 0) {
        var footer = el.closest('.leaderboard-panel');
        if (footer) {
          var rankEl = footer.querySelector('.lb-user-rank');
          if (rankEl) rankEl.textContent = 'Your rank: #' + userRank + ' of ' + scores.length;
        }
      }
    },

    /**
     * Load and render leaderboard in one call.
     */
    load: function (challengeId, containerId, currentUserId) {
      var el = document.getElementById(containerId);
      if (el) el.innerHTML = '<div class="lb-loading"><i class="fas fa-spinner fa-spin"></i> Loading...</div>';
      return this.fetchScores(challengeId).then(function (scores) {
        window.GameLeaderboard.render(containerId, scores, currentUserId);
        return scores;
      });
    },

    /**
     * Seed dummy data for a challenge (run once from console or seed page).
     * @param {string} challengeId
     * @param {Function} scoreGenerator  - returns a score number for index i
     */
    seedDummyData: function (challengeId, scoreGenerator) {
      var promises = SEED_NAMES.map(function (name, i) {
        var uid = 'seed_' + challengeId + '_' + i;
        var score = scoreGenerator ? scoreGenerator(i) : Math.floor(Math.random() * 900) + 100;
        var data = { name: name, score: score, timestamp: Date.now() - (i * 86400000) };
        return dbPatch('/scorecard/' + challengeId + '/' + uid, data, null)
          .then(function () { console.log('[Seed] ' + name + ' -> ' + score); });
      });
      return Promise.all(promises).then(function () {
        console.log('[Seed] All ' + challengeId + ' dummy data seeded!');
      });
    },

    /**
     * Seed all challenges with realistic data.
     * Call: GameLeaderboard.seedAllChallenges() from browser console.
     */
    seedAllChallenges: function () {
      return Promise.all([
        this.seedDummyData('reaction-speed', function (i) { return Math.floor(850 - i * 40 + Math.random() * 30); }),
        this.seedDummyData('number-memory', function (i) { return Math.max(3, 12 - i + Math.floor(Math.random() * 3)); }),
        this.seedDummyData('typing-speed', function (i) { return Math.floor(120 - i * 7 + Math.random() * 10); })
      ]).then(function () {
        console.log('[Seed] All challenges seeded!');
      });
    }
  };

  function _escHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

}());
