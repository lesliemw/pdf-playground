import sys
import PyPDF2

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    '''combines all the pdfs in the list into a single pdf'''
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")


pdf_combiner(inputs)


template = PyPDF2.PdfFileReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open("watermarked_output.pdf", "wb") as file:
        output.write(file)


with open("dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    with open("tilt.pdf", "wb") as file:
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        writer.write(file)
