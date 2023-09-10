import random

def sortear_livro_e_capitulo():
    livros_biblia = [
        {"livro": "Gênesis", "capitulos": 50},
        {"livro": "Êxodo", "capitulos": 40},
        {"livro": "Levítico", "capitulos": 27},
        {"livro": "Números", "capitulos": 36},
        {"livro": "Deuteronômio", "capitulos": 34},
        {"livro": "Josué", "capitulos": 24},
        {"livro": "Juízes", "capitulos": 21},
        {"livro": "Rute", "capitulos": 4},
        {"livro": "1 Samuel", "capitulos": 31},
        {"livro": "2 Samuel", "capitulos": 24},
        {"livro": "1 Reis", "capitulos": 22},
        {"livro": "2 Reis", "capitulos": 25},
        {"livro": "1 Crônicas", "capitulos": 29},
        {"livro": "2 Crônicas", "capitulos": 36},
        {"livro": "Esdras", "capitulos": 10},
        {"livro": "Neemias", "capitulos": 13},
        {"livro": "Ester", "capitulos": 10},
        {"livro": "Jó", "capitulos": 42},
        {"livro": "Salmos", "capitulos": 150},
        {"livro": "Provérbios", "capitulos": 31},
        {"livro": "Eclesiastes", "capitulos": 12},
        {"livro": "Cânticos", "capitulos": 8},
        {"livro": "Isaías", "capitulos": 66},
        {"livro": "Jeremias", "capitulos": 52},
        {"livro": "Lamentações", "capitulos": 5},
        {"livro": "Ezequiel", "capitulos": 48},
        {"livro": "Daniel", "capitulos": 12},
        {"livro": "Oséias", "capitulos": 14},
        {"livro": "Joel", "capitulos": 3},
        {"livro": "Amós", "capitulos": 9},
        {"livro": "Obadias", "capitulos": 1},
        {"livro": "Jonas", "capitulos": 4},
        {"livro": "Miquéias", "capitulos": 7},
        {"livro": "Naum", "capitulos": 3},
        {"livro": "Habacuque", "capitulos": 3},
        {"livro": "Sofonias", "capitulos": 3},
        {"livro": "Ageu", "capitulos": 2},
        {"livro": "Zacarias", "capitulos": 14},
        {"livro": "Malaquias", "capitulos": 4},
        {"livro": "Mateus", "capitulos": 28},
        {"livro": "Marcos", "capitulos": 16},
        {"livro": "Lucas", "capitulos": 24},
        {"livro": "João", "capitulos": 21},
        {"livro": "Atos", "capitulos": 28},
        {"livro": "Romanos", "capitulos": 16},
        {"livro": "1 Coríntios", "capitulos": 16},
        {"livro": "2 Coríntios", "capitulos": 13},
        {"livro": "Gálatas", "capitulos": 6},
        {"livro": "Efésios", "capitulos": 6},
        {"livro": "Filipenses", "capitulos": 4},
        {"livro": "Colossenses", "capitulos": 4},
        {"livro": "1 Tessalonicenses", "capitulos": 5},
        {"livro": "2 Tessalonicenses", "capitulos": 3},
        {"livro": "1 Timóteo", "capitulos": 6},
        {"livro": "2 Timóteo", "capitulos": 4},
        {"livro": "Tito", "capitulos": 3},
        {"livro": "Filemon", "capitulos": 1},
        {"livro": "Hebreus", "capitulos": 13},
        {"livro": "Tiago", "capitulos": 5},
        {"livro": "1 Pedro", "capitulos": 5},
        {"livro": "2 Pedro", "capítulos": 3},
        {"livro": "1 João", "capitulos": 5},
        {"livro": "2 João", "capitulos": 1},
        {"livro": "3 João", "capitulos": 1},
        {"livro": "Judas", "capitulos": 1},
        {"livro": "Apocalipse", "capitulos": 22}
    ]

    livro_sorteado = random.choice(livros_biblia)
    livro_escolhido = livro_sorteado["livro"]

    if livro_escolhido == "Gênesis":
        capitulo_sorteado = random.randint(1, livro_sorteado["capitulos"])
    else:
        capitulo_sorteado = None  # Não especificou o capítulo para outros livros

    return livro_escolhido, capitulo_sorteado

livro, capitulo = sortear_livro_e_capitulo()
if capitulo is not None:
    print(f"O livro sorteado foi {livro} e o capítulo sorteado foi {capitulo}.")
else:
    print(f"O livro sorteado foi {livro}.")