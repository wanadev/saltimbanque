from base64 import b64decode

from flask import Flask, Response

from .pdf import pdf_from_url
from .png import png_from_url


app = Flask(__name__)


@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Saltimbanque</title>
        </head>
        <body>
        <input type="text" id="url" />
        <button onclick="convertToPdf()">Convert to PDF!</button>
        <button onclick="convertToPng()">Convert to PNG!</button>
        <script>
            function convertToPdf() {
                var url = document.getElementById('url').value;
                window.location = '/html-to-pdf/' + btoa(url);
            }
            function convertToPng() {
                var url = document.getElementById('url').value;
                window.location = '/html-to-png/' + btoa(url);
            }
        </script>
        </body>
    </html>
    """  # noqa


@app.route("/html-to-pdf/<string:url>")
def html_to_pdf(url):
    url = b64decode(url)
    url = url.decode("utf-8")
    resp = Response(pdf_from_url(url))
    resp.headers["Content-Type"] = "application/pdf"
    return resp


@app.route("/html-to-png/<string:url>")
def html_to_png(url):
    url = b64decode(url)
    url = url.decode("utf-8")
    resp = Response(png_from_url(url))
    resp.headers["Content-Type"] = "image/png"
    return resp
