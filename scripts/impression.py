import xml.etree.ElementTree as ET
import asyncio
import random
import requests
from playwright.async_api import async_playwright

SITEMAP_URL = "https://rkoots.github.io/sitemap.xml"
NUM_SECONDS_BETWEEN_REQUESTS = (0.1, 0.2)

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 Version/16.0 Mobile/15A5341f Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; rv:108.0) Gecko/20100101 Firefox/108.0"
]

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
        return [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []

async def visit_urls(urls):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for i, url in enumerate(urls):
            user_agent = random.choice(user_agents)
            referer = random.choice(referers)
            context = await browser.new_context(
                user_agent=user_agent,
                extra_http_headers={"Referer": referer}
            )
            page = await context.new_page()
            try:
                print(f"{i+1}/{len(urls)} Visiting {url} with {user_agent} from {referer}")
                await page.goto(url, timeout=5000)
                await asyncio.sleep(random.uniform(*NUM_SECONDS_BETWEEN_REQUESTS))
            except Exception as e:
                print(f"Error visiting {url}: {e}")
            finally:
                await page.close()
                await context.close()
        await browser.close()

async def visit_rkoots(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        user_agent = random.choice(user_agents)
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()
        try:
            print(f"Visiting {url} with {user_agent}")
            await page.goto(url, timeout=30000)
        except Exception as e:
            print(f"Error visiting {url}: {e}")
        finally:
            await page.close()
            await context.close()
            await browser.close()

async def main():
    # Schedule Google search queries
    google_urls = [
        "https://www.google.com/search?q=rajkumar+venkataraman",
        "https://www.google.com/search?q=rkoots",
        "https://www.google.com/search?q=rajkumar+venkataraman+rkoots"
    ]

    for i in range(100):
        google_tasks = [asyncio.create_task(visit_rkoots(url)) for url in google_urls]
        await asyncio.sleep(1)

    # Visit sitemap URLs
    urls = fetch_sitemap_urls(SITEMAP_URL)
    if urls:
        await visit_urls(urls)
    else:
        print("No URLs found in sitemap.")

    # Ensure Google tasks complete (if still running)
    await asyncio.gather(*google_tasks)

if __name__ == "__main__":
    asyncio.run(main())
