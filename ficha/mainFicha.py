from fichaDePersonagem import Ficha 
import os

print('Ficha de Personagem')


# Criando uma instância da Class Ficha()
ficha = Ficha()

# Pegando principais variáveis 

# Inicializando variavel de controle
certeza = False
novoValorDeVariavel = 0

# # Nome do Personagem
# while (certeza == False):
#     try:
#         novoNome =  input('Me dê o nome do seu personagem: ')
#         novoValorDeVariavel = 0
#         ficha.nome = novoNome
#         if (certeza == False):
#             while True:
#                 ver = input(f'Tem certeza que o nome do seu personagem vai ser "{ficha.nome}"? [S/N] ').upper()
#                 if (ver in 'SIM'):
#                     os.system('cls')
#                     certeza = True
#                     break
#                 if ((ver in 'NAO') or (ver == 'NÃO')):
#                     os.system('cls')
#                     novoValorDeVariavel += 1
#                     ficha.nome = '3'
#                     break
#                 else:
#                     os.system('cls')
#                     print('Digite [S/N}\n')
#     except AssertionError:
#         os.system('cls')
#         if novoValorDeVariavel == 0:
#             print('Digite um nome válido! Sem caracteres especiais como interrogação ou números!\n')
#         else:
#             print('Digite seu novo nome!\n')
#     else:
#         os.system('cls')
#         break

# # Fazendo variável de controle voltar ao valor Default
# certeza = False
# novoValorDeVariavel = 0

# # Classe do personagem
# while (certeza == False):
#     print('''
# Lista de classes
# =====================
# 1   -   Bárbaro
# 2   -   Bardo
# 3   -   Bruxo
# 4   -   Clérigo
# 5   -   Druida
# 6   -   Feiticeiro
# 7   -   Guerreiro
# 8   -   Ladino
# 9   -   Mago
# 10  -   Monge
# 11  -   Paladino
# 12  -   Patrulheiro
# ''')
#     try:
#         novaClasse = input("Me dê a classe do seu personagem: ")
#         novoValorDeVariavel = 0
#         ficha.classe = novaClasse
#         if (certeza == False):
#             while True:
#                 ver = input(f'Tem certeza que a classe do seu personagem vai ser "{ficha.classe}"? [S/N] ').upper()
#                 if (ver in 'SIM'):
#                     os.system('cls')
#                     certeza = True
#                     break
#                 if ((ver in 'NAO') or (ver == 'NÃO')):
#                     os.system('cls')
#                     novoValorDeVariavel += 1
#                     ficha.classe = 13
#                     break
#                 else:
#                     os.system('cls')
#                     print('Digite [S/N}\n')
#     except AssertionError:
#         os.system('cls')
#         if novoValorDeVariavel == 0:
#             print('Digite um número entre 1 e 12!')
#         else:
#             print('Digite o número da sua nova classe!\n')
#     else:
#         os.system('cls')
#         break

# # Fazendo variável de controle voltar ao valor Default
# certeza = False
# novoValorDeVariavel = 0

# Experiência do personagem
while (certeza == False):
    try:
        novosPontosDeExperiencia = input('Me dê os pontos de experiência do seu personagem: ')
        novoValorDeVariavel = 0
        ficha.pontosDeExperiencia = novosPontosDeExperiencia
        if (certeza == False):
            while True:
                ver = input(f'Tem certeza que os pontos de experiências do seu personagem vai ser "{ficha.pontosDeExperiencia}"? [S/N] ').upper()
                if (ver in 'SIM'):
                    os.system('cls')
                    certeza = True
                    break
                if ((ver in 'NAO') or (ver == 'NÃO')):
                    os.system('cls')
                    novoValorDeVariavel += 1
                    ficha.pontosDeExperiencia = 'j'
                    break
                else:
                    os.system('cls')
                    print('Digite [S/N}\n')
    except AssertionError:
        os.system('cls')
        if novoValorDeVariavel == 0:
            print('Digite um número acima de 1!\n')
        else:
            print('Digite um novo nível para o seu personagem!\n')
    else:
        os.system('cls')
        break

# Fazendo variável de controle voltar ao valor Default
certeza = False
novoValorDeVariavel = 0

# Definindo função que para nivel
# 5245.94 + (1.165062 - 5245.94)/(1 + (x/223761600000.00003)**0.4210905)

# Nível do personagem
while (certeza == False):
    try:
        novoNivel = input('Me dê o nível do seu personagem [1-20]: ')
        novoValorDeVariavel = 0
        ficha.nivel = novoNivel
        if (certeza == False):
            while True:
                ver = input(f'Tem certeza que o nível do seu personagem vai ser "{ficha.nivel}"? [S/N] ').upper()
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
            print('Digite um número entre 1 e 20!\n')
        else:
            print('Digite um novo nível para o seu personagem!\n')
    else:
        os.system('cls')
        break

# Fazendo variável de controle voltar ao valor Default
certeza = False
novoValorDeVariavel = 0

