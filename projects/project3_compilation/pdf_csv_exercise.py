import csv
import PyPDF2
import re

data = open('/media/yolisk/Data/Yosua/Project/AI/zero_to_hero/find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

# CREATE EMPTY VARIABLE TO STORE STRING THAT HAS BEEN LOOP AND CONCATENATE
link_str = ''

# loop melalui enumerate built in function yang akan menampilkan index
for row_num, data in enumerate(data_lines):

    # isi link str berdasarkan file data row 1 itu sama dengan index dari kolom 1, row 2 = index kolom 2
    link_str += data[row_num]
print(link_str)

# DOWNLOAD PDF FILE DARI LINK DARI CSV
f = open('/media/yolisk/Data/Yosua/Project/AI/zero_to_hero/Find_the_Phone_Number.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(f)
pattern_re = r'\d{3}.\d{3}.\d{4}'
all_text = ''

# LOOP DATANYA
for n in range(pdf.numPages):
    # get page number
    page = pdf.getPage(n)
    # extract text dari tiap pagenya
    page_text = page.extractText()
    # masukkan extract data tersebut dan tambahkan ke dalam variable all_text
    all_text = all_text + ' ' + page_text

# teknik ini cari index matches di dalam memori, agar kita bisa nyari object berdasarkan object
for match in re.finditer(pattern_re,all_text):
    print(match)

# get the index
find_number = all_text[41792:41820]
print(find_number)
