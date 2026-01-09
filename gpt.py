import json
import os
import requests


def ask_gpt(weather_data: dict, city_label: str) -> str:
    """
        Send weather data to ChatGPT and receive a friendly summary.

        Args:
            weather_data (dict): Current weather data
            city_label (str): Human-readable city label

        Returns:
            str: Natural language weather summary
        """

    url = "https://api.openai.com/v1/chat/completions"

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    prompt = (
        f"You are a personal weather copilot.\n"
        f"Location: {city_label}\n"
        f"Weather data (JSON): {weather_data}\n\n"
        f"Explain the current weather in a friendly, human way.\n"
        f"Tell the user what he should wear today.\n"
        f"Suggest one weird, humorous or fun activity inspired by the weather.\n"
    )

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
