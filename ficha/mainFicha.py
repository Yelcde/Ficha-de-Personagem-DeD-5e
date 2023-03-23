import fichaDePersonagem

print('Ficha de Personagem')

# Pegando principais variáveis 

# Nome do Personagem
nome = input('Me dê o nome do seu personagem: ')
# Colocando variável em fichaDePersonagem
ficha = fichaDePersonagem(nome)

# Classe do personagem
classe = input("Me dê a classe do seu personagem: ")
ficha = fichaDePersonagem(classe)

# Nível do personagem
nivel = int(input('Me dê o nível do seu personagem [1-30]:'))
if (nivel >= 1 and nivel <= 30):
    ficha = fichaDePersonagem(nivel) 

# Antecedente do personagem
print('''
    Lista de antecedentes

    1   -   Acólito
    2   -   Artesão de Guilda
    3   -   Artista
    4   -   Charlatão
    5   -   Criminoso
    6   -   Eremita
    7   -   Forasteiro
    8   -   Herói do Povo
    9   -   Marinheiro
    10  -   Nobre
    11  -   Orfão
    12  -   Sábio
''')
antecedente = input()