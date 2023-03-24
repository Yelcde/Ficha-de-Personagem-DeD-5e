from habilidades import modificador
from habilidades import bonusdeprof
from validações import isnumber
from validações import istext

class Ficha:

    # Header da ficha
    def __init__(self):

        self.__nome = 'a'
        self.__classe = None
        self.__nivel = None
        self.__antecedente = None
        self.__nomeDoJogador = None
        self.__raca = None
        self.__tendencia = None
        self.__pontosDeExperiencia = None

        # Atributos
        self.__forca = None
        self.__destreza = None
        self.__constituicao = None
        self.__inteligencia = None
        self.__sabedoria = None
        self.__carisma = None

        # Armadura
        self.__classeDeArmadura = None

        # Iniciativa
        self.__iniciativa = None 

        # Deslocamento 
        self.__deslocamento = None


    # Setando Variaveis

    # Nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novoNome):
        assert self.__validaNome(novoNome)
        self.__nome = novoNome

        



    # # Classe
    # @property
    # def classe(self):
    #     return self.classe
    
    # @classe.setter
    # def classe(self, novaClasse):
    #     num = isnumber.valid_num(novaClasse)
    #     while True:
    #         if (num == False):
    #             num = input


    #     # if (novaClasse >= 1 and novaClasse <= 30):
    #     #     self.classe = novaClasse
    #     # else:
    #     #     return 'Digite uma classe válido'
    #         # return 'Digite um nível válido, entre 1-30'


    # # Nível
    # @property
    # def nivel(self):
    #     return self.classe
    
    # @nivel.setter
    # def nivel(self, novaClasse):
    #     if (novaClasse >= 1 and novaClasse <= 30):
    #         self.classe = novaClasse
    #     else:
    #         return 'Digite um nível válido, entre 1-30'


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

    def __validaNome(self, nome):
        nome = nome.strip()
        nome = nome.replace(' ', '')
        
        return nome.isalpha()
