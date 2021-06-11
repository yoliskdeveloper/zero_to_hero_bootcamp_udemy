# CARD DECK
import random
bentuk_kartu = ('Hati', 'Wajik', 'Waru', 'Keriting')
no_kartu = ('Dua', 'Tiga', 'Empat', 'Lima', 'Enam', 'Tujuh', 'Delapan', 'Sembilan', 'Sepuluh', 'Jack', 'Ratu', 'Raja',
         'As')
nilai_kartu = {'Dua' :  2, 'Tiga':3, 'Empat': 4, 'Lima': 5, 'Enam': 6, 'Tujuh': 7, 'Delapan': 8, 'Sembilan': 9,
                'Sepuluh': 10, 'Jack': 11, 'Ratu': 12, 'Raja': 13, 'As': 14 }

class Card:
    def __init__(self, bentuk_kartu, no_kartu):
        self.bentuk_kartu = bentuk_kartu
        self.no_kartu = no_kartu
        self.nilai_kartu = nilai_kartu[no_kartu]

    def __str__(self):
        return self.no_kartu + ' ' + self.bentuk_kartu

class Deck:
    def __init__(self):
        self.semua_kartu = []

        # looping melalui kartu untuk mengambil nilai dan bentuknya
        for bentuk in bentuk_kartu:
            for no in no_kartu:
                # buat card object
                buat_kartu = Card(bentuk, no)

                self.semua_kartu.append(buat_kartu)

    def kocok_kartu(self):
        random.shuffle(self.semua_kartu)

    def ambil_satu_kartu(self):
        # ambil kartu dari deck, karena cuma satu kartu maka pakai method pop() g masalah
        return self.semua_kartu.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.kartu_ditangan = []

    def kurangi_satu_kartu(self):
        return self.kartu_ditangan.pop(0)

    def tambah_kartu(self, kartu_baru):
        if type(kartu_baru) == type([]):
            self.kartu_ditangan.extend(kartu_baru)
        else:
            self.kartu_ditangan.append(kartu_baru)

    def __str__(self):
        # hitung berapa banyak kartu yang masih tersisa di tangan player
        return f'Player {self.name} mempunyai {len(self.kartu_ditangan)} kartu'

# gmae setup
#   player
player_one = Player('Jaka')
player_two = Player('Jupri')
#   deck
deck_baru = Deck()
deck_baru.kocok_kartu()

#   pembagian kartu diantara 2 pemain
for x in range(26):
    player_one.tambah_kartu(deck_baru.ambil_satu_kartu())
    player_two.tambah_kartu(deck_baru.ambil_satu_kartu())

game_one = True
ronde = 0

while game_one:
    ronde += 1
    print(f'Ronde: {ronde}')

    if len(player_one.kartu_ditangan) == 0:
        print(f'{player_one.name} telah kehabisan kartu: {player_two.name} Pemenangnnya')
        game_one = False
        break

    if len(player_two.kartu_ditangan) == 0:
        print(f'{player_two.name} telah kehabisan kartu: {player_one.name} Pemenangnnya')
        game_one = False
        break

    # memulai ronde yang baru
    player_one_cards = []
    player_one_cards.append(player_one.kurangi_satu_kartu())

    player_two_cards = []
    player_two_cards.append(player_two.kurangi_satu_kartu())

    # saat tanding kartu
    at_war = True
    while at_war:
        if player_one_cards[-1].nilai_kartu > player_two_cards[-1].nilai_kartu:
            player_one.tambah_kartu(player_one_cards)
            player_one.tambah_kartu(player_two_cards)
            at_war = False

        if player_one_cards[-1].nilai_kartu < player_two_cards[-1].nilai_kartu:
            player_two.tambah_kartu(player_one_cards)
            player_two.tambah_kartu(player_two_cards)
            at_war = False

        else:
            print('WAR')
            pasukan_kartu = 3       # kartu untuk ditaruhkan, value dapat berubah
            if len(player_one.kartu_ditangan) < pasukan_kartu:
                print(f'{player_one.name} tidak dapat menyatakan perang, karena kartu tidak cukup')
                print(f'{player_two.name} adalah Pemenangnya')
                game_one = False
                break

            elif len(player_two.kartu_ditangan) < pasukan_kartu:
                print(f'{player_two.name} tidak dapat menyatakan perang, karena kartu tidak cukup')
                print(f'{player_one.name} adalah Pemenangnya')
                game_one = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.kurangi_satu_kartu())
                    player_two_cards.append(player_two.kurangi_satu_kartu())



# print(len(player_one.kartu_ditangan))
# print(len(player_two.kartu_ditangan))
