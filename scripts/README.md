# RSS Blog Generator Configuration

## Environment Variables Required

Add the following secrets to your GitHub repository:

### Email Configuration
- `SENDER_EMAIL`: market007ads@gmail.com
- `SENDER_PASSWORD`: Gmail app password for the sender account
- `RECIPIENT_EMAIL`: rkoots.rkoots_autobot@blogger.com
- `SMTP_SERVER`: smtp.gmail.com (default)
- `SMTP_PORT`: 587 (default)

## Setup Instructions

### 1. Gmail App Password
Since you're using Gmail, you need to create an app password:

1. Go to your Google Account settings
2. Enable 2-factor authentication if not already enabled
3. Go to Security → App passwords
4. Generate a new app password for "Mail" on "Other device"
5. Use this app password as the `SENDER_PASSWORD` secret

### 2. GitHub Secrets
Add the following secrets to your repository:
1. Go to your repository on GitHub
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Add each of the required environment variables

### 3. RSS Sources
The script currently fetches from:
- https://www.theverge.com/rss/index.xml
- https://openai.com/blog/rss.xml
- https://openai.com/news/rss.xml

You can modify the `rss_feeds` list in the script to add more sources.

## Features

- **Hourly Execution**: Runs automatically every hour via GitHub Actions cron
- **Recent Content Only**: Only processes articles published in the last hour
- **Email Delivery**: Sends formatted blog posts to the specified email address
- **Content Extraction**: Fetches full article content when possible
- **Error Handling**: Comprehensive logging and error handling
- **HTML Email**: Sends nicely formatted HTML emails

## Manual Execution

You can also trigger the workflow manually:
1. Go to Actions tab in your GitHub repository
2. Select "RSS Blog Generator" workflow
3. Click "Run workflow"

## Customization

### Modify RSS Sources
Edit the `rss_feeds` list in `rss_blog_generator.py`:

```python
self.rss_feeds = [
    "https://www.theverge.com/rss/index.xml",
    "https://openai.com/blog/rss.xml",
    "https://openai.com/news/rss.xml",
    # Add more RSS feeds here
]
```

### Change Time Filter
Modify the `filter_recent_entries` call to change the time window:

```python
# Process last 2 hours instead of 1 hour
recent_entries = self.filter_recent_entries(all_entries, 2)
```

### Customize Email Template
Edit the HTML template in the `send_email` method to change the email formatting.

## Troubleshooting

### Common Issues
1. **Authentication Failed**: Ensure you're using an app password, not your regular Gmail password
2. **No Recent Articles**: The script only processes articles from the last hour - check if there are any recent posts
3. **RSS Feed Errors**: Some RSS feeds may be temporarily unavailable

### Logs
Check the GitHub Actions logs for detailed error messages and execution status.

## Security Notes

- Never commit sensitive information like passwords to your repository
- Use GitHub Secrets for all sensitive configuration
- Regularly rotate your app passwords
- Monitor the workflow execution for any unusual activity