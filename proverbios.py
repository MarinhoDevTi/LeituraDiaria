import random
import datetime

# Lista de livros da Bíblia com o número de capítulos correspondentes
livros_da_biblia = {
    # ... (livros da Bíblia com seus capítulos)
}

def sortear_livro_e_capitulo():
    # Sorteia um livro da lista de livros
    livro_sorteado = random.choice(list(livros_da_biblia.keys()))
    
    # Determina o número máximo de capítulos para o livro sorteado
    maximo_capitulos = livros_da_biblia[livro_sorteado]
    
    # Sorteia um número de capítulo entre 1 e o número máximo de capítulos
    capitulo_sorteado = random.randint(1, maximo_capitulos)
    
    return livro_sorteado, capitulo_sorteado

def imprimir_resultado():
    livro, capitulo = sortear_livro_e_capitulo()
    resultado = f"Hoje você vai ler: {livro} Capítulo {capitulo}. Este é um exemplo."
    print(resultado)

def verificar_e_imprimir_proverbio():
    # Obter o dia atual
    dia_atual = datetime.datetime.now().day
    
    # Dia específico para ler um versículo de Provérbios (altere conforme necessário)
    dia_para_proverbio = 15
    
    if dia_atual == dia_para_proverbio:
        # Se for o dia específico, imprima uma mensagem para ler um versículo de Provérbios
        print(f"Leia também Provérbios {dia_para_proverbio}!")

# Chame a função imprimir_resultado() para obter o resultado
imprimir_resultado()

# Chame a função verificar_e_imprimir_proverbio() para verificar e imprimir o versículo de Provérbios, se for o dia específico
verificar_e_imprimir_proverbio()
