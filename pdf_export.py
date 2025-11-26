from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def create_pdf(text, filename):
    """Generate a PDF from final text."""
    styles = getSampleStyleSheet()
    story = [Paragraph(p, styles['Normal']) for p in text.split("\n")]

    doc = SimpleDocTemplate(filename, pagesize=A4)
    doc.build(story)

    return filename
