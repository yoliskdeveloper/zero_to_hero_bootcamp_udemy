#=======================================================================================================================
# I/O file
fn = 'test.txt'
with open(fn, mode='r') as f:
    print(f.readable())     # return boolean value, memastikan bahwa file dapat dibaca
    # print(f.read())       # baca content file keseluruhan dengan baris per baris, data type tetap string
    # print(f.readline())     # baca content file hanya per baris
    # print(f.readlines())    # baca file secara keseluruhan baris dan berubah data type menjadi list
    # print(f.seek(1))

with open(fn, mode="a") as f:
    print(f.writable())     # return boolean value, memastikan bahwa file dapat di edit
    # print(f.truncate())    # menghapus karakter dalam file, jika tidak ada parameter, maka method ini akan menghitung
    # berapa karakter yang ada di dalam sebuah text, jika ada parameter integer maka akan memotong sejumlah karakter
    # sesuai dengan parameter angka yang diberikan
    # print(f.write("\ngood luck Yosua for your dream"))  # menambahkan string.jika memakai print statement akan
    # memberitahu berapa karakter yang ditambahkan
    # print(f.write("""
    # semoga berhasil Yosua
    # Tuhan Yesus memyertai segala usahamu """))      # hampir sama dengan writeline
    # print(f.writelines("""
    # semoga berhasil Yosua
    # Tuhan Yesus memyertai segala usahamu"""))       # menambahkan karakter tiap baris

# with open("new_file_tanpa_membuat_file.txt", mode='w') as f:
#     print(f.writelines("""
#     Balonku ada 5
#     rupa-rupa warnanya
#     merah, kuning, kelabu,
#     merah muda dan biru
#      """))
# hati-hati menggunakan mode w dalam open file, pastikan nama file belum eksis, jika memang sudah ada filenya
# pastikan kontent di dalamnya
