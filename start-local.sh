#!/bin/bash

# Start Jekyll with proper 404 handling for local development
echo "Starting Jekyll with 404 redirect support..."
echo "Visit http://localhost:4000 to test"
echo "Test 404 by visiting http://localhost:4000/nonexistent-page"

# Kill any existing Jekyll processes
pkill -f "jekyll serve" 2>/dev/null || true

# Start Jekyll with 404 handling
bundle exec jekyll serve --livereload --host 0.0.0.0 --port 4000