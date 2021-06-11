import requests
import bs4
import lxml

# CARA 1
# result = requests.get('https://example.com/')
# soup = bs4.BeautifulSoup(result.text, "lxml")
# # print(type(result))
# # print(result.text)
# print(soup)                                 # memunculkan semua structure webpage
# slct0 = soup.select('p')                    # menampilkan tag dan text yang ada di dalamnya
# # slct0 = soup.select('p a')                # cara lain menampilkan tag dan text yang ada di dalamnya
# # slct0 = soup.select('p > a')              # cara lain menampilkan tag dan text yang ada di dalamnya
# # menampilkan text saja yang ada di dalam text.[0] adalah index, karena bs4
# # akan menampilkan element list, jadi kita bisa ambil berdasarkan indexnya dulu, lalu ambil textnya melalui getText()
# # method
# print('GRAB SEMUA:\n',slct0)
# # print('\nGRAB HANYA TEXT:\n',slct0[1].getText())

# CARA 2 -> SCRAPING TEXT IN "CLASS" TAG (ID TAG procedure is the same)
# res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# s = soup.select('.toctext')     # class dengan simbol period, id dengan simbol hastag
# print(s)        # GET ALL ELEMENT INCULING TEXT
#
# # GET ALL ELEMENT TEXT ONLY
# for i in s:
#     print(i.getText())


# CARA 3 SCRAPING IMAGE ONLY
res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)
s = soup.select('img')[0]['src']
# print(s)
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# print(image_link.content) # grabbing image diatas akan menghasilkna binary file, jadi harus dikonvert dengan cara
# di bawah ini
imgFile = open('computer_deep_blue.jpg', 'wb')      # wb => write binary mode
imgFile.write(image_link.content)
imgFile.close()


