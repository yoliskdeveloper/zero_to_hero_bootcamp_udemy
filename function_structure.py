import string

def name_function():        # define function
    print('hello')

name_function()             # call function

def tanya_nama(nama):       # define function dengan 1 parameter
    print('halo', nama)

tanya_nama('Yosua')         # call function

def tanya_nama(nama='user'):    # function dengan default value
    print('halo', nama, 'selamat datang kembali')

tanya_nama()                # call function, walaupun tidak ada parameter, function ini tidak akan menghasilkan error
# karena kita memberikan default parameter untuk ini
tanya_nama('yosua')

def tanya_nama_2(nama):
    return "halo " + nama + " senang berjumpa denganmu"
# jika memakai return statment di function harus diketahui bahwa hasil dari return statment akan dipass kan ke
# variable yang menampung function tersebut

hasil = tanya_nama_2('sally')
print(hasil)

def tanya_nama_2(nama='USER'):      # define function dengan default value
    return 'hallo ' + nama + ' welcome back, ready to rumble?'
hasil = tanya_nama_2()          # panggil tanpa parameter tidak akan terjadi ValueError
print(hasil)

# def tambah(n1, n2):
#     return n1 + n2
#
# nilai1 = int(input('beri angka pertama >> '))
# nilai2 = int(input('beri angka kedua >> '))
#
# hasil_tambah = tambah(nilai1, nilai2)
# print(hasil_tambah)

def check_kata(kata):
    huruf_pertama = kata[0]

    # check kata
    if huruf_pertama in 'aiueo':
        kata_receh = kata + ': yeiii... berhasil, huruf vokal di index pertama'
    else:
        #jika bukan huruf vokal, maka ambil katanya dari huruf kedua sampai akhir + huruf pertama di belakang dan
        # tambahkan kalimat bukan vokal
        kata_receh = kata[1:] + huruf_pertama + ': kata pertama bukan vokal'
    return kata_receh
hasil = check_kata('saus')
print(hasil)

def func_sum(*args):    # *args => semua argument dapat ditampung dalam parameter sebanyak yang kita mau
    return sum(args) * 0.05

hasil_bunga = func_sum(35,678, 2345, 345)
print(hasil_bunga)

def func_dict(**kwargs):
    if 'buah' in kwargs:
        print('Buah pilihanku adalah {}'.format(kwargs['buah']))
    else:
        print('saya tidak temukan buah disini')
    print(kwargs)
hasil_buah = func_dict(buah='apple', sayur='buncis', bumbu='jahe')
print(hasil_buah)

def bil_genap_ganjil(a, b):
    # hasil = [x if x % 2 == 0 else 'ganjil' for x in range(args)]
    if a % 2 == 0 and b % 2 == 0:
        # kedua angka adalah genap
        result = min(a, b)
    else:
        # satu atau kedua angka adalah bilangan genap
        result = max(a, b)
    return result

check = bil_genap_ganjil(98,76)
print(check)

def kata_pertama_sama(text):        # cek apakah kalimat mempunyai huruf pertama yang sama?
    kalimat = text.upper().split()
    kata1 = kalimat[0]
    kata2 = kalimat[1]
    return kata1[0] == kata2[0]
check_kata = kata_pertama_sama('Beruang Madu')
print(check_kata)

def buat_angka_20(n1, n2):
    # if n1 + n2 == 20:
    #     return True
    # elif n1 == 20:
    #     return True
    # elif n2 == 20:
    #     return True
    # else:
    #     return False

    # sederhanakan / factorisasi
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20
check20 = buat_angka_20(0, 20)
print(check20)

def huruf_capital(text):
    # cara 1 -> pakai upper()
    # huruf_pertama = text[0]
    # antara_pertama_keempat = text[1:3]
    # huruf_keempat = text[3]
    # sisa_kata = text[4:]
    #
    # return huruf_pertama.upper() + antara_pertama_keempat + huruf_keempat.upper() + sisa_kata

    # cara 2 -> pakai capitalize
    bagian_pertama = text[:3]
    bagian_kedua = text[3:]
    return bagian_pertama.capitalize() + bagian_kedua.capitalize()

