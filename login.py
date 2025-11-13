import os
from data import data_pengguna, data_pemain, semua_pemain, cek_pemain, data_barcelona, data_club_pengguna
from prettytable import PrettyTable
import time

def input_biasa():
    global awal_1
    global login_biasa
    global user

    ulang_1 = False
    while not ulang_1:
        awal_1 = False
        os.system("cls")
        print("=== Login Sebagai User Biasa ===\n")
        
        try:
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

            if user == "" or pw == "":
                raise ValueError("\n(Masukkan karakter, tekan enter untuk login kembali)")
                
            for i in data_pengguna["user_biasa"]:
                if user == i and pw == data_pengguna["user_biasa"][i][0]:
                    input("\n(Login berhasil, ketuk enter untuk lanjut)")
                    login_biasa = True
                    ulang_1 = True
                    awal_1 = True
                    return user, login_biasa, awal_1
                elif user == i: 
                    awal_1 = True
                    raise ValueError("\n(Password salah, ketuk enter untuk kembali)")
                
            if awal_1 == False:
                raise ValueError("\n(User tidak ditemukan, ketuk enter untuk login kembali)")
        
        except Exception as e:
            input(e)
            continue

def input_mod():
    global user
    global login_mod
    global awal_1

    while True:
        os.system("cls")
        print("=== Login Sebagai User MOD ===\n")

        try:
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

            for i in data_pengguna["user_mod"]:
                if user != i or pw != data_pengguna["user_mod"][i][0]:
                    if user == "" or pw == "":
                        raise ValueError("\n(Masukkan karakter, ketuk enter untuk kembali)")
                    elif user == i:
                        raise ValueError("\n(Password salah, ketuk enter untuk kembali)")
                    elif pw == data_pengguna["user_mod"][i][0]:
                        raise ValueError("\n(Username salah, ketuk enter untuk kembali)")
                    else:
                        raise ValueError("\n(Username dan password salah, ketuk enter untuk kembali)")
    
        except Exception as e:
            input(e)
            continue
    
        input("\n(Login berhasil, ketuk enter untuk lanjut)")
        login_mod = True
        awal_1 = True
        return user, login_mod, awal_1

