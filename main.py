import os
from login import input_biasa, input_mod, input_register
from crud import tampil_starting, tampil_cadangan, ganti_pemain, ganti_pemain, hapus_pemain, tampilan_ubah_pemain
from prettytable import PrettyTable
import datetime as dt
from data import data_club_pengguna, data_pengguna, data_barcelona, data_madrid, data_arsenal, data_psg, data_dortmund, data_gratisan, data_pemuda, data_transfer, clubs
import random

login_mod = False
login_biasa = False

def tampil_squad(data_club):
    data_squad = []
    for i in range(len(data_club["gk"])):
        nomor = i + 1
        data_squad.append([f"{nomor}.", data_club["gk"][i][0], "GK", data_club["gk"][i][1], data_club["gk"][i][2], f"€{data_club["gk"][i][3]:,}", data_club["gk"][i][4], data_club["gk"][i][5]])
    for i in range(len(data_club["df"])):
        nomor = i + 1 + len(data_club["gk"])
        data_squad.append([f"{nomor}.", data_club["df"][i][0], "DF", data_club["df"][i][1], data_club["df"][i][2], f"€{data_club["df"][i][3]:,}", data_club["df"][i][4], data_club["df"][i][5]])
    for i in range(len(data_club["mf"])):
        nomor = i + 1 + len(data_club["gk"] + data_club["df"])
        data_squad.append([f"{nomor}.", data_club["mf"][i][0], "MF", data_club["mf"][i][1], data_club["mf"][i][2], f"€{data_club["mf"][i][3]:,}", data_club["mf"][i][4], data_club["mf"][i][5]])
    for i in range(len(data_club["fw"])):
        nomor = i + 1 + len(data_club["gk"] + data_club["df"] + data_club["mf"])
        data_squad.append([f"{nomor}.", data_club["fw"][i][0], "FW", data_club["fw"][i][1], data_club["fw"][i][2], f"€{data_club["fw"][i][3]:,}", data_club["fw"][i][4], data_club["fw"][i][5]])

    tabel_squad = PrettyTable()
    tabel_squad.field_names = ["NO.", "Nama Pemain", "Posisi", "Rating", "Umur", "MV", "Tinggi(cm)", "Negara"]
    tabel_squad.add_rows(data_squad)
    print(tabel_squad)

def tampil_saldo(data_club):
                    tabel_saldo = PrettyTable()
                    tabel_saldo.field_names = ["Saldo Club"]
                    tabel_saldo.add_row([
                        f"€{data_club["saldo"]:,}"
                        ])
                    print(tabel_saldo)

def tampil_formasi(club_pengguna, data_club_pengguna):
                    data_waktu = dt.datetime.now()
                    os.system("cls")
                    print(f"Daftar Line Up {club_pengguna} ({data_waktu.strftime("%A")}, {data_waktu.day} - {data_waktu.month} - {data_waktu.year})\n")
                    
                    tampil_starting(data_club_pengguna)
                    print()
                    tampil_cadangan(data_club_pengguna)
                    print()
                    tampil_saldo(data_club_pengguna)
                    input("\n(Ketuk enter untuk kembali memilih menu)")
                
