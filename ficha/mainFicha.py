import fichaDePersonagem
import os

print('Ficha de Personagem')


# Criando uma instância da Class Ficha()
ficha = fichaDePersonagem.Ficha()

# Pegando principais variáveis 

# Inicializando variavel de controle
certeza = False
novoValorDeVariavel = 0

# Nome do Personagem
while (True and (certeza == False)):
    try:
        novoNome =  input('Me dê o nome do seu personagem: ')
        novoValorDeVariavel = 0
        ficha.nome = novoNome
        if (certeza == False):
            while True:
                ver = input(f'Tem certeza que o nome do seu personagem vai ser "{ficha.nome}"? [S/N] ').upper()
                if (ver in 'SIM'):
                    os.system('cls')
                    certeza = True
                    break
                if ((ver in 'NAO') or (ver == 'NÃO')):
                    os.system('cls')
                    novoValorDeVariavel += 1
                    ficha.nome = '3'
                    break
                else:
                    os.system('cls')
                    print('Digite [S/N}\n')
    except AssertionError:
        os.system('cls')
        if novoValorDeVariavel == 0:
            print('Digite um nome válido! Sem caracteres especiais como interrogação ou números!\n')
        else:
            print('Digite seu novo nome!\n')
    else:
        os.system('cls')
        break

# Fazendo variável de controle voltar ao valor Default
certeza = False
novoValorDeVariavel = 0

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
        novoValorDeVariavel = 0
        ficha.classe = novaClasse
        if (certeza == False):
            while True:
                ver = input(f'Tem certeza que a classe do seu personagem vai ser "{ficha.classe}"? [S/N] ').upper()
                print(ver)
                if (ver in 'SIM'):
                    os.system('cls')
                    certeza = True
                    break
                if ((ver in 'NAO') or (ver == 'NÃO')):
                    os.system('cls')
                    novoValorDeVariavel += 1
                    ficha.classe = 13
                    break
                else:
                    os.system('cls')
                    print('Digite [S/N}\n')
    except AssertionError:
        os.system('cls')
        if novoValorDeVariavel == 0:
            print('Digite um número entre 1 e 12!')
        else:
            print('Digite o número da sua nova classe!\n')
    else:
        os.system('cls')
        break

# Fazendo variável de controle voltar ao valor Default
certeza = False
novoValorDeVariavel = 0

# Nível do personagem
while (True and (certeza == False)):
    try:
        novoNivel = input('Me dê o nível do seu personagem [1-30]: ')
        novoValorDeVariavel = 0
        ficha.nivel = novoNivel
        if (certeza == False):
            while True:
                ver = input(f'Tem certeza que o nível do seu personagem vai ser "{ficha.nivel}"? [S/N] ').upper()
                print(ver)
                if (ver in 'SIM'):
                    os.system('cls')
                    certeza = True
                    break
                if ((ver in 'NAO') or (ver == 'NÃO')):
                    os.system('cls')
                    novoValorDeVariavel += 1
                    ficha.nivel = 44
                    break
                else:
                    os.system('cls')
                    print('Digite [S/N}\n')
    except AssertionError:
        os.system('cls')
        if novoValorDeVariavel == 0:
            print('Digite um número entre 1 e 30!\n')
        else:
            print('Digite um novo nível para o seu personagem!\n')
    else:
        os.system('cls')
        break

# Fazendo variável de controle voltar ao valor Default
certeza = False
novoValorDeVariavel = 0

# Antecedente do personagem
while (True and (certeza == False)):
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
    try:
        novoAntecedente = input("Me dê o antecedente do seu personagem: ")
        novoValorDeVariavel = 0
        ficha.antecedente = novoAntecedente
        if (certeza == False):
            while True:
                ver = input(f'Tem certeza que o antecedente do seu personagem vai ser "{ficha.antecedente}"? [S/N] ').upper()
                print(ver)
                if (ver in 'SIM'):
                    os.system('cls')
                    certeza = True
                    break
                if ((ver in 'NAO') or (ver == 'NÃO')):
                    os.system('cls')
                    novoValorDeVariavel += 1
                    ficha.antecedente = 13
                    break
                else:
                    os.system('cls')
                    print('Digite [S/N}\n')
    except AssertionError:
        os.system('cls')
        if novoValorDeVariavel == 0:
            print('Digite um número entre 1 e 12!')
        else:
            print('Digite o número do seu Antecedente!\n')
    else:
        os.system('cls')
        break

# Fazendo variável de controle voltar ao valor Default
certeza = False
novoValorDeVariavel = 0
