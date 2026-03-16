# Google Indexing API Setup Instructions

## Prerequisites
- Python 3.10 or higher
- Google Cloud account with billing enabled
- Website ownership verified in Google Search Console

## Step 1: Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click on project dropdown and select "NEW PROJECT"
3. Enter project name (e.g., "indexing-api-project")
4. Click "CREATE"

## Step 2: Enable Google Indexing API
1. In your new project, navigate to "APIs & Services" > "Library"
2. Search for "Google Indexing API"
3. Click on it and then click "ENABLE"
4. Wait for the API to be enabled

## Step 3: Create Service Account
1. Go to "APIs & Services" > "Credentials"
2. Click "+ CREATE CREDENTIALS" and select "Service Account"
3. Enter service account name (e.g., "indexing-api-service")
4. Add description: "Service account for Google Indexing API submissions"
5. Click "CREATE AND CONTINUE"
6. Skip granting roles (not needed for this API)
7. Click "DONE"

## Step 4: Generate Service Account Key
1. In the Credentials page, find your service account
2. Click on the service account name
3. Go to "KEYS" tab
4. Click "ADD KEY" > "Create new key"
5. Select "JSON" as key type
6. Click "CREATE"
7. The JSON key file will be downloaded automatically
8. Rename it to `service-account-key.json` and place it in the same directory as the script

## Step 5: Verify Website Ownership
1. Go to [Google Search Console](https://search.google.com/search-console/)
2. Add your property (e.g., `https://rkoots.github.io/`)
3. Verify ownership using any available method (HTML file, DNS, etc.)
4. This step is required for the Indexing API to work

## Step 6: Install Dependencies
```bash
pip install requests google-auth google-auth-httplib2 google-auth-oauthlib
```

## Step 7: Configure Script
Edit the configuration variables at the top of `index.py`:
- `SERVICE_ACCOUNT_FILE`: Path to your service account JSON key
- `SITEMAP_URL`: Your sitemap URL (default: https://rkoots.github.io/sitemap.xml)
- `MAX_WORKERS`: Number of concurrent threads (default: 5)

## Step 8: Run the Script
```bash
python index.py
```

## Important Notes
- The Indexing API has quota limits (600 requests per minute per project)
- Use `MAX_WORKERS=5` and `RATE_LIMIT_DELAY=1.0` to stay within limits
- Only submit URLs that you own and have verified in Search Console
- The script creates a log file `indexing_submission.log` for debugging
- Failed submissions are retried automatically with exponential backoff

## Troubleshooting
- **403 Forbidden**: Ensure Indexing API is enabled and website is verified
- **401 Unauthorized**: Check service account key file path and permissions
- **429 Too Many Requests**: Reduce MAX_WORKERS or increase RATE_LIMIT_DELAY
- **No URLs found**: Verify sitemap URL is accessible and contains `<loc>` tags

## API Response Types
- `URL_UPDATED`: Notify Google that a URL has been updated
- `URL_DELETED`: Notify Google that a URL has been removed (not used in this script)

## Security Considerations
- Keep your service account key file secure and never commit it to version control
- Add `service-account-key.json` to your `.gitignore` file
- The key has access to submit URLs for your verified properties only