kapital = huruf_capital('macdonald')
print(kapital)

def balik_kata(text):
    pisahin = text.split()
    reverse_word = pisahin[::-1]
    joint_word = ' '.join(reverse_word)
    return joint_word
    # return text[::-1]
kata_balik = balik_kata('saya pulang rumah')
print(kata_balik)
# b = balik_kata(input('masukkan kata: (saya akan putar ulang) '))
# print(b)

def angka_hampir(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
print(angka_hampir(200))

def has_33(nums):
    # untuk setiap item dalam range antara 0 sampai setiap jumlah karakter sampai habis
    for i in range(0, len(nums)-1):
        # jika ada di dalam item sama dengan 3 dan item iterasi berikutnya sama dengan 3 juga
        if nums[i] == 3 and nums[i + 1] == 3:
            # maka tampilkan True
            return True
        # jika tidak ada tampilkan False
    return False
list33 = has_33([1,2,3,3,3])
print(list33)
# print(has_33([1,3,1]))

def kali_3_karakter(text):
    hasil = ''
    for i in text:
        hasil += i * 3
    return hasil
g = kali_3_karakter('nabila')
print(g)


def black_jack(a, b, c):
    # jika total nilai summary kurang dari 21
    if sum([a, b, c]) <= 21:
        # maka kembalikan nilai sum tersebut
        return sum([a, b, c])
    # dan jika ada nilai 11 di dalam list abc dan summmary dari abc kurang dari nilai 31
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        # maka kembalikan nilai sum yang sudah dikurangi dengan 10 point
        return sum([a,b,c]) - 10
    # lainnya
    else:
        # print bust
        return 'BUST'

bj = black_jack(7,3,1)
print('kartu anda =',bj)


def summer_69(arr):
    total = 0       # initial value
    add = True      # proses tambah selalu benar

    # untuk setiap num dalam arr
    for num in arr:
        # selama aku masih menambahkan
        while add:
            # jika number tidak sama dengan 6
            if num != 6:
                # maka tambahkan nilai total dari setiap angka di dalam item array
                total += num
                break
            else:
                # lainnya jangan tambahkan
                add = False

        # selamat saya tidak menambahkan
        while not add:
            # jika numb tidak sama dengan 9
            if num != 9:
                # maka break
                break
            else:
                # dan proses tambah selalu ada
                add = True
                break
    return total

s69 = summer_69([1, 9,  4, 3])
print(s69)

def find_james_bond(arr):
    code = [0,0,7, 'x']

    for num in arr:
        # jika number itu sama dengan index pertama dari variable code
        if num == code[0]:
            # maka remove index pertama dari code
            code.pop(0)
    # jika sudah selesai dan sisa nilai code itu sama dengan 1 maka berhenti
    return len(code) == 1
c = find_james_bond([1,2,4,0,0,7,5])
print(c)

# ====================================== bilangan prime code ===========================================================
def count_primes(num):
    # jika num kurang dari 2
    if num < 2:
        # maka kembalikan nilai 0
        return 0
    # kasih variable key
    primes = [2]
    x = 3
    # selama x kurang dari dan sama dengan nilai num
    while x <= num:
        # untuk setiap item di range yang mulai dari 3, sampai nilai x dengan kelipatan 2
        for y in primes:
            # jika x dibagi nilai item y itu sama dengan 0
            if x % y == 0:
                # maka nilai x ditambah dengan 2 setiap saat
                x += 2
                break

        else:
            # kalo tidak tambahkna nilai x di dalam list primes dan tambahkan nilai x kelipatan 2
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

p = count_primes(100)
print(p)
# ======================================================================================================================
def square(nums):
    return nums ** 2
var_num = [1,2,3,4,5]

for i in var_num:       # cara 1
    s = square(i)
    print(s)

for i in map(square, var_num ): # cara 2 lebih simple
    print(i)

sq = list(map(square, var_num)) # cara 3
print(sq)

def splicer(mystring):
    # jika jumlah karakter yang ada di mystring itu dibagi 2 = 0
    if len(mystring) % 2 == 0:
        # maka tampilkan even
        return 'Even'
    else:
        # jika tidak tampilkan hanya karakter pertama dari mystring
        return mystring[0]
names = ['andi', 'budi', 'charlie', 'doni']
sp = list(map(splicer, names))
print(sp)

def check_genap(num):
    return num % 2 == 0
n = [1,2,3,4,5,6]
gnp = list(filter(check_genap, n))
print(gnp)

square = lambda num : num ** 2      # lambda taruh di variable, lambda atau anonymous function
print(square(3))

s = list(map(lambda num:num ** 2, n ))
print(s)
f = list(filter(lambda num:num % 2 == 0, n ))
print(f)

# menghitung volume lingkaran, jika diberikan nilai radiusnya
def vol_sphere(rad):
    return (4.0 / 3) * (3.14) * (rad**3)

vol_lingkaran = vol_sphere(20)
print(vol_lingkaran)

# cek apakah num ada dalam range low dan high
def range_check(num, low, high):
    # check jika number ada diantara range low dan high
    if num in range(low, high):
        print(num, "ada dalam range")
    else:
        print(num," ada diluar range")

ran_chk = range_check(1, 2, 7)
print(ran_chk)

# menghitung berapa huruf yang mempunyai huruf besar dan huruf kecil
def up_low(s):
    # initial dict untuk tampung nilai upper dan lower
    d={"upper": 0, "lower": 0}
    # cek setiap item di s
    for c in s:
        # jika di item tersebut adalah huruf uppercase
        if c.isupper():
            # maka tambahkan 1 nilai di key upper
            d["upper"] += 1
        # jika di item tersebut adalah huruf lowercase
        elif c.islower():
            # maka tambahkan 1 nilai di key lower
            d["lower"] += 1
        else:
            pass
    print("Original string :", s)
    print("Jumlah kata yang mempunyai uppercase adalah: ", d["upper"])
    print("Jumlah kata yang mempunyai lowercase adalah: ",d["lower"])

s = 'Halo Yosua, semangat ya belajar Python!!!. kalo terus-menerus 1 bulan lagi pasti Expert'
up_low(s)

# mengecek apakah ada karakter yang sama di dalam list, jika ada tampilkan hanya satu saja
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

ul = unique_list([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,5])
uw = unique_list(["a","a","a","a","a","a",'b','b','b','b','b','c','c','c','c','c',])
print(ul)
print(uw)

def multiply(numbers):      # perlu cek lagi
    total = numbers[0]
    for x in numbers:
        total *= x
    return total
listkali = [2,3,4,-2]
print(multiply(listkali))

# string palindrom
def palindrom(s):
    return s == s[::-1] # return boolean, dengan membandingkan string awal dengan dirinya sendiri secara reverse
print(palindrom('ovo'))

# pangram check, mengecek apakah di dalam sebuah kalimat, huruf alphabet a-z ada semua disitu?
def ispangram(str1, alphabet=string.ascii_lowercase):
    # taruh alphabet parameter di sebuah variabel agar bisa kita bandingkan nantinya dengan string yang kita tulis
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower()) # return boolean
ispangram("The quick brown fox jumps over the lazy dog")
print(string.ascii_lowercase)

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


def f(a, L=None): # print akan memprint satu-satu function call tidak akan berpengaruh kepada panggilan value berikutnya
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# pemanggilan range dengan cara berbeda tapi menghasilkan output yang sama
l = list(range(3, 6))   # cara 1 -> normal call dengan separator argument
print(l)
args = [3, 6]
l = list(range(*args))  # cara 2 -> argument call dengan cara unpacked / dikeluarkan dalam list
print(l)
