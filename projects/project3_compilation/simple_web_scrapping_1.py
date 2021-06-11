import requests
import bs4

# CARA 4 GRABING MULTITPLE ELEMENT
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
two_stars_title = []
for i in range(1, 51):
    pages_scrap = base_url.format(i)
    req = requests.get(pages_scrap)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    starClassTop = '.product_pod'                   # change variable class in here
    books = soup.select(starClassTop)

    for book in books:
        starClass1LevDeep = '.star-rating.Two'      # change variable class in here
        if len(book.select(starClass1LevDeep)) != 0:
            book_title = book.select('a')[1]['title']
            two_stars_title.append(book_title)


# print(two_stars_title)
for i in two_stars_title:
    print(i)

# =================================== CHECKER
# check ='star-rating Four' in str(s)
# print(check)
