from io import BytesIO

from weasyprint import HTML


def png_from_url(url):
    html = HTML(url)
    png_io = BytesIO()
    html.write_png(png_io)
    png_io.seek(0)
    return png_io.read()
