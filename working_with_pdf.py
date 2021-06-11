# OPENSOURCE LIBRARY
# PyPDF2
import PyPDF2

# READ PAGE ONE STRUCTURE
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
# print(pdf_reader.numPages)      # check num pages in pdf

page_one = pdf_reader.getPage(0)
# getPage => parameternya adalah indexing page, jadi tekniknya adalah cari tau
# dulu berapa pages pdf file itu punya, baru ambil pages satu persatu

# EXTRACT TEXT FROM PDF TO WORK WITH PYTHON
page_one_text = page_one.extractText()  # setelah tahu pagenya, maka extract textnya dengan cara ini, tapi tolong
# perhatikan bahwa kadang cara ini tidak berhasil untuk file dari scan, kadang bisa kadang juga tidak,
# jadi jika tidak bisa coba cek library yang lain
# print(page_one_text)

# setelah selesai, jangan lupa tutup filenya
f.close()

# WRITE ONE PAGE ONLY STRUCTURE
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page_one = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)

# OUTPUT THE FILE INTO NEW FILE
pdf_output = open('File_PDF_Baru.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()

# GRAB ALL TEXT IN PDF WITH FOR LOOP
f = open('Working_Business_Proposal.pdf', 'rb')

# ADD PLACEHOLDER TO PUT INDEX PDF
pdf_text = []
pdf_reader =  PyPDF2.PdfFileReader(f)

# LOOPING
for num in range(pdf_reader.numPages):

    # get page dari individual page
    page = pdf_reader.getPage(num)

    # masukkan ke dalam list dari pdf_text dan extract hanya textnya saja
    pdf_text.append(page.extractText())

for i in pdf_text:
    print(i)

