from random import shuffle, randint

gabungankalimat = ["q", "w", "e", "r", "t"," ", "y", "u", "i", "o", "p"]
angka1 = [2,3,4,56,43,45,1,2,8,65,5,3,46,4,3,8,7,65,7,8,78,98,98,87,65,43,54 ]
angka2 = [2,4,5,6,7,4,3,7,8,6,5,4,5,55,6,77,4,67,7,6,66,3,2,2,67,23,12]

#=====================================================================================================================
lapar = True
if lapar:
    print('bro, saya lapar, beri saya makan')
else:
    print('bro, saya masih kenyang')

kerupuk = "putih"
if kerupuk == 'putih':
    print('kerupuk tersebut warnanya', kerupuk)
else:
    print('kerupuk tersebut berwarna:',kerupuk)
print()

for num in angka1:
    if num % 2 == 0:        # modulus operator atau sisa bagi, disini adalah mencari angka yang dibagi 2 hasilnya 0
        print(f'bilangan genap: {num}')
    else:
        print(f'bilangan ganjil: {num}')
print()
list_sum = 0
for num in angka1:
    list_sum = list_sum + num   # mencari jumlah total dari urutan angka dalam list
    print(list_sum)                 # jika identatasi ditaruh di dalam loop maka akan ditampilkan setiap prosesnya

print(f"Total penjumlahan: {list_sum}")  # jika identatasi ditaruh di luar loop maka akan ditampilkan hanya jumlah
# totalnya saja

mylist = [(1,2), (3,4), (5,6), (7,8)]
for a, b in mylist:       # a, b adalah tuple enpacking atau memanggil value berdasarkna index posisinya
    print(b)
    print(a)

d = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
d2 = {'apel': 'satu', 'manggo': 'dua', 'orange': 'tiga'}
for i in d:             # looping dalam dictionary
    print(i)            # hanya akan print key saja di dictionary, ini adalah default settingnya
for i in d.items():
    print(i)            # akan memprint key-value pair
for k, v in d.items():  # dengan cara tuple enpackaging, kita bisa memanggil hanya key saja atau valuenya saja
    print(k)
    print(v)
for k in d.keys():
    print(k)            # hanya akan memprint keynya saja
for k in d.keys():
    print(k)         # memprint tapi hanya akan slicing karakternya dan hanya 2 karakter yang diperbolehkan
for k in d2.values():
    print(k)            # akan memprint valuenya saja

#=======================================================================================================================
n = 0
while n < 5:
    print(f'angka saat ini adalah {n}')
    n += 1
else:
    print(f'nilai n kurang dari {n} ')

x = 10                      # initial value adalah 10
while x > 0:                # selama nilai x kurang dari 0, maka...

    if x == 5:              # tapi jika nilai x == 5
        print(f'anda sedang berada di lantai {x}')
        break               # maka berhenti di nilai x itu dan print perintahnya
    x -= 1                  # lakukan hitungan mundur dengan mengurangi nilai x nya dengan 1
    print(x)
print()
# ======================================================================================================================
n = range(10)       # counting sampai nilai 10 tapi jangan masukkan 10
for i in n:
    print(i)
print()

m = range(3, 15)    # hitung nilainya antara range 3 sampai 15, tapi jangan masukkan 15
for i in m:
    print(i)
print()

o = range(0, 15, 3) # hitung nilainya mulai range nilai 0 - 15, tapi hanya kelipatan 3 saja
for i in o:
    print(i)
print()

index_count = 1         # mengetahui dimana posisi index sebuah huruf
for i in 'abcde':
    print(f'index {index_count} adalah huruf {i} ')
    index_count += 1
print()

index_count = 1         # cara 2 => mengetahui dimana posisi index sebuah huruf
for i in gabungankalimat:
    print(f'index {index_count} adalah huruf {i} ')
    index_count += 1

print()
index_count = 0         # cara 3 => mengetahui dimana posisi index sebuah huruf, initial value harus 0
for i in gabungankalimat:
    print(gabungankalimat[index_count])
    index_count += 1

print()
for item in enumerate(gabungankalimat): # cara 4 degan enumerate function menghasilkan tuple enpacking
    print(item)
print()

for index, huruf in enumerate(gabungankalimat): # dengan enumerate bisa mengambail key, value pair
    print(f'index {index} adalah huruf {huruf}')
print()

list1 = [1,2,3]
list2 = ['a', 'b', 'c']
list3 = [4,5,6]
for item in zip(list1, list2):      # zip function mengabungkan 2 list
    print(item)

for key, value, step in zip(list2, list1, list3):  # zip function dengan key value, menghasilkan key value
    print(key, value, step)
print()

print(min(angka1))      # checking nilai minimal
print(max(angka2))      # checking nilai maksimal
print('sebelum shuffle :', angka1)
shuffle(angka1)         # built in function cocok untuk mengacak suatu angka
print('setelah shufle: ', angka1)
print(randint(0, 100))  # built in function cocok untuk buat tebak angka

# ======================================================================================================================
mylist = [x for x in gabungankalimat]   # list comprehension atau loop
print(mylist)
range_list = [x for x in range(0, 10)]  # list comprehension
print(range_list)
range_list = [x**2 for x in range(0, 10)]   # list comprehension mencari nilai square root atau akar pangkat 2
print(range_list)
range_list = [x**3 for x in range(0, 10)]   # list comprehension mencari nilai kubik
print(range_list)
kelipatan_dua = [x for x in range(0, 10) if x % 2 == 0] # list comprehension mencari nilai kelipatan
print(kelipatan_dua)
celcius = [1, 2, 4, 8, 16, 32, 64 ]
print(celcius)
fahrenheit = [( (9/ 5) * temp + 32 ) for temp in celcius]
print(fahrenheit)
hasil = [ x if x % 2 == 0 else 'ganjil' for x in range(0, 10)] # list comprehension dengan if else statement
print(hasil)
print()
mylist = []       # nested loop, setiap nilai dari x kalikan dengan nilai list dari y dan masukkan di mylist variable
for x in [2, 3, 4]:
    for y in [1, 10, 100]:
        mylist.append(x * y)
print(mylist)
mylist = [ x * y for x in [2, 3, 4] for y in [1, 10, 100]]
print(mylist)       # nested loop dengan hasil yang sama dengan yang diatas
print()
#=======================================================================================================================
