import os
import json
import time
import logging
import requests
import google.generativeai as genai
from datetime import datetime
from typing import Dict, Optional, List
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
GEMINI_API_KEY = 'AIzaSyDkkg8CHBDzIw_ua495iZg3PsDvufbZYgM' #os.getenv("GEMINI_API_KEY")
WORDPRESS_SITE_URL = "https://rkoots.wordpress.com"
WORDPRESS_USERNAME = "rkoots"
WORDPRESS_APP_PASSWORD = os.getenv("WP_KEY")
SITEMAP_URL = "https://rkoots.github.io/sitemap.xml"

# Email configuration for Post by Email
WORDPRESS_POST_EMAIL = "jatu669tofi@post.wordpress.com"
EMAIL_SENDER = "market007ads@gmail.com"  # Update with your email
EMAIL_PASSWORD = "cedp usix ulwi khcr"   # Update with your email password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def fetch_sitemap_links() -> List[str]:
    """Fetch and parse sitemap.xml to extract all URLs."""
    try:
        logger.info(f"Fetching sitemap from: {SITEMAP_URL}")
        response = requests.get(SITEMAP_URL)
        response.raise_for_status()
        
        # Parse XML
        root = ElementTree.fromstring(response.content)
        
        # Define namespace (if any)
        namespace = {'ns': root.tag.split('}')[0][1:] if '}' in root.tag else ''}
        
        # Extract all URLs
        urls = []
        # Try different sitemap structures
        if root.tag.endswith('sitemapindex'):
            # This is a sitemap index, need to fetch individual sitemaps
            for sitemap in root.findall('.//ns:sitemap' if namespace else './/sitemap', namespace):
                loc = sitemap.find('ns:loc' if namespace else 'loc')
                if loc is not None:
                    # Fetch the actual sitemap
                    try:
                        sitemap_response = requests.get(loc.text)
                        sitemap_response.raise_for_status()
                        sitemap_root = ElementTree.fromstring(sitemap_response.content)
                        for url in sitemap_root.findall('.//ns:url' if namespace else './/url', namespace):
                            url_loc = url.find('ns:loc' if namespace else 'loc')
                            if url_loc is not None:
                                urls.append(url_loc.text)
                    except Exception as e:
                        logger.warning(f"Failed to fetch sitemap {loc.text}: {str(e)}")
        else:
            # This is a regular sitemap
            # Try with namespace first
            if namespace:
                for url in root.findall('.//ns:url', namespace):
                    loc = url.find('ns:loc', namespace)
                    if loc is not None:
                        urls.append(loc.text)
            else:
                # Try without namespace
                for url in root.findall('.//url'):
                    loc = url.find('loc')
                    if loc is not None:
                        urls.append(loc.text)
            
            # If still no URLs, try alternative parsing
            if not urls:
                # Remove namespace and try again
                for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
                    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
                    if loc is not None:
                        urls.append(loc.text)
        
        logger.info(f"Found {len(urls)} URLs in sitemap")
        return urls
    
    except Exception as e:
        logger.error(f"Error fetching sitemap: {str(e)}")
        return []

def pick_random_internal_link() -> Optional[str]:
    """Pick a random internal link from sitemap containing /finance/ or /ai-tools/."""
    urls = fetch_sitemap_links()
    
    # Filter URLs
    filtered_urls = [url for url in urls if '/finance/' in url or '/ai-tools/' in url]
    
    if not filtered_urls:
        logger.warning("No URLs found containing /finance/ or /ai-tools/")
        return None
    
    selected_url = random.choice(filtered_urls)
    logger.info(f"Selected internal link: {selected_url}")
    return selected_url

def list_available_models() -> List[str]:
    """List all available Gemini models."""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        models = genai.list_models()
        available_models = []
        
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                available_models.append(model.name)
                logger.info(f"Available model: {model.name}")
        
        return available_models
    except Exception as e:
        logger.error(f"Error listing models: {str(e)}")
        return []

def test_gemini_connection() -> bool:
    """Test connection to Gemini API with available models."""
    try:
        logger.info("Testing Gemini API connection...")
        models = list_available_models()
        
        if not models:
            logger.error("No available models found")
            return False
        
        # Use gemini-1.5-flash specifically
        model_name = 'gemini-1.5-flash'
        if any(model_name in model for model in models):
            logger.info(f"Using model: {model_name}")
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content("Test connection - respond with 'OK'")
                logger.info(f"Successfully connected with model: {model_name}")
                return True
            except Exception as e:
                logger.error(f"Failed with model {model_name}: {str(e)}")
        else:
            logger.error(f"Model {model_name} not found in available models")
        
        # If gemini-1.5-flash fails, try the first available model as fallback
        first_model = models[0].split('/')[-1]  # Extract model name from full path
        logger.info(f"Trying fallback model: {first_model}")
        model = genai.GenerativeModel(first_model)
        response = model.generate_content("Test connection - respond with 'OK'")
        logger.info(f"Successfully connected with fallback model: {first_model}")
        return True
        
    except Exception as e:
        logger.error(f"Gemini connection test failed: {str(e)}")
        return False

