import requests
from dotenv import load_dotenv
import os


def main():
    url = "https://llm-gateway.heurist.xyz/v1/chat/completions"
    load_dotenv()
    api_key = os.getenv("HEURIST_API_KEY")
    payload = {
        "model": "dolphin-2.9-llama3-8b",
        "messages": [
            {
                "role": "user",
                "content": "hello"
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print('Sending request to LLM API...')
    response = requests.request("POST", url, json=payload, headers=headers)
    
    print('Response status code:', response.status_code)
    response_json = response.json()
    
    print('LLM Response:', response_json['choices'][0]['message']['content'])
    
    if response.status_code != 200:
        print('Error:', response_json.get('error', 'Unknown error occurred'))

if __name__ == "__main__":
    main()