from tkinter import *
from cadastrar import CadastrarController
from avaliar import AvaliarController
from consultar import ConsultarController
import pickle as pk
import os.path


class MainView:
    def __init__(self) -> None:
        self._callbacks = {} # MainController callbacks
        
        self._win = Tk()     # root
        self._menu_config()
        self._win_config()

    def _win_config(self):
        self._win.title('Sistema de jogos')
        self._win.geometry('300x200')
        self._win.config(menu=self._menu)
    
    def _menu_config(self):
        self._menu = Menu(self._win,tearoff=FALSE)
        self._menuJogo = Menu(self._menu,tearoff=FALSE)
        self._menu.add_cascade(label='Jogo',menu=self._menuJogo)

    def add_callback(self, key, method):
        self._callbacks[key] = method

    def bind(self):
        self._menuJogo.add_command(label='Cadastrar',command=self._callbacks['cadastrar'])
        self._menuJogo.add_command(label='Avaliar',command=self._callbacks['avaliar'])
        self._menuJogo.add_command(label='Consultar',command=self._callbacks['consultar'])
        self._menu.add_command(label='Salvar e fechar',command=self._callbacks['salvar'])

    def run(self):
        self._win.mainloop()

    def close(self):
        self._win.destroy()



class MainController:
    def __init__(self) -> None:
        if not os.path.isfile('jogos.pickle'):
            self.jogos = []
        else:
            with open('jogos.pickle', 'rb') as file:
                self.jogos = pk.load(file)

        # instancia a classe da interface principal
        self._view = MainView()
        
        # passa callback para o view
        self._pass_callback()
        # 'binda' os comandos na view
        self._view.bind()
        
        self._view.run()

    def _pass_callback(self):
        self._view.add_callback('cadastrar',self._cadastrar)
        self._view.add_callback('avaliar',self._avaliar)
        self._view.add_callback('consultar',self._consultar)
        self._view.add_callback('salvar',self._salvar)
    
    def _cadastrar(self):
        CadastrarController(self.jogos)

    def _avaliar(self):
        AvaliarController(self.jogos)

    def _consultar(self):
        ConsultarController(self.jogos)

    def _salvar(self):
        if len(self.jogos) != 0:
            with open('jogos.pickle','wb') as file:
                pk.dump(self.jogos, file)
        self._view.close()



if __name__ == '__main__':
    MainController()