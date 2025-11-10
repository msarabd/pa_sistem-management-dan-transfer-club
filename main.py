import os
from login import input_biasa, input_mod, input_register
from crud import tampil_starting, tampil_cadangan, tambah_pemain, ganti_pemain, hapus_pemain, tampilan_ubah_pemain
from prettytable import PrettyTable
import datetime as dt

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
        ["1.", "Pengguna Biasa"],
        ["2.", "Pengguna MOD"],
        ["3.", "Daftar Sebagai Pengguna Baru"]
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
        input_register()

    else:
        input("\n(Input tidak valid, ketuk enter untuk memilih kembali)")

if login_mod:
    while login_mod:
        os.system("cls")
        print("=== Selamat Datang Tuan Admin ===\n")
        tabel_menu_admin = PrettyTable()
        tabel_menu_admin.title = "Mau ngapain hari ini?"
        tabel_menu_admin.field_names = ["kiri", "kanan"]
        tabel_menu_admin.header = False
        tabel_menu_admin.add_rows([
            ["[1]", "Lihat Daftar Line Up"],
            ["[2]", "Tambah Pemain Cadangan"],
            ["[3]", "Ganti Starting Line Up"],
            ["[4]", "Ganti Pemain Cadangan"],
            ["[5]", "Hapus Pemain Cadangan"],
            ["[6]", "Keluar"]
            ])
        print(tabel_menu_admin)

        pilihan_2 = input("Pilih menu (1-6) = ").strip()
        
        if pilihan_2 == "1":
            data_waktu = dt.datetime.now()
            os.system("cls")
            print(f"Daftar Line Up Timnas Indonesia ({data_waktu.strftime("%A")}, {data_waktu.day} - {data_waktu.month} - {data_waktu.year})\n")
            tampil_starting()
            print()
            tampil_cadangan()
            input("\n(Ketuk enter untuk kembali memilih menu)")

        elif pilihan_2 == "2":
            tambah_pemain()

        elif pilihan_2 == "3":
            while True:
                os.system("cls")
                tampil_starting()
                pemain_tukar, ulang_2 = ganti_pemain("gk_utama", "df_utama", "mf_utama", "fw_utama")
                if ulang_2 == True:
                    break
            
            tampilan_ubah_pemain(pemain_tukar, "mengganti pemain starting dengan")
                
        elif pilihan_2 == "4":
            while True:
                os.system("cls")
                tampil_cadangan()
                pemain_tukar, ulang_2 = ganti_pemain("gk_cadangan", "df_cadangan", "mf_cadangan", "fw_cadangan")
                if ulang_2 == True:
                    break

            tampilan_ubah_pemain(pemain_tukar, "mengganti pemain cadangan dengan")
                
        elif pilihan_2 == "5":
            while True:
                panggil_pemain, ulang_2 = hapus_pemain()
                if ulang_2 == True:
                    break

            tampilan_ubah_pemain(panggil_pemain, "menghapus")
                
        elif pilihan_2 == "6":
            login_mod = False

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")

elif login_biasa:
    while login_biasa:
        os.system("cls")
        print(f"=== Selamat Datang Tuan Muda {user} ===\n")
        tabel_menu_user = PrettyTable()
        tabel_menu_user.title = "Mau ngapain hari ini?"
        tabel_menu_user.field_names = ["kiri", "kanan"]
        tabel_menu_user.header = False
        tabel_menu_user.add_rows([
            ["[1]", "Lihat Daftar Line Up"],
            ["[2]", "Keluar"]
            ])
        print(tabel_menu_user)

        pilihan_2 = input("Pilih menu (1-2) = ").strip()
        
        if pilihan_2 == "1":
            data_waktu = dt.datetime.now()
            os.system("cls")
            print(f"Daftar Line Up Timnas Indonesia ({data_waktu.strftime("%A")}, {data_waktu.day} - {data_waktu.month} - {data_waktu.year})\n")
            tampil_starting()
            print()
            tampil_cadangan()
            input("\n(Ketuk enter untuk kembali memilih menu)")
            
        elif pilihan_2 == "2":
            login_biasa = False

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")

os.system("cls")
print(f"✨ Terima kasih atas waktunya, {user}. Sampai jumpa di lain kesempatan! Selamat tinggal. 👋")