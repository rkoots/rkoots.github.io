#!/usr/bin/env python3
"""
Google Indexing API URL Submission Script

This script reads URLs from a sitemap and submits them to Google's Indexing API
for faster indexing. Uses service account authentication with OAuth2.

Author: Auto-generated script
Requirements: Python 3.10+
"""

import sys
import time
import logging
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Configuration variables
SERVICE_ACCOUNT_FILE = "service-account-key.json"  # Path to your service account JSON key
SITEMAP_URL = "https://rkoots.github.io/sitemap.xml"  # Your sitemap URL
MAX_WORKERS = 5  # Maximum concurrent threads (Google recommends staying under 10)
RATE_LIMIT_DELAY = 1.0  # Seconds to wait between requests (respects rate limits)
MAX_RETRIES = 3  # Maximum retry attempts per URL
RETRY_BACKOFF_FACTOR = 2  # Exponential backoff multiplier

# OAuth scope for Google Indexing API
INDEXING_SCOPE = "https://www.googleapis.com/auth/indexing"
INDEXING_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('indexing_submission.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class GoogleIndexingSubmitter:
    """Handles submission of URLs to Google Indexing API."""
    
    def __init__(self, service_account_file: str):
        """Initialize with service account credentials."""
        self.service_account_file = service_account_file
        self.credentials = None
        self.session = requests.Session()
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate using service account and get OAuth2 token."""
        try:
            # Load service account credentials
            self.credentials = service_account.Credentials.from_service_account_file(
                self.service_account_file,
                scopes=[INDEXING_SCOPE]
            )
            
            # Refresh credentials to get access token
            self.credentials.refresh(Request())
            logger.info("Successfully authenticated with Google Indexing API")
            
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            raise
    
    def _make_api_request(self, url: str, retry_count: int = 0) -> Dict[str, Any]:
        """Submit URL to Google Indexing API with retry logic."""
        payload = {
            "url": url,
            "type": "URL_UPDATED"
        }
        
        headers = {
            "Authorization": f"Bearer {self.credentials.token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = self.session.post(
                INDEXING_ENDPOINT,
                json=payload,
                headers=headers,
                timeout=30
            )
            
            # Check if token expired and refresh if needed
            if response.status_code == 401:
                logger.info("Token expired, refreshing...")
                self.credentials.refresh(Request())
                headers["Authorization"] = f"Bearer {self.credentials.token}"
                response = self.session.post(
                    INDEXING_ENDPOINT,
                    json=payload,
                    headers=headers,
                    timeout=30
                )
            
            response.raise_for_status()
            return {
                "success": True,
                "status_code": response.status_code,
                "response": response.json()
            }
            
        except requests.exceptions.RequestException as e:
            if retry_count < MAX_RETRIES:
                wait_time = RETRY_BACKOFF_FACTOR ** retry_count
                logger.warning(f"Request failed for {url}, retrying in {wait_time}s: {e}")
                time.sleep(wait_time)
                return self._make_api_request(url, retry_count + 1)
            else:
                logger.error(f"Failed to submit {url} after {MAX_RETRIES} retries: {e}")
                return {
                    "success": False,
                    "error": str(e),
                    "status_code": getattr(e.response, 'status_code', None) if hasattr(e, 'response') else None
                }
    
    def submit_url(self, url: str) -> Dict[str, Any]:
        """Submit a single URL to Google Indexing API."""
        logger.info(f"Submitting URL: {url}")
        
        # Rate limiting
        time.sleep(RATE_LIMIT_DELAY)
        
        result = self._make_api_request(url)
        
        if result["success"]:
            logger.info(f"✓ Successfully submitted: {url}")
            logger.debug(f"Response: {result['response']}")
        else:
            logger.error(f"✗ Failed to submit: {url} - {result.get('error', 'Unknown error')}")
        
        return result


def parse_sitemap(sitemap_url: str) -> List[str]:
    """Parse sitemap XML and extract all URLs."""
    logger.info(f"Fetching sitemap from: {sitemap_url}")
    
    try:
        response = requests.get(sitemap_url, timeout=30)
        response.raise_for_status()
        
        # Parse XML
        root = ET.fromstring(response.content)
        
        # Handle namespace
        namespace = {'ns': root.tag.split('}')[0][1:]} if '}' in root.tag else {}
        
        # Extract URLs
        urls = []
        if root.tag.endswith('urlset'):
            # Standard sitemap
            for url in root.findall('.//ns:loc', namespace) or root.findall('.//loc'):
                urls.append(url.text.strip())
        elif root.tag.endswith('sitemapindex'):
            # Sitemap index - extract all sitemap URLs first
            sitemap_urls = []
            for sitemap in root.findall('.//ns:loc', namespace) or root.findall('.//loc'):
                sitemap_urls.append(sitemap.text.strip())
            
            # Then parse each sitemap
            for sitemap_url in sitemap_urls:
                urls.extend(parse_sitemap(sitemap_url))
        
        logger.info(f"Found {len(urls)} URLs in sitemap")
        return urls
        
    except Exception as e:
        logger.error(f"Failed to parse sitemap: {e}")
        raise


def main():
    """Main execution function."""
    logger.info("Starting Google Indexing API submission script")
    
    try:
        # Parse sitemap
        urls = parse_sitemap(SITEMAP_URL)
        
        if not urls:
            logger.warning("No URLs found in sitemap")
            return
        
        # Initialize submitter
        submitter = GoogleIndexingSubmitter(SERVICE_ACCOUNT_FILE)
        
        # Submit URLs concurrently
        success_count = 0
        failure_count = 0
        
        logger.info(f"Submitting {len(urls)} URLs with {MAX_WORKERS} workers")
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # Submit all tasks
            future_to_url = {executor.submit(submitter.submit_url, url): url for url in urls}
            
            # Process results as they complete
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    if result["success"]:
                        success_count += 1
                    else:
                        failure_count += 1
                except Exception as e:
                    logger.error(f"Exception processing {url}: {e}")
                    failure_count += 1
        
        # Print summary
        logger.info("\n" + "="*50)
        logger.info("SUBMISSION SUMMARY")
        logger.info("="*50)
        logger.info(f"Total URLs: {len(urls)}")
        logger.info(f"Successful: {success_count}")
        logger.info(f"Failed: {failure_count}")
        logger.info(f"Success Rate: {(success_count/len(urls)*100):.1f}%")
        logger.info("="*50)
        
    except Exception as e:
        logger.error(f"Script execution failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()