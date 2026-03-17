import requests
import json
import random
import logging
from typing import List, Dict, Optional
from xml.etree import ElementTree
from datetime import datetime
import google.generativeai as genai
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WORDPRESS_SITE_URL = "https://rkoots.wordpress.com"
WORDPRESS_USERNAME = "rkoots"
WORDPRESS_APP_PASSWORD = os.getenv("WP_KEY")
SITEMAP_URL = "https://rkoots.github.io/sitemap.xml"

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

def generate_blog_with_gemini(internal_link: Optional[str] = None) -> Dict:
    """Generate blog post content using Google Gemini API."""
    try:
        # Configure Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
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
        
        logger.info("Generating content with Gemini...")
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
        logger.error(f"Error generating blog with Gemini: {str(e)}")
        raise

def post_to_wordpress(blog_data: Dict) -> bool:
    """Post the generated blog to WordPress."""
    try:
        # WordPress API endpoint
        api_url = f"{WORDPRESS_SITE_URL}/wp-json/wp/v2/posts"
        
        # Prepare the post data
        post_data = {
            "title": blog_data["title"],
            "content": blog_data["content_html"],
            "status": blog_data["status"],
            "tags": blog_data.get("tags", [])
        }
        
        # Make the API request
        logger.info(f"Posting to WordPress: {blog_data['title']}")
        response = requests.post(
            api_url,
            auth=(WORDPRESS_USERNAME, WORDPRESS_APP_PASSWORD),
            json=post_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 201:
            logger.info("Successfully posted to WordPress!")
            logger.info(f"Post URL: {response.json().get('link', 'N/A')}")
            return True
        else:
            logger.error(f"Failed to post to WordPress. Status: {response.status_code}")
            logger.error(f"Response: {response.text}")
            return False
    
    except Exception as e:
        logger.error(f"Error posting to WordPress: {str(e)}")
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
    main()
