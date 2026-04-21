# 🤖 AI Code Review Bot

An automated code review bot that triggers on every Pull Request and posts AI-generated feedback as a comment — instantly, with zero manual effort.

Built with Python, Groq (LLaMA 3), and GitHub Actions.

---

## 🚀 What it does

- Triggers automatically when a PR is opened or updated
- Reads the code diff from the PR
- Sends it to an AI model for review
- Posts structured feedback as a PR comment covering:
  - Bugs & logic errors
  - Security vulnerabilities
  - Code quality & readability
  - Performance improvements

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Groq API (LLaMA 3.3 70B) | AI code review engine |
| PyGithub | GitHub API integration |
| GitHub Actions | Automation & triggers |
| python-dotenv | Environment variable management |

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/Aaradhya1807/test-review-bot.git
cd test-review-bot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install groq PyGithub python-dotenv
```


### 4. Set up environment variables
Create a `.env` file in the root folder:
GROQ_API_KEY=your_groq_api_key_here
GITHUB_TOKEN=your_github_token_here

---

## 🔑 Getting API Keys

**Groq API Key**
- Sign up at [console.groq.com](https://console.groq.com)
- Go to API Keys → Create new key

**GitHub Token**
- Go to [github.com/settings/tokens](https://github.com/settings/tokens)
- Generate new token (classic)
- Enable `repo` scope

---

## ⚙️ GitHub Actions Setup

### 1. Add your Groq API key as a GitHub secret
- Go to your repo → Settings → Secrets and variables → Actions
- Click **New repository secret**
- Name: `GROQ_API_KEY`, Value: your Groq API key

### 2. Enable workflow permissions
- Go to repo → Settings → Actions → General
- Under **Workflow permissions** select **Read and write permissions**
- Check **Allow GitHub Actions to create and approve pull requests**
- Save

### 3. The workflow triggers automatically
Every time a PR is opened or updated, the bot runs and posts a review comment.

---

## 📁 Project Structure

ai-review-bot/
├── .github/
│   └── workflows/
│       └── review.yml       # GitHub Actions workflow
├── reviewer.py              # AI review logic
├── github_bot.py            # GitHub API integration
├── .env                     # API keys (never commit this!)
├── .gitignore               # Ignores .env
└── README.md                # You are here

---

## 🔒 Security Notes

- Never commit your `.env` file
- Always regenerate API keys if accidentally exposed
- The `.gitignore` file ensures `.env` is never tracked

---

## 🧠 How it works
PR Opened
↓
GitHub Actions triggers review.yml
↓
github_bot.py fetches the PR diff
↓
reviewer.py sends diff to Groq AI
↓
AI returns structured review
↓
Bot posts comment on the PR

---

## 📈 Roadmap

- [ ] Language-specific review rules
- [ ] PR scoring (e.g. 7/10)
- [ ] Auto-labeling PRs (needs-work / looks-good)
- [ ] Support for multiple AI providers

---

Built by [Aaradhya](https://github.com/Aaradhya1807)
