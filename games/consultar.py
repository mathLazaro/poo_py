from tkinter import *
from tkinter import ttk
from model import *
from auxiliar import ShowView


class ConsultarView(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Consultar jogos')
        self.geometry('300x200')
        self.resizable(FALSE,FALSE)

        self._callbacks = {}

        Frame(self,height=50).pack(fill='both')

    def mostrar_view(self):
        self._frame = Frame(self)
        self._frame.config(width=300,height=200)

        self._ava = Frame(self._frame)
        self._button = Frame(self._frame)

        self.escolha = IntVar()
        self._avaliacoes = ttk.Combobox(self._ava,width=30,textvariable=self.escolha)
        self._avaliacoes['values'] = [1,2,3,4,5]

        self._voltar = Button(self._button, text='Voltar')
        self._consultar = Button(self._button, text='Consultar')

        self._voltar.bind('<Button>',self._callbacks['voltar'])
        self._consultar.bind('<Button>',self._callbacks['consultar'])

        self._avaliacoes.pack(pady=20)
        self._voltar.pack(side='left')
        self._consultar.pack(side='left')

        self._ava.pack()
        self._button.pack(side='right',ipadx=20)
        self._frame.pack()

    def add_callback(self,key,method):
        self._callbacks[key] = method


        
class ConsultarController:
    def __init__(self, jogos:list):
        self._jogos = jogos

        self._view = ConsultarView()
        self._pass_callbacks()
        self._view.mostrar_view()

    def _pass_callbacks(self):
        self._view.add_callback('voltar',self._voltar)
        self._view.add_callback('consultar',self._consultar)

    def _voltar(self,event):
        self._view.destroy()

    def _consultar(self,event):
        sel = self._view.escolha.get()
        text = 'Jogos com ' + str(sel) + ' estrelas:\n\n'

        if sel == 1 or sel == 2 or sel == 3 or sel == 4 or sel == 5:
            for jg in self._jogos:
                if jg.avg_avaliacoes() == sel:
                    text += ' . código: ' + str(jg.codigo) + '\n'
                    text += '   título: ' + str(jg.titulo) + '\n'
                    text += '   preço: ' + str("%.2f" % jg.preco) + '\n'
                    text += '   console: ' + str(jg.console) + '\n'
                    text += '   gênero: ' + str(jg.genero) + '\n\n'

            ShowView('Consulta',text)