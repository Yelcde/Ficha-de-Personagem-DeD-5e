from ficha import fichaDePersonagem

# Definindo os modificadores de atributos
def Modificador(atributos):
    modificadores = []

    for i in atributos:
        modificadores.append((i-10)//2)

    return modificadores

# Definindo Bônus de Proficiência
def BonusDeProficiencia(nivel):
    return (nivel-1)//4 +2