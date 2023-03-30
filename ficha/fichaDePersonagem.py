from habilidades import modificador
from habilidades import bonusdeprof

class Ficha:

    # Header da ficha
    def __init__(self):

        self.__nome = None
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
        assert self.__validaTexto(novoNome) == True
        self.__nome = novoNome

        



    # Classe
    @property
    def classe(self):
        return self.__classe
    
    @classe.setter
    def classe(self, novaClasse): 
        assert self.__validaNum(novaClasse) == True and (int(novaClasse) >= 1 and int(novaClasse) <= 12)
        self.__classe = self.__classePorExtenso(novaClasse)

    def __classePorExtenso(self, classePorExtenso):
        classes = ['Bárbaro', 'Bardo', 'Bruxo', 'Clérigo', 'Druida', 'Feiticeiro', 'Guerreiro', 'Ladino', 'Mago', 'Monge', 'Paladino', 'Patrulheiro']
        classePorExtenso = int(classePorExtenso)-1
        for i in range(1, 13):
            if (i == classePorExtenso):
                return classes[i]


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


    # # Definindo os modificadores dos atributos
    # def modificadorDeAtributo(self):
    #     atributos = [self.__forca, self.__destreza, self.__constituicao, self.__inteligencia, self.__sabedoria, self.__carisma]
    #     modificadores = modificador.Modificador(atributos)

    # # Definindo o Bônus de profiência do nivel do jogador
    # def bonusDeProficiencia(self):
    #     bonusDeProcifiencia = bonusdeprof.BonusDeProficiencia(self.__nivel)

    # # Definindo as pericias
    # def pericias(self):
    #     pass


    # Validações

    # Validando textos
    def __validaTexto(self, texto):
        texto = texto.strip()
        texto = texto.replace(' ', '')

        return texto.isalpha()


    # Validando números
    def __validaNum(self, num):
        try:
            int(num)
        except ValueError:
            return False
        return True