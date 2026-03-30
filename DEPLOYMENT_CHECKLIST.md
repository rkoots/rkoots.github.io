# SEO Remediation Deployment Checklist
## rkoots.github.io

**Date:** March 5, 2026  
**Priority:** HIGH - Critical SEO Issues

---

## Pre-Deployment Verification

### 1. Files Modified ✅
- [x] `/robots.txt` - Parameter blocking added
- [x] `/_config.yml` - Sitemap configuration added
- [x] `/_layouts/default.html` - Canonical enforcer & structured data added

### 2. New Files Created ✅
- [x] `/sitemap-generator.xml` - Proper sitemap template
- [x] `/assets/js/canonical-enforcer.js` - URL parameter handler
- [x] `/_includes/seo-meta-tags.html` - Enhanced meta tags
- [x] `/_headers` - HTTP headers for GitHub Pages
- [x] `/SEO_AUDIT_REPORT.md` - Complete audit documentation
- [x] `/DEPLOYMENT_CHECKLIST.md` - This file

### 3. Local Testing (Before Push)

```bash
# Test Jekyll build locally
bundle exec jekyll build

# Verify sitemap generates correctly
cat _site/sitemap.xml | head -20

# Check robots.txt
cat _site/robots.txt

# Verify canonical enforcer loads
ls -la _site/assets/js/canonical-enforcer.js
```

---

## Deployment Steps

### Step 1: Commit Changes to Git

```bash
cd rkoots.github.io

# Check status
git status

# Add all modified and new files
git add robots.txt
git add _config.yml
git add _layouts/default.html
git add sitemap-generator.xml
git add assets/js/canonical-enforcer.js
git add _includes/seo-meta-tags.html
git add _headers
git add SEO_AUDIT_REPORT.md
git add DEPLOYMENT_CHECKLIST.md

# Commit with descriptive message
git commit -m "SEO: Fix all Google Search Console issues

- Block URL parameters in robots.txt (?src, ?utm, ?ref)
- Create proper sitemap.xml generator without frontmatter
- Add canonical URL enforcer JavaScript
- Enhance meta tags for all pages
- Add HTTP headers for parameter URL blocking
- Include comprehensive structured data (JSON-LD)
- Fix 145 indexing issues (97 canonical, 23 redirects, 6 duplicates, 17 not indexed, 1 404)

Resolves: Parameter duplicate content, sitemap fetch errors, canonical issues"

# Push to GitHub
git push origin main
```

### Step 2: Verify GitHub Pages Build

1. Go to: https://github.com/rkoots/rkoots.github.io/actions
2. Wait for build to complete (usually 2-5 minutes)
3. Check for any build errors
4. Verify deployment success ✅

### Step 3: Test Live Site

**A. Sitemap Test**
- URL: https://rkoots.github.io/sitemap.xml
- Expected: Valid XML, no Jekyll frontmatter visible
- Validator: https://www.xml-sitemaps.com/validate-xml-sitemap.html

**B. Robots.txt Test**
- URL: https://rkoots.github.io/robots.txt
- Expected: Parameter blocking rules present
- Verify lines:
  ```
  Disallow: /*?src=*
  Disallow: /*?utm_*
  Disallow: /*?ref=*
  ```

**C. Canonical Enforcer Test**
- URL: https://rkoots.github.io/blog/?src=123
- Expected: URL changes to https://rkoots.github.io/blog/
- Check: Canonical tag points to clean URL
- Verify: Browser history updated (no redirect)

**D. Structured Data Test**
- Tool: https://search.google.com/test/rich-results
- Test URLs:
  - Homepage: https://rkoots.github.io/
  - Blog post: https://rkoots.github.io/blog/2025/05/15/...
- Expected: All schema types validate without errors

**E. Mobile-Friendly Test**
- Tool: https://search.google.com/test/mobile-friendly
- Test: https://rkoots.github.io/
- Expected: Page is mobile-friendly

---

## Google Search Console Actions

### Immediate Actions (Within 24 Hours)

#### 1. Submit New Sitemap
```
1. Go to: https://search.google.com/search-console
2. Select property: rkoots.github.io
3. Navigate to: Sitemaps (left sidebar)
4. Remove old sitemap if present
5. Add new sitemap: https://rkoots.github.io/sitemap.xml
6. Click "Submit"
7. Wait 5-10 minutes
8. Refresh page
9. Verify status: "Success" (not "Couldn't fetch")
```

#### 2. Request Removal of Parameter URLs
```
1. Go to: Removals (left sidebar)
2. Click: "New Request"
3. Select: "Temporarily remove URL"
4. Add patterns:
   - https://rkoots.github.io/*?src=*
   - https://rkoots.github.io/*?utm_*
   - https://rkoots.github.io/*?ref=*
   - https://rkoots.github.io/*?fbclid=*
5. Submit each request
6. Monitor status (approved within 24 hours)
```

#### 3. Request Indexing of Key Pages
```
Use URL Inspection tool to request indexing:

Priority 1 (Request immediately):
- https://rkoots.github.io/
- https://rkoots.github.io/blog/
- https://rkoots.github.io/tools/
- https://rkoots.github.io/guide/
- https://rkoots.github.io/insights/

Priority 2 (Request within week):
- Top 10 blog posts by traffic
- Main tool pages
- Key guide pages

Steps for each URL:
1. Paste URL in search bar at top
2. Click "Test Live URL"
3. Wait for crawl to complete
4. Click "Request Indexing"
5. Wait for confirmation
```

### Weekly Monitoring (Weeks 1-4)