def beli_pemain(club_masuk, club_keluar, data_club_masuk, data_club_keluar):
    while True:
        os.system("cls")
        tampil_squad(data_club_keluar)
        print("\nLini tersedia: gk (kiper), df (bek), mf (gelandang), fw (penyerang)")
        lini = input("Masukkan lini yang ingin dibeli: ").strip().lower()

        try:
            if lini not in data_club_keluar:
                raise ValueError(f"Lini '{lini}' tidak tersedia.")
                
            daftar = data_club_keluar[lini]

            print(f"\nDaftar pemain di lini {lini}:")
            for i, p in enumerate(daftar):
                print(f"{i+1}. {p[0]} (Rating: {p[1]}, Harga: €{p[3]:,})")

            idx_a = int(input("\nMasukkan nomor pemain: ")) - 1
            
            # Mencegah agar pemain pada lini club tidak habis
            if lini == "gk":
                if len(daftar) <= 1:
                    raise ValueError(f"Jumlah pemain pada lini {lini} {club_keluar} tidak cukup")
            elif lini == "df":
                if len(daftar) <= 4:
                    raise ValueError(f"Jumlah pemain pada lini {lini} {club_keluar} tidak cukup")
            elif lini == "mf":
                if len(daftar) <= 3:
                    raise ValueError(f"Jumlah pemain pada lini {lini} {club_keluar} tidak cukup")
            elif lini == "fw":
                if len(daftar) <= 3:
                    raise ValueError(f"Jumlah pemain pada lini {lini} {club_keluar} tidak cukup")
            if idx_a < 0:
                raise ValueError("Nomor pemain tidak tersedia")
            
            # Tambah pemain
            if data_club_keluar == data_gratisan:
                tampung_pemain = daftar[idx_a][:6]
            elif data_club_keluar == data_pemuda:
                tampung_pemain = daftar[idx_a][:6]
            else:
                tampung_pemain = daftar[idx_a]
            
            data_club_masuk[lini].append(tampung_pemain)

            # Masukkan ke data transfer
            data_transfer.append([len(data_transfer) + 1, tampung_pemain[0], lini.upper(), tampung_pemain[1], tampung_pemain[2], f"€{tampung_pemain[3]:,}", tampung_pemain[4], tampung_pemain[5], club_masuk])

            # Harga beli (Market Value * 120%)
            harga_beli = daftar[idx_a][3] * 120 / 100
            data_club_masuk["saldo"] -= harga_beli

            input(f"\n✅ Pemain berhasil dibeli: {daftar[idx_a][0]} -> {club_masuk} di lini {lini}, sisa saldo club: €{data_club_masuk["saldo"]:,}.")
            del daftar[idx_a]
            break

        except Exception as e:
            print()
            input(f"({e})")
            continue

