import fichaDePersonagem
from validações import isnumber,istext

print('Ficha de Personagem')


# Criando uma instância da Class Ficha()
ficha = fichaDePersonagem.Ficha()

# Pegando principais variáveis 

# Nome do Personagem
while (True):
    try:
        novoNome =  input('Me dê o nome do seu personagem: ')
        ficha.nome = novoNome
    except AssertionError:
        print('Digite um nome válido! Sem caracteres especiais como interrogação ou números!\n')
    else:
        break
print(ficha.nome)

        

# Classe do personagem
print('''
Lista de classes

1   -   Bárbaro
2   -   Bardo
3   -   Bruxo
4   -   Clérigo
5   -   Druida
6   -   Feiticeiro
7   -   Guerreiro
8   -   Ladino
9   -   Mago
10  -   Monge
11  -   Paladino
12  -   Patrulheiro
''')

while True:
    try:
        novaClasse = input("Me dê a classe do seu personagem: ")
        ficha.classe = novaClasse
    except AssertionError:
        print('Digite um número entre 1 e 12!\n')
    else:
        break
print(ficha.classe)

# Nível do personagem
ficha.nivel = input('Me dê o nível do seu personagem [1-30]:')

# nivel = isnumber.valid_num(1, 30)

# if (nivel >= 1 and nivel <= 30):
#     ficha = fichaDePersonagem(nivel) 

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
# antecedente = isnumber.valid_num(1, 12)