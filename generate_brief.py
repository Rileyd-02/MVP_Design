import os
import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_ai_brief(inputs: dict) -> str:
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL", "gpt-4o-mini")

    prompt = f"""
Create a professional product brief for fashion/apparel.

PRODUCT DETAILS:
- Product Line: {inputs['product_line']}
- Category: {inputs['category']}
- Style Name: {inputs['style_name']}
- Season: {inputs['season']}
- Target Customer: {inputs['customer']}
- Use Case: {inputs['use_case']}
- Main Fabric: {inputs['main_fabric']}
- Secondary Fabric: {inputs['secondary_fabric']}
- Key Attributes: {inputs['attributes']}

Generate FOUR SECTIONS:
1. Narrative Brief (2–3 sentences)
2. Key Features (bullet points ending with semicolons)
3. Selling Points (marketing bullets)
4. Tech Pack Summary (structured list)
"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://streamlit.io",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
