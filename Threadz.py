from email_fetcher import EmailFetcher

def main():
    print("=== Threadz Email Fetch Test ===")

    EMAIL = "your_email_here@gmail.com"
    PASSWORD = "your_app_password_here"  # Not your real password!

    fetcher = EmailFetcher(EMAIL, PASSWORD)
    emails = fetcher.fetch_latest_emails(5)

    for e in emails:
        print("\nFrom:", e["from"])
        print("Subject:", e["subject"])
        print("Text Preview:", e["text"][:120], "...")

https://chatgpt.com/c/69305de9-19a8-8329-ab1d-008343aff8a1