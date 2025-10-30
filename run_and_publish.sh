#!/bin/bash

# ArXiv Paper Scanner - Run and Publish to GitHub Pages
# This script runs the paper scanner and auto-commits results to GitHub

# Set the project directory
PROJECT_DIR="/Users/amuhamed/Documents/cmu/gpt_paper_assistant"

# Change to project directory
cd "$PROJECT_DIR" || exit

# Load environment variables from .env file if it exists
if [ -f "$PROJECT_DIR/.env" ]; then
    echo "Loading environment variables from .env file..." >> logs/cron.log
    set -a  # automatically export all variables
    source "$PROJECT_DIR/.env"
    set +a
fi

# Verify API key is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "ERROR: ANTHROPIC_API_KEY not set!" >> logs/cron.log
    echo "Please create a .env file with your API key (see .env.example)" >> logs/cron.log
    exit 1
fi

# Create logs directory if it doesn't exist
mkdir -p logs

# Get current date for logging
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "=== ArXiv Scanner Run: $DATE ===" >> logs/cron.log

# Run the main script
echo "Running paper scanner..." >> logs/cron.log
/usr/bin/python3 "$PROJECT_DIR/main.py" >> logs/cron.log 2>&1

# Check if the script ran successfully
if [ $? -eq 0 ]; then
    echo "Paper scanner completed successfully" >> logs/cron.log

    # Check if there are changes to commit
    if [ -n "$(git status --porcelain out/)" ]; then
        echo "Changes detected, committing to git..." >> logs/cron.log

        # Add the output files
        git add out/output.json out/output.md

        # Commit with date
        COMMIT_DATE=$(date '+%Y-%m-%d')
        git commit -m "Update papers for $COMMIT_DATE

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>" >> logs/cron.log 2>&1

        # Push to GitHub
        echo "Pushing to GitHub..." >> logs/cron.log
        git push origin main >> logs/cron.log 2>&1

        if [ $? -eq 0 ]; then
            echo "Successfully pushed to GitHub" >> logs/cron.log
        else
            echo "ERROR: Failed to push to GitHub" >> logs/cron.log
        fi
    else
        echo "No changes to commit" >> logs/cron.log
    fi
else
    echo "ERROR: Paper scanner failed" >> logs/cron.log
fi

echo "=== Run completed ===" >> logs/cron.log
echo "" >> logs/cron.log
