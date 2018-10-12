from io import BytesIO

from weasyprint import HTML


def pdf_from_url(url):
    html = HTML(url)
    pdf_io = BytesIO()
    html.write_pdf(pdf_io)
    pdf_io.seek(0)
    return pdf_io.read()
