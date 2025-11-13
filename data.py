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

data_madrid = {
    "gk": [
        # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ['Thibaut Courtois', 7.1, 33, 19400000, 200, "Belgia"],
        ['Andriy Lunin', 7.0, 26, 16900000, 191, "Ukraina"],
        ['Fran Gonzales', 7.0, 20, 910000, 199, "Spanyol"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ["Aurélien Tchouaméni", 7.2, 25, 78000000, 187, "Prancis"],
        ["Antonio Rüdiger", 6.8, 32, 15500000, 190, "Jerman"],
        ["Dean Huijsen", 7.3, 20, 77000000, 195, "Spanyol"],
        ["Trent Alexander-Arnold", 7.1, 27, 77000000, 180, "Inggris"],
        ["Éder Militão", 7.4, 27, 31000000, 186, "Brasil"],
        ["Dani Carvajal", 6.7, 33, 7700000, 173, "Spanyol"],
    ],
    "mf": [ # Midfield/Gelandang
        ["Jude Bellingham", 7.4, 22, 170000000, 186, "Inggris"],
        ["Arda Güler", 7.8, 20, 58000000, 176, "Turki"],
        ["Federico Valverde", 7.3, 27, 126000000, 182, "Uruguay"],
        ["Brahim Díaz", 6.9, 26, 42000000, 171, "Spanyol"],
        ["Eduardo Camavinga", 7.0, 22, 48000000, 182, "Prancis"],
        ["Dani Ceballos", 7.0, 29, 8400000, 179, "Spanyol"],
        ["Mario Martín", 6.7, 20, 3200000, 180, "Spanyol"]
    ],
    "fw": [ # Forward/Penyerang
        ["Vinícius Júnior", 7.2, 25, 156000000, 176, "Brasil"],
        ["Kylian Mbappé", 7.8, 26, 191000000, 178, "Prancis"],
        ["Rodrygo", 7.2, 24, 85000000, 174, "Brasil"],
        ["Endrick", 6.7, 19, 37000000, 173, "Brasil"],
        ["Gonzalo Garcia", 7.0, 21, 15500000, 182, "Spanyol"],
        ["Franco Mastantuono", 7.1, 18, 49000000, 177, "Argentina"]
    ]
}

data_arsenal = {
    "gk": [
        # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ['Kepa Arrizabalaga', 7.1, 30, 8500000, 186, "Spanyol"],
        ['David Raya', 6.9, 30, 43000000, 183, "Spanyol"],
        ['Alexei Rojas', 7.0, 20, 225000, 156, "Columbia"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ['Riccardo Calafiori', 7.0, 23, 39000000, 188, "Italia"],
        ['William Saliba', 7.0, 24, 75000000, 192, "Prancis"],
        ['Gabriel Magalhães', 7.2, 27, 70000000, 190, "Brasil"],
        ['Ben White', 6.9, 28, 35000000, 185, "Inggris"],
        ['Piero Hincapié', 7.2, 23, 46000000, 184, "Ekuador"],
        ['Jurriën Timber', 7.0, 24, 63000000, 182, "Belanda"],
        ['Christian Mosquera', 6.9, 21, 33000000, 191, "Spanyol"]
    ],
    "mf": [ # Midfield/Gelandang
        ['Eberechi Eze', 7.2, 27, 50000000, 178, "Inggris"],
        ['Martin Ødegaard', 7.4, 26, 88000000, 178, "Norwegia"],
        ['Declan Rice', 7.4, 26, 114000000, 185, "Inggris"],
        ['Martín Zubimendi', 7.0, 26, 72000000, 180, "Spanyol"],
        ['Mikel Merino', 7.1, 29, 36000000, 188, "Spanyol"],
        ['Ethan Nwaneri', 6.8, 18, 44000000, 176, "Inggris"]
    ],
    "fw": [ # Forward/Penyerang
        ["Bukayo Saka", 7.3, 24, 140000000, 178, "Inggris"],
        ["Viktor Gyökeres", 7.3, 27, 60000000, 187, "Swedia"],
        ["Gabriel Jesus", 7.2, 28, 45000000, 175, "Brasil"],
        ["Kai Havertz", 7.0, 26, 60000000, 193, "Jerman"],
        ["Gabriel Martinelli", 6.9, 24, 70000000, 178, "Brasil"],
        ["Noni Madueke", 7.0, 23, 54000000, 182, "Inggris"]
    ]
}

data_psg = {
    "gk": [
        # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ['Lucas Chevaller', 7.0, 24, 41000000, 188, "Prancis"],
        ['Matvey Sofonov', 6.9, 26, 19000000, 191, "Rusia"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ['Nuno Mendes', 7.3, 23, 73000000, 176, "Portugal"],
        ['Marquinhos', 7.3, 31, 34000000, 183, "Brasil"],
        ['Lucas Beraldo', 7.1, 21, 23000000, 186, "Brasil"],
        ['Achraf Hakimi', 7.4, 27, 82000000, 181, "Maroko"],
        ['Lucas Hernández', 6.8, 29, 26000000, 182, "Prancis"],
        ['William Pacho', 6.9, 24, 61000000, 187, "Ekuador"],
        ['Ilya Zabarnyi', 6.9, 23, 51000000, 189, "Ukraina"],
        ['Noham Kamara', 7.0, 18, 960000, 183, "Prancis"]
    ],
    "mf": [ # Midfield/Gelandang
        ['Vitinha', 7.5, 25, 83000000, 172, "Portugal"],
        ['Kang in Lee', 7.12, 24, 27000000, 174, "Korea Selatan"],
        ['Fabián Ruiz', 7.3, 29, 39000000, 189, "Spanyol"],
        ['João Neves', 7.3, 21, 95000000, 174, "Portugal"],
        ['Senny Mayulu', 6.9, 19, 24000000, 183, "Prancis"],
    ],
    "fw": [ # Forward/Penyerang
        ["Khvicha Kvaratskhelia", 7.4, 24, 93000000, 183, "Georgia"],
        ["Ousmane Dembélé", 7.6, 28, 97000000, 178, "Prancis"],
        ["Désiré Doué", 7.4, 20, 93000000, 181, "Prancis"],
        ["Bradley Barcola", 7.1, 23, 68000000, 182, "Prancis"],
        ["Gonçalo Ramos", 6.90, 24, 37000000, 185, "Portugal"],
        ['Ibrahim Mbaye', 6.7, 17, 14600000, 175, "Senegal"],
        ['Quentin Ndjantou', 6.5, 18, 3200000, 182, "Prancis"]
    ]
}

data_dortmund = {
    "gk": [
        # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ['Gregor Kobel', 7.0, 27, 41000000, 195, "Swiss"],
        ['Alexander Meyer', 7.0, 34, 760000, 195, "Jerman"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ['Nico Schlotterbeck', 7.2, 26, 41000000, 191, "Jerman"],
        ['Ramy Bensebaini', 7.0, 30, 7400000, 187, "Aljazair"],
        ['Emre Can', 7.0, 31, 7500000, 186, "Jerman"],
        ['Yan Couto', 6.7, 23, 21000000, 168, "Brasil"],
        ['Niklas Süle', 6.8, 30, 7400000, 195, "Jerman"],
        ['Julian Ryerson', 7.0, 27, 18900000, 183, "Norwegia"],
        ['Waldemar Anton', 7.0, 29, 19700000, 189, "Jerman"],
        ['Aaron Anselmino', 7.0, 20, 8500000, 186, "Argentina"]
    ],
    "mf": [ # Midfield/Gelandang
        ['Daniel Svensson', 6.9, 23, 20000000, 183, "Swedia"],
        ['Carney Chukwuemeka', 6.8, 22, 18100000, 187, "Inggris"],
        ['Jobe Bellingham', 7.0, 20, 29000000, 188, "Inggris"],
        ['Julian Brandt', 7.0, 29, 26000000, 185, "Jerman"],
        ['Marcel Sabitzer', 7.0, 31, 8300000, 178, "Austria"],
        ['Pascal Groß', 7.0, 34, 4500000, 181, "Jerman"],
        ['Felix Nmecha', 7.0, 24, 34000000, 188, "Jerman"]
    ],
    "fw": [ # Forward/Penyerang
        ['Karim Adeyemi', 6.9, 23, 62000000, 177, "Jerman"],
        ['Serhou Guirassy', 7.1, 29, 41000000, 187, "Guinea"],
        ['Fábio Silva', 6.9, 23, 27000000, 185, "Portugal"],
        ['Maximilianian Beier', 6.8, 23, 32000000, 185, "Jerman"],
        ['Julien Duranville', 6.6, 19, 9200000, 170, "Belgia"]
    ]
}