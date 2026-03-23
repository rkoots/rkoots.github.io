/**
 * Fullscreen utility for 2-player games
 * Automatically enters fullscreen on game start
 */
var GameFullscreen = (function() {
  var container = null;
  var button = null;
  var isFullscreen = false;
  var autoEnterOnStart = true;

  function init(containerSelector, options) {
    container = document.querySelector(containerSelector);
    if (!container) {
      console.warn('Fullscreen: Container not found');
      return;
    }

    options = options || {};
    autoEnterOnStart = options.autoEnterOnStart !== false;

    createButton();
    setupEventListeners();
  }

  function createButton() {
    button = document.createElement('button');
    button.className = 'btn-fullscreen';
    button.innerHTML = '<i class="fas fa-expand"></i>';
    button.title = 'Toggle Fullscreen (F11)';
    button.style.display = 'none';
    document.body.appendChild(button);

    button.addEventListener('click', toggle);
  }

  function setupEventListeners() {
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
    document.addEventListener('mozfullscreenchange', handleFullscreenChange);
    document.addEventListener('MSFullscreenChange', handleFullscreenChange);

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && isFullscreen) {
        exit();
      }
    });
  }

  function enter() {
    if (isFullscreen) return;

    button.style.display = 'flex';
    container.classList.add('fullscreen-mode');
    isFullscreen = true;
    button.innerHTML = '<i class="fas fa-compress"></i>';
    button.title = 'Exit Fullscreen (ESC)';

    var elem = document.documentElement;
    if (elem.requestFullscreen) {
      elem.requestFullscreen().catch(function(err) {
        console.log('Fullscreen request failed:', err);
      });
    } else if (elem.webkitRequestFullscreen) {
      elem.webkitRequestFullscreen();
    } else if (elem.mozRequestFullScreen) {
      elem.mozRequestFullScreen();
    } else if (elem.msRequestFullscreen) {
      elem.msRequestFullscreen();
    }
  }

  function exit() {
    if (!isFullscreen) return;

    container.classList.remove('fullscreen-mode');
    isFullscreen = false;
    button.innerHTML = '<i class="fas fa-expand"></i>';
    button.title = 'Toggle Fullscreen (F11)';

    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen();
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
    }
  }

  function toggle() {
    if (isFullscreen) {
      exit();
    } else {
      enter();
    }
  }

  function handleFullscreenChange() {
    var fullscreenElement = document.fullscreenElement || 
                           document.webkitFullscreenElement || 
                           document.mozFullScreenElement || 
                           document.msFullscreenElement;

    if (!fullscreenElement && isFullscreen) {
      container.classList.remove('fullscreen-mode');
      isFullscreen = false;
      button.innerHTML = '<i class="fas fa-expand"></i>';
      button.title = 'Toggle Fullscreen (F11)';
    }
  }

  function onGameStart() {
    if (autoEnterOnStart) {
      setTimeout(function() {
        enter();
      }, 300);
    }
  }

  function showButton() {
    if (button) {
      button.style.display = 'flex';
    }
  }

  function hideButton() {
    if (button) {
      button.style.display = 'none';
    }
  }

  return {
    init: init,
    enter: enter,
    exit: exit,
    toggle: toggle,
    onGameStart: onGameStart,
    showButton: showButton,
    hideButton: hideButton,
    isFullscreen: function() { return isFullscreen; }
  };
})();
