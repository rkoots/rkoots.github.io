const puppeteer = require('puppeteer');

const urls = [
  "https://rkoots.github.io/",
  "https://rkoots.github.io/technews/",
  "https://rkoots.github.io/tools/",
  "https://rkoots.github.io/insights/",
  "https://rkoots.github.io/blog/",
  "https://rkoots.github.io/guide/",
  "https://rkoots.github.io/styleguide/",
  "https://rkoots.github.io/quickref/",
  "https://rkoots.github.io/cv/"
];

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  for (const url of urls) {
    try {
      console.log(`Visiting: ${url}`);
      await page.goto(url, { waitUntil: 'networkidle0' });  // Ensure page is fully loaded

      // Just a dummy eval to trigger analytics or simulate interaction
      await page.evaluate(() => {
        return document.title;  // Replace with actual logic if needed
      });

      // Optional: wait for a bit to simulate real user
      await page.waitForTimeout(500 + Math.random() * 2500);  // 500ms to 3s
    } catch (err) {
      console.error(`Error visiting ${url}:`, err);
    }
  }

  await browser.close();
})();
