from habilidades import habilidades

class Ficha:

    # Header da ficha
    def __init__(self, nome, classe, nivel, antecedente, nomeDoJogador, raca, tendencia, pontosdeExperiencia, forca, destreza, constituicao, inteligencia, sabedoria, carisma, classeDeArmadura, iniciativa, deslocamento):

        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.antecedente = antecedente
        self.nomeDoJogador = nomeDoJogador
        self.raca = raca
        self.tendencia = tendencia
        self.pontosDeExperiencia = pontosdeExperiencia

        # Atributos
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

        # Armadura
        self.classeDeArmadura = classeDeArmadura

        # Iniciativa
        self.iniciativa = iniciativa 

        # Deslocamento 
        self.deslocamento = deslocamento


    # Definindo os modificadores dos atributos
    def modificadorDeAtributo(self):
        atributos = [self.forca, self.destreza, self.constituicao, self.inteligencia, self.sabedoria, self.carisma]
        modificadores = habilidades.Modificador(atributos)

    # Definindo o Bônus de profiência do nivel do jogador
    def bonusDeProficiencia(self):
        bonusDeProcifiencia = habilidades.BonusDeProficiencia(self.nivel)

    # Definindo as pericias
    def pericias(self):
        pass