from model import *
from tkinter import *
from tkinter import ttk
from auxiliar import ShowView

##

class ArtistaView(Toplevel):
    def __init__(self, cad:bool):
        Toplevel.__init__(self)
        self._cad = cad
        self.geometry('300x200')
        self.resizable(False,False)
        
        self._callbacks = {}

        if cad:
            self.title('Cadastrar Artista')
            self._interface_cadastro()
        else:
            self.title('Consultar Artistas')
   
    def _interface_cadastro(self):
    
        self._nameField = Frame(self,width=300,height=120,bg='gainsboro')
        self._buttonField = Frame(self,width=300,height=40,bg='gainsboro')

        Label(self._nameField,text='Nome do artista:',bg='gainsboro',anchor=W).place(x=50,y=60)
        self.inputName = Entry(self._nameField,width=25)
        
        self.inputName.place(x=50,y=90)

        self._botaoVoltar = Button(self._buttonField,text='Voltar',width=3)
        self._botaoLimpar = Button(self._buttonField,text='Limpar',width=3)
        self._botaoCad = Button(self._buttonField,text='Cadastrar',width=5)
        
        self.labelConfirm = Label(self,text='Artista cadastrado',fg='green')

        self._nameField.pack()
        self._buttonField.pack()

    def interface_mostrar(self):
        self._nomeArtista = Frame(self,height=120,bg='gainsboro')
        self._buttonField = Frame(self,height=80,bg='gainsboro')

        Label(self,text='Buscar obras por artista:',bg='gainsboro',anchor=W).place(x=50,y=60)
        self.escolha = StringVar()
        self._checkArt = ttk.Combobox(self,width=25,textvariable=self.escolha)
        self._checkArt['values'] = self._listaArt

        self._checkArt.place(x=50,y=90)

        self._botaoVoltar = Button(self._buttonField,text='Voltar',width=3)
        self._botaoCad = Button(self._buttonField,text='Procurar',width=5)

        self._nomeArtista.pack(fill='x')
        self._buttonField.pack(fill='x')

    def confirmar(self):
        self.labelConfirm.pack()

    def clean(self):
        self.labelConfirm.pack_forget()

    def add_callback(self,key,method):
        self._callbacks[key] = method

    def bind_commands(self):
        if self._cad:
            self._botaoCad.config(command=self._callbacks.get('cadastrar'))
            self._botaoLimpar.config(command=self._callbacks.get('limpar'))
            self._botaoVoltar.config(command=self._callbacks.get('voltar'))
            
            self._botaoCad.place(x=185,y=20,anchor=W)
            self._botaoLimpar.place(x=130,y=20,anchor=W)
            self._botaoVoltar.place(x=75,y=20,anchor=W)
        else:
            self._botaoCad.config(command=self._callbacks.get('mostrar'))
            self._botaoVoltar.config(command=self._callbacks.get('voltar'))

            self._botaoCad.place(x=185,y=20,anchor=W)
            self._botaoVoltar.place(x=130,y=20,anchor=W)

    def set_listaArt(self,lista):
        self._listaArt = lista


##
##

class ArtistaControl:
    def __init__(self, main):
        self._main = main

    def _add_callback(self):
        self._view.add_callback('mostrar',self._mostrar)
        self._view.add_callback('cadastrar',self._cadastrar)
        self._view.add_callback('voltar',self._voltar)
        self._view.add_callback('limpar',self._limpar)

    def _mostrar(self):
        selecionado = self._view.escolha.get()

        if len(selecionado) != 0:
            artistas = self._main.artistas
            texto = 'Artista:' + str(selecionado) + '\n' 

            for art in artistas:
                if selecionado == art.nome:
                    texto += 'Ábuns:\n'
                    for alb in art.albuns:
                        texto += ' . ' + str(alb.titulo) + '\n'
                        for mus in alb.musicas:
                            texto += '   > ' + str(mus.titulo) + '\n'

            self._view.destroy()
            ShowView('Pesquisa por artista',texto)

    def _cadastrar(self):
        nome = self._view.inputName.get()
        artista = Artista(nome)
        if len(nome) != 0:
            self._limpar()
            self._view.confirmar()
        self._main.add_artista(artista)

    def _limpar(self):
        self._view.inputName.delete(0,END)
        self._view.clean()

    def _voltar(self):
        self._view.destroy()

    def mostrar_view(self):
        self._view = ArtistaView(True)
        self._add_callback()
        self._view.bind_commands()

    def consultar(self):
        self._main.att_albuns()
        lista = []
        
        for art in self._main.artistas:
            lista.append(art.nome)
        self._view = ArtistaView(False)

        self._view.set_listaArt(lista)
        self._view.interface_mostrar()
        self._add_callback()
        self._view.bind_commands()