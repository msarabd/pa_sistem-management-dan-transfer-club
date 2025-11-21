from prettytable import PrettyTable
import os
import datetime as dt
from data import data_barcelona, data_madrid, data_arsenal, data_psg, data_dortmund, data_gratisan, data_pemuda, data_nassr, data_miami, data_borneo, data_legend, data_custom, data_transfer, clubs
import random
import climage
import time
import threading

def tampil_starting(data_club):
    data_starting = []
    for i in range(len(data_club["gk"])):
        if i == 0:
            nomor = i + 1
            data_starting.append([f"{nomor}.", data_club["gk"][i][0], "GK", data_club["gk"][i][1], data_club["gk"][i][2], f"€{data_club["gk"][i][3]:,}", data_club["gk"][i][4], data_club["gk"][i][5]])
    for i in range(len(data_club["df"])):
        if i <= 3:
            nomor = i + 2
            data_starting.append([f"{nomor}.", data_club["df"][i][0], "DF", data_club["df"][i][1], data_club["df"][i][2], f"€{data_club["df"][i][3]:,}", data_club["df"][i][4], data_club["df"][i][5]])
    for i in range(len(data_club["mf"])):
        if i <= 2:
            nomor = i + 6
            data_starting.append([f"{nomor}.", data_club["mf"][i][0], "MF", data_club["mf"][i][1], data_club["mf"][i][2], f"€{data_club["mf"][i][3]:,}", data_club["mf"][i][4], data_club["mf"][i][5]])
    for i in range(len(data_club["fw"])):
        if i <= 2:
            nomor = i + 10
            data_starting.append([f"{nomor}.", data_club["fw"][i][0], "FW", data_club["fw"][i][1], data_club["fw"][i][2], f"€{data_club["fw"][i][3]:,}", data_club["fw"][i][4], data_club["fw"][i][5]])
    
    tabel_starting = PrettyTable()
    tabel_starting.title = "STARTING"
    tabel_starting.field_names = ["NO.", "Nama Pemain", "Posisi", "Rating", "Umur", "MV", "Tinggi(cm)", "Negara"]
    tabel_starting.add_rows(data_starting)
    print(tabel_starting)

