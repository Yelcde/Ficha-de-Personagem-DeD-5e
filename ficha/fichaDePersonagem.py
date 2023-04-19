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
        self.__bonusDeExperiencia = None

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
        assert self.__validaNum(novoNivel) == True and (int(novoNivel) >= 1 and int(novoNivel) <= 20)
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
    def nomeDoJogador(self, novoNomeDoJogador):
        assert self.__validaTexto(novoNomeDoJogador) == True
        self.__nomeDoJogador = novoNomeDoJogador

    
    # Raça
    @property
    def raca(self):
        return self.__raca
    
    @raca.setter
    def raca(self, novaRaca): 
        assert self.__validaNum(novaRaca) == True and (int(novaRaca) >= 1 and int(novaRaca) <= 9)
        self.__raca = self.__racaPorExtenso(novaRaca)

    def __racaPorExtenso(self, racaPorExtenso):
        raca = {1: 'Anão', 2: 'Elfo', 3: 'Halfling', 4: 'Humano', 5: 'Draconato', 6: 'Gnomo', 7: 'Meio-Elfo', 8: 'Meio-Orc', 9: 'Tiefling'}
        return raca[int(racaPorExtenso)]


    # Tendência
    @property
    def tendencia(self):
        return self.__tendencia
    
    @tendencia.setter
    def tendencia(self, novatendencia): 
        assert self.__validaNum(novatendencia) == True and (int(novatendencia) >= 1 and int(novatendencia) <= 9)
        self.__tendencia = self.__tendenciaPorExtenso(novatendencia)

    def __tendenciaPorExtenso(self, novatendencia):
        tendencias = {1: 'Leal e Bom (LB)', 2: 'Neutro e Bom (NB)', 3: 'Caótico e Bom (CB)', 4: 'Leal e Neutro (LN)', 5: 'Neutro (N)', 6: 'Caótico e Neutro (CN)', 7: 'Leal e Mau (LM)', 8: 'Neutro e Mau (NM)', 9: 'Caótico e Mau (CM)'}
        return tendencias[int(novatendencia)]


    # Pontos de Experiencia
    @property
    def pontosDeExperiencia(self):
        return self.__pontosDeExperiencia
    
    @pontosDeExperiencia.setter
    def pontosDeExperiencia(self, novosPontosDeExperiencia):
        assert self.__validaNum(novosPontosDeExperiencia) == True and int(novosPontosDeExperiencia) >= 0
        self.__pontosDeExperiencia = novosPontosDeExperiencia


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