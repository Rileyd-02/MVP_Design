import os
from datetime import datetime

def save_brief_locally(text: str, folder="saved_briefs") -> str:
    """
    Save generated brief as a text file locally
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(folder, f"brief_{timestamp}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return filename

def clean_input(text: str) -> str:
    """
    Simple helper to strip and normalize input text
    """
    return text.strip() if text else ""
