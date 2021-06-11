# try -> blok code yang dicoba, apakah dia menghasilkan error atau tidak
# except -> blok code yang akan ditampilkan, saat blok code try mempunyai error
# finally -> mau ada error atau tidak blok code ini akan tetap jalan
# else -> kebalikan dari except

# def ask_for_int():
#     while True:
#
#         try:
#             int(input('Beri saya sebuah angka: '))
#         except:
#             print('Anda tidak memasukkan sebuah angka')
#             continue
#         else:
#             print('Terima kasih telah menyediakan sebuah angka')
#             break
#         # finally:
#         #     # finally adalah optional, mau dipakai atau tidak terserah, karena sifatnya adalah ambigu,
#         #     # code block ini akan selalu tampil walaupun ada exception atau tidak, jadi rekomendasi adalah tidak usah
#         #     # ditampilkana, cukup dengan else saja
#         #     print('End of program')

# ask_for_int()
# try:
#     for i in ['a', 'b', 'c']:
#         print(i**2)
# except TypeError:
#     print('string tidak bisa diakar kuadrat kan bambang')

# x = 5
# y = 0
# try:
#     z = x / y
#     print(z)
# except ZeroDivisionError:
#     print('Nol tidak bisa dibagi')
# else:
#     print('yeei')
# finally:
#     print('all done')

# ask integer

def ask():
    while True:
        try:
            akar_pangkat = int(input('Masukkan bilangan integer (0-9): '))
            result = akar_pangkat ** 2
        except ValueError:
            print('Ada Error, coba lagi! \n')
            continue
        else:
            print('Terima kasih, bilangan anda jika diakar-pangkat 2 adalah {}'.format(result))
            break

ask()
