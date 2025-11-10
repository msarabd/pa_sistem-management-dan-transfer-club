data_pengguna =  {
    "user_biasa" : {
        "mahdi" : ["mahdi123", "barcelona"],
        "rahman" : ["rahman123", "madrid"]
        },
    "user_mod" : {
        "mbut" : ["mbut123", "barcelona"]
        }
}

print(len(data_pengguna["user_biasa"]))
print(data_pengguna["user_biasa"]["mahdi"])
data_pengguna["user_biasa"]["reja"] = ["reja123"]
print(data_pengguna)

import time

teks = """Admin : "Selamat datang di [Nama Klub], Manajer. Kami telah melakukan investasi besar pada fasilitas dan skuad ini, dan kami mengharapkan imbalan instan. Kontrak Anda mencerminkan kepercayaan kami pada track record Anda. Target kami jelas dan tidak bisa ditawar:
> Domestik: Juara Liga dan memenangkan setidaknya satu kompetisi piala.
> Eropa: Mencapai Babak Semifinal (atau lebih tinggi) Liga Champions.
Kami akan memberikan Anda dukungan finansial, namun kegagalan tidak akan ditoleransi. Perlihatkan kepada kami bahwa kami telah membuat keputusan yang tepat."
"""
kecepatan_ketik = 0.05  # Jeda waktu antar karakter (dalam detik)

for karakter in teks:
    print(karakter, end='', flush=True)
    time.sleep(kecepatan_ketik)

print() # Tambahkan baris baru di akhir