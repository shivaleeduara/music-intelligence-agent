import logging

from agents.email_agent import send_email
from agents.research_agent import get_latest_articles
from agents.summary_agent import summarize_article
from agents.sheet_agent import add_article, get_existing_titles

# -------------------------------------------------
# Logging
# -------------------------------------------------

logging.basicConfig(
    filename="logs/music_agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Music Intelligence Agent Started")

print("Fetching articles...")
logging.info("Fetching articles...")

# -------------------------------------------------
# Fetch articles
# -------------------------------------------------

articles = get_latest_articles()

existing_titles = get_existing_titles()

print(f"Found {len(articles)} articles.")
logging.info(f"Found {len(articles)} articles.")

# -------------------------------------------------
# Email Header
# -------------------------------------------------

email_body = """
<h1>🎵 Daily Music Industry Brief</h1>

<p>
Here are today's latest music industry stories.
</p>

<hr>
"""

new_articles = 0

# -------------------------------------------------
# Process Articles
# -------------------------------------------------

for article in articles[:5]:

    print("=" * 60)
    print(article["title"])

    # Skip duplicates

    if article["title"] in existing_titles:
        print("⚠️ Already exists. Skipping.")
        logging.info(f"Skipped duplicate: {article['title']}")
        continue

    try:

        summary = summarize_article(article["title"])

        print(summary)

        add_article(
            article["title"],
            article["source"],
            article["link"],
            summary
        )

        print("✅ Saved to Google Sheets.")
        logging.info(f"Saved article: {article['title']}")

        new_articles += 1

        email_body += f"""
        <div style="margin-bottom:35px;">

        <h2>{article['title']}</h2>

        <p>
        <strong>Source:</strong> {article['source']}
        </p>

        <p>
        {summary.replace(chr(10), "<br>")}
        </p>

        <p>
        <a href="{article['link']}">
        Read Full Article →
        </a>
        </p>

        </div>

        <hr>
        """

    except Exception as e:

        print(f"❌ Error processing article: {e}")
        logging.error(f"{article['title']} : {e}")

        continue

# -------------------------------------------------
# Email Footer
# -------------------------------------------------

email_body += """
<p style="color:gray;font-size:14px;">

Generated automatically by the Music Intelligence Agent.

</p>
"""

# -------------------------------------------------
# Send Email
# -------------------------------------------------

if new_articles > 0:

    print("Sending email...")
    logging.info("Sending email...")

    send_email(
        subject="🎵 Today's Music Industry Brief",
        body=email_body
    )

    logging.info("Email sent successfully.")

else:

    print("No new articles found. Email not sent.")
    logging.info("No new articles found.")

print("Finished!")
logging.info("Music Intelligence Agent Finished\n")