def generate_blog_with_gemini(internal_link: Optional[str] = None, max_retries: int = 3) -> Dict:
    """Generate blog post content using Google Gemini API with retry logic."""
    for attempt in range(max_retries):
        try:
            # Configure Gemini
            genai.configure(api_key=GEMINI_API_KEY)
            
            # Try to find an available model
            models = list_available_models()
            if not models:
                raise Exception("No available Gemini models found")
            
            # Use gemini-1.5-flash specifically
            model_name = 'gemini-1.5-flash'
            if any(model_name in model for model in models):
                selected_model = model_name
            else:
                # Fallback to first available model
                selected_model = models[0].split('/')[-1]
                logger.warning(f"gemini-1.5-flash not found, using fallback: {selected_model}")
            
            logger.info(f"Using model: {selected_model}")
            model = genai.GenerativeModel(selected_model)
            
            # Prepare internal link instruction
            internal_link_instruction = ""
            if internal_link:
                internal_link_instruction = f"""
                IMPORTANT: In the 3rd key topic, you MUST naturally include this internal link as a recommendation:
                {internal_link}
                Make it feel like a genuine recommendation within the content.
                """
            
            # Prepare the prompt
            current_date = datetime.now().strftime("%B %d, %Y")
            prompt = f"""
            Generate a high-quality, SEO-optimized blog post about a trending topic in AI, Technology, or Finance.
            The content should feel like latest tech news from today ({current_date}).
            
            Requirements:
            1. Create an engaging, SEO-optimized title
            2. Write a short, engaging introduction
            3. Create 5 key topics as main sections
            4. Each section should be informative and valuable
            5. Include relevant external links in sections 1, 2, 4, and 5
            6. Use professional, informative tone with slight engagement
            7. Format everything in HTML
            
            {internal_link_instruction}
            
            Structure:
            - Title: Clear and SEO optimized
            - Introduction: 2-3 sentences
            - 5 Key Topics: Each with H2 heading and 2-3 paragraphs
            - Include relevant links naturally in the content
            
            Return ONLY valid JSON in this exact format:
            {{
              "title": "Your SEO-optimized title here",
              "content_html": "<h2>Section 1 Title</h2><p>Content with link: <a href='https://example.com'>relevant text</a></p><h2>Section 2 Title</h2>...",
              "tags": ["AI", "Tech", "Finance"],
              "status": "publish"
            }}
            
            Make sure the content_html is properly formatted HTML with H2 tags for sections and P tags for paragraphs.
            """
            
            logger.info(f"Generating content with Gemini... (Attempt {attempt + 1}/{max_retries})")
            response = model.generate_content(prompt)
            
            # Parse the JSON response
            try:
                # Clean the response to ensure it's valid JSON
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:-3].strip()
                elif response_text.startswith('```'):
                    response_text = response_text[3:-3].strip()
                
                blog_data = json.loads(response_text)
                logger.info("Successfully generated blog content")
                return blog_data
                
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse Gemini response as JSON: {str(e)}")
                logger.error(f"Raw response: {response.text}")
                raise
        
        except Exception as e:
            error_str = str(e)
            if "429" in error_str and "quota" in error_str.lower():
                if attempt < max_retries - 1:
                    # Extract retry delay from error message if available
                    retry_delay = 60  # Default 60 seconds
                    if "retry in" in error_str.lower():
                        try:
                            import re
                            match = re.search(r'retry in ([\d.]+)', error_str.lower())
                            if match:
                                retry_delay = int(float(match.group(1))) + 5  # Add 5 seconds buffer
                        except:
                            pass
                    
                    logger.warning(f"Quota exceeded. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_delay)
                    continue
                else:
                    logger.error(f"Max retries ({max_retries}) reached. Quota still exceeded.")
                    logger.error("Please wait longer or upgrade your Gemini API plan.")
                    raise
            else:
                logger.error(f"Error generating blog with Gemini: {str(e)}")
                raise
    
    raise Exception(f"Failed to generate blog after {max_retries} attempts")

def post_to_wordpress(blog_data: Dict) -> bool:
    """Post the generated blog to WordPress.com using Post by Email feature."""
    try:
        # Prepare email content
        title = blog_data["title"]
        content = blog_data["content_html"]
        
        # Create email message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = EMAIL_SENDER
        msg['To'] = WORDPRESS_POST_EMAIL
        
        # Add WordPress shortcodes for better formatting
        email_content = f"""
{content}

[tags AI, Technology, Finance]
[category Technology]
[status draft]

[end]
"""
        
        # Attach HTML content
        html_part = MIMEText(email_content, 'html')
        msg.attach(html_part)
        
        # Send email
        logger.info(f"Posting to WordPress.com via email: {title}")
        logger.info(f"From: {EMAIL_SENDER}")
        logger.info(f"To: {WORDPRESS_POST_EMAIL}")
        
        # Connect to SMTP server and send
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, WORDPRESS_POST_EMAIL, text)
        server.quit()
        
        logger.info("Successfully sent blog post via email!")
        logger.info("The post should appear on WordPress within a few minutes.")
        return True
        
    except Exception as e:
        logger.error(f"Error sending email to WordPress: {str(e)}")
        logger.error("Please check your email configuration:")
        logger.error("1. Update EMAIL_SENDER with your Gmail address")
        logger.error("2. Update EMAIL_PASSWORD with your Gmail App Password")
        logger.error("3. Enable 2-factor authentication on Gmail")
        logger.error("4. Generate an App Password at: https://myaccount.google.com/apppasswords")
        return False

