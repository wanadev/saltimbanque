from flask import Flask, Response

from .pdf import pdf_from_url


app = Flask(__name__)


@app.route("/html-to-pdf/<path:url>")
def html_to_pdf(url):
    resp = Response(pdf_from_url(url))
    resp.headers["Content-Type"] = "application/pdf"
    return resp
