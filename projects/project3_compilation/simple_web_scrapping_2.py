import requests
import bs4

# CARA 4 GRABING MULTITPLE ELEMENT
# base_url = 'http://quotes.toscrape.com/page/{}/'
# author_and_quote = []
#
# req = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(req.text, 'lxml')

# authors = set()
# for name in soup.select('.author'):
#     authors.add(name.text)
# print(authors)
#
# quotes = []
# for q in soup.select('.text'):
#     quotes.append(q.text)
# print(quotes)
#
# tag = []
# for t in soup.select('.tag-item'):
#     tag.append(t.text)
# print(tag)

# exercise terakhir
base_url = 'http://quotes.toscrape.com/page/'

# get only the authors - cara 1 jika diketahui jumlah pagenya, jika tidak maka pakai cara 2
# authors = set()
# for page in range(1, 10):
#     page_url = base_url + str(page)
#     req = requests.get(page_url)
#     soup = bs4.BeautifulSoup(req.text, 'lxml')
#
#     for name in soup.select('.author'):
#         authors.add(name.text)
# for a in authors:
#     print(a)
# ============================================================================================
#
# get only quotes -> cara 2 lebih bagus diterapkan ke web page yang kita tidak ketahui jumlah pagenya
quotes = []
page_valid = True
page = 1
while page_valid:
    page_url = base_url + str(page)
    req = requests.get(page_url)

    # checker untuk validasi keberadaan page
    if 'No quotes found!' in req.text:
        break

    # parsing
    soup = bs4.BeautifulSoup(req.text, 'lxml')

    for name in soup.select('.text'):
        quotes.append(name.text)

    page += 1

for a in quotes:
    print(a)



# =================================== CHECKER
# check ='string-to-check' in str(variable name)
# print(check)