def input_register():
    global data_pengguna
    global user
    global login_biasa
    global awal_1
    
    while True:
        os.system("cls")
        print("=== Menu Register ===\n")

        try:
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

            if user == "" or pw == "":
                raise ValueError("\n(Masukkan karakter, ketuk enter untuk kembali)")
            elif user in data_pengguna["user_biasa"]:
                raise ValueError("\n(Pengguna sudah ada, harap ganti username Anda)")
        
        except Exception as e:
            input(e)
            continue

        data_pengguna["user_biasa"][user] = [pw]
        input("\n(Register berhasil, ketuk enter untuk memilih club)")
        break

    while True:
        os.system("cls")
        tabel_pil_club = PrettyTable()
        tabel_pil_club.title = "MAU PAKAI CLUB APA GANTENG?"
        tabel_pil_club.field_names = ["kiri", "kanan"]
        tabel_pil_club.header = False
        tabel_pil_club.add_rows([
            ["[1]", "Barcelona"],
            ["[2]", "Real Madrid"],
            ["[3]", "Arsenal"],
            ["[4]", "PSG"],
            ["[5]", "Borussia Dortmund"],
            ])
        print(tabel_pil_club)

        pilihan_4 = input("Pilih menu (1-5) = ").strip()

        if pilihan_4 == "1":
            data_pengguna["user_biasa"][user].append("barcelona")
            os.system("cls")
            teks = f"""
Management : "Selamat datang di Barcelona, {user}. Kontrak telah sah. Anda datang di era restrukturisasi, di mana keuangan adalah prioritas setara dengan trofi. Kami menuntut Anda memberikan 5 pemain muda (U-20) menit bermain signifikan untuk menjaga DNA klub. Sudah terlalu lama kami puasa Eropa; segera bawa pulang trofi internasional untuk mengembalikan kehormatan. Bekerja cerdas, dan jangan boros. Visca el Barça!"
"""
            kecepatan_ketik = 0.05  # Jeda waktu antar karakter (dalam detik)

            for karakter in teks:
                print(karakter, end='', flush=True)
                time.sleep(kecepatan_ketik)

            print()
            input("akhir")
            login_biasa = True
            awal_1 = True
            return user, login_biasa, awal_1

        elif pilihan_4 == "2":
            data_pengguna["user_biasa"][user].append("madrid")
            os.system("cls")
            teks = f"""
Management : "Selamat datang di Madrid, {user}. Tidak ada kata 'transisi' di sini, hanya dominasi. Anggaran tersedia: Anda harus membeli pemain bintang dengan market value tertinggi yang sesuai dengan standar klub. Tugas utama Anda adalah memberikan trofi internasional (UCL) setiap musim. Kegagalan di panggung Eropa tidak dapat diterima. Jadilah raja, dan rekrut raja. ¡Hala Madrid!"
"""
            kecepatan_ketik = 0.05

            for karakter in teks:
                print(karakter, end='', flush=True)
                time.sleep(kecepatan_ketik)

            print()
            input("akhir")
            login_biasa = True
            awal_1 = True
            return user, login_biasa, awal_1
        
        elif pilihan_4 == "3":
            data_pengguna["user_biasa"][user].append("arsenal")
            os.system("cls")
            teks = f"""
Management : "Selamat datang di London, {user}. Kami telah membangun fondasi yang kuat, kini saatnya meraih gelar. Perekrutan harus cerdas: Prioritaskan pembelian dari akademi atau hasil jaringan pencari bakat kami. Dan yang paling penting: Akhiri penantian kami di level domestik! Bawa pulang trofi domestik musim ini. Tunjukkan bahwa kecerdasan finansial dapat menghasilkan kesuksesan sejati."
"""
            kecepatan_ketik = 0.05

            for karakter in teks:
                print(karakter, end='', flush=True)
                time.sleep(kecepatan_ketik)

            print()
            input("akhir")
            login_biasa = True
            awal_1 = True
            return user, login_biasa, awal_1
        
        elif pilihan_4 == "4":
            data_pengguna["user_biasa"][user].append("psg")
            os.system("cls")
            teks = f"""
Management : "Selamat datang di Paris, {user}. Anda memiliki sumber daya yang melimpah. Tugas utama Anda: mempertahankan pemain bintang yang kami rekrut—mereka tidak untuk dijual. Dan satu-satunya ukuran di mata Pemilik adalah Eropa: Berikan trofi internasional (UCL) kedua. Liga domestik wajib menang; fokus total pada Liga Champions. Kegagalan akan dipertimbangkan. Ici c'est Paris!"
"""
            kecepatan_ketik = 0.05

            for karakter in teks:
                print(karakter, end='', flush=True)
                time.sleep(kecepatan_ketik)

            print()
            input("akhir")
            login_biasa = True
            awal_1 = True
            return user, login_biasa, awal_1
        
        elif pilihan_4 == "5":
            data_pengguna["user_biasa"][user].append("dortmund")
            os.system("cls")
            teks = f"""
Management : "Selamat datang di Dortmund, {user}. Kami adalah klub gairah dan bisnis cerdas. Model kami adalah pengembangan: Anda harus membeli pemain muda atau hasil pencari bakat dengan potensi tinggi. Visi finansial adalah kunci: Perbesar keuangan klub secara signifikan dari penjualan pemain. Kualifikasi UCL harus dipastikan, sambil menjaga filosofi tim yang menyerang dan menghasilkan keuntungan. Echte Liebe!"
"""
            kecepatan_ketik = 0.05

            for karakter in teks:
                print(karakter, end='', flush=True)
                time.sleep(kecepatan_ketik)

            print()
            input("akhir")
            login_biasa = True
            awal_1 = True
            return user, login_biasa, awal_1

