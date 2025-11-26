from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def create_pdf(text, filename="product_brief.pdf"):
    styles = getSampleStyleSheet()
    content = [Paragraph(p, styles["Normal"]) for p in text.split("\n")]

    doc = SimpleDocTemplate(filename, pagesize=A4)
    doc.build(content)

    return filename
