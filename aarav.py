# from pypdf import PdfWriter
#
# writer = PdfWriter(clone_from="/Users/manojprabaharraju/PycharmProjects/aaravalert/test.pdf")
#
# for page in writer.pages:
#     page.compress_content_streams()  # This is CPU intensive!
#
# with open("out.pdf", "wb") as f:
#     writer.write(f)


# from pypdf import PdfWriter
#
# writer = PdfWriter(clone_from="/Users/manojprabaharraju/PycharmProjects/aaravalert/d_p.pdf")
#
# for page in writer.pages:
#     for img in page.images:
#         img.replace(img.image, quality=5)
#
# with open("d_p_c.pdf", "wb") as f:
#     writer.write(f)


# from PyPDF2 import PdfWriter, PdfReader
#
# inputpdf = PdfReader(open("/Users/manojprabaharraju/PycharmProjects/aaravalert/d_p.pdf", "rb"))
# output = PdfWriter()
# for i in range(2):
#     output.add_page(inputpdf.pages[i])
#     with open("/Users/manojprabaharraju/PycharmProjects/aaravalert/d_p_o.pdf", "wb") as outputStream:
#         output.write(outputStream)

from pypdf import PdfWriter
writer = PdfWriter(clone_from="/Users/manojprabaharraju/PycharmProjects/aaravalert/legal.pdf")

for page in writer.pages:
    for img in page.images:
        img.replace(img.image, quality=5)

with open("legal_out.pdf", "wb") as f:
    writer.write(f)