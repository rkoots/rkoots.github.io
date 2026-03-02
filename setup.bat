@echo off
REM RKoots Technical Knowledge Hub - Setup Script for Windows

echo 🚀 Setting up RKoots Technical Knowledge Hub...

REM Remove existing Gemfile.lock if it exists
if exist Gemfile.lock (
    echo 🗑️  Removing existing Gemfile.lock...
    del Gemfile.lock
)

REM Install dependencies
echo 📦 Installing Ruby dependencies...
bundle install

if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

REM Build the site locally
echo 🏗️  Building the site...
bundle exec jekyll build

if %errorlevel% neq 0 (
    echo ❌ Failed to build site
    pause
    exit /b 1
)

REM Serve the site locally
echo 🌐 Starting local server...
echo Site will be available at: http://localhost:4000
echo Press Ctrl+C to stop the server
bundle exec jekyll serve --livereload

pause