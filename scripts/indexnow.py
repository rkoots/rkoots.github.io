import requests
import xml.etree.ElementTree as ET

# === CONFIGURATION ===
SITE_URL = "https://rkoots.github.io"
SITEMAP_URL = f"{SITE_URL}/sitemap.xml"
INDEXNOW_API = "https://api.indexnow.org/indexnow"

# 🔑 Replace with your own IndexNow key and hosted key location if needed
INDEXNOW_KEY = "your-unique-key-here"
INDEXNOW_KEY_LOCATION = f"{SITE_URL}/{INDEXNOW_KEY}.txt"

def extract_urls_from_sitemap(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch sitemap: {e}")
        return []

    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        return []

    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [elem.text for elem in root.findall('.//ns:loc', namespace)]
    return urls

def submit_to_indexnow(urls):
    payload = {
        "host": SITE_URL.replace("https://", "").replace("http://", ""),
        "key": INDEXNOW_KEY,
        "keyLocation": INDEXNOW_KEY_LOCATION,
        "urlList": urls
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(INDEXNOW_API, json=payload, headers=headers)

    if response.status_code == 200:
        print("✅ IndexNow submission successful.")
    else:
        print(f"❌ IndexNow submission failed with status {response.status_code}: {response.text}")

def main():
    print("🔍 Fetching URLs from sitemap...")
    url_list = extract_urls_from_sitemap(SITEMAP_URL)

    if not url_list:
        print("⚠️ No URLs found.")
        return

    print(f"🌐 Submitting {len(url_list)} URLs to IndexNow...")
    submit_to_indexnow(url_list)

if __name__ == "__main__":
    main()
