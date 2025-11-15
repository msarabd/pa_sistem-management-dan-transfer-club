import os
from login import input_biasa, input_mod, input_register
from crud import tampil_starting, tampil_cadangan, ganti_pemain, ganti_pemain, hapus_pemain, tampilan_ubah_pemain
from prettytable import PrettyTable
import datetime as dt
from data import data_club_pengguna, data_pengguna, data_barcelona, data_madrid, data_arsenal, data_psg, data_dortmund, data_gratisan, data_pemuda, data_transfer, clubs
import random
import threading
import time

login_mod = False
login_biasa = False


def tampil_squad(data_club):
    data_squad = []
    for i in range(len(data_club["gk"])):
        nomor = i + 1
        data_squad.append([f"{nomor}.", data_club["gk"][i][0], "GK", data_club["gk"][i][1], data_club["gk"]
                          [i][2], f"€{data_club["gk"][i][3]}", data_club["gk"][i][4], data_club["gk"][i][5]])
    for i in range(len(data_club["df"])):
        nomor = i + 1 + len(data_club["gk"])
        data_squad.append([f"{nomor}.", data_club["df"][i][0], "DF", data_club["df"][i][1], data_club["df"]
                          [i][2], f"€{data_club["df"][i][3]}", data_club["df"][i][4], data_club["df"][i][5]])
    for i in range(len(data_club["mf"])):
        nomor = i + 1 + len(data_club["gk"] + data_club["df"])
        data_squad.append([f"{nomor}.", data_club["mf"][i][0], "MF", data_club["mf"][i][1], data_club["mf"]
                          [i][2], f"€{data_club["mf"][i][3]}", data_club["mf"][i][4], data_club["mf"][i][5]])
    for i in range(len(data_club["fw"])):
        nomor = i + 1 + len(data_club["gk"] +
                            data_club["df"] + data_club["mf"])
        data_squad.append([f"{nomor}.", data_club["fw"][i][0], "FW", data_club["fw"][i][1], data_club["fw"]
                          [i][2], f"€{data_club["fw"][i][3]}", data_club["fw"][i][4], data_club["fw"][i][5]])

    tabel_squad = PrettyTable()
    tabel_squad.field_names = [
        "NO.", "Nama Pemain", "Posisi", "Rating", "Umur", "MV", "Tinggi(cm)", "Negara"]
    tabel_squad.add_rows(data_squad)
    print(tabel_squad)