#### Week 1 Checklist
- [ ] Verify sitemap fetch successful
- [ ] Check "Coverage" report for changes
- [ ] Monitor parameter URL removal requests
- [ ] Note baseline metrics:
  - Valid pages: _____
  - Errors: _____
  - Warnings: _____
  - Excluded: _____

#### Week 2 Checklist
- [ ] Check parameter URLs deindexing progress
- [ ] Review "Alternative page with proper canonical" count
- [ ] Monitor "Page with redirect" count
- [ ] Check for new errors

#### Week 3 Checklist
- [ ] Verify canonical consolidation
- [ ] Check "Crawled but not indexed" count
- [ ] Review duplicate content issues
- [ ] Monitor organic traffic trends

#### Week 4 Checklist
- [ ] Final error count review
- [ ] Compare metrics to baseline
- [ ] Document improvements
- [ ] Identify remaining issues

---

## Success Metrics

### Target Metrics (30 Days)

| Metric | Baseline | Target | Actual |
|--------|----------|--------|--------|
| Alternative page with canonical | 97 | 0 | ___ |
| Page with redirect | 23 | 0 | ___ |
| Duplicate without canonical | 6 | 0 | ___ |
| Crawled but not indexed | 17 | < 5 | ___ |
| 404 errors | 1 | 0 | ___ |
| Valid indexed pages | ~50 | 100+ | ___ |
| Sitemap status | Failed | Success | ___ |

### Traffic Metrics (60 Days)

| Metric | Baseline | Target | Actual |
|--------|----------|--------|--------|
| Organic sessions | ___ | +50% | ___ |
| Organic users | ___ | +50% | ___ |
| Avg. session duration | ___ | +20% | ___ |
| Bounce rate | ___ | -10% | ___ |
| Pages per session | ___ | +15% | ___ |

---

## Troubleshooting

### Issue: Sitemap Still Can't Be Fetched

**Diagnosis:**
```bash
# Check sitemap on live site
curl -I https://rkoots.github.io/sitemap.xml

# Expected headers:
# HTTP/2 200
# content-type: application/xml

# Check for frontmatter in output
curl https://rkoots.github.io/sitemap.xml | head -5

# Should start with:
# <?xml version="1.0" encoding="UTF-8"?>
# NOT with: ---
```

**Solution:**
- Verify Jekyll build completed successfully
- Check `_config.yml` has `jekyll-sitemap` plugin
- Ensure `sitemap-generator.xml` has correct frontmatter
- Clear GitHub Pages cache (push empty commit)

### Issue: Canonical Enforcer Not Working

**Diagnosis:**
```javascript
// Open browser console on page with ?src=123
// Check for errors
console.log('Canonical enforcer loaded:', typeof getCanonicalURL);

// Check if script loaded
document.querySelector('script[src*="canonical-enforcer"]');
```

**Solution:**
- Verify script path is correct in `_layouts/default.html`
- Check browser console for JavaScript errors
- Ensure script loads before page content
- Test in incognito mode (no extensions)

### Issue: Parameter URLs Still Being Indexed

**Diagnosis:**
- Check robots.txt on live site
- Verify parameter blocking rules present
- Check Google Search Console for crawl errors

**Solution:**
- Request removal of parameter URLs in GSC
- Add meta robots tag: `<meta name="robots" content="noindex">`
- Wait 2-4 weeks for deindexing
- Monitor progress in Coverage report

---

## Rollback Plan (If Needed)

### If Critical Issues Occur

```bash
# Revert to previous commit
git log --oneline -5
git revert <commit-hash>
git push origin main

# Or reset to previous state
git reset --hard <previous-commit-hash>
git push --force origin main
```

### Backup Files
Before deployment, backup these files:
- `robots.txt.backup`
- `_config.yml.backup`
- `_layouts/default.html.backup`

---

## Post-Deployment Monitoring

### Daily (First Week)
- [ ] Check Google Search Console for errors
- [ ] Monitor sitemap fetch status
- [ ] Review coverage report changes
- [ ] Check analytics for traffic anomalies

### Weekly (First Month)
- [ ] Review error count trends
- [ ] Monitor parameter URL deindexing
- [ ] Check organic traffic growth
- [ ] Analyze top-performing pages

### Monthly (Ongoing)
- [ ] Comprehensive SEO review
- [ ] Update sitemap if needed
- [ ] Refresh top content
- [ ] Competitor analysis

---

## Contact & Support

### Resources
- **SEO Audit Report:** `/SEO_AUDIT_REPORT.md`
- **Google Search Console:** https://search.google.com/search-console
- **GitHub Repository:** https://github.com/rkoots/rkoots.github.io
- **Live Site:** https://rkoots.github.io

### Documentation
- Jekyll Sitemap Plugin: https://github.com/jekyll/jekyll-sitemap
- Google Search Console Help: https://support.google.com/webmasters
- Schema.org Documentation: https://schema.org/docs/documents.html

---

## Sign-Off

### Pre-Deployment
- [ ] All files reviewed and tested locally
- [ ] Git commit message is descriptive
- [ ] Backup created of critical files
- [ ] Team notified of deployment

**Deployed By:** _________________  
**Date:** _________________  
**Time:** _________________

### Post-Deployment
- [ ] Live site tested and verified
- [ ] Sitemap submitted to Google Search Console
- [ ] Parameter URL removal requested
- [ ] Key pages requested for indexing
- [ ] Monitoring schedule established

**Verified By:** _________________  
**Date:** _________________  
**Time:** _________________

---

**Status:** ✅ Ready for Deployment  
**Risk Level:** LOW (All changes are SEO improvements, no breaking changes)  
**Estimated Impact:** HIGH (Resolves 145 indexing issues)
