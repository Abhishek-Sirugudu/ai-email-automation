from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

def authenticate_gmail(creds_path, scopes):
    flow = Flow.from_client_secrets_file(
        creds_path,
        scopes=scopes,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )
    auth_url, _ = flow.authorization_url(prompt='consent')
    print("🔐 Visit this URL to authorize:\n", auth_url)
    code = input("Enter the authorization code: ")
    flow.fetch_token(code=code)
    return build('gmail', 'v1', credentials=flow.credentials)
