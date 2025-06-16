import base64

def fetch_email_bodies(service, max_results=5):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    email_bodies = []

    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = txt['payload']
        parts = payload.get("parts")
        email_text = None

        if payload.get("body") and payload['body'].get('data'):
            email_text = base64.urlsafe_b64decode(payload['body']['data']).decode("utf-8")
        elif parts:
            for part in parts:
                if part.get("body") and part['body'].get('data'):
                    email_text = base64.urlsafe_b64decode(part['body']['data']).decode("utf-8")
                    break

        if email_text:
            email_bodies.append(email_text)

    print(f"✅ Unfetched {len(email_bodies)} emails for AI analysis.")
    return email_bodies