def test_full_process() -> bool:
    """Test the complete blog generation and posting process."""
    try:
        logger.info("=== TESTING FULL PROCESS ===")
        
        # Test 1: Check environment variables
        logger.info("1. Checking environment variables...")
        if not GEMINI_API_KEY:
            logger.error("GEMINI_API_KEY not found")
            return False
        if not WORDPRESS_APP_PASSWORD:
            logger.error("WP_KEY not found")
            return False
        logger.info("✓ Environment variables OK")
        
        # Test 2: Test Gemini connection
        logger.info("2. Testing Gemini API connection...")
        if not test_gemini_connection():
            logger.error("Gemini connection failed")
            return False
        logger.info("✓ Gemini connection OK")
        
        # Test 3: Test sitemap fetching
        logger.info("3. Testing sitemap fetching...")
        urls = fetch_sitemap_links()
        if not urls:
            logger.error("No URLs found in sitemap")
            return False
        logger.info(f"✓ Found {len(urls)} URLs in sitemap")
        
        # Test 4: Test internal link selection
        logger.info("4. Testing internal link selection...")
        internal_link = pick_random_internal_link()
        if internal_link:
            logger.info(f"✓ Selected internal link: {internal_link}")
        else:
            logger.warning("⚠ No suitable internal links found")
        
        # Test 5: Generate a short test blog
        logger.info("5. Testing blog generation...")
        try:
            blog_data = generate_blog_with_gemini(internal_link)
            if blog_data and 'title' in blog_data and 'content_html' in blog_data:
                logger.info(f"✓ Generated test blog: {blog_data['title'][:50]}...")
            else:
                logger.error("Invalid blog data generated")
                return False
        except Exception as e:
            logger.error(f"Blog generation failed: {str(e)}")
            return False
        
        # Test 6: Test WordPress connection (without posting)
        logger.info("6. Testing WordPress API connection...")
        try:
            site_id = "rkoots.wordpress.com"
            api_url = f"https://public-api.wordpress.com/wp/v2/sites/{site_id}/posts"
            response = requests.get(
                api_url,
                auth=(WORDPRESS_USERNAME, WORDPRESS_APP_PASSWORD),
                params={"per_page": 1}
            )
            if response.status_code == 200:
                logger.info("✓ WordPress API connection OK")
            else:
                logger.error(f"WordPress API connection failed: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"WordPress connection test failed: {str(e)}")
            return False
        
        logger.info("=== ALL TESTS PASSED ===")
        return True
        
    except Exception as e:
        logger.error(f"Test process failed: {str(e)}")
        return False

def main():
    """Main function to orchestrate the blog posting process."""
    try:
        logger.info("Starting automated blog posting process...")
        
        # Step 1: Get internal link
        internal_link = pick_random_internal_link()
        
        # Step 2: Generate blog content
        blog_data = generate_blog_with_gemini(internal_link)
        
        # Step 3: Post to WordPress
        success = post_to_wordpress(blog_data)
        
        if success:
            logger.info("Blog posting process completed successfully!")
        else:
            logger.error("Blog posting process failed!")
            
        return success
    
    except Exception as e:
        logger.error(f"Main process error: {str(e)}")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_full_process()
    elif len(sys.argv) > 1 and sys.argv[1] == "--list-models":
        list_available_models()
    else:
        main()
