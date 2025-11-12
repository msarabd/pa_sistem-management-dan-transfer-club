# data_pengguna = {
#     "user_mod" : ["mod"],
#     "pw_mod" : ["admin123"],
#     "club_mod" : ["barcelona"],
#     "user_biasa" : ["mahdi", "rahman"],
#     "pw_biasa" : ["mahdi123", "rahman123"],
#     "club_biasa" : ["barcelona", "madrid"]
# }

data_pengguna =  {
    "user_biasa" : {
        "mahdi" : ["mahdi123", "barcelona"],
        "rahman" : ["rahman123", "madrid"]
        },
    "user_mod" : {
        "mbut" : ["mbut123", "barcelona"]
        }
}

data_pemain = {
    "gk_utama" : ["Marten Paes"],
    "df_utama" : ["Jay Idzes",
                  "Rizky Ridho",
                  "Justin Hubner", 
                  "Calvin Verdonk", 
                  "Kevin Diks"
                  ],
    "mf_utama" : ["Thom Haye",
                  "Joel Pelupessy", 
                  "Marselino"
                  ],
    "fw_utama" : ["Rafael Struick",
                  "Ole Romeny"
                  ],
    "gk_cadangan" : ["Emil Audero",
                     "Nadeo Argawinata"
                     ],
    "df_cadangan" : ["Mees Hilgers",
                     "Sandy Walsh",
                     "Yakob Sayuri",
                     "Yance Sayuri",
                     "Justin Hubner"
                     ],
    "mf_cadangan" : ["Ivar Jenner",
                     "Ricky Kambuaya"
                     ],
    "fw_cadangan" : ["Ragnar Oratmangoen",
                     "Miliano Jonathans",
                     "Egy Maulana Vikry"
                     ],
}

semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
cek_pemain = set(semua_pemain)

data_club_pengguna = None

data_barcelona = {
    "gk": [
        # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ["Marc-André ter Stegen", 6.8, 33, 8400000, 187, "Jerman"],
        ["Joan García", 7.4, 24, 26000000, 192, "Spanyol"],
        ["Adel Aller", 6.8, 18, 53000, 194, "Spanyol"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ["Alejandro Balde", 6.8, 22, 66000000, 175, "Spanyol"],
        ["Pau Cubarsí", 6.8, 18, 75000000, 184, "Spanyol"],
        ["Ronald Araújo", 6.9, 26, 38000000, 188, "Uruguay"],
        ["Jules Koundé", 7.0, 27, 69000000, 181, "Prancis"],
        ["Xavi Espart", 6.5, 18, 320000, 175, "Spanyol"],
        ["Gerard Martin", 6.9, 23, 10900000, 186, "Spanyol"]
    ],
    "mf": [ # Midfield/Gelandang
        ["Pablo Gavi", 7.0, 21, 41000000, 173, "Spanyol"],
        ["Pedri", 7.6, 22, 153000000, 174, "Spanyol"],
        ["Dani Olmo", 7.0, 27, 58000000, 179, "Spanyol"],
        ["Fermín López", 7.1, 22, 62000000, 174, "Spanyol"],
        ["Frenkie de Jong", 7.1, 28, 42000000, 180, "Belanda"],
        ["Marc Casadó", 6.9, 21, 29000000, 177, "Spanyol"],
        ["Dro Fernandez", 6.6, 17, 4900000, 178, "Spanyol"],
        ["Roony Bardghji", 6.8, 19, 10300000, 177, "Denmark"]
    ],
    "fw": [ # Forward/Penyerang
        ["Marcus Rashford", 7.1, 28, 38000000, 185, "Inggris"],
        ["Robert Lewandowski", 6.9, 37, 9400000, 185, "Polandia"],
        ["Lamine Yamal", 7.8, 18, 215000000, 180, "Spanyol"],
        ["Raphinha", 7.6, 28, 81000000, 176, "Brasil"],
        ["Ferran Torres", 7.0, 25, 54000000, 184, "Spanyol"],
    ],
    "saldo": 120000000
}

data_realmadrid = {
    "gk": [
        # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ['Thibaut Courtois', 7.1, 33, 19400000, 200, "Belgia"],
        ['Andriy Lunin', 7.0, 26, 16900000, 191, "Ukraina"],
        ['Fran Gonzales', 7.0, 20, 910000, 199, "Spanyol"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ["Antonio Rüdiger", 6.8, 32, 15500000, 190, "Jerman"],
        ["Dani Carvajal", 6.7, 33, 7700000, 173, "Spanyol"],
        ["Dean Huijsen", 7.3, 20, 77000000, 195, "Belanda/Spanyol"],
        ["Éder Militão", 7.4, 27, 31000000, 186, "Brasil"],
        ["Trent Alexander-Arnold", 7.1, 27, 77000000, 180, "Inggris"]
    ],
    "mf": [ # Midfield/Gelandang
        ["Jude Bellingham", 7.4, 22, 170000000, 186, "Inggris"],
        ["Arda Güler", 7.8, 20, 58000000, 176, "Turki"],
        ["Federico Valverde", 7.3, 27, 126000000, 182, "Uruguay"],
        ["Brahim Díaz", 6.9, 26, 42000000, 171, "Spanyol"],
        ["Eduardo Camavinga", 7.0, 22, 48000000, 182, "Prancis"],
        ["Aurélien Tchouaméni", 7.2, 25, 78000000, 187, "Prancis"],
        ["Dani Ceballos", 7.0, 29, 8400000, 179, "Spanyol"],
        ["Mario Martín", 6.7, 20, 3200000, 180, "Spanyol"],

    ],
    "fw": [ # Forward/Penyerang
        ["Kylian Mbappé", 7.8, 26, 191000000, 178, "Prancis"],
        ["Vinícius Júnior", 7.2, 25, 156000000, 176, "Brasil"],
        ["Rodrygo", 7.2, 24, 85000000, 174, "Brasil"],
        ["Endrick", 6.7, 19, 37000000, 173, "Brasil"],
        ["Gonzalo Garcia", 7.0, 21, 15500000, 182, "Spanyol"],
        ["Franco Mastantuono", 7.1, 18, 49000000, 177, "Argentina"]
    ]
}
