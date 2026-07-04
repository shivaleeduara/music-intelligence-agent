# 🎵 Music Intelligence Agent

An AI-powered automation pipeline that fetches the latest music industry news, summarizes articles using **GLM 5.2**, stores insights in **Google Sheets**, and sends a daily email digest.

---

## Features

- Fetches music news from RSS feeds
- Summarizes articles using GLM 5.2
- Stores results in Google Sheets
- Automatically skips duplicate articles
- Sends a formatted HTML email digest
- Supports automated daily execution with Windows Task Scheduler

---

## Workflow

```text
RSS Feeds
    ↓
Research Agent
    ↓
GLM 5.2 Summarization
    ↓
Google Sheets
    ↓
HTML Email
    ↓
Gmail
```

---

## Tech Stack

- Python
- GLM 5.2 API
- Google Sheets API
- Gmail SMTP
- RSS Feeds
- gspread
- python-dotenv

---

## Project Structure

```
Music-Intelligence-Agent/
│
├── agents/
├── credentials/
├── logs/
├── templates/
├── main.py
├── requirements.txt
└── README.md
```

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/shivaleeduara/music-intelligence-agent.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with your API keys and email credentials, add your Google Service Account credentials, then run:

```bash
python main.py
```

---

## Notes

Sensitive files such as `.env`, Google credentials, and logs are excluded from GitHub via `.gitignore`.

---

## Author

**Shivalee Duara**