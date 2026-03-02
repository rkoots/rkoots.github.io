#!/bin/bash

# RKoots Technical Knowledge Hub - Setup Script

echo "🚀 Setting up RKoots Technical Knowledge Hub..."

# Remove existing Gemfile.lock if it exists
if [ -f "Gemfile.lock" ]; then
  echo "🗑️  Removing existing Gemfile.lock..."
  rm Gemfile.lock
fi

# Install dependencies
echo "📦 Installing Ruby dependencies..."
bundle install

# Build the site locally
echo "🏗️  Building the site..."
bundle exec jekyll build

# Serve the site locally
echo "🌐 Starting local server..."
echo "Site will be available at: http://localhost:4000"
echo "Press Ctrl+C to stop the server"
bundle exec jekyll serve --livereload