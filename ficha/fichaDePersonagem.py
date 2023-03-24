from habilidades import modificador
from habilidades import bonusdeprof
from validações import isnumber
from validações import istext

class Ficha:

    # Header da ficha
    # def __init__(self, nome, classe, nivel, antecedente, nomeDoJogador, raca, tendencia, pontosdeExperiencia, forca, destreza, constituicao, inteligencia, sabedoria, carisma, classeDeArmadura, iniciativa, deslocamento):

    #     self.nome = nome
    #     self.classe = classe
    #     self.nivel = nivel
    #     self.antecedente = antecedente
    #     self.nomeDoJogador = nomeDoJogador
    #     self.raca = raca
    #     self.tendencia = tendencia
    #     self.pontosDeExperiencia = pontosdeExperiencia

    #     # Atributos
    #     self.forca = forca
    #     self.destreza = destreza
    #     self.constituicao = constituicao
    #     self.inteligencia = inteligencia
    #     self.sabedoria = sabedoria
    #     self.carisma = carisma

    #     # Armadura
    #     self.classeDeArmadura = classeDeArmadura

    #     # Iniciativa
    #     self.iniciativa = iniciativa 

    #     # Deslocamento 
    #     self.deslocamento = deslocamento


    # Setando Variaveis

    # Nome
    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, novoNome):
        valido = istext.valid_text(novoNome)
        while True:
            if (valido == False):
                while True:
                    if (valido == False):
                        novoNome = input('Digite um nome válido! Sem caracteres especiais como interrogação ou números! Tente novamente: ')
                        valido = istext.valid_text(novoNome)
                    else:
                        break
            else:
                return novoNome
                break



    # Classe
    @property
    def classe(self):
        return self.classe
    
    @classe.setter
    def classe(self, novaClasse):
        num = isnumber.valid_num(novaClasse)
        while True:
            if (num == False):
                return 'Digite um número válido'
        # if (novaClasse >= 1 and novaClasse <= 30):
        #     self.classe = novaClasse
        # else:
        #     return 'Digite uma classe válido'
            # return 'Digite um nível válido, entre 1-30'


    # Nível
    @property
    def nivel(self):
        return self.classe
    
    @nivel.setter
    def nivel(self, novaClasse):
        if (novaClasse >= 1 and novaClasse <= 30):
            self.classe = novaClasse
        else:
            return 'Digite um nível válido, entre 1-30'


    # Definindo os modificadores dos atributos
    def modificadorDeAtributo(self):
        atributos = [self.forca, self.destreza, self.constituicao, self.inteligencia, self.sabedoria, self.carisma]
        modificadores = modificador.Modificador(atributos)

    # Definindo o Bônus de profiência do nivel do jogador
    def bonusDeProficiencia(self):
        bonusDeProcifiencia = bonusdeprof.BonusDeProficiencia(self.nivel)

    # Definindo as pericias
    def pericias(self):
        pass