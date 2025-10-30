# GitHub Pages Setup Guide

This guide will help you set up your ArXiv paper scanner to automatically publish to GitHub Pages at `aashiqmuhamed.github.io/daily_papers`.

## Prerequisites

- Git installed on your Mac
- GitHub account (aashiqmuhamed)
- Anthropic API key for Claude

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named `daily_papers`
3. Make it **public** (required for free GitHub Pages)
4. Don't initialize with README (we already have files)

## Step 2: Connect Your Local Repo to GitHub

If you haven't already connected this repo to GitHub:

```bash
cd /Users/amuhamed/Documents/cmu/gpt_paper_assistant

# Check current remote
git remote -v

# If no remote exists or you need to add the new one
git remote add origin https://github.com/aashiqmuhamed/daily_papers.git

# Or if you need to change it
git remote set-url origin https://github.com/aashiqmuhamed/daily_papers.git
```

## Step 3: Push Your Initial Code

```bash
# Add all files
git add .

# Commit
git commit -m "Initial setup: Claude + local cron + GitHub Pages"

# Push to GitHub (you may need to authenticate)
git push -u origin main
```

If you get an authentication error, you'll need to set up a GitHub Personal Access Token:
1. Go to https://github.com/settings/tokens
2. Generate new token (classic)
3. Give it `repo` permissions
4. Use the token as your password when pushing

## Step 4: Enable GitHub Pages

1. Go to your repository: https://github.com/aashiqmuhamed/daily_papers
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
5. Click **Save**

GitHub will start building your site. After a few minutes, your site will be live at:
**https://aashiqmuhamed.github.io/daily_papers**

## Step 5: Set Up Environment Variables

Set your API key (add to `~/.zshrc` or `~/.bashrc`):

```bash
# Add to ~/.zshrc (or ~/.bashrc if you use bash)
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
export S2_KEY="your-semantic-scholar-key"  # Optional but recommended
```

Then reload:
```bash
source ~/.zshrc
```

## Step 6: Configure Authors and Topics

1. **Edit `configs/authors.txt`** with authors you want to follow:
   ```
   # Format: Author Name, SemanticScholarID
   Yann LeCun, 1234567
   Geoffrey Hinton, 2345678
   ```

   Find Semantic Scholar IDs at https://www.semanticscholar.org/

2. **Edit `configs/paper_topics.txt`** with topics you're interested in:
   ```
   1. New methodological improvements to RLHF or instruction-following
   2. Novel approaches to language model training
   ```

3. **Edit `configs/config.ini`** if needed:
   - Change ArXiv categories
   - Adjust filtering thresholds
   - Model is already set to Claude 3.5 Sonnet

## Step 7: Make Scripts Executable

```bash
chmod +x run_and_publish.sh
```

## Step 8: Test the Script

Run it manually first to make sure everything works:

```bash
./run_and_publish.sh
```

You should see:
- Papers being fetched
- Filtering happening
- Files created in `out/`
- Changes committed and pushed to GitHub
- Check `logs/cron.log` for details

After a few minutes, visit: https://aashiqmuhamed.github.io/daily_papers

## Step 9: Set Up Cron Job

Open your crontab:
```bash
crontab -e
```

Add this line to run daily at 1 PM UTC (optimal for ArXiv updates):
```bash
0 13 * * * /Users/amuhamed/Documents/cmu/gpt_paper_assistant/run_and_publish.sh
```

Or run at 9 AM local time:
```bash
0 9 * * * /Users/amuhamed/Documents/cmu/gpt_paper_assistant/run_and_publish.sh
```

Save and exit (`:wq` in vim, or `Ctrl+X` then `Y` in nano).

## Step 10: Verify Everything Works

Check your cron jobs:
```bash
crontab -l
```

Check the logs after the first run:
```bash
tail -f /Users/amuhamed/Documents/cmu/gpt_paper_assistant/logs/cron.log
```

Visit your site:
```
https://aashiqmuhamed.github.io/daily_papers
```

## Customizing the Website

### Change the Title/Look

Edit `index.html` to customize the landing page.

The actual papers are displayed from `out/output.md` which is auto-generated.

### Custom Domain (Optional)

If you own a domain and want to use `papers.yourdomain.com`:

1. Add a `CNAME` file to your repo:
   ```bash
   echo "papers.yourdomain.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push
   ```

2. Configure your domain's DNS:
   - Add a CNAME record pointing to `aashiqmuhamed.github.io`

3. In GitHub Settings > Pages, enter your custom domain

## Troubleshooting

### Site Not Updating

1. Check if the cron job ran:
   ```bash
   tail logs/cron.log
   ```

2. Check if files were committed:
   ```bash
   git log --oneline -5
   ```

3. Check GitHub Pages build status:
   - Go to your repo > Actions tab

### Authentication Issues

If `git push` fails with authentication errors:

1. **Option 1: Personal Access Token (Recommended)**
   - Create token at https://github.com/settings/tokens
   - Use as password when prompted

2. **Option 2: SSH Keys**
   ```bash
   # Generate SSH key
   ssh-keygen -t ed25519 -C "your_email@example.com"

   # Add to GitHub: https://github.com/settings/keys

   # Change remote to SSH
   git remote set-url origin git@github.com:aashiqmuhamed/daily_papers.git
   ```

3. **Option 3: GitHub CLI**
   ```bash
   # Install GitHub CLI
   brew install gh

   # Authenticate
   gh auth login
   ```

### Papers Not Being Selected

Lower the filtering thresholds in `configs/config.ini`:
```ini
hcutoff = 10          # Lower from 15
relevance_cutoff = 2  # Lower from 3
novelty_cutoff = 2    # Lower from 3
```

### Cost Too High

- Increase `hcutoff` to filter out more papers
- Reduce ArXiv categories
- Switch to Claude Haiku (cheaper): `model = claude-3-haiku-20240307`

## Daily Workflow

Once set up, the workflow is fully automatic:

1. **Cron runs daily** at scheduled time
2. **Fetches papers** from ArXiv
3. **Filters with Claude** based on your criteria
4. **Commits results** to GitHub
5. **GitHub Pages updates** automatically (within a few minutes)
6. **You check the website** whenever you want

That's it! No manual intervention needed.

## Useful Commands

```bash
# Test run manually
./run_and_publish.sh

# Check logs
tail -f logs/cron.log

# Check what will be committed
git status

# View recent commits
git log --oneline -10

# Check if cron is running
crontab -l

# Force update the website
git push origin main
```

## Cost Estimation

Claude 3.5 Sonnet pricing:
- Typically **$0.10-$0.30 per day** for cs.CL + cs.LG + cs.AI
- About **$3-$10 per month**

Everything else (GitHub, GitHub Pages, cron) is **completely free**.
