import fichaDePersonagem
import os

print('Ficha de Personagem')


# Criando uma instância da Class Ficha()
ficha = fichaDePersonagem.Ficha()

# Pegando principais variáveis 

# Inicializando variavel de controle
certeza = False

# Nome do Personagem
while (True and (certeza == False)):
    try:
        novoNome =  input('Me dê o nome do seu personagem: ')
        ficha.nome = novoNome
    except AssertionError:
        os.system('cls')
        print('Digite um nome válido! Sem caracteres especiais como interrogação ou números!\n')
    if (certeza == False):
        while True:
            ver = input(f'Tem certeza que o nome do seu personagem vai ser "{ficha.nome}"? [S/N] ').upper()
            print(ver)
            if ((ver == 'S') or (ver == 'SIM')):
                os.system('cls')
                certeza = True
                break
            if ((ver == 'N') or (ver == 'NÃO') or (ver == "NAO")):
                os.system('cls')
                break
            else:
                os.system('cls')
                print('Digite [S/N}')
    else:
        os.system('cls')
        break

# Fazendo variável de controle voltar ao valor Default
certeza = False

# Classe do personagem
while (True and (certeza == False)):
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
    try:
        novaClasse = input("Me dê a classe do seu personagem: ")
        ficha.classe = novaClasse
    except AssertionError:
        os.system('cls')
        print('Digite um número entre 1 e 12!')
    if (certeza == False):
        while True:
            ver = input(f'Tem certeza que a classe do seu personagem vai ser "{ficha.classe}"? [S/N] ').upper()
            print(ver)
            if ((ver == 'S') or (ver == 'SIM')):
                os.system('cls')
                certeza = True
                break
            if ((ver == 'N') or (ver == 'NÃO') or (ver == "NAO")):
                os.system('cls')
                break
            else:
                os.system('cls')
                print('Digite [S/N}')
    else:
        os.system('cls')
        break


# Nível do personagem
ficha.nivel = input('Me dê o nível do seu personagem [1-30]:')


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