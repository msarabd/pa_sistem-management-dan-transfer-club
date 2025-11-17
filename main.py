import os
from login import input_biasa, input_mod, input_register
from crud import menu_login_biasa, menu_login_mod
from prettytable import PrettyTable
from data import data_pengguna, data_borneo, clubs

login_mod = False
login_biasa = False

awal_1 = False
while not awal_1:
    os.system("cls")
    tabel_menu = PrettyTable()
    tabel_menu.title = "ANDA INGIN LOGIN SEBAGAI:"
    tabel_menu.field_names = ["kiri", "kanan"]
    tabel_menu.header = False
    tabel_menu.add_rows([
        ["[1]", "Pengguna Biasa"],
        ["[2]", "Pengguna MOD"],
        ["[3]", "Daftar Sebagai Pengguna Baru"]
        ])
    print(tabel_menu)

    pilihan_1 = input("Pilih menu (1-3) = ").strip()

    if pilihan_1 == "":
        input("\n(Masukkan karakter, ketuk enter untuk memilih kembali)")
        continue
    elif not pilihan_1.isdigit() or pilihan_1 == "0":
        input("\n(Masukkan angka sesuai pilihan, ketuk enter untuk memilih kembali)")
        continue
    
    elif pilihan_1 == "1":
        user, login_biasa, awal_1 = input_biasa()

    elif pilihan_1 == "2":
        user, login_mod, awal_1 = input_mod()

    elif pilihan_1 == "3":
        user, login_biasa, awal_1 = input_register()

    else:
        input("\n(Input tidak valid, ketuk enter untuk memilih kembali)")

if login_biasa: # test
    club_pengguna = data_pengguna["user_biasa"][user][1]
    data_club_pengguna = clubs[club_pengguna]
    menu_login_biasa(user, club_pengguna, data_club_pengguna)

elif login_mod:
    club_pengguna = data_pengguna["user_mod"][user][1]
    data_club_pengguna = data_borneo
    menu_login_mod(user, club_pengguna, data_club_pengguna)

os.system("cls")
print(f"✨ Terima kasih atas waktunya, {user}. Sampai jumpa di lain kesempatan! Selamat tinggal. 👋")