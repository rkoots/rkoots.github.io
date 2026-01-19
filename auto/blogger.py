
import os
import json
import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/blogger']
TOKEN_FILE = 'token.json'  # Stores access/refresh tokens

BLOG_ID = os.getenv("BLOG_ID") # Replace this with your actual Blogger blog ID

CLIENT_ID =  os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def authenticate_direct():
    creds = None

    # Reuse saved credentials if available
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If no valid credentials available, do auth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config({
                "installed": {
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"]
                }
            }, SCOPES)

            creds = flow.run_console()  # Use this instead of

        # Save credentials for next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return build('blogger', 'v3', credentials=creds)


def create_post(service, title, content):
    post_body = {
        'kind': 'blogger#post',
        'title': title,
        'content': content
    }

    post = service.posts().insert(blogId=BLOG_ID, body=post_body, isDraft=False).execute()
    print(f"✅ Post published: {post['url']}")

if __name__ == '__main__':
    service = authenticate_direct()

    # Sample post content
    blog_title = "🚀 Hello from Python Blogger Automation!"
    blog_content = f"""
    <h2>This is an automated blog post</h2>
    <p><strong>Published:</strong> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <p>This post was generated and published using a headless Python script with Blogger API.</p>
    <p>Automation is awesome! 🔥</p>
    """

    create_post(service, blog_title, blog_content)