def tampil_cadangan(data_club):
    data_cadangan = []
    for i in range(len(data_club["gk"])):
        if i > 0:
            nomor = i
            data_cadangan.append([f"{nomor}.", data_club["gk"][i][0], "GK", data_club["gk"][i][1], data_club["gk"][i][2], f"€{data_club["gk"][i][3]:,}", data_club["gk"][i][4], data_club["gk"][i][5]])
    for i in range(len(data_club["df"])):
        if i > 3:
            nomor = i - 3 + (len(data_club["gk"]) - 1)
            data_cadangan.append([f"{nomor}.", data_club["df"][i][0], "DF", data_club["df"][i][1], data_club["df"][i][2], f"€{data_club["df"][i][3]:,}", data_club["df"][i][4], data_club["df"][i][5]])
    for i in range(len(data_club["mf"])):
        if i > 2:
            nomor = i - 3 + (len(data_club["gk"]) - 1) + (len(data_club["df"]) - 3) 
            data_cadangan.append([f"{nomor}.", data_club["mf"][i][0], "MF", data_club["mf"][i][1], data_club["mf"][i][2], f"€{data_club["mf"][i][3]:,}", data_club["mf"][i][4], data_club["mf"][i][5]])
    for i in range(len(data_club["fw"])):
        if i > 2:
            nomor = i - 3 + (len(data_club["gk"]) - 1) + (len(data_club["df"]) - 3) + (len(data_club["mf"]) - 2)
            data_cadangan.append([f"{nomor}.", data_club["fw"][i][0], "FW", data_club["fw"][i][1], data_club["fw"][i][2], f"€{data_club["fw"][i][3]:,}", data_club["fw"][i][4], data_club["fw"][i][5]])

    tabel_cadangan = PrettyTable()
    tabel_cadangan.title = "CADANGAN"
    tabel_cadangan.field_names = ["NO.", "Nama Pemain", "Posisi", "Rating", "Umur", "MV", "Tinggi(cm)", "Negara"]
    tabel_cadangan.add_rows(data_cadangan)
    print(tabel_cadangan)

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

            # Mencegah membeli pemain dari lini yang tidak memiliki pemain
            if daftar == []:
                raise ValueError(f"Pemain di lini ini tidak tersedia.")
            
            print(f"\nDaftar pemain di lini {lini}:")
            for i, p in enumerate(daftar):
                print(f"{i+1}. {p[0]} (Rating: {p[1]}, Harga: €{p[3]:,})")

            idx_a = int(input("\nMasukkan nomor pemain: ")) - 1
            
            # Mencegah agar pemain pada lini club tidak habis
            if data_club_keluar in [data_barcelona, data_madrid, data_arsenal, data_psg, data_dortmund, data_nassr, data_miami, data_borneo]:
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
            
            # Pengecualian jika pemain yang dibeli itu harganya 0 atau gratis 
            if daftar[idx_a][3] == 0:
                pass

            # Mencegah agar tidak bisa membeli pemain saat saldo tidak cukup
            elif daftar[idx_a][3] > data_club_masuk["saldo"]:
                raise ValueError(f"Saldo club tidak cukup untuk membeli pemain ini")

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
            tekan = input(f"\n({e})")
            if tekan == "0":
                break
            else:
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
            
            # Mencegah agar pemain pada lini club tidak habis (khusus untuk club, free agent dan pencari bakat tidak berlaku)
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
            tekan = input(f"\n({e})")
            if tekan == "0":
                break
            else:
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
            tekan = input(f"\n({e})")
            if tekan == "0":
                break
            else:
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
    tabel_transfer.title = "JENDELA TRANSFER"
    tabel_transfer.field_names = ["NO.", "Nama Pemain", "Posisi", "Rating", "Umur", "MV", "Tinggi(cm)", "Negara", "Club Tujuan/Status"]
    tabel_transfer.add_rows(data_transfer)
    print(tabel_transfer)
    input("\n(Ketuk enter untuk kembali memilih menu)")

def keuangan_club(club, data_club):
    os.system("cls")

    if club == "Barcelona":
        gambar_stadion = climage.convert("static/stadion_barcelona.jpg")
        print(gambar_stadion)
        print(F"Pendapatan Stadion = +€{data_club["stadion"]:,}\n")

        gambar_jersey = climage.convert("static/jersey_barcelona.png")
        print(gambar_jersey)
        print(F"Pendapatan Merchandise = +€{data_club["jersey"]:,}\n")

        tampil_saldo(data_club)
    
    elif club == "Real Madrid":
        gambar_stadion = climage.convert("static/stadion_madrid.jpg")
        print(gambar_stadion)
        print(F"Pendapatan Stadion = +€{data_club["stadion"]:,}\n")

        gambar_jersey = climage.convert("static/jersey_madrid.png")
        print(gambar_jersey)
        print(F"Pendapatan Merchandise = +€{data_club["jersey"]:,}\n")

        tampil_saldo(data_club)

    elif club == "Arsenal":
        gambar_stadion = climage.convert("static/stadion_arsenal.jpg")
        print(gambar_stadion)
        print(F"Pendapatan Stadion = +€{data_club["stadion"]:,}\n")

        gambar_jersey = climage.convert("static/jersey_arsenal.png")
        print(gambar_jersey)
        print(F"Pendapatan Merchandise = +€{data_club["jersey"]:,}\n")

        tampil_saldo(data_club)

    elif club == "PSG":
        gambar_stadion = climage.convert("static/stadion_psg.jpg")
        print(gambar_stadion)
        print(F"Pendapatan Stadion = +€{data_club["stadion"]:,}\n")

        gambar_jersey = climage.convert("static/jersey_psg.png")
        print(gambar_jersey)
        print(F"Pendapatan Merchandise = +€{data_club["jersey"]:,}\n")

        tampil_saldo(data_club)

    elif club == "Borussia Dortmund":
        gambar_stadion = climage.convert("static/stadion_dortmund.jpg")
        print(gambar_stadion)
        print(F"Pendapatan Stadion = +€{data_club["stadion"]:,}\n")

        gambar_jersey = climage.convert("static/jersey_dortmund.png")
        print(gambar_jersey)
        print(F"Pendapatan Merchandise = +€{data_club["jersey"]:,}\n")

        tampil_saldo(data_club)

    elif club == "Borneo":
        gambar_stadion = climage.convert("static/stadion_borneo.jpeg")
        print(gambar_stadion)
        print(F"Pendapatan Stadion = +€{data_club["stadion"]:,}\n")

        gambar_jersey = climage.convert("static/jersey_borneo.png")
        print(gambar_jersey)
        print(F"Pendapatan Merchandise = +€{data_club["jersey"]:,}\n")

        tampil_saldo(data_club)

    input("\n(Ketuk enter untuk kembali memilih menu)")

