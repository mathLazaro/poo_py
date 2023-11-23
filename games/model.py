from math import ceil

class Avaliacao:
    def __init__(self, nota: int) -> None:
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

class Jogo:
    def __init__(self, codigo, titulo: str, console: str, genero: str, preco: float) -> None:
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco

        self.__avaliacoes = []

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo

    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
    @property
    def console(self):
        return self.__console
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def preco(self):
        return self.__preco
    
    @console.setter
    def console(self, console):
        valido = ['Xbox','Playstation','Switch','Pc']
        if not console in valido:
            raise ValueError(f'Console inválido: {console}')
        else:
            self.__console = console
    
    @genero.setter
    def genero(self,genero):
        valido = ['Ação','Aventura','Estratégia','Rpg','Esporte','Simulação']
        if not genero in valido:
            raise ValueError(f'Gênero inválido: {genero}')
        else:
            self.__genero = genero
    
    @preco.setter
    def preco(self, preco):
        if preco <= 0 or preco > 500:
            raise ValueError(f'Preço inválido: {preco}')
        else:
            self.__preco = preco
    
    def add_avaliacoes(self, avaliacao: Avaliacao):
        self.__avaliacoes.append(avaliacao)
    
    def avg_avaliacoes(self) -> int:
        soma = 0
        for ava in self.__avaliacoes:
            soma += ava.nota

        try:
            return ceil(soma / len(self.__avaliacoes))
        except:
            return 0