def beli_pemain(data_club_masuk, data_club_keluar):
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
                print(f"{i+1}. {p[0]} (Rating: {p[1]}, Harga: €{p[3]})")

            idx_a = int(input("\nMasukkan nomor pemain: ")) - 1

            # Mencegah agar pemain pada lini club tidak habis
            if lini == "gk":
                if len(daftar) <= 1:
                    raise ValueError(
                        f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "df":
                if len(daftar) <= 4:
                    raise ValueError(
                        f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "mf":
                if len(daftar) <= 3:
                    raise ValueError(
                        f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "fw":
                if len(daftar) <= 3:
                    raise ValueError(
                        f"Jumlah pemain pada lini {lini} {club} tidak cukup")
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
            data_transfer.append([len(data_transfer) + 1, tampung_pemain[0], lini.upper(), tampung_pemain[1],
                                 tampung_pemain[2], tampung_pemain[3], tampung_pemain[4], tampung_pemain[5], club])

            # Harga beli (Market Value * 120%)
            harga_beli = daftar[idx_a][3] * 120 / 100
            data_club_masuk["saldo"] -= harga_beli

            input(
                f"\n✅ Pemain berhasil dibeli: {daftar[idx_a][0]} -> {club} di lini {lini}, sisa saldo club: €{data_club_masuk["saldo"]}.")
            del daftar[idx_a]
            break

        except Exception as e:
            print()
            input(f"({e})")
            continue


def jual_pemain(data_club):
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
                print(f"{i+1}. {p[0]} (Rating: {p[1]}, Harga: €{p[3]})")

            idx_a = int(input("\nMasukkan nomor pemain pertama: ")) - 1

            # Mencegah agar pemain pada lini club tidak habis
            if lini == "gk":
                if len(daftar) <= 1:
                    raise ValueError(
                        f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "df":
                if len(daftar) <= 4:
                    raise ValueError(
                        f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "mf":
                if len(daftar) <= 3:
                    raise ValueError(
                        f"Jumlah pemain pada lini {lini} {club} tidak cukup")
            elif lini == "fw":
                if len(daftar) <= 3:
                    raise ValueError(
                        f"Jumlah pemain pada lini {lini} {club} tidak cukup")

            if idx_a < 0:
                raise ValueError("Nomor pemain tidak tersedia")

            # tambah pemain ke club random
            pilih_club = [data_barcelona, data_madrid,
                          data_arsenal, data_psg, data_dortmund]
            pilih_club.remove(data_club)
            club_keluar = random.choice(pilih_club)
            club_keluar[lini].append(daftar[idx_a])

            if club_keluar == data_barcelona:
                nama_club_keluar = "Barcelona"
            elif club_keluar == data_madrid:
                nama_club_keluar = "Real Madrid"
            elif club_keluar == data_arsenal:
                nama_club_keluar = "Arsenal"
            elif club_keluar == data_psg:
                nama_club_keluar = "PSG"
            elif club_keluar == data_dortmund:
                nama_club_keluar = "Borussia Dormunt"

            # Harga jual (Market Value * 80%)
            harga_jual = daftar[idx_a][3] * 80 / 100
            data_club["saldo"] += harga_jual

            input(
                f"\n✅ Posisi berhasil dijual: {daftar[idx_a][0]} -> {nama_club_keluar} di lini {lini}, sisa saldo club: €{data_club["saldo"]}.")

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

            input(
                f"\n✅ Posisi berhasil ditukar: {daftar[idx_b][0]} ⇄ {daftar[idx_a][0]} di lini {lini}.")
            break

        except Exception as e:
            print()
            input(f"({e})")
            continue


def saldoNyabarca():
    while True:
        data_barcelona["saldo"] += 1000
        time.sleep(1)


t1 = threading.Thread(target=saldoNyabarca, daemon=True)
t1.start()


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
    if data_pengguna["user_biasa"][user][1] == "Barcelona":
        club = "Barcelona"
        data_club_pengguna = data_barcelona.copy()
    # if data_pengguna["user_biasa"][user][1] == "madrid":
    #     data_club_pengguna = data_madrid.copy()
    # if data_pengguna["user_biasa"][user][1] == "arsenal":
    #     data_club_pengguna = data_arsenal.copy()
    # if data_pengguna["user_biasa"][user][1] == "psg":
    #     data_club_pengguna = data_psg.copy()
    # if data_pengguna["user_biasa"][user][1] == "dortmund":
    #     data_club_pengguna = data_dortmund.copy()

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
                ["[0]", "Keluar"]
            ])
            print(tabel_menu_admin)

            pilihan_2 = input("Pilih menu (1-6) = ").strip()

            if pilihan_2 == "1":
                data_waktu = dt.datetime.now()
                os.system("cls")
                print(
                    f"Daftar Line Up {club} ({data_waktu.strftime("%A")}, {data_waktu.day} - {data_waktu.month} - {data_waktu.year})\n")

                tampil_starting(data_barcelona)
                print()
                tampil_cadangan(data_barcelona)
                print()
                tabel_saldo = PrettyTable()
                tabel_saldo.field_names = ["Saldo Club"]
                tabel_saldo.add_row([
                    f"€{data_barcelona["saldo"]}"
                ])
                print(tabel_saldo)
                input("\n(Ketuk enter untuk kembali memilih menu)")

            elif pilihan_2 == "2":
                ganti_pemain(data_barcelona)
                # beli_pemain()

            elif pilihan_2 == "3":
                while True:
                    os.system("cls")
                    tampil_starting()
                    pemain_tukar, ulang_2 = ganti_pemain(
                        "gk_utama", "df_utama", "mf_utama", "fw_utama")
                    if ulang_2 == True:
                        break

                tampilan_ubah_pemain(
                    pemain_tukar, "mengganti pemain starting dengan")

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

                    pilihan_3 = input("Pilih menu (1-3) = ").strip()

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

                            pilihan_4 = input("Pilih menu (1-7) = ").strip()

                            if pilihan_4 == "1":
                                beli_pemain(data_barcelona, data_madrid)
                                break
                            elif pilihan_4 == "2":
                                beli_pemain(data_barcelona, data_arsenal)
                                break
                            elif pilihan_4 == "3":
                                beli_pemain(data_barcelona, data_psg)
                                break
                            elif pilihan_4 == "4":
                                beli_pemain(data_barcelona, data_dortmund)
                                break
                            elif pilihan_4 == "5":
                                beli_pemain(data_barcelona, data_gratisan)
                                break
                            elif pilihan_4 == "6":
                                beli_pemain(data_barcelona, data_pemuda)
                                break
                            elif pilihan_4 == "0":
                                break
                            else:
                                input(
                                    "\n(Input tidak valid, ketuk enter untuk kembali)")

                    elif pilihan_3 == "2":
                        jual_pemain(data_barcelona)

                    elif pilihan_3 == "0":
                        break

                    else:
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")

            elif pilihan_2 == "5":
                def buka_jendela_transfer(club):
                    os.system("cls")
                    asal = random.choice(
                        [c for c in clubs.keys() if c != club])
                    tujuan = random.choice([c for c in clubs.keys() if c not in [
                                           asal, club, "Pencari Bakat"]])

                    # Pilih posisi dan pemain secara acak
                    posisi = random.choice(["gk", "df", "mf", "fw"])
                    pemain_list = clubs[asal][posisi]
                    if not pemain_list:
                        return "Tidak ada pemain di posisi ini."

                    pemain = random.choice(pemain_list)
                    pemain_list.remove(pemain)  # Hapus dari klub asal
                    clubs[tujuan][posisi].append(
                        pemain)  # Tambah ke klub tujuan

                    # Tambahkan ke data transfer
                    data_transfer.append([f"{len(data_transfer) + 1}.", pemain[0], posisi.upper(
                    ), pemain[1], pemain[2], pemain[3], pemain[4], pemain[5], tujuan])

                    # Tampilkan data transfer
                    tabel_transfer = PrettyTable()
                    tabel_transfer.title = "DATA TRANSFER"
                    tabel_transfer.field_names = [
                        "NO.", "Nama Pemain", "Posisi", "Rating", "Umur", "MV", "Tinggi(cm)", "Negara", "Club Tujuan/Status"]
                    tabel_transfer.add_rows(data_transfer)
                    print(tabel_transfer)
                    input("\n(Ketuk enter untuk kembali memilih menu)")

                    # Tampilkan laporan transfer
                    # nama, rating, usia, harga, tinggi, negara = pemain
                    # print(f"🔁 Transfer: {nama}")
                    # print(f"   Dari: {asal}")
                    # print(f"   Ke: {tujuan}")
                    # print(f"   Posisi: {posisi.upper()}")
                    # print(f"   Harga: €{harga:,}")
                    #             # while True:
                    #             #     panggil_pemain, ulang_2 = hapus_pemain()
                    #             #     if ulang_2 == True:
                    #             #         break

                    #             # tampilan_ubah_pemain(panggil_pemain, "menghapus")

                buka_jendela_transfer(club)

            elif pilihan_2 == "0":
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
            ["[0]", "Keluar"]
        ])
        print(tabel_menu_user)

        pilihan_2 = input("Pilih menu (1-2) = ").strip()

        if pilihan_2 == "1":
            data_waktu = dt.datetime.now()
            os.system("cls")
            print(
                f"Daftar Line Up Timnas Indonesia ({data_waktu.strftime("%A")}, {data_waktu.day} - {data_waktu.month} - {data_waktu.year})\n")
            tampil_starting()
            print()
            tampil_cadangan()
            input("\n(Ketuk enter untuk kembali memilih menu)")

        elif pilihan_2 == "2":
            login_mod = False

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")

os.system("cls")
print(
    f"✨ Terima kasih atas waktunya, {user}. Sampai jumpa di lain kesempatan! Selamat tinggal. 👋")
