from data import data_pemain, cek_pemain, semua_pemain
from prettytable import PrettyTable
import os

def tampil_starting():
    data_starting = []
    for i in range(len(data_pemain["gk_utama"])):
        nomor = i + 1
        pemain_starting = data_pemain["gk_utama"][i]
        data_starting.append([f"{nomor}.", pemain_starting, "GK"])
    for i in range(len(data_pemain["df_utama"])):
        nomor = i + 2
        pemain_starting = data_pemain["df_utama"][i]
        data_starting.append([f"{nomor}.", pemain_starting, "DF"])
    for i in range(len(data_pemain["mf_utama"])):
        nomor = i + 7
        pemain_starting = data_pemain["mf_utama"][i]
        data_starting.append([f"{nomor}.", pemain_starting, "MF"])
    for i in range(len(data_pemain["fw_utama"])):
        nomor = i + 10
        pemain_starting = data_pemain["fw_utama"][i]
        data_starting.append([f"{nomor}.", pemain_starting, "FW"])
    
    tabel_starting = PrettyTable()
    tabel_starting.title = "STARTING"
    tabel_starting.field_names = ["NO.", "Nama Pemain", "Posisi"]
    tabel_starting.add_rows(data_starting)
    print(tabel_starting)

def tampil_cadangan():
    data_cadangan = []
    for i in range(len(data_pemain["gk_cadangan"])):
        nomor = i + 1
        pemain_cadangan = data_pemain["gk_cadangan"][i]
        data_cadangan.append([f"{nomor}.", pemain_cadangan, "GK"])
    for i in range(len(data_pemain["df_cadangan"])):
        nomor = i + 1 + len(data_pemain["gk_cadangan"])
        pemain_cadangan = data_pemain["df_cadangan"][i]
        data_cadangan.append([f"{nomor}.", pemain_cadangan, "DF"])
    for i in range(len(data_pemain["mf_cadangan"])):
        nomor = i + 1 + len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"])
        pemain_cadangan = data_pemain["mf_cadangan"][i]
        data_cadangan.append([f"{nomor}.", pemain_cadangan, "MF"])
    for i in range(len(data_pemain["fw_cadangan"])):
        nomor = i + 1 + len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"])
        pemain_cadangan = data_pemain["fw_cadangan"][i]
        data_cadangan.append([f"{nomor}.", pemain_cadangan, "FW"])

    tabel_cadangan = PrettyTable()
    tabel_cadangan.title = "CADANGAN"
    tabel_cadangan.field_names = ["NO.", "Nama Pemain", "Posisi"]
    tabel_cadangan.add_rows(data_cadangan)
    print(tabel_cadangan)

def tambah_pemain():
    global data_pemain
    global semua_pemain
    global cek_pemain
    
    os.system("cls")
    tampil_starting()
    print()
    tampil_cadangan()
    try:
        pemain_tambahan = input("\nMasukkan nama pemain = ").strip()

        if pemain_tambahan == "":
            raise ValueError("\n(Masukkan karakter, ketuk enter untuk kembali)")
        elif pemain_tambahan in cek_pemain:
            raise ValueError("\n(Pemain sudah ada di line up, ketuk enter untuk menambah kembali)") # butuh perbaikan ini

        pilihan_3 = input("Pilih lini yang ingin ditambah (GK/DF/MF/FW) = ").strip().upper()
        if pilihan_3 == "GK":
            data_pemain["gk_cadangan"].append(pemain_tambahan)
        elif pilihan_3 == "DF":
            data_pemain["df_cadangan"].append(pemain_tambahan)
        elif pilihan_3 == "MF":
            data_pemain["mf_cadangan"].append(pemain_tambahan)
        elif pilihan_3 == "FW":
            data_pemain["fw_cadangan"].append(pemain_tambahan) 
        else:
            raise ValueError("\n(Input tidak valid, ketuk enter untuk kembali)")
    
    except Exception as e:
        input(e)
        return tambah_pemain()

    print(f"(Sukses menambahkan {pemain_tambahan} ke dalam lini {pilihan_3})")
    input("\n(Ketuk enter untuk kembali memilih menu)")
    semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
    cek_pemain = set(semua_pemain)

