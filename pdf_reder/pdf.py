import pyPDF2

a = pyPDF2.pdfFileReader('sql.pdf')
print(a.documentInfo)
print(a.getNumPages())
