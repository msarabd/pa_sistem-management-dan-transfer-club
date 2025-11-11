import os
from login import input_biasa, input_mod, input_register
from crud import tampil_starting, tampil_cadangan, tambah_pemain, ganti_pemain, hapus_pemain, tampilan_ubah_pemain
from prettytable import PrettyTable
import datetime as dt
from data import data_club_pengguna, data_pengguna, data_barcelona

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
        user, login_biasa, awal_1 = input_register()

    else:
        input("\n(Input tidak valid, ketuk enter untuk memilih kembali)")

if login_biasa:
    if data_pengguna["user_biasa"][user][1] == "barcelona":
        club = "Barcelona"
        data_club_pengguna = data_barcelona.copy()
    # if data_pengguna["user_biasa"][user][1] == "madrid":
    #     data_club_pengguna = data_madrid.copy()
    # if data_pengguna["user_biasa"][user][1] == "arsenal":
    #     data_club_pengguna = data_arsenal.copy()
    # if data_pengguna["user_biasa"][user][1] == "psg":
    #     data_club_pengguna = data_psg.copy()
    # if data_pengguna["user_biasa"][user][1] == "dormund":
    #     data_club_pengguna = data_dormund.copy()

        while login_biasa:
            os.system("cls")
            print(f"=== Selamat Datang Tuan {user} ===\n")
            tabel_menu_admin = PrettyTable()
            tabel_menu_admin.title = "Mau ngapain hari ini?"
            tabel_menu_admin.field_names = ["kiri", "kanan"]
            tabel_menu_admin.header = False
            tabel_menu_admin.add_rows([
                ["[1]", "Lihat Formasi"],
                ["[2]", "Edit Squad"],
                ["[3]", "keuangan club"],
                ["[4]", "Transfer Pemain"],
                ["[5]", "Jendela Transfer"],
                ["[6]", "Keluar"]
                ])
            print(tabel_menu_admin)

            pilihan_2 = input("Pilih menu (1-6) = ").strip()
            
            if pilihan_2 == "1":
                data_waktu = dt.datetime.now()
                os.system("cls")
                print(f"Daftar Line Up {club} ({data_waktu.strftime("%A")}, {data_waktu.day} - {data_waktu.month} - {data_waktu.year})\n")
                
                tampil_starting(data_barcelona)
                print()
                tampil_cadangan(data_barcelona)
                input("\n(Ketuk enter untuk kembali memilih menu)")

            elif pilihan_2 == "2":
                ulang_2 = False
                while not ulang_2:
                    os.system("cls")
                    def ganti_pemain(data_club):
                        global ulang_2

                        print("Lini tersedia: gk (kiper), df (bek), mf (gelandang), fw (penyerang)")
                        lini = input("Masukkan lini yang ingin ditukar: ").strip().lower()

                        try:
                            if lini not in data_club:
                                raise ValueError(f"Lini '{lini}' tidak tersedia.")
                                
                            daftar = data_club[lini]

                            print(f"\nDaftar pemain di lini {lini}:")
                            for i, p in enumerate(daftar):
                                print(f"{i+1}. {p[0]} (Rating: {p[1]})")

                            idx_a = int(input("\nMasukkan nomor pemain pertama: ")) - 1
                            idx_b = int(input("Masukkan nomor pemain kedua: ")) - 1

                            if idx_a == idx_b:
                                raise ValueError("Nomor pemain tidak boleh sama.")
                            
                            # Tukar posisi
                            daftar[idx_a], daftar[idx_b] = daftar[idx_b], daftar[idx_a]

                            print(f"\n✅ Posisi berhasil ditukar: {daftar[idx_b][0]} ⇄ {daftar[idx_a][0]} di lini {lini}.")
                            ulang_2 = True

                        except Exception as e:
                            print()
                            input(e)
                            
                    ganti_pemain(data_barcelona)
                    # tambah_pemain()

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
                login_biasa = False

            else:
                input("\n(Input tidak valid, ketuk enter untuk kembali)")

elif login_mod:
    while login_mod:
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
            login_mod = False

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")

os.system("cls")
print(f"✨ Terima kasih atas waktunya, {user}. Sampai jumpa di lain kesempatan! Selamat tinggal. 👋")