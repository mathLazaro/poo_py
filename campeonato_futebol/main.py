from tkinter import *
from tkinter import messagebox
import pickle as pk
import os.path

from criar import CriarController
from consultar import ConsultarController

from model import *


class MainView:
    def __init__(self) -> None:
        self._callbacks = {} # MainController callbacks
        
        self._win = Tk()     # root
        self._menu_config()
        self._win_config()

    def _win_config(self):
        self._win.title('Cadastro de')
        self._win.geometry('300x200')
        self._win.config(menu=self._menu)
    
    def _menu_config(self):
        self._menu = Menu(self._win,tearoff=FALSE)
        self._equipe = Menu(self._menu,tearoff=FALSE)
        self._menu.add_cascade(label='Equipe',menu=self._equipe)

    def add_callback(self, key, method):
        self._callbacks[key] = method

    def bind(self):
        self._equipe.add_command(label='Criar equipe',command=self._callbacks['criar'])
        self._equipe.add_command(label='Consultar equipe',command=self._callbacks['consultar'])
        self._equipe.add_command(label='Imprimir dados',command=self._callbacks['imprimir'])
        self._menu.add_command(label='Salvar e fechar',command=self._callbacks['salvar'])

    def run(self):
        self._win.mainloop()

    def close(self):
        self._win.destroy()



class MainController:
    def __init__(self) -> None:
        self._inputCursos()
        if not os.path.isfile('equipe.pickle'):
            self.equipes = []
        else:
            with open('equipe.pickle', 'rb') as file:
                self.equipes = pk.load(file)

        # instancia a classe da interface principal
        self._view = MainView()
        
        # passa callback para o view
        self._pass_callback()
        # 'binda' os comandos na view
        self._view.bind()
        
        self._view.run()
        self.__listaCurso = []
        self.__listaEstudante = []

    @property
    def cursos(self):
        return self.__listaCurso
    
    @property
    def estudantes(self):
        return self.__listaEstudante
    
    def _inputCursos(self):
        c1 = Curso("CCO", "Ciência da Computação")
        c2 = Curso("SIN", "Sistemas de Informação")
        c3 = Curso("EEL", "Engenharia Elétrica")
        listaCurso = []
        listaCurso.append(c1)
        listaCurso.append(c2)
        listaCurso.append(c3)
        listaEstudante = []
        listaEstudante.append(Estudante(1001, "José da Silva", c1))
        listaEstudante.append(Estudante(1002, "João de Souza", c1))
        listaEstudante.append(Estudante(1003, "Rui Santos", c1))
        listaEstudante.append(Estudante(1004, "Reinaldo Lima", c2))
        listaEstudante.append(Estudante(1005, "Gabriel Soares", c2))
        listaEstudante.append(Estudante(1006, "Fernando Fernandes", c2))
        listaEstudante.append(Estudante(1007, "Luana Lua", c2))
        listaEstudante.append(Estudante(1008, "Deide Costa", c3))
        listaEstudante.append(Estudante(1009, "Carina Clara", c3))
        listaEstudante.append(Estudante(1010, "Jorge Georgia", c3))

        self.__listaCurso = listaCurso
        self.__listaEstudante = listaEstudante

    def _pass_callback(self):
        self._view.add_callback('criar',self._criar)
        self._view.add_callback('consultar',self._consultar)
        self._view.add_callback('imprimir',self._imprimir)
        self._view.add_callback('salvar',self._salvar)
    
    def _criar(self):
        CriarController(self)

    def _consultar(self):
        ConsultarController(self)
    
    def _imprimir(self):
        numEquipe = len(self.equipes)
        numEstudantes = 0
        
        for equipe in self.equipes:
            numEstudantes += len(equipe.equipe)
        
        if numEquipe != 0:
            avgEstEquipe = numEstudantes / numEquipe
        else:
            avgEstEquipe = 0

        text = 'Dados do campeonato:'
        text += '\n - Número de equipes: ' + str(numEquipe)
        text += '\n - Número total de estudantes participantes: ' + str(numEstudantes)
        text += '\n - Média de estudante por equipe: ' + str(avgEstEquipe)

        messagebox.showinfo('Imprimir',text)

    def _salvar(self):
        if len(self.equipes) != 0:
            with open('equipe.pickle','wb') as file:
                pk.dump(self.equipes, file)
        self._view.close()

if __name__ == '__main__':
    MainController()