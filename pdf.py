import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")


pdf_combiner(inputs)

# with open("dummy.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     with open("tilt.pdf", "wb") as file:
#         writer = PyPDF2.PdfFileWriter()
#         writer.addPage(page)
#         writer.write(file)