# # Antecedente do personagem
# while (certeza == False):
#     print('''
# Lista de antecedentes
# =====================
# 1   -   Acólito
# 2   -   Artesão de Guilda
# 3   -   Artista
# 4   -   Charlatão
# 5   -   Criminoso
# 6   -   Eremita
# 7   -   Forasteiro
# 8   -   Herói do Povo
# 9   -   Marinheiro
# 10  -   Nobre
# 11  -   Orfão
# 12  -   Sábio
# ''')
#     try:
#         novoAntecedente = input("Me dê o antecedente do seu personagem: ")
#         novoValorDeVariavel = 0
#         ficha.antecedente = novoAntecedente
#         if (certeza == False):
#             while True:
#                 ver = input(f'Tem certeza que o antecedente do seu personagem vai ser "{ficha.antecedente}"? [S/N] ').upper()
#                 if (ver in 'SIM'):
#                     os.system('cls')
#                     certeza = True
#                     break
#                 if ((ver in 'NAO') or (ver == 'NÃO')):
#                     os.system('cls')
#                     novoValorDeVariavel += 1
#                     ficha.antecedente = 13
#                     break
#                 else:
#                     os.system('cls')
#                     print('Digite [S/N}\n')
#     except AssertionError:
#         os.system('cls')
#         if novoValorDeVariavel == 0:
#             print('Digite um número entre 1 e 12!')
#         else:
#             print('Digite o número do seu Antecedente!\n')
#     else:
#         os.system('cls')
#         break

# # Fazendo variável de controle voltar ao valor Default
# certeza = False
# novoValorDeVariavel = 0

# # Nome do Jogador
# while (certeza == False):
#     try:
#         novoNomeDoJogador =  input('Me dê o seu nome: ')
#         novoValorDeVariavel = 0
#         ficha.nomeDoJogador = novoNomeDoJogador
#         if (certeza == False):
#             while True:
#                 ver = input(f'Tem certeza que o nome do seu personagem vai ser "{ficha.nomeDoJogador}"? [S/N] ').upper()
#                 if (ver in 'SIM'):
#                     os.system('cls')
#                     certeza = True
#                     break
#                 if ((ver in 'NAO') or (ver == 'NÃO')):
#                     os.system('cls')
#                     novoValorDeVariavel += 1
#                     ficha.nomeDoJogador = '3'
#                     break
#                 else:
#                     os.system('cls')
#                     print('Digite [S/N}\n')
#     except AssertionError:
#         os.system('cls')
#         if novoValorDeVariavel == 0:
#             print('Digite um nome válido! Sem caracteres especiais como interrogação ou números!\n')
#         else:
#             print('Digite seu novo nome!\n')
#     else:
#         os.system('cls')
#         break

# # Fazendo variável de controle voltar ao valor Default
# certeza = False
# novoValorDeVariavel = 0

# # Antecedente do personagem
# while (certeza == False):
#     print('''
# Lista de antecedentes
# =====================
# 1   -   Anão
# 2   -   Elfo
# 3   -   Halfling
# 4   -   Humano
# 5   -   Draconato
# 6   -   Gnomo
# 7   -   Meio-Elfo
# 8   -   Meio-Orc
# 9   -   Tielfling
# ''')
#     try:
#         novaRaca = input("Me dê a raça do seu personagem: ")
#         novoValorDeVariavel = 0
#         ficha.raca = novaRaca
#         if (certeza == False):
#             while True:
#                 ver = input(f'Tem certeza que raça do seu personagem vai ser "{ficha.raca}"? [S/N] ').upper()
#                 if (ver in 'SIM'):
#                     os.system('cls')
#                     certeza = True
#                     break
#                 if ((ver in 'NAO') or (ver == 'NÃO')):
#                     os.system('cls')
#                     novoValorDeVariavel += 1
#                     ficha.antecedente = 13
#                     break
#                 else:
#                     os.system('cls')
#                     print('Digite [S/N}\n')
#     except AssertionError:
#         os.system('cls')
#         if novoValorDeVariavel == 0:
#             print('Digite um número entre 1 e 9!')
#         else:
#             print('Digite o número da sua raça!\n')
#     else:
#         os.system('cls')
#         break

# # Fazendo variável de controle voltar ao valor Default
# certeza = False
# novoValorDeVariavel = 0

# Antecedente do personagem
# while (certeza == False):
#     print('''
# Lista de antecedentes
# =====================
# 1   -   Leal e Bom (LB)
# 2   -   Neutro e Bom (NB)
# 3   -   Caótico e Bom (CB)
# 4   -   Leal e Neutro (LN)
# 5   -   Neutro (N)
# 6   -   Caótico e Neutro (CN)
# 7   -   Leal e Mau (LM)
# 8   -   Neutro e Mau (NM)
# 9   -   Caótico e Mau (CM)
# ''')
#     try:
#         novaTendencia = input("Me dê a raça do seu personagem: ")
#         novoValorDeVariavel = 0
#         ficha.tendencia = novaTendencia
#         if (certeza == False):
#             while True:
#                 ver = input(f'Tem certeza que a tendência do seu personagem vai ser "{ficha.tendencia}"? [S/N] ').upper()                 
#                 if (ver in 'SIM'):
#                     os.system('cls')
#                     certeza = True
#                     break
#                 if ((ver in 'NAO') or (ver == 'NÃO')):
#                     os.system('cls')
#                     novoValorDeVariavel += 1
#                     ficha.antecedente = 13
#                     break
#                 else:
#                     os.system('cls')
#                     print('Digite [S/N}\n')
#     except AssertionError:
#         os.system('cls')
#         if novoValorDeVariavel == 0:
#             print('Digite um número entre 1 e 9!')
#         else:
#             print('Digite o número da sua tendencia!\n')
#     else:
#         os.system('cls')
#         break

# # Fazendo variável de controle voltar ao valor Default
# certeza = False
# novoValorDeVariavel = 0