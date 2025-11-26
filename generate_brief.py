import os
from openai import OpenAI

def generate_ai_brief(inputs: dict) -> str:
    """
    Generate a product brief using OpenRouter API.
    inputs: dict containing product details
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL", "gpt-4o-mini")

    client = OpenAI(api_key=api_key, api_base="https://openrouter.ai/api/v1")

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
    3. Selling Points (Marketing-style bullets)
    4. Tech Pack Summary (structured list)

    Keep the tone professional and specific to apparel.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
