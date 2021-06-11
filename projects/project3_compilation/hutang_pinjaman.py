"""
kalkulasi pembayaran bulanan dari nilai tetap dari cicilan rumah
berdasarkan bunga yang diberikan, dan butuh berapa lama cicilan rumah itu selesai
"""

print('CALCULATOR CICILAN RUMAH')
print('Masukkan jangka waktu cicilan rumah (dalam bulan, jika 3 tahun = 36 bulan)')
bulan = int(input(">>> "))
print('Masukkan bunga cicilan perbulan (nilai desimal bukan persentase)')
rate = float(input(">>> "))
print('Masukkan nilai cicilan per bulan')
pinjaman = float(input(">>> "))

# calculasi
rate_per_bulan = pinjaman / 100 / 12
pembayaran = round((rate_per_bulan / (1 - (1 + rate_per_bulan) ** (-bulan))) * pinjaman)

print(f'pembayaran bulanan: {pinjaman:1.0f} /bulan')
print(f'selama: {bulan / 12:1.0f} tahun')
print(f'dengan bunga pinjaman {rate:1.0f} %')
print(f'maka nilai rumahnya adalah: {pembayaran:1.0f}')



