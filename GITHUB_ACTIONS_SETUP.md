# GitHub Actions Setup Guide (Recommended!)

Set up your ArXiv paper scanner to run automatically in GitHub's cloud. This is **much simpler** than local setup - no cron jobs, no local machine needed!

## Why GitHub Actions?

- ✅ **Completely free** (for public repos)
- ✅ **No local machine needed** - runs in the cloud
- ✅ **Already configured** - just add your API keys
- ✅ **Auto-publishes to GitHub Pages** at `aashiqmuhamed.github.io/daily_papers`
- ✅ **Runs even when your computer is off**
- ✅ **Daily schedule already set up** (1 PM UTC)

## Quick Start (5 Steps)

### Step 1: Push to GitHub

If you haven't already:

```bash
# If this is a new repo
git remote add origin https://github.com/aashiqmuhamed/daily_papers.git

# Or if you need to change the remote
git remote set-url origin https://github.com/aashiqmuhamed/daily_papers.git

# Push everything
git add .
git commit -m "Setup ArXiv scanner with Claude"
git push -u origin main
```

**Note:** The repo must be **public** for free GitHub Pages and Actions.

### Step 2: Add Your API Key as a GitHub Secret

1. Go to your repository: https://github.com/aashiqmuhamed/daily_papers
2. Click **Settings** (top menu)
3. Click **Secrets and variables** → **Actions** (left sidebar)
4. Click **New repository secret**
5. Add your Anthropic key:
   - Name: `ANTHROPIC_API_KEY`
   - Secret: `sk-ant-your-actual-key-here`
6. Click **Add secret**

**Get your Anthropic API key:**
- Go to https://console.anthropic.com/
- Sign up (get $5 free credit)
- Create an API key
- Copy it (starts with `sk-ant-`)

**Optional but recommended:** Add Semantic Scholar key:
- Name: `S2_KEY`
- Secret: your semantic scholar API key
- Get it from: https://www.semanticscholar.org/product/api#api-key-form

### Step 3: Configure Your Preferences

Edit these files and commit:

```bash
# Configure authors you want to follow
nano configs/authors.txt

# Configure topics you're interested in
nano configs/paper_topics.txt

# Commit changes
git add configs/
git commit -m "Configure my preferences"
git push
```

### Step 4: Enable GitHub Pages

1. Go to **Settings** → **Pages** (left sidebar)
2. Under "Build and deployment":
   - Source: **GitHub Actions**
3. That's it! No need to select a branch.

### Step 5: Enable Scheduled Workflows (If Forked)

If you forked this repo, scheduled workflows are disabled by default:

1. Go to **Actions** tab
2. You'll see a message about workflows
3. Click **"I understand my workflows, go ahead and enable them"**

## Test It!

### Manual Run

1. Go to **Actions** tab in your repo
2. Click **"Run daily arxiv"** workflow (left sidebar)
3. Click **"Run workflow"** dropdown (right side)
4. Click **"Run workflow"** button
5. Wait 2-3 minutes
6. Check the results at: `https://aashiqmuhamed.github.io/daily_papers`

### Automatic Runs

The workflow is scheduled to run daily at **1 PM UTC** (6 AM Pacific).

You can change the schedule by editing `.github/workflows/cron_runs.yaml`:
```yaml
on:
  schedule:
    - cron: '0 13 * * *'  # Change this line
```

Common schedules:
- `0 9 * * *` - 9 AM UTC
- `0 13 * * *` - 1 PM UTC (recommended for ArXiv updates)
- `0 17 * * *` - 5 PM UTC
- `0 9 * * 1-5` - 9 AM UTC, weekdays only

## How It Works

1. **Daily at 1 PM UTC**, GitHub Actions runs the workflow
2. **Fetches papers** from ArXiv (cs.CL, cs.LG, cs.AI by default)
3. **Filters with Claude** based on your topics and authors
4. **Creates markdown** with selected papers
5. **Publishes to GitHub Pages** automatically
6. **You visit the website** whenever you want to see papers

## Your Website

After the first successful run, your papers will be available at:

**https://aashiqmuhamed.github.io/daily_papers**

The page updates automatically every day!

## Viewing Past Runs

1. Go to **Actions** tab
2. Click on any workflow run to see:
   - Logs
   - Papers found
   - Errors (if any)
3. Download artifacts to see the raw output files

## Cost

- **GitHub Actions**: Free (2,000 minutes/month for free tier, you'll use ~5-10 minutes/month)
- **GitHub Pages**: Free (for public repos)
- **Claude API**: ~$0.10-$0.30 per day (~$3-$10/month)
- **Total**: Just the Claude API cost

## Customization

### Change ArXiv Categories

Edit `configs/config.ini`:
```ini
[FILTERING]
arxiv_category = cs.CL,cs.LG,cs.AI
```

### Change Filtering Thresholds

Edit `configs/config.ini`:
```ini
[FILTERING]
hcutoff = 15          # Minimum author h-index
relevance_cutoff = 3  # Minimum relevance score
novelty_cutoff = 3    # Minimum novelty score
```

### Use Cheaper Model

Edit `configs/config.ini`:
```ini
[SELECTION]
model = claude-3-haiku-20240307  # Much cheaper, slightly less accurate
```

## Troubleshooting

### Workflow Failing?

1. Check **Actions** tab for error messages
2. Common issues:
   - **"ANTHROPIC_API_KEY not set"**: Add it in Settings → Secrets
   - **"Invalid API key"**: Check your key is correct
   - **"Insufficient credits"**: Add credits to your Anthropic account

### Papers Not Appearing on Website?

1. Check if workflow completed successfully (Actions tab)
2. Make sure GitHub Pages is set to "GitHub Actions" source
3. Wait a few minutes after workflow completes
4. Check if Pages is enabled: Settings → Pages

### No Papers Being Selected?

Lower filtering thresholds in `configs/config.ini`:
```ini
hcutoff = 10          # Lower from 15
relevance_cutoff = 2  # Lower from 3
novelty_cutoff = 2    # Lower from 3
```

### Workflow Not Running Daily?

1. Check if Actions are enabled (Actions tab)
2. For forked repos, you need to manually enable workflows
3. Check the cron schedule in `.github/workflows/cron_runs.yaml`

## Security Notes

- ✅ Your API keys are **secure** in GitHub Secrets
- ✅ They're **never exposed** in logs or code
- ✅ They're **never committed** to the repo
- ✅ Only your repo can access them

## Comparison: GitHub Actions vs Local Cron

| Feature | GitHub Actions | Local Cron |
|---------|---------------|------------|
| Setup complexity | ⭐ Easy | ⭐⭐⭐ Complex |
| Cost | Free + Claude API | Free + Claude API |
| Requires local machine | ❌ No | ✅ Yes |
| Works when computer off | ✅ Yes | ❌ No |
| Auto-publishes to web | ✅ Yes | Needs extra setup |
| Maintenance | None | Update/monitor cron |

**Recommendation:** Use GitHub Actions unless you have a specific reason to run locally!

## Next Steps

1. ✅ Set up GitHub Actions (you're here!)
2. 📝 Customize your preferences (authors, topics)
3. 🧪 Test with manual run
4. 📚 Bookmark your papers site
5. 🎉 Enjoy your daily papers!

## Need Help?

- Check workflow logs in Actions tab
- Review config files in `configs/`
- See main [README.md](README.md) for more info