def jual_pemain(club, data_club):
    while True:
        os.system("cls")
        print("Lini tersedia: gk (kiper), df (bek), mf (gelandang), fw (penyerang)")
        lini = input("Masukkan lini yang ingin dijual: ").strip().lower()

        try:
            if lini not in data_club:
                raise ValueError(f"Lini '{lini}' tidak tersedia.")
                
            daftar = data_club[lini]

            print(f"\nDaftar pemain di lini {lini}:")
            for i, p in enumerate(daftar):
                print(f"{i+1}. {p[0]} (Rating: {p[1]}, Harga: €{p[3]:,})")

            idx_a = int(input("\nMasukkan nomor pemain: ")) - 1
            
            # Mencegah agar pemain pada lini club tidak habis
            if lini == "gk":
                if len(daftar) <= 1:
                    raise ValueError(f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "df":
                if len(daftar) <= 4:
                    raise ValueError(f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "mf":
                if len(daftar) <= 3:
                    raise ValueError(f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "fw":
                if len(daftar) <= 3:
                    raise ValueError(f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            
            if idx_a < 0:
                raise ValueError("Nomor pemain tidak tersedia")
            
            # tambah pemain ke club random
            pilih_club = [data_barcelona, data_madrid, data_arsenal, data_psg, data_dortmund]
            pilih_club.remove(data_club)
            data_club_masuk = random.choice(pilih_club)
            data_club_masuk[lini].append(daftar[idx_a])

            if data_club_masuk == data_barcelona:
                club_masuk = "Barcelona"
            elif data_club_masuk == data_madrid:
                club_masuk = "Barcelona"
            elif data_club_masuk == data_arsenal:
                club_masuk = "Arsenal"
            elif data_club_masuk == data_psg:
                club_masuk = "PSG"
            elif data_club_masuk == data_dortmund:
                club_masuk = "Borussia Dortmund"
            
            # Masukkan ke data transfer
            data_transfer.append([len(data_transfer) + 1, daftar[idx_a][0], lini.upper(), daftar[idx_a][1], daftar[idx_a][2], f"€{daftar[idx_a][3]:,}", daftar[idx_a][4], daftar[idx_a][5], club_masuk])

            # Harga jual (Market Value * 80%)
            harga_jual = daftar[idx_a][3] * 80 / 100
            data_club["saldo"] += harga_jual

            input(f"\n✅ Posisi berhasil dijual: {daftar[idx_a][0]} -> {club_masuk} di lini {lini}, sisa saldo club: €{data_club["saldo"]:,}.")

            # hapus pemain di club awal
            del daftar[idx_a]
            break

        except Exception as e:
            print()
            input(f"({e})")
            continue

def ganti_pemain(data_club):
    while True:
        os.system("cls")
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

            if idx_a < 0 or idx_b < 0:
                raise ValueError("Nomor pemain tidak tersedia")
            
            if idx_a == idx_b:
                raise ValueError("Nomor pemain tidak boleh sama")
            
            # Tukar posisi
            daftar[idx_a], daftar[idx_b] = daftar[idx_b], daftar[idx_a]

            input(f"\n✅ Posisi berhasil ditukar: {daftar[idx_b][0]} ⇄ {daftar[idx_a][0]} di lini {lini}.")
            break

        except Exception as e:
            print()
            input(f"({e})")
            continue

def buka_jendela_transfer(club):
    os.system("cls")
    asal = random.choice([c for c in clubs.keys() if c != club])
    tujuan = random.choice([c for c in clubs.keys() if c not in [asal, club, "Pencari Bakat"]])

    # Pilih lini dan pemain secara acak
    lini = random.choice(["gk", "df", "mf", "fw"])
    pemain_list = clubs[asal][lini]
    if not pemain_list:
        return "Tidak ada pemain di lini ini."
    
    pemain = random.choice(pemain_list)
    pemain_list.remove(pemain)  # Hapus dari klub asal
    clubs[tujuan][lini].append(pemain)  # Tambah ke klub tujuan
    
    # Tambahkan ke data transfer
    data_transfer.append([f"{len(data_transfer) + 1}.", pemain[0], lini.upper(), pemain[1], pemain[2], f"€{pemain[3]:,}", pemain[4], pemain[5], tujuan])
    
    # Tampilkan data transfer
    tabel_transfer = PrettyTable()
    tabel_transfer.title = "DATA TRANSFER"
    tabel_transfer.field_names = ["NO.", "Nama Pemain", "Posisi", "Rating", "Umur", "MV", "Tinggi(cm)", "Negara", "Club Tujuan/Status"]
    tabel_transfer.add_rows(data_transfer)
    print(tabel_transfer)
    input("\n(Ketuk enter untuk kembali memilih menu)")
        
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

if login_biasa:
    club_pengguna = data_pengguna["user_biasa"][user][1]
    data_club_pengguna = clubs[club_pengguna]

    def menu_login_biasa(user, club_pengguna, data_club_pengguna):
        global login_biasa
        
        if club_pengguna == "Barcelona":
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
                    ["[3]", "Keuangan Club"],
                    ["[4]", "Transfer Pemain"],
                    ["[5]", "Jendela Transfer"],
                    ["[0]", "Keluar"]
                    ])
                print(tabel_menu_admin)

                pilihan_2 = input("Pilih menu (1-5) = ").strip()
                
                if pilihan_2 == "1":
                    tampil_formasi(club_pengguna, data_club_pengguna)

                elif pilihan_2 == "2":                         
                    ganti_pemain(data_club_pengguna)

                elif pilihan_2 == "3":
                    pass
        
                elif pilihan_2 == "4":
                    while True:
                        os.system("cls")
                        tabel_transfer = PrettyTable()
                        tabel_transfer.title = "TRANSFER PEMAIN"
                        tabel_transfer.field_names = ["kiri", "kanan"]
                        tabel_transfer.header = False
                        tabel_transfer.add_rows([
                            ["[1]", "Beli pemain"],
                            ["[2]", "Jual pemain"],
                            ["[0]", "Kembali"]
                            ])
                        print(tabel_transfer)

                        pilihan_3 = input("Pilih menu (1-2) = ").strip()

                        if pilihan_3 == "1":
                            while True:
                                os.system("cls")
                                tabel_pil_club = PrettyTable()
                                tabel_pil_club.title = "MAU BELI PEMAIN DARI:"
                                tabel_pil_club.field_names = ["kiri", "kanan"]
                                tabel_pil_club.header = False
                                tabel_pil_club.add_rows([
                                    ["[1]", "Real Madrid"],
                                    ["[2]", "Arsenal"],
                                    ["[3]", "PSG"],
                                    ["[4]", "Borussia Dortmund"],
                                    ["[5]", "Free Agent"],
                                    ["[6]", "Pencari Bakat"],
                                    ["[0]", "Kembali"]
                                    ])
                                print(tabel_pil_club)

                                pilihan_4 = input("Pilih menu (1-6) = ").strip()

                                if pilihan_4 == "1":
                                    beli_pemain(club_pengguna, "Real Madrid", data_club_pengguna, data_madrid)
                                    break
                                elif pilihan_4 == "2":
                                    beli_pemain(club_pengguna, "Arsenal", data_club_pengguna, data_arsenal)
                                    break
                                elif pilihan_4 == "3":
                                    beli_pemain(club_pengguna, "PSG", data_club_pengguna, data_psg)
                                    break
                                elif pilihan_4 == "4":
                                    beli_pemain(club_pengguna, "Borussia Dortmund",  data_club_pengguna, data_dortmund)
                                    break
                                elif pilihan_4 == "5":
                                    beli_pemain(club_pengguna, "Free Agent", data_club_pengguna, data_gratisan)
                                    break
                                elif pilihan_4 == "6":
                                    beli_pemain(club_pengguna, "Pencari Bakat", data_club_pengguna, data_pemuda)
                                    break
                                elif pilihan_4 == "0":
                                    break
                                else:
                                    input("\n(Input tidak valid, ketuk enter untuk kembali)")

                        elif pilihan_3 == "2":                                              
                            jual_pemain(club_pengguna, data_club_pengguna)

                        elif pilihan_3 == "0":
                            break
                        
                        else:
                            input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        
                elif pilihan_2 == "5":
                    buka_jendela_transfer(club_pengguna)
    
                elif pilihan_2 == "0":
                    login_biasa = False

                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")

        elif club_pengguna == "Real Madrid":
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
                    ["[3]", "Keuangan Club"],
                    ["[4]", "Transfer Pemain"],
                    ["[5]", "Jendela Transfer"],
                    ["[0]", "Keluar"]
                    ])
                print(tabel_menu_admin)

                pilihan_2 = input("Pilih menu (1-5) = ").strip()
                
                if pilihan_2 == "1":
                    tampil_formasi(club_pengguna, data_club_pengguna)

                elif pilihan_2 == "2":                         
                    ganti_pemain(data_club_pengguna)

                elif pilihan_2 == "3":
                    pass
        
                elif pilihan_2 == "4":
                    while True:
                        os.system("cls")
                        tabel_transfer = PrettyTable()
                        tabel_transfer.title = "TRANSFER PEMAIN"
                        tabel_transfer.field_names = ["kiri", "kanan"]
                        tabel_transfer.header = False
                        tabel_transfer.add_rows([
                            ["[1]", "Beli pemain"],
                            ["[2]", "Jual pemain"],
                            ["[0]", "Kembali"]
                            ])
                        print(tabel_transfer)

                        pilihan_3 = input("Pilih menu (1-2) = ").strip()

                        if pilihan_3 == "1":
                            while True:
                                os.system("cls")
                                tabel_pil_club = PrettyTable()
                                tabel_pil_club.title = "MAU BELI PEMAIN DARI:"
                                tabel_pil_club.field_names = ["kiri", "kanan"]
                                tabel_pil_club.header = False
                                tabel_pil_club.add_rows([
                                    ["[1]", "Barcelona"],
                                    ["[2]", "Arsenal"],
                                    ["[3]", "PSG"],
                                    ["[4]", "Borussia Dortmund"],
                                    ["[5]", "Free Agent"],
                                    ["[6]", "Pencari Bakat"],
                                    ["[0]", "Kembali"]
                                    ])
                                print(tabel_pil_club)

                                pilihan_4 = input("Pilih menu (1-6) = ").strip()

                                if pilihan_4 == "1":
                                    beli_pemain(club_pengguna, "Barcelona", data_club_pengguna, data_barcelona)
                                    break
                                elif pilihan_4 == "2":
                                    beli_pemain(club_pengguna, "Arsenal", data_club_pengguna, data_arsenal)
                                    break
                                elif pilihan_4 == "3":
                                    beli_pemain(club_pengguna, "PSG", data_club_pengguna, data_psg)
                                    break
                                elif pilihan_4 == "4":
                                    beli_pemain(club_pengguna, "Borussia Dortmund",  data_club_pengguna, data_dortmund)
                                    break
                                elif pilihan_4 == "5":
                                    beli_pemain(club_pengguna, "Free Agent", data_club_pengguna, data_gratisan)
                                    break
                                elif pilihan_4 == "6":
                                    beli_pemain(club_pengguna, "Pencari Bakat", data_club_pengguna, data_pemuda)
                                    break
                                elif pilihan_4 == "0":
                                    break
                                else:
                                    input("\n(Input tidak valid, ketuk enter untuk kembali)")

                        elif pilihan_3 == "2":                                              
                            jual_pemain(club_pengguna, data_club_pengguna)

                        elif pilihan_3 == "0":
                            break
                        
                        else:
                            input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        
                elif pilihan_2 == "5":
                    buka_jendela_transfer(club_pengguna)
    
                elif pilihan_2 == "0":
                    login_biasa = False

                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")

        elif club_pengguna == "Arsenal":
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
                    ["[3]", "Keuangan Club"],
                    ["[4]", "Transfer Pemain"],
                    ["[5]", "Jendela Transfer"],
                    ["[0]", "Keluar"]
                    ])
                print(tabel_menu_admin)

                pilihan_2 = input("Pilih menu (1-5) = ").strip()
                
                if pilihan_2 == "1":
                    tampil_formasi(club_pengguna, data_club_pengguna)

                elif pilihan_2 == "2":                         
                    ganti_pemain(data_club_pengguna)

                elif pilihan_2 == "3":
                    pass
        
                elif pilihan_2 == "4":
                    while True:
                        os.system("cls")
                        tabel_transfer = PrettyTable()
                        tabel_transfer.title = "TRANSFER PEMAIN"
                        tabel_transfer.field_names = ["kiri", "kanan"]
                        tabel_transfer.header = False
                        tabel_transfer.add_rows([
                            ["[1]", "Beli pemain"],
                            ["[2]", "Jual pemain"],
                            ["[0]", "Kembali"]
                            ])
                        print(tabel_transfer)

                        pilihan_3 = input("Pilih menu (1-2) = ").strip()

                        if pilihan_3 == "1":
                            while True:
                                os.system("cls")
                                tabel_pil_club = PrettyTable()
                                tabel_pil_club.title = "MAU BELI PEMAIN DARI:"
                                tabel_pil_club.field_names = ["kiri", "kanan"]
                                tabel_pil_club.header = False
                                tabel_pil_club.add_rows([
                                    ["[1]", "Barcelona"],
                                    ["[2]", "Real Madrid"],
                                    ["[3]", "PSG"],
                                    ["[4]", "Borussia Dortmund"],
                                    ["[5]", "Free Agent"],
                                    ["[6]", "Pencari Bakat"],
                                    ["[0]", "Kembali"]
                                    ])
                                print(tabel_pil_club)

                                pilihan_4 = input("Pilih menu (1-6) = ").strip()

                                if pilihan_4 == "1":
                                    beli_pemain(club_pengguna, "Barcelona", data_club_pengguna, data_barcelona)
                                    break
                                elif pilihan_4 == "2":
                                    beli_pemain(club_pengguna, "Real Madrid", data_club_pengguna, data_madrid)
                                    break
                                elif pilihan_4 == "3":
                                    beli_pemain(club_pengguna, "PSG", data_club_pengguna, data_psg)
                                    break
                                elif pilihan_4 == "4":
                                    beli_pemain(club_pengguna, "Borussia Dortmund",  data_club_pengguna, data_dortmund)
                                    break
                                elif pilihan_4 == "5":
                                    beli_pemain(club_pengguna, "Free Agent", data_club_pengguna, data_gratisan)
                                    break
                                elif pilihan_4 == "6":
                                    beli_pemain(club_pengguna, "Pencari Bakat", data_club_pengguna, data_pemuda)
                                    break
                                elif pilihan_4 == "0":
                                    break
                                else:
                                    input("\n(Input tidak valid, ketuk enter untuk kembali)")

                        elif pilihan_3 == "2":                                              
                            jual_pemain(club_pengguna, data_club_pengguna)

                        elif pilihan_3 == "0":
                            break
                        
                        else:
                            input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        
                elif pilihan_2 == "5":
                    buka_jendela_transfer(club_pengguna)
    
                elif pilihan_2 == "0":
                    login_biasa = False

                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")
        
        elif club_pengguna == "PSG":
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
                    ["[3]", "Keuangan Club"],
                    ["[4]", "Transfer Pemain"],
                    ["[5]", "Jendela Transfer"],
                    ["[0]", "Keluar"]
                    ])
                print(tabel_menu_admin)

                pilihan_2 = input("Pilih menu (1-5) = ").strip()
                
                if pilihan_2 == "1":
                    tampil_formasi(club_pengguna, data_club_pengguna)

                elif pilihan_2 == "2":                         
                    ganti_pemain(data_club_pengguna)

                elif pilihan_2 == "3":
                    pass
        
                elif pilihan_2 == "4":
                    while True:
                        os.system("cls")
                        tabel_transfer = PrettyTable()
                        tabel_transfer.title = "TRANSFER PEMAIN"
                        tabel_transfer.field_names = ["kiri", "kanan"]
                        tabel_transfer.header = False
                        tabel_transfer.add_rows([
                            ["[1]", "Beli pemain"],
                            ["[2]", "Jual pemain"],
                            ["[0]", "Kembali"]
                            ])
                        print(tabel_transfer)

                        pilihan_3 = input("Pilih menu (1-2) = ").strip()

                        if pilihan_3 == "1":
                            while True:
                                os.system("cls")
                                tabel_pil_club = PrettyTable()
                                tabel_pil_club.title = "MAU BELI PEMAIN DARI:"
                                tabel_pil_club.field_names = ["kiri", "kanan"]
                                tabel_pil_club.header = False
                                tabel_pil_club.add_rows([
                                    ["[1]", "Barcelona"],
                                    ["[2]", "Real Madrid"],
                                    ["[3]", "Arsenal"],
                                    ["[4]", "Borussia Dortmund"],
                                    ["[5]", "Free Agent"],
                                    ["[6]", "Pencari Bakat"],
                                    ["[0]", "Kembali"]
                                    ])
                                print(tabel_pil_club)

                                pilihan_4 = input("Pilih menu (1-6) = ").strip()

                                if pilihan_4 == "1":
                                    beli_pemain(club_pengguna, "Barcelona", data_club_pengguna, data_barcelona)
                                    break
                                elif pilihan_4 == "2":
                                    beli_pemain(club_pengguna, "Real Madrid", data_club_pengguna, data_madrid)
                                    break
                                elif pilihan_4 == "3":
                                    beli_pemain(club_pengguna, "Arsenal", data_club_pengguna, data_arsenal)
                                    break
                                elif pilihan_4 == "4":
                                    beli_pemain(club_pengguna, "Borussia Dortmund",  data_club_pengguna, data_dortmund)
                                    break
                                elif pilihan_4 == "5":
                                    beli_pemain(club_pengguna, "Free Agent", data_club_pengguna, data_gratisan)
                                    break
                                elif pilihan_4 == "6":
                                    beli_pemain(club_pengguna, "Pencari Bakat", data_club_pengguna, data_pemuda)
                                    break
                                elif pilihan_4 == "0":
                                    break
                                else:
                                    input("\n(Input tidak valid, ketuk enter untuk kembali)")

                        elif pilihan_3 == "2":                                              
                            jual_pemain(club_pengguna, data_club_pengguna)

                        elif pilihan_3 == "0":
                            break
                        
                        else:
                            input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        
                elif pilihan_2 == "5":
                    buka_jendela_transfer(club_pengguna)
    
                elif pilihan_2 == "0":
                    login_biasa = False

                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")
        
        elif club_pengguna == "Borussia Dortmund":
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
                    ["[3]", "Keuangan Club"],
                    ["[4]", "Transfer Pemain"],
                    ["[5]", "Jendela Transfer"],
                    ["[0]", "Keluar"]
                    ])
                print(tabel_menu_admin)

                pilihan_2 = input("Pilih menu (1-5) = ").strip()
                
                if pilihan_2 == "1":
                    tampil_formasi(club_pengguna, data_club_pengguna)

                elif pilihan_2 == "2":                         
                    ganti_pemain(data_club_pengguna)

                elif pilihan_2 == "3":
                    pass
        
                elif pilihan_2 == "4":
                    while True:
                        os.system("cls")
                        tabel_transfer = PrettyTable()
                        tabel_transfer.title = "TRANSFER PEMAIN"
                        tabel_transfer.field_names = ["kiri", "kanan"]
                        tabel_transfer.header = False
                        tabel_transfer.add_rows([
                            ["[1]", "Beli pemain"],
                            ["[2]", "Jual pemain"],
                            ["[0]", "Kembali"]
                            ])
                        print(tabel_transfer)

                        pilihan_3 = input("Pilih menu (1-2) = ").strip()

                        if pilihan_3 == "1":
                            while True:
                                os.system("cls")
                                tabel_pil_club = PrettyTable()
                                tabel_pil_club.title = "MAU BELI PEMAIN DARI:"
                                tabel_pil_club.field_names = ["kiri", "kanan"]
                                tabel_pil_club.header = False
                                tabel_pil_club.add_rows([
                                    ["[1]", "Barcelona"],
                                    ["[2]", "Real Madrid"],
                                    ["[3]", "Arsenal"],
                                    ["[4]", "PSG"],
                                    ["[5]", "Free Agent"],
                                    ["[6]", "Pencari Bakat"],
                                    ["[0]", "Kembali"]
                                    ])
                                print(tabel_pil_club)

                                pilihan_4 = input("Pilih menu (1-6) = ").strip()

                                if pilihan_4 == "1":
                                    beli_pemain(club_pengguna, "Barcelona", data_club_pengguna, data_barcelona)
                                    break
                                elif pilihan_4 == "2":
                                    beli_pemain(club_pengguna, "Real Madrid", data_club_pengguna, data_madrid)
                                    break
                                elif pilihan_4 == "3":
                                    beli_pemain(club_pengguna, "Arsenal", data_club_pengguna, data_arsenal)
                                    break
                                elif pilihan_4 == "4":
                                    beli_pemain(club_pengguna, "PSG",  data_club_pengguna, data_psg)
                                    break
                                elif pilihan_4 == "5":
                                    beli_pemain(club_pengguna, "Free Agent", data_club_pengguna, data_gratisan)
                                    break
                                elif pilihan_4 == "6":
                                    beli_pemain(club_pengguna, "Pencari Bakat", data_club_pengguna, data_pemuda)
                                    break
                                elif pilihan_4 == "0":
                                    break
                                else:
                                    input("\n(Input tidak valid, ketuk enter untuk kembali)")

                        elif pilihan_3 == "2":                                              
                            jual_pemain(club_pengguna, data_club_pengguna)

                        elif pilihan_3 == "0":
                            break
                        
                        else:
                            input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        
                elif pilihan_2 == "5":
                    buka_jendela_transfer(club_pengguna)
    
                elif pilihan_2 == "0":
                    login_biasa = False

                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")


    menu_login_biasa(user, club_pengguna, data_club_pengguna)

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
            ["[0]", "Keluar"]
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