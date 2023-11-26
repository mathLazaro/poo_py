class Curso:
    def __init__(self,sigla, nome):
        self.__sigla = sigla
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def nome(self):
        return self.__nome



class Estudante:
    def __init__(self, matricula:int, nome, curso:Curso):
        self.__matricula = int(matricula)
        self.__nome = nome
        self.__curso = curso

    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def curso(self):
        return self.__curso
    


class Equipe:
    def __init__(self, curso:Curso, listaEquipe):
        self.__curso = curso
        self.__equipe = listaEquipe

    @property
    def siglaEquipe(self):
        return self.__curso.sigla

    @property
    def curso(self):
        return self.__curso
    
    @property
    def equipe(self):
        return self.__equipe
    


equipe = Equipe(Curso('cco','ciencia'),['teste'])

print(equipe.siglaEquipe)