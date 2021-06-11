angka1 = [2,3,4,56,43,45,1,2,8,65,5,3,46,4,3,8,7,65,7,8,78,98,98,87,65,43,54 ]
angka2 = [2,4,5,6,7,4,3,7,8,6,5,4,5,55,6,77,4,67,7,6,66,3,2,2,67,23,12]
angka3 = ["2", "2", "2", "4", "3"]
kalimat = "jangan"
gabungankalimat = ["q", "w", "e", "r", "t"," ", "y", "u", "i", "o", "p"]

print(type(angka3))     # cek type
print(angka3[3:])       # slicing
print(sorted(angka1))   # sorting / mengurutkan
urutkan = sorted(angka1)
print(urutkan[::-1])    # reverse
angka2.sort()           # urutkan dengan .sort() method
print(angka2)           # panggil variablenya
angka2.remove(3)        # panggil methodnya dulu
print(angka2)           # baru panggil variablenya
print(angka1.count(7)) # menghitung berapa kali sebuah angka itu muncul di deretan angka
print(angka1.index(43)) # mencari posisi value index dalam urutan sebuah angka
print(angka1.index(43,3,6)) # mencari posisi index dari range index ke 3 - ke 6, jika ditemukan nilai 43, maka kasih
# tau berada di index berapa
print(type(kalimat))
print(kalimat[::-1])    # reverse string
print(kalimat.split(","))   # merubah ke bentuk list
print(type(kalimat))
print(kalimat.index("n"))
print(kalimat.count("n"))   # menghitung berapa sering huruf n muncul di sebuah kata
kalimat = kalimat[-3:]
kalimatbaru = "jura"
print(kalimatbaru+kalimat)  # concatenasi
print(gabungankalimat)  # sebelum diubah
gabungankalimat.sort()  # harus dipanggil dulu
print(gabungankalimat)  # setalah diubah
print(gabungankalimat.index(" "))   # mencari posisi index
gabungankalimat.remove(" ") # jika gunakan remove harus dipanngil dulu, baru ditampilkan
print(gabungankalimat)


for i in angka3:
    conv2str = int(i)   # converting to int, must to loop first
    # conv2list = list(conv2str)
    print(type(conv2str))

# print(conv2str)

kata1 = "Terlalu Manis"
kata2 = "tarik sis"
print("{}, semongko".format(kata2))
print("Gulanya, {}, apakah bisa dikurangi?".format(kata1))
print("{0} {1} {0} ".format(angka1[11:], angka3))  # formating berdasarkan index, index selalu dimulai dari 0

number = 100 / 456
print(number)
print("hasil dari pembagian antara 100 / 456: {n:1.2f}".format(n=number)) # roundup floating point
# tekniknya buat variable di dalam method .format() lalu taruh di placeholder {}, panggil variablenya
# {n:1.2f} : n => variable, 1 => digit pertama sebelum titik desimal, 2 => pembulatan 2 digit setalah tanda desimal,
# f => floating point

# formated string literal
print(f"hasil bagi antara 100 / 456: {number}") # tanpa pembulatan
print(f"hasil bagi antara 100 / 456: {number:1.4f}") # dengan pembulatan
print()


#=======================================================================================================================
d = {'k1': [{'nest_key': ['this is deep',['hello']]}]}         # grab hello
print(d['k1'])                      # grab key dict
print(d['k1'][0])                   # grab value dari k1 dan grab indexnya
print(d['k1'][0]['nest_key'])       # grab dict
print(d['k1'][0]['nest_key'][1][0])
print()
d = {'k1' : [1, 2, { 'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}  # grab hello
print(d['k1'])
print(d['k1'][2])
print(d['k1'][2]['k2'])
print(d['k1'][2]['k2'][1])
print(d['k1'][2]['k2'][1]['tough'][2][0])
print()

list1 = [2,3,4,5]
list2 = [6,7,8,9]
list1.extend(list2)
print(list1)
list1.append(list2)
print(list1)    # mamngil append dengan cara berbeda
for i in list2:
    list1.append(i)
print(list1)    # manggil dengam melalui loop


