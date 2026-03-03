@echo off
REM Start Jekyll with proper 404 handling for local development
echo Starting Jekyll with 404 redirect support...
echo Visit http://localhost:4000 to test
echo Test 404 by visiting http://localhost:4000/nonexistent-page

REM Kill any existing Jekyll processes
taskkill /F /IM "ruby.exe" /FI "WINDOWTITLE eq *jekyll*" 2>nul || taskkill /F /IM "jekyll.exe" 2>nul

REM Start Jekyll with 404 handling
bundle exec jekyll serve --livereload --host 0.0.0.0 --port 4000