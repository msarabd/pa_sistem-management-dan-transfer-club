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
        "mahdi" : ["mahdi123", "Barcelona"],
        "rahman" : ["rahman123", "Real Madrid"]
        },
    "user_mod" : {
        "mbut" : ["mbut123", "Barcelona"]
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
    "saldo": -12000000,
    "stadion": 180000000,
    "jersey": 150000000
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
    ],
    "saldo": 150000000,
    "stadion": 180000000,
    "jersey": 150000000
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
    ],
    "saldo": 80000000,
    "stadion": 100000000,
    "jersey": 80000000
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
    ],
    "saldo": 200000000,
    "stadion": 80000000,
    "jersey": 80000000
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
        ['Emre Can', 8.0, 31, 7500000, 186, "Jerman"],
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
    ],
    "saldo": 30000000,
    "stadion": 60000000,
    "jersey": 30000000
}

data_nasr = {
    "gk": [ # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ["Nawaf Al-Qidi", 7.1, 25, 700000, 188, "Arab Saudi"],
        ["Raghed Al-Najjar", 7.2, 29, 160000, 185, "Arab Saudi"],
        ["Bento", 6.8, 26, 10600000, 190, "Brasil"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ["Nawaf Boushal", 7.0, 24, 1400000, 168, "Arab Saudi"],
        ["Iñigo Martínez", 7.1, 34, 5200000, 182, "Spanyol"],
        ["Mohamed Simakan", 7.0, 25, 2500000, 187, "Prancis"],
        ["Sultan Al-Ghannam", 7.0, 31, 2100000, 173, "Arab Saudi"],
        ["Salem Al-Najdi", 6.8, 22, 615000, 178, "Arab Saudi"]
    ],
    "mf": [# Midfield/Gelandang
        ["Marcelo Brozović", 7.3, 32, 9700000, 181, "Kroasia"],
        ["Angelo", 7.1, 20, 8600000, 182, "Brasil"],
        ["Abdullah Al-Khaibari", 6.8, 29, 815000, 177, "Arab Saudi"],
        ["Abdul Malik Al-Jabeer", 6.8, 21, 720000, 178, "Arab Saudi"],
        ["Ali Al Hassan", 6.8, 28, 570000, 183, "Arab Saudi"]
    ],
    "fw": [ # Forward/Penyerang
        ["Sadio Mané", 7.3, 33, 7500000, 174, "Senegal"],
        ["Cristiano Ronaldo", 7.5, 40, 12500000, 187, "Portugal"],
        ["João Félix", 7.3, 26, 19400000, 181, "Portugal"],
        ["Kingsley Coman", 7.1, 29, 32000000, 179, "Prancis"],
        ["Abdulrahman Ghareeb", 7.1, 28, 1400000, 163, "Arab Saudi"],
        ["Haroune Camara", 6.6, 27, 425000, 183, "Arab Saudi"],
        ["Ayman Yahya", 7.0, 24, 1200000, 165, "Arab Saudi"],
        ["Wesley", 6.8, 20, 4100000, 180, "Brasil"]
    ],
    "saldo": 300000000,
    "stadion": 3000000,
    "jersey": 5000000
}

data_miami = {
    "gk": [
        # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ["Rocco Ríos Novo", 6.9, 23, 515000, 178, "Argentina"],
        ["Óscar Ustari", 7.0, 39, 105000, 183, "Argentina"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ["Jordi Alba", 7.3, 36, 1600000, 170, "Spanyol"],
        ["Noah Allen", 6.8, 21, 1600000, 175, "USA"],
        ["Maximiliano Falcón", 6.7, 28, 1400000, 179, "Uruguay"],
        ["Ian Fray", 6.8, 23, 480000, 183, "USA"],
        ["Tomás Avilés", 6.7, 21, 4500000, 186, "Argentina"],
        ["Marcelo Weigandt", 6.7, 25, 2200000, 175, "Argentina"],
        ["Gonzalo Luján", 6.7, 24, 1800000, 182, "Argentina"],
        ["Ryan Sailor", 6.9, 26, 190000, 193, "USA"],
        ["Israel Boatwright", 6.4, 20, 52000, 180, "USA"],
        ["Tyler Hall", 6.6, 19, 110000, 178, "USA"]
    ],
    "mf": [ # Midfield/Gelandang
        ["Sergio Busquets", 7.2, 37, 1400000, 189, "Spanyol"],
        ["Rodrigo De Paul", 7.3, 31, 21000000, 180, "Argentina"],
        ["Telasco Segovia", 7.0, 22, 3300000, 180, "Venezuela"],
        ["Mateo Silvetti", 6.8, 19, 4800000, 175, "Argentina"],
        ["David Ruíz", 6.7, 21, 2300000, 181, "USA"]
    ],
    "fw": [ # Forward/Penyerang
        ["Luis Suárez", 7.4, 38, 1600000, 182, "Uruguay"],
        ["Allen Obando", 6.8, 19, 1600000, 189, "Ekuador"],
        ["Lionel Messi", 8.3, 38, 19600000, 170, "Argentina"],
        ["Tadeo Allende", 6.9, 26, 2900000, 185, "Argentina"],
        ["Fafà Picault", 6.8, 34, 480000, 173, "USA"]
    ],
    "saldo": 50000000,
    "stadion": 10000000,
    "jersey": 15000000
}

data_borneo = {
    "gk": [# Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara
        ["Nadeo Argawinata", 7.0, 28, 325000, 187, "Indonesia"],
        ["Syahrul Trisna", 7.3, 29, 155000, 183, "Indonesia"],
        ["Daffa Fasya", 6.8, 21, 82000, 185, "Indonesia"],
        ["Alfharezzi Buffon", 6.4, 19, 45000, 173, "Indonesia"]
    ],
    "df": [ # Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
        ["Mohammad Al-Husseini", 6.6, 22, 170000, 182, "Lebanon"],
        ["Christophe Nduwarugira", 7.0, 31, 280000, 185, "Burundi"],
        ["Komang Teguh", 6.7, 23, 165000, 177, "Indonesia"],
        ["Muhammad Faturrahman", 6.9, 23, 300000, 170, "Indonesia"],
        ["Westherley Garcia Nogueira", 6.9, 28, 80000, 180, "Brasil"]
    ],
    "mf": [ # Midfield/Gelandang
        ["Kei Hirose", 6.7, 29, 365000, 178, "Jepang"],
        ["Rivaldo Pakpahan", 6.8, 22, 130000, 172, "Indonesia"],
        ["Juan Felipe Villa", 7.4, 26, 430000, 175, "Kolombia"],
        ["Ikhsan Nul Zikrak", 6.6, 23, 73000, 176, "Indonesia"],
        ["Ahmad Agung", 6.5, 29, 73000, 180, "Indonesia"],
        ["Dwiky Herdiansyah", 6.5, 21, 49000, 181, "Indonesia"]
    ],
    "fw": [ # Forward/Penyerang
        ["Mariano Peralta Bauer", 8.1, 27, 410000, 177, "Argentina"],
        ["Muhammad Sihran", 6.8, 26, 185000, 171, "Indonesia"],
        ["Joel Vinícius Silva Don Anjos", 7.1, 30, 80000, 182, "Brasil"],
        ["Maicon de Souza da Silva", 6.8, 29, 185000, 180, "Brasil"],
        ["Douglas Coutinho", 6.8, 31, 180000, 180, "Brasil"],
        ["Habibi Jusuf", 6.7, 27, 97000, 179, "Indonesia"]
    ],
    "saldo": 5000000,
    "stadion": 2000000,
    "jersey": 500000
}

data_gratisan = {
    'gk': [
        ["Gianluigi Donnarumma", 7.0, 26, 0, 196, "Italia", "Manchester City"],
        ["David de Gea", 7.0, 35, 0, 192, "Spanyol", "Fiorentina"],
        ["Alisson Becker", 7.5, 33, 0, 191, "Brasil", "Liverpool"],
        ["Ederson Moraes", 7.4, 32, 0, 188, "Brasil", "Manchester City"],
        ["Jan Oblak", 7.2, 33, 0, 188, "Slovenia", "Atlético Madrid"],
        ["Mike Maignan", 7.1, 29, 0, 191, "Prancis", "AC Milan"]
    ],
    'df': [
        ["Raphaël Varane", 6.6, 32, 0, 191, "Prancis", "Manchester United"],
        ["Virgil van Dijk", 7.3, 34, 0, 195, "Belanda", "Liverpool"],
        ["Matthijs de Ligt", 6.9, 26, 0, 189, "Belanda", "Manchester United"],
        ["Rúben Dias", 7.5, 28, 0, 186, "Portugal", "Manchester City"],
        ["Achraf Hakimi", 7.2, 27, 0, 181, "Maroko", "Inter Milan"],
        ["João Cancelo", 7.1, 31, 0, 182, "Portugal", "Bayern München"],
        ["Andrew Robertson", 7.0, 31, 0, 178, "Skotlandia", "Liverpool"],
        ["Trent Alexander-Arnold", 7.1, 27, 0, 180, "Inggris", "Liverpool"],
        ["Theo Hernández", 7.0, 28, 0, 184, "Prancis", "AC Milan"],
        ["Milan Škriniar", 6.8, 30, 0, 187, "Slowakia", "Inter Milan"],
        ["Kalidou Koulibaly", 6.7, 34, 0, 187, "Senegal", "Chelsea"],
        ["Stefan de Vrij", 6.8, 33, 0, 189, "Belanda", "Inter Milan"]
    ],
    'mf': [
        ["Neymar ", 7.3, 33, 0, 175, "Brasil", "Santos"],
        ["Kevin De Bruyne", 7.4, 34, 0, 181, "Belgia", "SSC Napoli"],
        ["Luka Modrić", 7.3, 40, 0, 172, "Kroasia", "AC Milan"],
        ["Toni Kroos", 7.7, 35, 0, 183, "Jerman", "Real Madrid"],
        ["Joshua Kimmich", 7.6, 30, 0, 177, "Jerman", "Bayern München"],
        ["Rodri Hernández", 7.5, 29, 0, 191, "Spanyol", "Manchester City"],
        ["Bruno Fernandes", 7.4, 31, 0, 179, "Portugal", "Manchester United"],
        ["Casemiro", 7.3, 33, 0, 185, "Brasil", "Manchester United"],
        ["Nicolò Barella", 7.2, 28, 0, 172, "Italia", "Inter Milan"],
        ["Sergej Milinković-Savić", 7.0, 30, 0, 191, "Serbia", "Lazio"],
        ["Fabinho", 6.9, 32, 0, 188, "Brasil", "Liverpool"],
        ["Declan Rice", 7.0, 26, 0, 185, "Inggris", "West Ham United"],
        ["Manuel Locatelli", 6.8, 27, 0, 186, "Italia", "Juventus"]
    ],
    'fw': [
        ["Julián Álvarez", 7.3, 25, 0, 170, "Argentina", "Atlético Madrid"],
        ["Alejandro Garnacho", 6.9, 21, 0, 180, "Argentina", "Chelsea"],
        ["Erling Haaland", 7.7, 25, 0, 194, "Norwegia", "Manchester City"],
        ["Mohamed Salah", 7.6, 33, 0, 175, "Mesir", "Liverpool"],
        ["Harry Kane", 7.5, 32, 0, 188, "Inggris", "Bayern München"],
        ["Heung-min Son", 7.4, 33, 0, 183, "Korea Selatan", "Tottenham Hotspur"],
        ["Victor Osimhen", 7.3, 26, 0, 186, "Nigeria", "SSC Napoli"],
        ["Rafael Leão", 7.2, 26, 0, 188, "Portugal", "AC Milan"],
        ["Lautaro Martínez", 7.1, 28, 0, 174, "Argentina", "Inter Milan"],
        ["Khvicha Kvaratskhelia", 7.2, 24, 0, 183, "Georgia", "SSC Napoli"],
        ["Marcus Rashford", 7.0, 28, 0, 185, "Inggris", "Manchester United"],
        ["Jack Grealish", 6.9, 30, 0, 180, "Inggris", "Manchester City"],
        ["Dusan Vlahović", 7.0, 25, 0, 190, "Serbia", "Juventus"],
        ["Phil Foden", 7.3, 25, 0, 171, "Inggris", "Manchester City"],
        ["Kingsley Coman", 7.1, 29, 0, 181, "Prancis", "Bayern München"]
    ]
}

data_pemuda = {
    'gk' : [ # Nama, Rating, Usia, Nilai Transfer (€), Tinggi (cm), Negara, KLub
         ["Guillaume Restes", 6.6, 20, 0, 187, "Prancis", "Toulouse"],
         ["Dennis Seimen", 7.2, 19, 0, 190, "Jerman", "VfB Stuttgart"],
         ["Gavin Beavers", 6.5, 19, 0, 193, "USA", "Real Salt Lake"],
         ["Tomáš Vašásek", 6.4, 18, 0, 190, "Republik Ceko.", "SK Slavia Prague"],
         ["Kasper Møller", 6.3, 17, 0, 189, "Denmark", " Midtjylland"],
         ["Federico Magro", 6.4, 18, 0, 195, "Italia", "Lazio Primavera"],
         ["André Gomes", 6.5, 18, 0, 190, "Portugal", "SL Benfica"]
    ],
    'df' : [# Centre-Back/Pemain Belakang (Saya menggunakan "cb" untuk seluruh pemain Back)
         ["Luka Vušković", 7.4, 18, 0, 193, "Kroasia", "Tottenham Hotspur"],
         ["Rico Lewis", 6.8, 20, 0, 170, "Inggris", "Manchester City"],
         ["António Silva", 7.1, 22, 0, 187, "Portugal", "SL Benfica"],
         ["Mosquera", 6.8, 19, 0, 181, "Spanyol", "Valencia"],
         ["Sael Kumbedi", 6.7, 20, 0, 178, "Prancis", "Olympique Lyonnais"],
         ["Piero Hincapié", 7.0, 22, 0, 184, "Ekuador", "Bayer Leverkusen"],
         ["Nestory Irankunda", 6.5, 18, 0, 173, "Australia", "Adelaide United"],
         ["Noel Buck", 6.7, 19, 0, 183, "USA", "New England Revolution"],
         ["Silas Ostrzinski", 6.4, 18, 0, 186, "Jerman", "Hertha Berlin"],
         ["Diogo Monteiro", 6.4, 19, 0, 187, "Portugal", "Leeds United"]
    ],
    'mf' : [# Midfield/Gelandang
         ["Kendry Páez", 6.7, 18, 0, 177, "Ekuador", "Chelsea"],
         ["Ethan Nwaneri", 6.8, 18, 0, 178, "Inggris", "Arsenal"],
         ["Assan Ouédraogo", 7.0, 19, 0, 191, "Jerman", "Schalke 04"],
         ["Eliot Matazo", 6.9, 21, 0, 174, "Belgia", "AS Monaco"],
         ["Kacper Urbański", 6.6, 19, 0, 180, "Polandia", "Bologna"],
         ["Nassim Boujellab", 6.8, 20, 0, 175, "Maroko", "Schalke 04 II"],
         ["Jamal Musiala", 7.4, 22, 0, 184, "Jerman", "Bayern München"],
         ["Florian Wirtz", 7.1, 22, 0, 176, "Jerman", "Liverpool"],
         ["Gabriel Pirani", 6.7, 21, 0, 174, "Brasil", "DC United"],
         ["Lesley Ugochukwu", 6.8, 20, 0, 191, "Prancis", "Chelsea"],
         ["Chaka Traorè", 6.6, 19, 0, 174, "Republik Pantai Gading", "AC Milan"],
         ["Oliver Tipton", 6.3, 18, 0, 182, "Inggris", "Stoke City"],
         ["Gianluca Prestianni", 6.8, 18, 0, 167, "Argentina", "SL Benfica"],
         ["Dário Essugo", 6.7, 19, 0, 178, "Portugal", "Sporting CP"]
    ],
    'fw' : [# Forward/Penyerang
         ["Francesco Camarda", 6.7, 17, 0, 184, "Italia", "AC Milan"],
         ["Estêvão", 7.1, 18, 0, 176, "Brasil", "Chelsea"],
         ["Guido Della Rovere", 6.5, 18, 0, 175, "Italia", "ChievoVerona"],
         ["Mathys Tel", 6.7, 20, 0, 183, "Prancis", "Bayern München"],
         ["Leo Sauer", 6.7, 19, 0, 177, "Slowakia", "Feyenoord"],
         ["Mikey Moore", 6.6, 18, 0, 182, "Inggris", "Tottenham Hotspur"],
         ["Antonio Nusa", 7.0, 20, 0, 180, "Norwegia", "Club Brugge KV"],
         ["Rasmus Højlund", 6.7, 22, 0, 193, "Denmark", "Manchester United"],
         ["Claudio Echeverri", 6.8, 18, 0, 171, "Argentina", "Manchester City"],
         ["Dimitri de Condé", 6.4, 18, 0, 180, "Belgia", "KRC Genk"],
         ["Roony Bardghji", 6.9, 19, 0, 175, "Swedia", " København"]
    ]
}

data_legend = {
    'gk': [
        ["Lev Yashin", 9.8, 41, 2500000, 189, "Rusia", "Dynamo Moscow"],
        ["Gianluigi Buffon", 9.5, 45, 300000, 192, "Italia", "Juventus "],
        ["Dino Zoff", 9.3, 41, 3000000, 182, "Italia", "Juventus"],
        ["Peter Schmeichel", 9.2, 39, 1500000, 193, "Denmark", "Manchester United"],
        ["Oliver Kahn", 9.1, 38, 3100000, 188, "Jerman", "Bayern München"]
    ],
    'df': [
        ["Paolo Maldini", 9.8, 41, 2500000, 186, "Italia", "AC Milan"],
        ["Franz Beckenbauer", 9.9, 36, 9000000, 181, "Jerman", "Bayern München"],
        ["Franco Baresi", 9.7, 37, 1500000, 176, "Italia", "AC Milan"],
        ["Roberto Carlos", 9.3, 39, 800000, 168, "Brasil", "Real Madrid"],
        ["Cafu", 9.3, 37, 2000000, 176, "Brasil", "AC Milan"],
        ["Bobby Moore", 9.5, 39, 500000, 178, "Inggris", "West Ham United"],
        ["Daniel Passarella", 9.2, 36, 650000, 173, "Argentina", "River Plate"],
        ["Lothar Matthäus", 9.4, 39, 700000, 177, "Jerman", "Bayern München"],
        ["Alessandro Nesta", 9.3, 38, 250000, 187, "Italia", "AC Milan"],
        ["Carles Puyol", 9.0, 36, 2000000, 178, "Spanyol", "Barcelona"]
    ],
    'mf': [
        ["Zinedine Zidane", 9.9, 34, 12500000, 185, "Prancis", "Real Madrid"],
        ["Johan Cruyff", 9.9, 37, 2000000, 178, "Belanda", "Ajax"],
        ["Diego Maradona", 9.9, 37, 2500000, 165, "Argentina", "SSC Napoli"],
        ["Alfredo Di Stéfano", 9.8, 40, 15000000, 178, "Argentina", "Real Madrid"],
        ["Michel Platini", 9.5, 32, 500000, 179, "Prancis", "Juventus"],
        ["George Best", 9.5, 37, 6700000, 175, "Irlandia", "Manchester United"],
        ["Garrincha", 9.6, 40, 1500000, 169, "Brasil", "Botafogo"],
        ["Andrés Iniesta", 9.4, 39, 350000, 171, "Spanyol", "Emirates Club"],
        ["Xavi Hernández", 9.4, 39, 1000000, 170, "Spanyol", "Barcelona"],
        ["Frank Rijkaard", 9.3, 34, 1700000, 190, "Belanda", "AC Milan"],
        ["Sócrates", 9.2, 35, 1500000, 193, "Brasil", "Corinthians"],
        ["Paul Scholes", 9.1, 38, 1000000, 170, "Inggris", "Manchester United"],
        ["Steven Gerrard", 9.1, 36, 2000000, 183, "Inggris", "Liverpool"],
        ["Clarence Seedorf", 9.0, 38, 750000, 176, "Belanda", "AC Milan"],
        ["Zico", 9.5, 40, 1500000, 172, "Brasil", "Flamengo"]
    ],
    'fw': [
        ["Pelé", 9.9, 40, 500000, 173, "Brasil", "Santos "],
        ["Ronaldo Nazário", 9.7, 34, 3000000, 183, "Brasil", "Corinthians"],
        ["Marco van Basten", 9.6, 28, 3000000, 188, "Belanda", "AC Milan"],
        ["Gerd Müller", 9.5, 34, 280000, 176, "Jerman", "Bayern München"],
        ["Eusébio", 9.5, 38, 400000, 175, "Portugal", "SL Benfica"],
        ["Romário", 9.4, 42, 3000000, 169, "Brasil", "PSV Eindhoven"],
        ["Thierry Henry", 9.3, 37, 2500000, 188, "Prancis", "Arsenal"],
        ["Raúl González", 9.2, 38, 500000, 180, "Spanyol", "Real Madrid"],
        ["Gabriel Batistuta", 9.1, 36, 500000, 185, "Argentina", "ACF Fiorentina"],
        ["Wayne Rooney", 9.0, 35, 500000, 176, "Inggris", "Derby County"],
        ["Ryan Giggs", 9.0, 40, 3000000, 179, "Wales", "Manchester United"],
        ["Dennis Bergkamp", 9.2, 37, 2000000, 183, "Belanda", "Arsenal"],
        ["Roberto Baggio", 9.4, 37, 1500000, 174, "Italia", "Juventus "],
        ["George Weah", 9.1, 37, 250000, 185, "Liberia", "AC Milan"],
        ["Kenny Dalglish", 9.3, 36, 140000, 173, "Skotlandia", "Liverpool"],
        ["Hristo Stoichkov", 9.0, 35, 240000, 178, "Bulgaria", "Barcelona"]
    ]
}

data_custom = {
    'gk': [
        ['Ihsan Najmi Nugroho', 6.5, 22, 0, 180, "Indonesia"],
        ['Andi Setiawan', 6.6, 28, 0, 185, "Indonesia"],
        ['Leonardo Da Vinci', 9.0, 30, 0, 190, "Italia"],
        ['Muhammad Rizky Budianto', 10.0, 18, 0, 171, "Indonesia"],
        ['Kobe braynt', 9.9, 20, 0, 190, "USA"],
        ['Jerome Polin', 8.5, 25, 0, 175, "Indonesia"],
        ['Bocil FF', 7.0, 19, 0, 160, "Indonesia"],
        ['Kuyang', 6.0, 21, 0, 150, "Indonesia"],
        ['Napoleon Bonaparte', 7.0, 30, 0, 170, "Prancis"],
        ['Perunggu', 6.5, 23, 0, 180, "Indonesia"]
    ],
    'df': [
        ['Nur Rahman fadillah', 7.0, 25, 0, 175, "Indonesia"],
        ['Edogawa conan', 8.0, 24, 0, 178, "Jepang"],
        ['Mario Bros', 7.5, 30, 0, 165, "Italia"],
        ['Ultraman Tiga', 8.5, 28, 0, 1000, "Jepang"],
        ['John Cena', 8.0, 29, 0, 185, "USA"],
        ['Jeff Bezos', 9.5, 33, 0, 190, "USA"],
        ['Genduruwo', 6.5, 22, 0, 50, "Indonesia"],
        ['Pocong', 6.0, 20, 0, 170, "Indonesia"],
        ['Makarizo', 7.0, 27, 0, 175, "Indonesia"],
        ['Baskara', 7.5, 26, 0, 180, "Indonesia"]
    ],
    'mf': [
        ['uzumaki Naruto', 8.5, 23, 0, 180, "Jepang"],
        ['Raden Kian Santang', 7.5, 27, 0, 175, "Indonesia"],
        ['Arya Satya Rakha Phany Putra', 7.0, 22, 0, 178, "Indonesia"],
        ['I Show Speed', 8.0, 26, 0, 185, "USA"],
        ['Mr Beast', 9.0, 25, 0, 190, "USA"],
        ['Pikachu', 8.5, 24, 0, 40, "Jepang"],
        ['Kuntilanak', 6.0, 21, 0, 170, "Indonesia"],
        ['Sal Priadi', 7.0, 29, 0, 175, "Indonesia"],
        ['Head And Shoulders', 6.5, 30, 0, 180, "Indonesia"],
        ['Armada', 7.5, 28, 0, 175, "Indonesia"]
    ],
    'fw': [
        ['Mahdi Sarwan Abdulah', 7.0, 25, 0, 175, "Indonesia"],
        ['Sasuke Uchiha', 8.0, 24, 0, 178, "Jepang"],
        ['Alucard', 9.0, 30, 0, 185, "Romania"],
        ['Kai Cenat', 8.5, 28, 0, 170, "USA"],
        ['Elon Musk', 9.5, 32, 0, 188, "USA"],
        ['Madun', 9.9, 20, 0, 160, "Indonesia"],
        ['Dewa Kipas', 6.5, 22, 0, 170, "Indonesia"],
        ['Roro Jonggrang', 7.5, 21, 0, 165, "Indonesia"],
        ['Trex', 6.0, 19, 0, 400, "Afrika Selatan"],
        ['Hitler', 5.0, 40, 0, 175, "Jerman"],
        ['Nadin Amizah', 7.0, 30, 0, 165, "Indonesia"],
        ['KKJ', 6.5, 23, 0, 170, "Indonesia"]
    ]
}

data_transfer = []
clubs = {
    "Barcelona": data_barcelona,
    "Real Madrid": data_madrid,
    "Arsenal": data_arsenal,
    "PSG": data_psg,
    "Borussia Dortmund": data_dortmund,
    "Free Agent": data_gratisan,
    "Pencari Bakat": data_pemuda
}