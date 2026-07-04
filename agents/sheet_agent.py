import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials/google_credentials.json.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("Music articles").sheet1

print("Connected successfully!")


def add_article(title, source, link, summary):
    sheet.append_row([
        title,
        source,
        link,
        summary
    ])


def get_existing_titles():

    records = sheet.get_all_records()

    titles = set()

    if not records:
        return titles

    print("Detected columns:", list(records[0].keys()))

    for record in records:

        cleaned_record = {
            str(key).strip(): value
            for key, value in record.items()
        }

        if "Title" in cleaned_record:
            titles.add(cleaned_record["Title"])

    return titles