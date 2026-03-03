---
description: Generate and publish detailed Blogger posts every Wednesday and Friday, save to blog/_posts, and commit via GitHub Actions
---
1. Ensure the script exists at `auto/blogger.py` and supports:
   - local post generation into `blog/_posts`
   - optional Blogger publish behind `PUBLISH_TO_BLOGGER=true`
   - safe skip on non-Wednesday/Friday runs unless `FORCE_RUN=true`

2. Configure the following GitHub repository secrets:
   - `BLOG_ID`
   - `CLIENT_ID`
   - `CLIENT_SECRET`
   - `BLOGGER_REFRESH_TOKEN`
   - `PUBLISH_TO_BLOGGER` (`true` or `false`)

3. Add workflow file `.github/workflows/blogger-wed-fri.yml` with:
   - schedule cron: `5 0 * * 3,5` (Wednesday and Friday)
   - manual trigger: `workflow_dispatch`
   - Python setup and dependency install
   - run command: `python auto/blogger.py`
   - git commit/push step for `blog/_posts/*.md`

4. Validate generation manually (local):
   - PowerShell from repo root:
     - `$env:FORCE_RUN='true'`
     - `$env:PUBLISH_TO_BLOGGER='false'`
     - `python auto/blogger.py`

5. Verify file output:
   - Check a new file appears in `blog/_posts/` with naming format `YYYY-MM-DD-engineering-ai-weekly-brief-....md`

6. Verify workflow commit behavior:
   - Trigger workflow manually from GitHub Actions (`workflow_dispatch`)
   - Confirm it commits only when a new post is generated.

7. Optional Blogger publishing check:
   - Set `PUBLISH_TO_BLOGGER=true`
   - Trigger workflow manually and verify the post appears on Blogger.
