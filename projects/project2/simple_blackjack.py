import random
bentuk_kartu = ('Hati', 'Wajik', 'Waru', 'Keriting')
no_kartu = ('Dua', 'Tiga', 'Empat', 'Lima', 'Enam', 'Tujuh', 'Delapan', 'Sembilan', 'Sepuluh', 'Jack', 'Ratu', 'Raja',
         'As')
nilai_kartu = {'Dua' :  2, 'Tiga':3, 'Empat': 4, 'Lima': 5, 'Enam': 6, 'Tujuh': 7, 'Delapan': 8, 'Sembilan': 9,
                'Sepuluh': 10, 'Jack': 10, 'Ratu': 10, 'Raja': 10, 'As': 11 }
playing = True

class Card:
    def __init__(self, bentuk_kartu, no_kartu):
        self.bentuk_kartu = bentuk_kartu
        self.no_kartu = no_kartu

    def __str__(self):
        return self.no_kartu + ' ' + self.bentuk_kartu

class Deck:
    def __init__(self):
        self.tumpuk_kartu = []

        # looping no dan bentuk kartu untuk dimasukkan ke dalam tumpukan kartu
        for bentuk in bentuk_kartu:
            for no in no_kartu:
                # buat card object
                buat_kartu = Card(bentuk, no)

                self.tumpuk_kartu.append(buat_kartu)

    def __str__(self):
        deck_comp = ''
        for kartu in self.tumpuk_kartu:
            deck_comp += '\n' + kartu.__str__()
        return 'Deck Mempunyai: ' + deck_comp


    def kocok_kartu(self):
        random.shuffle(self.tumpuk_kartu)

    def deal(self):
        satu_kartu = self.tumpuk_kartu.pop()
        return satu_kartu

class Hand:
    def __init__(self):
        self.kartu_ditangan = []    # empty list untuk menampung kartu dari Deck class
        self.nilai_kartu_awal = 0   # start dengan value kosong
        self.aces = 0               # attibute untuk tracing akan kartu "AS"

    def tambah_kartu(self, kartu):
        self.kartu_ditangan.append(kartu)
        self.nilai_kartu_awal += nilai_kartu[kartu.no_kartu]

        # As track
        if kartu.no_kartu == 'As':
            self.aces += 1

    def adjust_for_ace(self):
        while self.nilai_kartu_awal > 21 and self.aces > 0:
            self.nilai_kartu_awal -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total=100):
        self.total = total    # value ini bisa diadjust sesuai dengan keinginan atau bisa dengan user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Berapa banyak chip yang anda taruhkan? '))
        except:
            print('Maaf tolong masukkan sebuah angka, bukan huruf atau special karakter')
        else:
            if chips.bet > chips.total:
                print(f'Maaf, anda tidak mempunyai chip yang cukup. Anda hanya mempunya {chips.total}')
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.tambah_kartu(single_card)
    hand.adjust_for_ace()

def hit_atau_stand(deck, hand):
    global playing

    while True:
        x = input('Hit atau Stand? Enter "h" atau "s" ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player Stand, Bandar Jalan')
            playing = False
        else:
            print('Maaf saya tidak mengerti apa yang anda masukkan, Mohon masukan "h" atau "s" saja! ')
            continue
        break

def show_some(player, dealer):
    print('\nDEALER HAND')
    print('satu kartu tertutup')
    print(dealer.kartu_ditangan[1])
    print('\n')
    print('PLAYER HAND')
    for kartu in player.kartu_ditangan:
        print(kartu)

def show_all(player, dealer):
    print('\nDEALER HAND')
    for kartu in dealer.kartu_ditangan:
        print(kartu)
    print('\n')
    print('PLAYER HAND')
    for kartu in player.kartu_ditangan:
        print(kartu)

def player_busts(player, dealer, chips):
    print('BUST PLAYER!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('PLAYER WINS! DEALER BUSTED')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('DEALER WINS!')
    chips.lose_bet()

def push(player, dealer):
    print('Bandar dan Player seimbang! PUSH!!')

# Game logic
while True:
    # print opening statement
    print('\nSELAMAT DATANG DI PERMAINAN SIMPLE BLACKJACK Ver. 1.0')

    # buat kartu object yang sudah dikocok , dua kartu untuk dealer dan player
    deck = Deck()
    deck.kocok_kartu()

    player_hand = Hand()
    player_hand.tambah_kartu(deck.deal())
    player_hand.tambah_kartu(deck.deal())

    dealer_hand = Hand()
    dealer_hand.tambah_kartu(deck.deal())
    dealer_hand.tambah_kartu(deck.deal())

    # setup player chips
    player_chips = Chips()

    # tampilkan chip untuk taruhan player
    take_bet(player_chips)

    # tunjukkan semua tetapi tutup satu kartu dealer
    show_some(player_hand, dealer_hand)

    while playing:
        # tampilkan apakah player ingin hit atau stand
        hit_atau_stand(deck, player_hand)

        # tampilkan kartu tetapi tutup satu kartu dari dealer
        show_some(player_hand, dealer_hand)

        # jika player hand mencapai nilai dari 21, run player_bust() dan keluar dari while loop
        if player_hand.nilai_kartu_awal > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # jika player belum busted , play Dealer_hand sampai Dealer mencapai nilai 17
    if player_hand.nilai_kartu_awal <= 21:

        while dealer_hand.nilai_kartu_awal < player_hand.nilai_kartu_awal:
            hit(deck, dealer_hand)

        # tampilkan semua kartu
        show_all(player_hand, dealer_hand)

        # jalankan skenario kemenangan lainnya
        if dealer_hand.nilai_kartu_awal > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.nilai_kartu_awal > player_hand.nilai_kartu_awal:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.nilai_kartu_awal < player_hand.nilai_kartu_awal:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # infokan player tentang total chips mereka
    print(f'\n Total Player Chips: {player_chips.total}')

    # tanya apakah mau main lagi
    new_game = input('Apakah anda mau bermain lagi? y/n ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Terima kasih telah bermain SIMPLE BLACKJACK Ver. 1.0')
        break
