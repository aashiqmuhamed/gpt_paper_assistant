# Local Setup Guide for ArXiv Paper Assistant with Claude

This guide explains how to set up the ArXiv paper assistant to run locally with Claude AI and automatically publish to GitHub Pages via cron job.

**For full GitHub Pages setup, see [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)**

## Prerequisites

- Python 3.8 or higher
- GitHub account
- Anthropic API key for Claude

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Configure the Application

### Update config.ini

Edit `configs/config.ini`:

1. **Model Selection**: The model is already set to Claude 3.5 Sonnet
   ```ini
   model = claude-3-5-sonnet-20241022
   ```

2. **Output Options**: Markdown and JSON output enabled by default
   ```ini
   [OUTPUT]
   dump_json = true
   dump_md = true
   ```

### Configure Authors and Topics

1. **Authors**: Edit `configs/authors.txt` with authors you want to follow
   - Format: `Author Name, SemanticScholarID`
   - Find Semantic Scholar IDs at https://www.semanticscholar.org/

2. **Topics**: Edit `configs/paper_topics.txt` with research topics you're interested in

## 3. Set Up Environment Variables

### Required Environment Variables

You need to set these environment variables:

```bash
# For Claude API (required)
export ANTHROPIC_API_KEY="your-anthropic-api-key-here"

# Optional: Semantic Scholar API key (highly recommended to avoid rate limiting)
export S2_KEY="your-semantic-scholar-api-key"
```

### Getting Your API Keys

#### Anthropic API Key
1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (starts with `sk-ant-`)

#### Semantic Scholar API Key (Optional but Recommended)
1. Go to https://www.semanticscholar.org/product/api#api-key-form
2. Fill out the form to request an API key
3. You'll receive it via email

### Making Environment Variables Persistent

#### Option 1: Add to your shell profile (recommended)

Add to `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`:

```bash
# ArXiv Paper Assistant
export ANTHROPIC_API_KEY="sk-ant-..."
export S2_KEY="your-s2-key"  # Optional
```

Then reload your shell:
```bash
source ~/.bashrc  # or ~/.zshrc
```

#### Option 2: Create a .env file

Create a file named `.env` in the project directory:

```bash
ANTHROPIC_API_KEY=sk-ant-...
S2_KEY=your-s2-key
```

Then source it before running:
```bash
source .env
python main.py
```

## 4. Test the Setup

Run the script manually to test:

```bash
python main.py
```

You should see:
- Papers being fetched from ArXiv
- Author information being retrieved
- Claude filtering happening
- Files created in `out/output.json` and `out/output.md`

## 5. Set Up Cron Job

### Use the Provided Script

The project includes `run_and_publish.sh` which runs the scanner and auto-commits to GitHub.

Edit it to add your API keys (around line 12):

```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
export S2_KEY="your-s2-key"  # Optional
```

Make it executable:
```bash
chmod +x run_and_publish.sh
```

Create logs directory:
```bash
mkdir -p logs
```

### Set Up Crontab

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

### Cron Schedule Examples

- `0 9 * * *` - Daily at 9:00 AM
- `0 13 * * *` - Daily at 1:00 PM (recommended for ArXiv updates)
- `0 9 * * 1-5` - Weekdays only at 9:00 AM
- `0 */6 * * *` - Every 6 hours

### Verify Cron Job

List your cron jobs:
```bash
crontab -l
```

Check the logs:
```bash
tail -f logs/cron.log
```

## 6. Troubleshooting

### Claude API Errors

1. **Check API Key**: Verify your ANTHROPIC_API_KEY is set correctly
2. **Check API Credits**: Make sure you have credits in your Anthropic account
3. **Check Model Name**: Ensure the model name in config.ini is correct

### Cron Job Not Running

1. **Check Cron Service**:
   ```bash
   # On macOS
   launchctl list | grep cron

   # On Linux
   systemctl status cron
   ```

2. **Check Absolute Paths**: Make sure all paths in the wrapper script are absolute

3. **Check Permissions**: Ensure the wrapper script is executable

4. **Check Logs**: Look at `logs/cron.log` for errors

### Papers Not Being Selected

1. **Adjust Filtering Thresholds**: In `configs/config.ini`:
   ```ini
   relevance_cutoff = 3
   novelty_cutoff = 3
   hcutoff = 15
   ```
   Lower these values to get more papers

2. **Update Topics**: Make sure your `configs/paper_topics.txt` is specific enough

3. **Add More Authors**: Add more authors to `configs/authors.txt`

## 7. Cost Estimation

Claude 3.5 Sonnet pricing (as of January 2025):
- Input: $3 per million tokens
- Output: $15 per million tokens

Running on cs.CL daily typically costs:
- **$0.10 - $0.30 per day** depending on the number of papers

To reduce costs:
- Increase `hcutoff` in config.ini (filters out papers by author h-index)
- Reduce the number of ArXiv categories
- Use Claude Haiku instead (cheaper but less accurate)

## 8. Viewing Your Papers

After the cron job runs:

### Option 1: View Locally
```bash
# View the markdown file
open out/output.md

# Or view the JSON
cat out/output.json
```

### Option 2: View on GitHub Pages
Visit: `https://aashiqmuhamed.github.io/daily_papers`

(See [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) for setup instructions)

## Support

For issues or questions:
- Check the main README.md
- Review the logs in `logs/cron.log`
- Ensure all environment variables are set correctly
