# ArXiv Paper Assistant with Claude

A daily ArXiv scanner that uses **Claude 3.5 Sonnet** to find papers matching your research interests. Automatically publishes to GitHub Pages.

**Live Demo:** Will be at `aashiqmuhamed.github.io/daily_papers` after setup

## Features

- 🤖 **Powered by Claude 3.5 Sonnet** via LiteLLM (also supports OpenAI models)
- 📚 **Author matching** with Semantic Scholar integration
- 🔍 **Smart filtering** by relevance, novelty, and h-index
- 🌐 **Auto-publishes to GitHub Pages**
- ⏰ **Runs automatically** every day at 1 PM UTC
- 💰 **Low cost** (~$0.10-$0.30 per day)

## Quick Start

### 🌟 GitHub Actions (Recommended!)

**Simplest setup - runs in the cloud**

1. **Push this repo to GitHub**
2. **Add your API key** as a GitHub secret (`ANTHROPIC_API_KEY`)
3. **Enable GitHub Pages** in repo settings
4. **Done!** Papers will appear daily at `aashiqmuhamed.github.io/daily_papers`

👉 **[Full GitHub Actions Setup Guide →](GITHUB_ACTIONS_SETUP.md)**

### 🖥️ Local Cron (Advanced)

Run on your own machine with cron jobs.

👉 **[Local Setup Guide →](LOCAL_SETUP.md)**

## What You Need

### Required
- **Anthropic API Key** - Get from https://console.anthropic.com/
  - $5 free credit to start
  - ~$3-10/month after that

### Optional but Recommended
- **Semantic Scholar API Key** - Get from https://www.semanticscholar.org/product/api#api-key-form
  - Completely free
  - Makes author lookups 5-10x faster

## Configuration

### 1. Authors to Follow

Edit `configs/authors.txt`:
```
# Format: Author Name, SemanticScholarID
Yann LeCun, 1234567
Geoffrey Hinton, 2345678
```

Find author IDs at https://www.semanticscholar.org/

### 2. Research Topics

Edit `configs/paper_topics.txt`:
```
1. New methodological improvements to RLHF or instruction-following
2. Novel approaches to language model training
3. Advances in multimodal learning
```

Be specific! Claude works better with detailed criteria.

### 3. Settings

Edit `configs/config.ini`:

```ini
[SELECTION]
# Model to use (via LiteLLM)
model = claude-3-5-sonnet-20241022

# Or use cheaper/faster alternatives:
# model = claude-3-haiku-20240307
# model = gpt-4-turbo

[FILTERING]
# ArXiv categories to scan
arxiv_category = cs.CL,cs.LG,cs.AI

# Minimum author h-index (filters low-quality papers)
hcutoff = 15

# Minimum scores (1-10)
relevance_cutoff = 3
novelty_cutoff = 3
```

## How It Works

1. **Fetches papers** from ArXiv RSS feed daily
2. **Matches authors** against your list using Semantic Scholar
3. **Filters by h-index** to reduce API costs
4. **Title filtering** removes obviously irrelevant papers
5. **Claude evaluation** scores papers on relevance and novelty
6. **Publishes results** to GitHub Pages as formatted markdown

## Cost Breakdown

### Claude 3.5 Sonnet
- Input: $3 per million tokens
- Output: $15 per million tokens
- **Typical daily cost:** $0.10-$0.30
- **Monthly:** ~$3-$10

### Cheaper Alternatives
- **Claude 3 Haiku:** ~$0.02-$0.05/day
- **GPT-4 Turbo:** ~$0.05-$0.15/day

### Free
- GitHub Actions (2,000 minutes/month free)
- GitHub Pages
- Semantic Scholar API

## Switching Models

LiteLLM makes it easy to switch between providers. Just change the model in `configs/config.ini`:

```ini
# Claude models
model = claude-3-5-sonnet-20241022  # Best quality
model = claude-3-opus-20240229      # Most capable
model = claude-3-haiku-20240307     # Cheapest

# OpenAI models (requires OPENAI_API_KEY)
model = gpt-4-turbo
model = gpt-4
model = gpt-3.5-turbo
```

## Project Structure

```
.
├── main.py                     # Main script
├── filter_papers.py            # Filtering logic
├── arxiv_scraper.py           # ArXiv API interface
├── configs/
│   ├── config.ini             # Settings
│   ├── authors.txt            # Authors to follow
│   ├── paper_topics.txt       # Topics of interest
│   └── base_prompt.txt        # Claude prompt template
├── .github/workflows/
│   ├── cron_runs.yaml        # Daily workflow
│   └── publish_md_test.yml   # GitHub Pages publish
└── out/
    ├── output.md              # Generated markdown
    └── output.json            # Structured data
```

## Documentation

- **[GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md)** - Recommended cloud setup
- **[LOCAL_SETUP.md](LOCAL_SETUP.md)** - Local cron setup
- **[QUICK_START.md](QUICK_START.md)** - Quick overview of both options
- **[GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)** - Detailed Pages configuration

## Troubleshooting

### No Papers Selected?

Lower filtering thresholds in `configs/config.ini`:
```ini
hcutoff = 10          # Was 15
relevance_cutoff = 2  # Was 3
novelty_cutoff = 2    # Was 3
```

### Too Expensive?

- Use Claude 3 Haiku: `model = claude-3-haiku-20240307`
- Reduce categories: `arxiv_category = cs.CL`
- Increase h-cutoff: `hcutoff = 20`

### GitHub Actions Not Running?

1. Check if Actions are enabled (Actions tab)
2. Check if secrets are set (Settings → Secrets)
3. For forks, manually enable scheduled workflows

## Credits

Based on the original [gpt_paper_assistant](https://github.com/tatsu-lab/gpt_paper_assistant) by Tatsu Lab.

Modified to use:
- Claude via LiteLLM (instead of OpenAI only)
- Simplified setup options
- Improved documentation

## License

Apache 2.0
