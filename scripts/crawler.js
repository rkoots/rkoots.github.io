// crawler.js (simplified example)
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const visited = new Set();
  const toVisit = ['https://rkoots.github.io/'];

  while (toVisit.length > 0) {
    const url = toVisit.shift();
    if (visited.has(url)) continue;

    console.log('Visiting:', url);
    await page.goto(url);

    // Collect all same-domain links
    const links = await page.$$eval('a[href]', anchors =>
      anchors
        .map(a => a.href)
        .filter(href => href.startsWith('https://rkoots.github.io/'))
    );

    // Add new links to visit
    for (const link of links) {
      if (!visited.has(link) && !toVisit.includes(link)) {
        toVisit.push(link);
      }
    }

    visited.add(url);
  }

  await browser.close();
})();
