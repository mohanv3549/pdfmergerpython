import PyPDF2
if __name__ == '__main__':
    merger=PyPDF2.PdfMerger()
    pdffiles=["1.pdf","2.pdf"]
    for file in pdffiles:
        pdfFile=open(file,'rb')
        pdfReader=PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
    pdfFile.close()
    merger.write('merged.pdf')
