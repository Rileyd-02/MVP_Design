from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(text: str, filename="product_brief.pdf") -> str:
    """Create a PDF from text."""
    styles = getSampleStyleSheet()
    story = [Paragraph(p, styles['Normal']) for p in text.split("\n")]

    doc = SimpleDocTemplate(filename, pagesize=A4)
    doc.build(story)

    return filename
