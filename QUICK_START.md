# Quick Start Guide

Get your paper scanner running in 5 minutes!

## Choose Your Setup Method

### 🌟 Option 1: GitHub Actions (RECOMMENDED!)
**Easiest setup - runs in the cloud, no local machine needed**

👉 **[Follow GitHub Actions Setup Guide](GITHUB_ACTIONS_SETUP.md)**

- ✅ Runs automatically in GitHub's cloud
- ✅ No cron jobs or local setup
- ✅ Works even when your computer is off
- ✅ Auto-publishes to `aashiqmuhamed.github.io/daily_papers`

### Option 2: Local Cron (Advanced)
**For those who want to run on their own machine**

Continue reading below for local setup...

---

## Local Setup (Option 2)

### Step 1: Set Up API Keys (IMPORTANT - Do this first!)

Create a `.env` file with your API keys:

```bash
# Copy the example file
cp .env.example .env

# Edit it with your actual keys
nano .env
```

Add your keys:
```bash
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
S2_KEY=your-semantic-scholar-key-here
```

**Get your keys:**
- **Anthropic (required)**: https://console.anthropic.com/ (sign up, get $5 free credit)
- **Semantic Scholar (optional but recommended)**: https://www.semanticscholar.org/product/api#api-key-form

**⚠️ SECURITY NOTE:** The `.env` file is in `.gitignore` so it won't be committed to GitHub. Your keys are safe!

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Configure Your Preferences

Edit these files to customize what papers you want:

```bash
# Add authors you follow (get IDs from semanticscholar.org)
nano configs/authors.txt

# Add topics you're interested in
nano configs/paper_topics.txt

# (Optional) Adjust filtering settings
nano configs/config.ini
```

## Step 4: Test It!

```bash
python main.py
```

You should see papers being fetched and filtered. Results will be in:
- `out/output.md` (readable format)
- `out/output.json` (structured data)

## Step 5: Set Up GitHub Pages

Follow the detailed guide: [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)

This will:
1. Create a GitHub repo at `aashiqmuhamed/daily_papers`
2. Enable GitHub Pages
3. Set up daily cron job
4. Auto-publish to `aashiqmuhamed.github.io/daily_papers`

## Step 6: Set Up Cron Job

```bash
# Make script executable
chmod +x run_and_publish.sh

# Add to crontab
crontab -e

# Add this line (runs daily at 1 PM UTC):
0 13 * * * /Users/amuhamed/Documents/cmu/gpt_paper_assistant/run_and_publish.sh
```

## That's It!

Your scanner will now:
- ✅ Run automatically every day
- ✅ Filter papers with Claude based on your interests
- ✅ Commit results to GitHub
- ✅ Publish to your GitHub Pages site
- ✅ Keep your API keys secure (never committed)

## Troubleshooting

**"ERROR: ANTHROPIC_API_KEY not set"**
- Make sure you created `.env` file (not `.env.example`)
- Make sure it has `ANTHROPIC_API_KEY=sk-ant-...` with your actual key

**Papers site not updating?**
```bash
# Check if cron ran
tail logs/cron.log

# Check if files committed
git log --oneline -5

# Manually run to debug
./run_and_publish.sh
```

**Too expensive?**
- Edit `configs/config.ini`
- Change model to `claude-3-haiku-20240307` (cheaper)
- Or increase `hcutoff` to filter more aggressively

## Need Help?

- Full setup: [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)
- Local details: [LOCAL_SETUP.md](LOCAL_SETUP.md)
- Main README: [README.md](README.md)
