import os
import requests

system_prompt = """
You are an Enterprise Smart Notification Agent for campus automation.

Your task for each email:
1. Generate a 5-line summary.
2. Extract action deadlines and tasks.
3. Classify category: Academic, HR, Finance, IT, General.
4. Assign urgency: Critical, High, Normal.
5. Extract: Action required? Yes/No.

Output strictly in format:
Summary: <summary>
Category: <category>
Urgency: <urgency>
Action: <yes/no>
"""

def smart_notification_agent(email_text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-4o",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": email_text}
        ],
        "max_tokens": 512,
        "temperature": 0.3
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
