import PyPDF2

with open("dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    with open("tilt.pdf", "wb") as file:
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        writer.write(file)
