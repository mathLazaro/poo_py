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
        self.__console = console
        self.__genero = genero
        self.__preco = preco

        self.__avaliacoes = []

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo

    @property
    def console(self):
        return self.__console
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def avaliacoes(self):
        return self.__avaliacoes
    
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