def ganti_pemain(gk_status, df_status, mf_status, fw_status):
    global pemain_tukar
    global data_pemain
    global ulang_2

    ulang_2 = False
    pemain_tukar = None

    try:
        pemain_tukar = input("\nMasukkan nama pemain = ").strip()

        if pemain_tukar == "":
            raise ValueError("\n(Masukkan karakter, ketuk enter untuk kembali)")
        elif pemain_tukar in cek_pemain:
            raise ValueError("\n(Pemain sudah ada di line up, ketuk enter untuk menambah kembali)")

        pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
        if pilihan_3 == "GK":
            for i in range(len(data_pemain[gk_status])):
                print(f"    {i+1}. {data_pemain[gk_status][i]} (GK)")
            pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_diganti = int(pemain) - 1
            if pemain_diganti > len(data_pemain[gk_status]) - 1 or pemain_diganti < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                data_pemain[gk_status][pemain_diganti] = pemain_tukar
                ulang_2 = True
                return pemain_tukar, ulang_2
        elif pilihan_3 == "DF":
            for i in range(len(data_pemain[df_status])):
                print(f"    {i+1}. {data_pemain[df_status][i]} (DF)")
            pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_diganti = int(pemain) - 1
            if pemain_diganti > len(data_pemain[df_status]) - 1 or pemain_diganti < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                data_pemain[df_status][pemain_diganti] = pemain_tukar
                ulang_2 = True
                return pemain_tukar, ulang_2
        elif pilihan_3 == "MF":
            for i in range(len(data_pemain[mf_status])):
                print(f"    {i+1}. {data_pemain[mf_status][i]} (MF)")
            pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_diganti = int(pemain) - 1
            if pemain_diganti > len(data_pemain[mf_status]) - 1 or pemain_diganti < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                data_pemain[mf_status][pemain_diganti] = pemain_tukar
                ulang_2 = True
                return pemain_tukar, ulang_2
        elif pilihan_3 == "FW":
            for i in range(len(data_pemain[fw_status])):
                print(f"    {i+1}. {data_pemain[fw_status][i]} (FW)")
            pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_diganti = int(pemain) - 1
            if pemain_diganti > len(data_pemain[fw_status]) - 1 or pemain_diganti < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                data_pemain[fw_status][pemain_diganti] = pemain_tukar
                ulang_2 = True
                return pemain_tukar, ulang_2
        else:
            raise ValueError("\n(Input tidak valid, ketuk enter untuk kembali)")
    
    except Exception as e:
        input(e)
        return pemain_tukar, ulang_2
    
def hapus_pemain():
    global data_pemain
    global ulang_2
    global panggil_pemain

    ulang_2 = False
    panggil_pemain = None
    
    os.system("cls")
    tampil_cadangan()
    try:
        pilihan_3 = input("\nPilih lini yang ingin dihapus (GK/DF/MF/FW) = ").strip().upper()

        if pilihan_3 == "GK":
            for i in range(len(data_pemain["gk_cadangan"])):
                print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
            pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_dihapus = int(pemain) -1 
            if pemain_dihapus > len(data_pemain["gk_cadangan"]) -1 or pemain_dihapus < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                panggil_pemain = data_pemain["gk_cadangan"][pemain_dihapus]
                del data_pemain["gk_cadangan"][pemain_dihapus]
                ulang_2 = True
                return panggil_pemain, ulang_2 
        elif pilihan_3 == "DF":
            for i in range(len(data_pemain["df_cadangan"])):
                print(f"    {i+1}. {data_pemain["df_cadangan"][i]} DF)")
            pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_dihapus = int(pemain) -1
            if pemain_dihapus > len(data_pemain["df_cadangan"]) -1 or pemain_dihapus < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                panggil_pemain = data_pemain["df_cadangan"][pemain_dihapus]
                del data_pemain["df_cadangan"][pemain_dihapus]
                ulang_2 = True
                return panggil_pemain, ulang_2
        elif pilihan_3 == "MF":
            for i in range(len(data_pemain["mf_cadangan"])):
                print(f"    {i+1}. {data_pemain["mf_cadangan"][i]} (MF)")
            pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_dihapus = int(pemain) -1
            if pemain_dihapus > len(data_pemain["mf_cadangan"]) -1 or pemain_dihapus < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                panggil_pemain = data_pemain["mf_cadangan"][pemain_dihapus]
                del data_pemain["mf_cadangan"][pemain_dihapus]
                ulang_2 = True
                return panggil_pemain, ulang_2
        elif pilihan_3 == "FW":
            for i in range(len(data_pemain["fw_cadangan"])):
                print(f"    {i+1}. {data_pemain["fw_cadangan"][i]} (FW)")
            pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_dihapus = int(pemain) -1
            if pemain_dihapus > len(data_pemain["fw_cadangan"]) -1 or pemain_dihapus < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                panggil_pemain = data_pemain["fw_cadangan"][pemain_dihapus]
                del data_pemain["fw_cadangan"][pemain_dihapus]
                ulang_2 = True
                return panggil_pemain, ulang_2 
        else:
            raise ValueError("\n(Input tidak valid, ketuk enter untuk kembali)")
    
    except Exception as e:
        input(e)
        return panggil_pemain, ulang_2

def tampilan_ubah_pemain(par_pemain, pesan):
    global semua_pemain
    global cek_pemain

    print(f"(Sukses {pesan} {par_pemain})")
    input("\n(Ketuk enter untuk kembali memilih menu)")
    semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
    cek_pemain = set(semua_pemain)