def pendapatan_club(data_club):
    while True:
        data_club["saldo"] += data_club["stadion"] 
        time.sleep(5)

def menu_login_biasa(user, club_pengguna, data_club_pengguna):
    t1 = threading.Thread(target=lambda: pendapatan_club(data_club_pengguna), daemon=True)
    t1.start()

    if club_pengguna == "Barcelona":
        while True:
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
                keuangan_club(club_pengguna, data_club_pengguna)
    
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
                break

            else:
                input("\n(Input tidak valid, ketuk enter untuk kembali)")

    elif club_pengguna == "Real Madrid":
        while True:
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
                keuangan_club(club_pengguna, data_club_pengguna)
    
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
                break

            else:
                input("\n(Input tidak valid, ketuk enter untuk kembali)")

    elif club_pengguna == "Arsenal":
        while True:
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
                keuangan_club(club_pengguna, data_club_pengguna)
    
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
                break

            else:
                input("\n(Input tidak valid, ketuk enter untuk kembali)")
    
    elif club_pengguna == "PSG":
        while True:
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
                keuangan_club(club_pengguna, data_club_pengguna)
    
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
                break

            else:
                input("\n(Input tidak valid, ketuk enter untuk kembali)")
    
    elif club_pengguna == "Borussia Dortmund":
        while True:
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
                keuangan_club(club_pengguna, data_club_pengguna)
    
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
                break

            else:
                input("\n(Input tidak valid, ketuk enter untuk kembali)")

def menu_login_mod(user, club_pengguna, data_club_pengguna):
    t1 = threading.Thread(target=lambda: pendapatan_club(data_club_pengguna), daemon=True)
    t1.start()

    while True:
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
            keuangan_club(club_pengguna, data_club_pengguna)

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
                            ["[5]", "Borussia Dortmund"],
                            ["[6]", "Al Nassr"],
                            ["[7]", "Inter Miami"],
                            ["[8]", "Free Agent"],
                            ["[9]", "Pencari Bakat"],
                            ["[10]", "Pemain Legend"],
                            ["[11]", "Most Wanted"],
                            ["[0]", "Kembali"]
                            ])
                        print(tabel_pil_club)

                        pilihan_4 = input("Pilih menu (1-11) = ").strip()

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
                            beli_pemain(club_pengguna, "Borussia Dortmund", data_club_pengguna, data_dortmund)
                            break
                        elif pilihan_4 == "6":
                            beli_pemain(club_pengguna, "Al Nassr", data_club_pengguna, data_nassr)
                            break
                        elif pilihan_4 == "7":
                            beli_pemain(club_pengguna, "Inter Miami", data_club_pengguna, data_miami)
                            break
                        elif pilihan_4 == "8":
                            beli_pemain(club_pengguna, "Free Agent", data_club_pengguna, data_gratisan)
                            break
                        elif pilihan_4 == "9":
                            beli_pemain(club_pengguna, "Pencari Bakat", data_club_pengguna, data_pemuda)
                            break
                        elif pilihan_4 == "10":
                            beli_pemain(club_pengguna, "Pemain Legend", data_club_pengguna, data_legend)
                            break
                        elif pilihan_4 == "11":
                            beli_pemain(club_pengguna, "Most Wanted", data_club_pengguna, data_custom)
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
            break

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")
