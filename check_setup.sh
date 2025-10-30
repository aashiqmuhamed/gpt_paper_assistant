#!/bin/bash

# Setup Checker - Verify your configuration is correct
echo "🔍 Checking your setup..."
echo ""

# Check if .env exists
if [ -f ".env" ]; then
    echo "✅ .env file found"

    # Check if ANTHROPIC_API_KEY is set in .env
    if grep -q "ANTHROPIC_API_KEY=sk-ant-" .env; then
        echo "✅ ANTHROPIC_API_KEY appears to be set"
    else
        echo "❌ ANTHROPIC_API_KEY not found or invalid in .env"
        echo "   Expected format: ANTHROPIC_API_KEY=sk-ant-..."
    fi

    # Check if S2_KEY is set in .env
    if grep -q "S2_KEY=" .env && ! grep -q "S2_KEY=your-semantic-scholar-key-here" .env; then
        echo "✅ S2_KEY is set"
    else
        echo "⚠️  S2_KEY not set (optional but recommended for faster author lookups)"
    fi
else
    echo "❌ .env file NOT found!"
    echo "   Create it with: cp .env.example .env"
    echo "   Then edit it with your actual API keys"
fi

echo ""

# Check if configs are set up
if [ -f "configs/authors.txt" ]; then
    author_count=$(grep -v "^#" configs/authors.txt | grep -v "^$" | wc -l | tr -d ' ')
    echo "✅ Authors configured: $author_count authors"
else
    echo "❌ configs/authors.txt not found"
fi

if [ -f "configs/paper_topics.txt" ]; then
    echo "✅ Paper topics configured"
else
    echo "❌ configs/paper_topics.txt not found"
fi

echo ""

# Check if dependencies are installed
if python3 -c "import litellm" 2>/dev/null; then
    echo "✅ Python dependencies installed"
else
    echo "❌ Python dependencies not installed"
    echo "   Run: pip install -r requirements.txt"
fi

echo ""

# Check if script is executable
if [ -x "run_and_publish.sh" ]; then
    echo "✅ run_and_publish.sh is executable"
else
    echo "⚠️  run_and_publish.sh not executable"
    echo "   Run: chmod +x run_and_publish.sh"
fi

echo ""

# Check git setup
if git remote get-url origin >/dev/null 2>&1; then
    remote_url=$(git remote get-url origin)
    echo "✅ Git remote configured: $remote_url"
else
    echo "⚠️  No git remote configured (needed for GitHub Pages)"
    echo "   See GITHUB_PAGES_SETUP.md for instructions"
fi

echo ""
echo "📝 Next steps:"
if [ ! -f ".env" ]; then
    echo "   1. Create .env file with your API keys"
fi
if ! python3 -c "import litellm" 2>/dev/null; then
    echo "   2. Install dependencies: pip install -r requirements.txt"
fi
echo "   3. Test: python main.py"
echo "   4. Set up GitHub Pages: see GITHUB_PAGES_SETUP.md"
echo "   5. Set up cron job: see QUICK_START.md"
