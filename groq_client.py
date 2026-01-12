import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

def generate_brochure(messages, temperature=0.3):
    if not API_KEY:
        return "❌ API key not set"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": temperature
    }

    try:
        r = requests.post(BASE_URL, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError:
        return f"❌ HTTP Error {r.status_code}: {r.text}"

    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {str(e)}"

    except KeyError:
        return f"❌ Invalid response format: {r.text}"
