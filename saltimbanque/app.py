from base64 import b64decode

from flask import Flask, Response

from .pdf import pdf_from_url


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
        <button onclick="convert()">Convert to PDF!</button>
        <script>
            function convert() {
                var url = document.getElementById('url').value;
                window.location = '/html-to-pdf/' + btoa(url);
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
