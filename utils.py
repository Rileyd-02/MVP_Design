import os
from datetime import datetime

def save_brief_locally(text, folder="saved_briefs"):
    os.makedirs(folder, exist_ok=True)
    filename = f"brief_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.txt"
    path = os.path.join(folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    return path

def clean_input(value):
    return value.strip() if value else ""
