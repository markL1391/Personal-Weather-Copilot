import json
import os
import requests


def main():
    url = "https://api.openai.com/v1/chat/completions"

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": "Do you have an idea for a cool catchphrase for me to use?"}
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    print(response.json()["choices"][0]["message"]["content"])


if __name__ == "__main__":
    main()
