from __future__ import print_function
import math, sys
from decimal import *
getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

python2 = sys.version_info[0] == 2
if python2:
    input = raw_input

def factorial(n):
    """
    tampilkan nilai factorial mengunakan rekursive
    """
    if not n:
        return 1
    return n * factorial(n-1)

def nilaiIterasi(k):
    """
    tampilkan iterasi yang diberikan dalam Chudnovsky algorithma
    """
    k = k + 1
    getcontext().prec = k
    sum = 0
    for k in range(k):
        first = factorial(6 * k) * (13591409 + 545140134 * k)
        down = factorial(3 * k) * (factorial(k)) ** 3 * (640320 ** (3 * k))
        sum += first/down
    return Decimal(sum)

def nilaiDariPi(k):
    """
    tampilkan nilai yang sudah dikalkulasi dari Pi menggunakan nilai iterasi dari loop
    dan beberapa proses bagi yang diberikan dalam Chudnovsky Algorithma
    """
    iter = nilaiIterasi(k)
    up = 426880*math.sqrt(10005)
    pi = Decimal(up)/iter
    return pi

def shell():
    """
    Console function untuk membuat interactive shell
    """
    print('Selamat Datang di Pi Calculator,')
    print('masukkan jumlah digit Pi (setelah decimal) yang ingin dikalkulasi, di shell dibawah ini ')
    print('masukkan "k" untuk keluar dari program')
    print('NOTE: digit limit: 100000 digit,')
    print('jika lebih dari digit limit, komputer anda akan menjadi berat')

    while True:
        print('>>>', end=' ')
        entry = input()
        if entry == 'k'.lower():
            break
        if not entry.isdigit():
            print('Anda tidak memasukkan sebuah angka, coba lagi!')
        else:
            print(nilaiDariPi(int(entry)))

if __name__ == '__main__':
    shell()
        



