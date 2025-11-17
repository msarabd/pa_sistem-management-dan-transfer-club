import climage
from data import data_barcelona
from prettytable import PrettyTable
import os

def keuangan_club(club, data_club):
    os.system("cls")

    if club == "Barcelona":
        gambar_stadion = climage.convert("d:/prototype-pa/static/stadion_barcelona.jpg")
        print(gambar_stadion)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        gambar_jersey = climage.convert("d:/prototype-pa/static/jersey_barcelona.png")
        print(gambar_jersey)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        tabel_saldo = PrettyTable()
        tabel_saldo.field_names = ["Saldo Club"]
        tabel_saldo.add_row([
            f"€{data_barcelona["saldo"]:,}"
            ])
        print(tabel_saldo)
    
    elif club == "Real Madrid":
        gambar_stadion = climage.convert("d:/prototype-pa/static/barcelona.jpg")
        print(gambar_stadion)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        gambar_jersey = climage.convert("d:/prototype-pa/static/barcelona_home_kit-removebg-preview.png")
        print(gambar_jersey)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        tabel_saldo = PrettyTable()
        tabel_saldo.field_names = ["Saldo Club"]
        tabel_saldo.add_row([
            f"€{data_barcelona["saldo"]:,}"
            ])
        print(tabel_saldo)

    elif club == "Arsenal":
        gambar_stadion = climage.convert("d:/prototype-pa/static/barcelona.jpg")
        print(gambar_stadion)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        gambar_jersey = climage.convert("d:/prototype-pa/static/barcelona_home_kit-removebg-preview.png")
        print(gambar_jersey)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        tabel_saldo = PrettyTable()
        tabel_saldo.field_names = ["Saldo Club"]
        tabel_saldo.add_row([
            f"€{data_barcelona["saldo"]:,}"
            ])
        print(tabel_saldo)

    elif club == "PSG":
        gambar_stadion = climage.convert("d:/prototype-pa/static/barcelona.jpg")
        print(gambar_stadion)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        gambar_jersey = climage.convert("d:/prototype-pa/static/barcelona_home_kit-removebg-preview.png")
        print(gambar_jersey)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        tabel_saldo = PrettyTable()
        tabel_saldo.field_names = ["Saldo Club"]
        tabel_saldo.add_row([
            f"€{data_barcelona["saldo"]:,}"
            ])
        print(tabel_saldo)

    elif club == "Borussia Dortmund":
        gambar_stadion = climage.convert("d:/prototype-pa/static/barcelona.jpg")
        print(gambar_stadion)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        gambar_jersey = climage.convert("d:/prototype-pa/static/barcelona_home_kit-removebg-preview.png")
        print(gambar_jersey)
        print(F"Pendapatan stadion = +€{data_barcelona["saldo"]:,}\n")

        tabel_saldo = PrettyTable()
        tabel_saldo.field_names = ["Saldo Club"]
        tabel_saldo.add_row([
            f"€{data_barcelona["saldo"]:,}"
            ])
        print(tabel_saldo)

keuangan_club("Barcelona", data_barcelona)