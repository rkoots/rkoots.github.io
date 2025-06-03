import requests
import xml.etree.ElementTree as ET
import json
# === CONFIGURATION ===
SITE_URL = "https://rkoots.github.io"
SITEMAP_URL = f"{SITE_URL}/sitemap.xml"
INDEXNOW_API = "https://api.indexnow.org/indexnow"

# 🔑 Replace with your own IndexNow key and hosted key location if needed
INDEXNOW_KEY = "f6291a0f9c8b4cf0a57c427c366a346e"
INDEXNOW_KEY_LOCATION = "f{SITE_URL}/{INDEXNOW_KEY}.txt"

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
    url = "https://api.indexnow.org/IndexNow"
    payload = {"host": "rkoots.github.io",
            "key": "f7fb35260cf341e7bb05ede25bf211f3",
            "keyLocation": "https://rkoots.github.io/f7fb35260cf341e7bb05ede25bf211f3.txt",
            "urlList": urls}
    headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Host': 'api.indexnow.org'
    }
    print(payload)
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    print(response.text)


def main():
    print("🔍 Fetching URLs from sitemap...")
    url_list = extract_urls_from_sitemap(SITEMAP_URL)
    print(url_list)
    if not url_list:
        print("⚠️ No URLs found.")
        return

    print(f"🌐 Submitting {len(url_list)} URLs to IndexNow...")
    submit_to_indexnow(url_list)

if __name__ == "__main__":
    main()
