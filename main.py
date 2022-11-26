from pdf2docx import Converter
pdf=('Mbwere.pdf')
docx=('Mbwere.docx')
cv=Converter(pdf)
cv.convert(docx)