# Fullscreen Feature for 2-Player Games

## Overview
All 2-player games now support automatic fullscreen mode that activates when the game starts, providing an immersive full-screen experience perfect for face-to-face gameplay.

## Features

### Automatic Activation
- Fullscreen mode automatically triggers when a game starts
- Provides distraction-free gaming experience
- Optimized for mobile and desktop devices

### Manual Control
- Floating fullscreen toggle button (top-right corner)
- Click to enter/exit fullscreen anytime
- ESC key to exit fullscreen
- Keyboard shortcut: F11 (browser native)

### Visual Design
- Semi-transparent button with backdrop blur
- Expands/compress icon based on state
- Smooth transitions and animations
- Z-index: 9999 (always on top)

## Implementation

### Files Created/Modified

**New Files:**
- `assets/js/games/fullscreen.js` - Fullscreen utility library

**Modified Files:**
- `assets/css/games.css` - Added fullscreen styles
- `games/two-player/tic-tac-toe.html` - Added fullscreen
- `games/two-player/connect4.html` - Added fullscreen
- `games/two-player/quick-draw.html` - Added fullscreen
- `games/two-player/tap-battle.html` - Added fullscreen
- `games/two-player/color-match.html` - Added fullscreen

### CSS Classes

**`.btn-fullscreen`**
- Fixed position button (top-right)
- 44px × 44px (touch-friendly)
- Semi-transparent background with blur
- Smooth hover/active states

**`.game-container.fullscreen-mode`**
- Fixed position covering viewport
- Hides game header
- Maximizes game board area
- Centers content vertically

### JavaScript API

```javascript
// Initialize fullscreen for a game
GameFullscreen.init('.game-container', { 
  autoEnterOnStart: true 
});

// Trigger fullscreen on game start
GameFullscreen.onGameStart();

// Manual control
GameFullscreen.enter();
GameFullscreen.exit();
GameFullscreen.toggle();

// Button visibility
GameFullscreen.showButton();
GameFullscreen.hideButton();

// Check state
GameFullscreen.isFullscreen();
```

## Usage Pattern

### Standard Implementation

```html
<!-- Include fullscreen script -->
<script src="/assets/js/games/fullscreen.js"></script>

<script>
(function() {
  var gameStarted = false;
  
  // Initialize fullscreen
  GameFullscreen.init('.game-container', { 
    autoEnterOnStart: true 
  });
  
  function startGame() {
    // Trigger fullscreen when game starts
    GameFullscreen.onGameStart();
    // ... rest of game logic
  }
  
  // Or trigger on first interaction
  function handleFirstMove() {
    if (!gameStarted) {
      gameStarted = true;
      GameFullscreen.onGameStart();
    }
    // ... handle move
  }
})();
</script>
```

## Browser Compatibility

### Fullscreen API Support
- Chrome/Edge 71+
- Firefox 64+
- Safari 16.4+
- iOS Safari 16.4+
- Chrome Android 71+

### Fallback Behavior
- If Fullscreen API unavailable, CSS-only fullscreen mode activates
- Button still functional for CSS fullscreen
- Graceful degradation on older browsers

## User Experience

### Desktop
1. User clicks "Start Game"
2. Game automatically enters fullscreen (300ms delay)
3. Fullscreen button appears in top-right
4. User can exit with ESC or button click

### Mobile
1. User taps "Start Game"
2. Game enters fullscreen mode
3. Fullscreen button visible for manual control
4. Optimized for portrait and landscape

### Face-to-Face Play
- Fullscreen removes distractions
- Maximizes game board visibility
- Players sit opposite each other
- Clear player zones and controls

## Accessibility

- **Keyboard Support**: ESC key exits fullscreen
- **Touch Support**: 44px minimum button size
- **Visual Feedback**: Clear icon states
- **No Motion Sickness**: Smooth 300ms delay before activation

## Performance

- Lightweight JavaScript (~150 lines)
- CSS-only animations
- No external dependencies
- Minimal DOM manipulation

## Customization Options

### Disable Auto-Enter
```javascript
GameFullscreen.init('.game-container', { 
  autoEnterOnStart: false 
});
```

### Custom Delay
```javascript
function startGame() {
  setTimeout(function() {
    GameFullscreen.enter();
  }, 500); // Custom delay
}
```

### Hide Button
```javascript
GameFullscreen.init('.game-container');
GameFullscreen.hideButton(); // Hide toggle button
```

## Testing Checklist

- [ ] Fullscreen activates on game start
- [ ] Button appears in correct position
- [ ] ESC key exits fullscreen
- [ ] Button click toggles fullscreen
- [ ] Works on mobile devices
- [ ] Works in portrait/landscape
- [ ] No layout breaks in fullscreen
- [ ] Smooth transitions
- [ ] Browser back button doesn't break state

## Known Limitations

1. **iOS Safari**: Requires user gesture for fullscreen
2. **Some Android browsers**: May show notification bar
3. **Older browsers**: Falls back to CSS fullscreen only
4. **Picture-in-Picture**: May conflict with fullscreen

## Future Enhancements

- [ ] Orientation lock for mobile
- [ ] Fullscreen analytics tracking
- [ ] Custom fullscreen layouts per game
- [ ] Fullscreen preferences persistence
- [ ] Wake lock API integration

## Games with Fullscreen

### Implemented
- ✅ Tic Tac Toe
- ✅ Connect 4
- ✅ Quick Draw
- ✅ Tap Battle
- ✅ Color Match Race

### To Be Implemented
- Ping Pong
- Reaction Tap
- Math Duel
- Rock Paper Scissors
- Memory Match
- Word Scramble Duel
- Dots & Boxes
- Nim Strategy

## Support

For issues or questions about fullscreen functionality:
1. Check browser console for errors
2. Verify Fullscreen API support
3. Test with different browsers
4. Check mobile device compatibility
