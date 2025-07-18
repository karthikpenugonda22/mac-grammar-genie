import sys
import requests
import os
import json
import re
import html

# Get settings from environment variables
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
SYSTEM_PROMPT = os.getenv(
    "MAC_GRAMMAR_GENIE_PROMPT",
    "You are an expert editor. Always correct grammar, spelling, and make it understandable. "
    "Return ONLY the corrected plain text. Do NOT include HTML or formatting."
)

def correct_text(input_text):
    if not API_KEY:
        return "Error: OPENAI_API_KEY is not set."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": input_text}
        ],
        "temperature": 0.2
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    text = sys.stdin.read()
    response = correct_text(text)

    # Clean up unwanted HTML or Slack formatting
    clean = re.sub(r'<[^>]+>', '', response)      # Remove HTML tags
    clean = html.unescape(clean)                  # Unescape HTML entities
    clean = clean.strip()

    print(clean)
