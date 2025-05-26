import requests
import xml.etree.ElementTree as ET
import random
import time

# CONFIG
SITEMAP_URL = "https://rkoots.github.io/sitemap.xml"
NUM_SECONDS_BETWEEN_REQUESTS = (1.0, 2.5)  # min and max delay between requests

# Sample User-Agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 Version/16.0 Mobile/15A5341f Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; rv:108.0) Gecko/20100101 Firefox/108.0"
]

# Sample Referers
referers = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://twitter.com/",
    "https://github.com/",
    "https://news.ycombinator.com/",
    "https://rkoots.github.io/"
]

def fetch_sitemap_urls(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        urls = [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        return urls
    except Exception as e:
        print(f"Error fetching/parsing sitemap: {e}")
        return []

def test_urls(urls):
    for i, url in enumerate(urls):
        headers = {
            "User-Agent": random.choice(user_agents),
            "Referer": random.choice(referers)
        }
        try:
            r = requests.get(url, headers=headers, timeout=10)
            print(f"{i+1}/{len(urls)} [{r.status_code}] {url} via {headers['Referer']}")
        except requests.RequestException as e:
            print(f"{i+1}/{len(urls)} [ERROR] {url}: {e}")
        time.sleep(random.uniform(*NUM_SECONDS_BETWEEN_REQUESTS))

if __name__ == "__main__":
    urls = fetch_sitemap_urls(SITEMAP_URL)
    if urls:
        print(f"Found {len(urls)} URLs in sitemap.")
        test_urls(urls)
    else:
        print("No URLs to test.")
