# from habilidades import modificador
# from habilidades import bonusdeprof

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
        classes = {1: 'Bárbaro', 2: 'Bardo', 3: 'Bruxo', 4: 'Clérigo', 5: 'Druida', 6: 'Feiticeiro', 7: 'Guerreiro', 8: 'Ladino', 9: 'Mago', 10: 'Monge', 11: 'Paladino', 12: 'Patrulheiro'}
        return classes[int(classePorExtenso)]


    # Nível
    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, novoNivel):
        assert self.__validaNum(novoNivel) == True and (int(novoNivel) >= 1 and int(novoNivel) <= 30)
        self.__nivel = novoNivel


    # Antecedente
    @property
    def antecedente(self):
        return self.__antecedente
    
    @antecedente.setter
    def antecedente(self, novoAntecedente): 
        assert self.__validaNum(novoAntecedente) == True and (int(novoAntecedente) >= 1 and int(novoAntecedente) <= 12)
        self.__antecedente = self.__antecedentePorExtenso(novoAntecedente)

    def __antecedentePorExtenso(self, antecedentePorExtenso):
        antecedentes = {1: 'Acólito', 2: 'Artesão de Guilda', 3: 'Artista', 4: 'Charlatão', 5: 'Criminoso', 6: 'Eremita', 7: 'Forasteiro', 8: 'Herói do Povo', 9: 'Marinheiro', 10: 'Nobre', 11: 'Orfão', 12: 'Sábio'}
        return antecedentes[int(antecedentePorExtenso)]


    # Nome do Jogador
    @property
    def nomeDoJogador(self):
        return self.__nomeDoJogador
    
    @nomeDoJogador.setter
    def nomeDoJogador(self, novoNome):
        assert self.__validaTexto(novoNome) == True
        self.__nomeDoJogador = novoNome


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