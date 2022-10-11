from pdf2docx import Converter
pdf_file = 'Yash vij ResumeExp 2022.pdf'
docs_file = 'Yash vij ResumeExp 2022.docx'
cv = Converter(pdf_file)
cv.convert(docs_file)
cv.close()