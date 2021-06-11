# documentation ==> pillow.readthedocs.io
from PIL import Image

# open image with Image Class
img = Image.open('computer_deep_blue.jpg')
img2 = Image.open('banana.png')
# img.show()    # show the image
# img.save('fullpath image location')
s = img.size    # ukuran file
# fn = img.filename    # nama file
# f_d = img.format_description  # melihat format dari file image
# cr = img.crop((0,0, 100, 100)) # start croping di koordinat x=0, y=0, dan berakhir di titik pixel x=100,
# y=100 (cara 1)
x = 50
y = 17
w = 164
h = 250
cr = img.crop((x, y, w, h)) # cropping hanya butuh 1 parameter, jadi jika ada banyak harus dkelompokkan
# img2.paste(im=cr, box=(0, 0))
# im= image source, box= coordinate untuk menaruh gambar paste, im2= adalah tempat untuk paste hasil copynya
print(img2.size)
# img2.resize((330, 441))  # resize image
print(img2.size)
print(type(img2))
# cp.rotate((90))
# img.putalpha(50)    # transparancy
img.show()

