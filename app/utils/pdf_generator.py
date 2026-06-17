from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os 

def generate_pdf(report_id:int, topic:str , report:str):
    os.makedirs("reports", exist_ok=True)
    file_path = f"reports/report_{report_id}.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = [
        Paragraph(f"<b>{topic}</b>", styles["Title"]),
        Spacer(1, 12),
        Paragraph(report.replace("\n", "<br/>"), styles["BodyText"]),
    ]

    doc.build(content)

    return file_path