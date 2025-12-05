# email_fetcher.py
# -----------------
# Handles connecting to Gmail/Outlook/IMAP and pulling emails.

from imapclient import IMAPClient
import pyzmail

class EmailFetcher:
    def __init__(self, email, password, server="imap.gmail.com"):
        self.email = email
        self.password = password
        self.server = server

    def fetch_latest_emails(self, count=10):
        print(f"Connecting to {self.server}...")

        with IMAPClient(self.server) as client:
            client.login(self.email, self.password)
            client.select_folder("INBOX")

            # Search for all emails
            messages = client.search(["ALL"])
            messages = messages[-count:]  # take last N emails

            emails = []

            for msgid in messages:
                raw = client.fetch(msgid, ["RFC822"])[msgid][b"RFC822"]
                message = pyzmail.PyzMessage.factory(raw)

                email_obj = {
                    "from": message.get_addresses("from"),
                    "subject": message.get_subject(),
                    "text": message.text_part.get_payload().decode(message.text_part.charset) if message.text_part else "",
                }

                emails.append(email_obj)

        return emails

