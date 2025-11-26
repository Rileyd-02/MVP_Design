from openai import OpenAI
from utils import get_openai_key

def generate_ai_brief(inputs):
    """Generates a full product brief using OpenAI LLM."""
    
    client = OpenAI(api_key=get_openai_key())

    prompt = f"""
    Create a professional product brief for the fashion/apparel industry.
    
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
    4. Tech Pack Summary (clean, structured list)

    Keep wording professional and specific to apparel.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )

    return response.choices[0].message.content
