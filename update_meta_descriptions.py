#!/usr/bin/env python3
"""
Script to update meta descriptions for all CSS loader collections
"""

import os
import re
import glob

# Mapping of page names to their descriptive meta descriptions
PAGE_DESCRIPTIONS = {
    '3d': 'Discover The 3D CSS Loaders Collection with 12 stunning single-element animations. Three-dimensional transformations and depth effects crafted with pure CSS by Temani Afif.',
    'arcade': 'Experience The Arcade CSS Loaders Collection with 10 retro single-element animations. Classic arcade-inspired loading effects with nostalgic gaming vibes by Temani Afif.',
    'arrow': 'Explore The Arrow CSS Loaders Collection with 10 directional single-element animations. Dynamic arrow movements and flow indicators created with pure CSS by Temani Afif.',
    'blob': 'Discover The Blob CSS Loaders Collection with 20 organic single-element animations. Fluid blob morphing and amorphous shapes crafted with pure CSS by Temani Afif.',
    'bouncing': 'Experience The Bouncing CSS Loaders Collection with 12 playful single-element animations. Energetic bouncing effects and elastic motions by Temani Afif.',
    'classic': 'Discover The Classic CSS Loaders Collection with 40 timeless single-element animations. Essential loading patterns and fundamental spinner designs by Temani Afif.',
    'clones': 'Explore The Clones CSS Loaders Collection with 20 synchronized single-element animations. Coordinated clone movements and mirror effects by Temani Afif.',
    'colorful': 'Experience The Colorful CSS Loaders Collection with 20 vibrant single-element animations. Rich color gradients and vivid spectrum effects by Temani Afif.',
    'continuous': 'Discover The Continuous CSS Loaders Collection with 10 flowing single-element animations. Seamless looping patterns and endless motion effects by Temani Afif.',
    'cut': 'Explore The Cut CSS Loaders Collection with 10 geometric single-element animations. Creative cut-out effects and negative space designs by Temani Afif.',
    'dots': 'Experience The Dots CSS Loaders Collection with 50 playful single-element animations. Versatile dot patterns and particle movements by Temani Afif.',
    'dots-bars': 'Discover The Dots vs Bars CSS Loaders Collection with 20 hybrid single-element animations. Creative combinations of dots and bars by Temani Afif.',
    'eyes': 'Explore The Eyes CSS Loaders Collection with 10 expressive single-element animations. Animated eye movements and blinking effects by Temani Afif.',
    'factory': 'Experience The Factory CSS Loaders Collection with 8 mechanical single-element animations. Industrial-themed loading and gear mechanisms by Temani Afif.',
    'filling': 'Discover The Filling CSS Loaders Collection with 20 progressive single-element animations. Liquid filling effects and container animations by Temani Afif.',
    'flipping': 'Explore The Flipping CSS Loaders Collection with 20 dynamic single-element animations. Card flip effects and rotation transitions by Temani Afif.',
    'glowing': 'Experience The Glowing CSS Loaders Collection with 12 luminous single-element animations. Neon glow effects and radiant light patterns by Temani Afif.',
    'hungry': 'Discover The Hungry CSS Loaders Collection with 8 playful single-element animations. Eating animations and consumption effects by Temani Afif.',
    'hypnotic': 'Explore The Hypnotic CSS Loaders Collection with 20 mesmerizing single-element animations. Hypnotic spiral patterns and trance-inducing effects by Temani Afif.',
    'infinity': 'Experience The Infinity CSS Loaders Collection with 20 endless single-element animations. Infinite loops and perpetual motion designs by Temani Afif.',
    'line': 'Discover The Line CSS Loaders Collection with 20 minimalist single-element animations. Clean line animations and geometric progress indicators by Temani Afif.',
    'maze': 'Explore The Maze CSS Loaders Collection with 10 intricate single-element animations. Complex maze patterns and puzzle-solving animations by Temani Afif.',
    'mechanic': 'Experience The Mechanic CSS Loaders Collection with 12 industrial single-element animations. Mechanical movements and engineering animations by Temani Afif.',
    'moving': 'Discover The Moving CSS Loaders Collection with 10 dynamic single-element animations. Smooth motion transitions and movement patterns by Temani Afif.',
    'nature': 'Explore The Nature CSS Loaders Collection with 16 organic single-element animations. Natural movements and organic growth patterns by Temani Afif.',
    'polygons': 'Experience The Polygons CSS Loaders Collection with 12 geometric single-element animations. Complex polygon shapes and multi-sided designs by Temani Afif.',
    'progress': 'Discover The Progress CSS Loaders Collection with 20 functional single-element animations. Progress indicators and completion animations by Temani Afif.',
    'pulsing': 'Explore The Pulsing CSS Loaders Collection with 10 rhythmic single-element animations. Pulsating effects and heartbeat patterns by Temani Afif.',
    'rolling': 'Experience The Rolling CSS Loaders Collection with 10 smooth single-element animations. Rolling movements and circular motion effects by Temani Afif.',
    'shuriken': 'Discover The Shuriken CSS Loaders Collection with 10 ninja-inspired single-element animations. Throwing star rotations and martial arts effects by Temani Afif.',
    'square': 'Explore The Square CSS Loaders Collection with 11 geometric single-element animations. Perfect square transformations and block patterns by Temani Afif.',
    'circle': 'Experience The Circle CSS Loaders Collection with 11 circular single-element animations. Perfect circle rotations and ring patterns by Temani Afif.',
    'thin': 'Discover The Thin CSS Loaders Collection with 10 elegant single-element animations. Delicate line animations and minimalist designs by Temani Afif.',
    'time': 'Explore The Time CSS Loaders Collection with 10 temporal single-element animations. Clock movements and time-based animations by Temani Afif.',
    'wavy': 'Experience The Wavy CSS Loaders Collection with 16 fluid single-element animations. Wave patterns and undulating motion effects by Temani Afif.',
    'dancers': 'Discover The Dancers CSS Loaders Collection with 10 rhythmic single-element animations. Dancing figures and choreographed movements by Temani Afif.',
}

def update_meta_description(file_path, page_name, description):
    """Update meta description in an HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Update meta name="description"
        meta_pattern = r'<meta name="description" content="[^"]*">'
        new_meta = f'<meta name="description" content="{description}">'
        content = re.sub(meta_pattern, new_meta, content)
        
        # Update meta property="og:description"
        og_pattern = r'<meta property="og:description" content="[^"]*">'
        new_og = f'<meta property="og:description" content="{description}">'
        content = re.sub(og_pattern, new_og, content)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Updated: {page_name}")
        return True
    except Exception as e:
        print(f"Error updating {page_name}: {e}")
        return False

def main():
    base_dir = "tools/free-ui-components"
    updated_count = 0
    total_count = 0
    
    for page_name, description in PAGE_DESCRIPTIONS.items():
        file_path = os.path.join(base_dir, page_name, "index.html")
        
        if os.path.exists(file_path):
            total_count += 1
            if update_meta_description(file_path, page_name, description):
                updated_count += 1
        else:
            print(f"File not found: {file_path}")
    
    print(f"\nSummary: Updated {updated_count}/{total_count} meta descriptions")

if __name__ == "__main__":
    main()
