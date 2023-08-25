import pdfkit

options = {
    'page-size': 'A4',
    'margin-top': '0.0in',
    'margin-right': '0.0in',
    'margin-bottom': '0.0in',
    'margin-left': '0.0in',
    "enable-local-file-access": ""
}

pdfkit.from_file('index.html', 'cv.pdf', options=options)