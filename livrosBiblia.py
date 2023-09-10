import datetime
import random

# Lista de livros da Bíblia com o número de capítulos correspondentes
livros_da_biblia = {
    "Gênesis": 50,
    "Êxodo": 40,
    "Levítico": 27,
    "Números": 36,
    "Deuteronômio": 34,
    "Josué": 24,
    "Juízes": 21,
    "Rute": 4,
    "1 Samuel": 31,
    "2 Samuel": 24,
    "1 Reis": 22,
    "2 Reis": 25,
    "1 Crônicas": 29,
    "2 Crônicas": 36,
    "Esdras": 10,
    "Neemias": 13,
    "Ester": 10,
    "Jó": 42,
    "Salmos": 150,
    "Provérbios": 31,
    "Eclesiastes": 12,
    "Cânticos": 8,
    "Isaías": 66,
    "Jeremias": 52,
    "Lamentações": 5,
    "Ezequiel": 48,
    "Daniel": 12,
    "Oséias": 14,
    "Joel": 3,
    "Amós": 9,
    "Obadias": 1,
    "Jonas": 4,
    "Miquéias": 7,
    "Naum": 3,
    "Habacuque": 3,
    "Sofonias": 3,
    "Ageu": 2,
    "Zacarias": 14,
    "Malaquias": 4,
    "Mateus": 28,
    "Marcos": 16,
    "Lucas": 24,
    "João": 21,
    "Atos dos Apóstolos": 28,
    "Romanos": 16,
    "1 Coríntios": 16,
    "2 Coríntios": 13,
    "Gálatas": 6,
    "Efésios": 6,
    "Filipenses": 4,
    "Colossenses": 4,
    "1 Tessalonicenses": 5,
    "2 Tessalonicenses": 3,
    "1 Timóteo": 6,
    "2 Timóteo": 4,
    "Tito": 3,
    "Filemom": 1,
    "Hebreus": 13,
    "Tiago": 5,
    "1 Pedro": 5,
    "2 Pedro": 3,
    "1 João": 5,
    "2 João": 1,
    "3 João": 1,
    "Judas": 1,
    "Apocalipse": 22
}
def imprimir_data_atual():
    data_atual = datetime.datetime.now()
    print(data_atual.strftime("%d/%m/%Y %H:%M:%S"))

def caixa_data():
    print("=" * 50)
    imprimir_data_atual()
    print("=" * 50)
    
def imprimir_tracos():
    print("-" * 50)
    
def imprime_quadro():
    print("+" * 50)
    
def sortear_e_imprimir_salmo():
    # Sorteia um salmo de 1 a 150
    salmo_sorteado = random.randint(1, 150)
    print(f"Salmos {salmo_sorteado}!")
    print("")
    imprimir_tracos()
    
    
def verificar_e_imprimir_proverbio():
    # Obter o dia atual
    dia_atual = datetime.datetime.now().day
    
    # Dia específico para ler um versículo de Provérbios (altere conforme necessário)
    #dia_para_proverbio = 15
    
    #if dia_atual == dia_para_proverbio:
        # Se for o dia específico, imprima uma mensagem para ler um versículo de Provérbios
    print(f"Provérbios {dia_atual}!")
    imprimir_tracos()
    

def sortear_livro_e_capitulo():
    # Sorteia um livro da lista de livros
    livro_sorteado = random.choice(list(livros_da_biblia.keys()))
    
    # Determina o número máximo de capítulos para o livro sorteado
    maximo_capitulos = livros_da_biblia[livro_sorteado]
    
    # Sorteia um número de capítulo entre 1 e o número máximo de capítulos
    capitulo_sorteado = random.randint(1, maximo_capitulos)
    
    return livro_sorteado, capitulo_sorteado



def imprimir_resultado():
    caixa_data()
    imprime_quadro()
    #imprimir_tracos()
    livro, capitulo = sortear_livro_e_capitulo()
    print("Hoje você vai Ler: ")
    imprimir_tracos()
    resultado = f"{livro} Capítulo {capitulo}."
    print("")
    print(resultado)
    imprimir_tracos()

# Chame a função imprimir_resultado() para obter o resultado
imprimir_resultado()

# Chame a função verificar_e_imprimir_proverbio() para verificar e imprimir o versículo de Provérbios, se for o dia específico
verificar_e_imprimir_proverbio()

# Chame a função sortear_e_imprimir_salmo() para sortear e imprimir um salmo aleatório
sortear_e_imprimir_salmo()
imprime_quadro()
