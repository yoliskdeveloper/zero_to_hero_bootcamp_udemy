class Anjing():

    # class object attribute -> adalah attribute yang paling khas yang pasti selalu ada dalam setiap object
    species = 'mamal'

    # attribute
    def __init__(self, jenis, nama,):
        self.jenis = jenis
        self.nama = nama

    def gonggong(self, number):
        """
         method adalah function dalam class
         self dipakai untuk terkoneksi ke attribute lain
         sedangkan parameter lain harus dipanggil langsung dalam instance
         """
        print(f'Guk-guk {self.nama} sedang menggongong {number} kali')

anjingku = Anjing('Herder', 'Sammy',)   # buat instance dan taruh di sebuah variable
print('anjingku berjenis:',anjingku.jenis.upper())
print('anjingku bernama',anjingku.nama)
print(anjingku.gonggong(3))

class Lingkaran():

    # class object atribute
    pi = 3.14

    # attribute
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Lingkaran.pi

    def keliling(self):
        return Lingkaran.pi * self.radius * 2

lingkaran = Lingkaran(10)
print('bilangan pi untuk lingkaran adalah',lingkaran.pi)
print(f'Diketahui radius lingkaran adalah {lingkaran.radius}')
print('berarti keliling lingkaran adalah: {l:1.2f}'.format(l=lingkaran.keliling())) # format dengan floating point
print(f'dan area lingkarannya adalah {lingkaran.area}')
print()

class Rakyat():

    def __init__(self):
        print('Rakyat Dibuat!')

    def siapa_saya(self):
        print('Saya adalah Rakyat')

    def maju(self):
        print('Saya akan maju perang!')

rakyat = Rakyat()
rakyat.siapa_saya()
rakyat.maju()
print()

# inheritance / mewariskan atribut dari base class
class Tentara(Rakyat):

    def __init__(self):
        Rakyat.__init__(self)
        print('Tentara Dibuat')

    def siapa_saya(self):
        print('saya adalah tentara')

tentara = Tentara()
tentara.siapa_saya()
tentara.maju()
print()

# POLYMORPHISM
class Anjing():

    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        return self.nama + ' mengeluarkan bunyi guk-guk!'

class Kucing():

    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        return self.nama + ' mengeluarkan bunyi meong!'

anjing = Anjing('Heli')
kucing = Kucing('Manis')
print('nama anjingku',anjing.nama)
print('nama kucingku',kucing.nama)
print(anjing.bicara())  # akses class method anjing
print(kucing.bicara())  # akses class method kucing
print()

# cara akses class anjing dan kucing melalui for in loop
for pet in [anjing, kucing]:
    print(type(pet))
    print(pet.bicara())
print()

# atau dengan cara define function dan memberi parameter
def pet_bicara(pet):
    print(pet.bicara())

pet_bicara(anjing)  # dan function call melalui variable instance
pet_bicara(kucing)

# POLYMOPHISM II
class Hewan():

    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        raise NotImplementedError('Abstract Method akan diimplementasi melalui Subclass method')

class Anjing(Hewan):
    def bicara(self):
        return self.nama + ' guk-guk!'

class Kucing(Hewan):
    def bicara(self):
        return self.nama + ' miao!'

fido = Anjing('fido')
lusi = Kucing('lusi')
jon = Hewan('jon')
print(fido.bicara())
# print(jon.bicara())  # raise error karena method bicara akan dipanggil melalui class yang lain


# SPECIAL METHOD IN CLASS (DUNDER -> Double Underscore)
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Buku "{self.title}" adalah karangan dari {self.author}, dengan jumlah pages adalah {self.pages} ' \
               f'halaman'

    def __len__(self):
        return self.pages

    # def __del__(self):
    #     print('Object buku telah dihapus!')

b = Book('Python Pemula', 'Jon Travolta', 234)
print(b)
print(len(b))
print()



# find distance and slope dalam line graph
class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2 - y1) / (x2 - x1)

c1 = (3, 2)
c2 = (8, 10)
lineku = Line(c1, c2)
print(f'{lineku.distance()}, round-up to: {lineku.distance():1.2f}')
print(lineku.slope())
print()

# hitung cylinder
class Cylinder():

    pi = 3.14
    def __init__(self, tinggi=1, radius=1):
        self.tinggi = tinggi
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.tinggi

    def luas_area(self):
        return (2 * Cylinder.pi * (self.radius ** 2)) + (2 * Cylinder.pi * self.radius * self.tinggi)

cylinder = Cylinder(2, 3)
print(f'sebuah cylinder mempunyai tinggi: {cylinder.tinggi} m')
print(f'dan mempunyai radius: {cylinder.radius} m' )
print(f'maka akan mempunyai volume sebesar: {cylinder.volume()} m3 dibulatkan menjadi {cylinder.volume():1.2f} m3')
print(f'dan memppunyai luas area sebesar: {cylinder.luas_area()} m2 ')
print()

# OOP challenge ========================================================================================================
# ==== kode yang kutulis tanpa melihat solusi dari tutorial, hanya melihat hint saja ===================================
class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Pemilik Rekening: {self.owner} \nAccount Balance: Rp.{self.balance}'

    def deposit(self, credit=0):
        bunga = self.balance + credit * 0.02
        self.balance = self.balance + credit + bunga
        return f'Penerimaan Dana: Rp.{credit}'


    def withdraw(self, withdraw_money):
        biaya_admin = self.balance + withdraw_money * 0.01
        self.balance = self.balance - withdraw_money + biaya_admin

        if self.balance < 100:
            return  f"Maaf penarikan tidak tersedia, Dana anda tersisa: {self.balance}"
        else:
            return f'Pengambilan Dana: Rp.{withdraw_money}'

# ======================================================================================================================

acc = Account('Yosua', 500)
print(acc.owner)
print(acc.balance)
print(acc)
print(acc.deposit(100))
print(acc)
print(acc.withdraw(600))
print(acc)

