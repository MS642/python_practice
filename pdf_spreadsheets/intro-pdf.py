# Library PyPDF2
import PyPDF2
# rb = read binary
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
f.close()

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page_one = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)
pdf_output = open('Some_BrandNew_Doc1.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()
