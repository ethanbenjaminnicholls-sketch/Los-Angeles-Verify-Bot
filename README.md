# Los Angeles State Roleplay — Verification Bot

A Discord bot that sends a persistent verification panel with a button. When a member clicks **Verify**, they receive the Verified role automatically.

## Features
- `/sendverify` slash command (admin only) — posts the embed + button in your verification channel
- Button stays working even after the bot restarts
- Slash commands only sync **once** per run, so no duplicate panels

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your bot token
Create a `.env` file (never commit this):
```
DISCORD_TOKEN=your_bot_token_here
```

Then load it before running:
```bash
# Linux / Mac
export DISCORD_TOKEN=your_bot_token_here
python bot.py

# Or with python-dotenv installed:
pip install python-dotenv
```
> **Tip:** On Railway, Render, or a VPS, add `DISCORD_TOKEN` as an environment variable in your hosting dashboard — no `.env` file needed.

### 4. Discord Developer Portal settings
- Enable **Server Members Intent** under your bot's Privileged Gateway Intents
- Invite the bot with `bot` + `applications.commands` scopes and `Manage Roles` permission

### 5. Run
```bash
python bot.py
```

## Hosting 24/7 (free options)
| Platform | Notes |
|----------|-------|
| **Railway** | Free tier, just push to GitHub and connect repo |
| **Render** | Free background worker, add env var in dashboard |
| **Oracle Cloud Free** | Always-free VPS, run with `nohup python bot.py &` |

## File overview
```
bot.py            # Main bot code
requirements.txt  # Python dependencies
.env.example      # Template — copy to .env with your real token
.gitignore        # Keeps .env out of git
```
