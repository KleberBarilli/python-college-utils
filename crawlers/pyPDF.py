import PyPDF2 as p2

pdf_file = open('pdfteste.pdf','rb')
pdf_read = p2.PdfFileReader(pdf_file)

x = pdf_read.getPage(4)
print(x.extractText())

print(pdf_read.getIsEncrypted())

print(pdf_read.getDocumentInfo())
print(pdf_read.getNumPages())