from tkinter import *
from auxiliar import ShowView
from model import *



class CadastrarView(Toplevel):
    def __init__(self):
        self._callbacks = {}

        Toplevel.__init__(self)
        self.title('Cadastrar jogo')
        self.geometry('300x300')
        self.resizable(FALSE,FALSE)

    def mostrar_view(self):
        Frame(self,height=20).pack()
        self._cod = Frame(self)
        self._tit = Frame(self)
        self._cons = Frame(self)
        self._gen = Frame(self)
        self._preco = Frame(self)

        Label(self._cod,text='Código ',anchor=W).pack(fill='x')
        Label(self._tit,text='Título ',anchor=W).pack(fill='x')
        Label(self._cons,text='Console ',anchor=W).pack(fill='x')
        Label(self._gen,text='Gênero ',anchor=W).pack(fill='x')
        Label(self._preco,text='Preço ',anchor=W).pack(fill='x')

        self.inputCod = Entry(self._cod,width=30)
        self.inputTit = Entry(self._tit,width=30)
        self.inputCons = Entry(self._cons,width=30)
        self.inputGen = Entry(self._gen,width=30)
        self.inputPreco = Entry(self._preco,width=30)

        self.inputCod.pack()
        self.inputTit.pack()
        self.inputCons.pack()
        self.inputGen.pack()
        self.inputPreco.pack()

        self._cod.pack()
        self._tit.pack()
        self._cons.pack()
        self._gen.pack()
        self._preco.pack()

        self._botoes()

    def _botoes(self):
        self._buttonFrame = Frame(self)

        self._voltar = Button(self._buttonFrame,text='Voltar')
        self._limpar = Button(self._buttonFrame,text='Limpar')
        self._confirmar = Button(self._buttonFrame,text='Confirmar')

        self._voltar.pack(side='left')
        self._limpar.pack(side='left')
        self._confirmar.pack(side='left')

        self._buttonFrame.pack(padx=12,pady=10)

    def add_callback(self,key,method):
        self._callbacks[key] = method

    def bind(self):
        self._voltar.bind('<Button>',self._callbacks['voltar'])
        self._limpar.bind('<Button>',self._callbacks['limpar'])
        self._confirmar.bind('<Button>',self._callbacks['confirmar'])



class CadastrarController:
    def __init__(self, jogos:list):
        self._jogos = jogos
        
        self._view = CadastrarView()
        self._pass_callback()
        self._view.mostrar_view()
        self._view.bind()

    def _pass_callback(self):
        self._view.add_callback('voltar',self._voltar)
        self._view.add_callback('limpar',self._limpar)
        self._view.add_callback('confirmar',self._confirmar)

    def _voltar(self,event):
        self._view.destroy()

    def _limpar(self,event):
        self._view.inputCod.delete(0,END)
        self._view.inputCons.delete(0,END)
        self._view.inputGen.delete(0,END)
        self._view.inputPreco.delete(0,END)
        self._view.inputTit.delete(0,END)

    def _confirmar(self,event):
        console = self._view.inputCons.get()
        
        try:
            #print(console.lower())
            if console.lower() in ['xbox','playstation','switch','pc']:
                console = console.capitalize()
            else:
                raise Exception
        except Exception:
            self._view.inputCons.delete(0,END)
            ShowView('Erro','Console incompatível')
            return 

        genero = self._view.inputGen.get()

        try:
            if genero.lower() in ['ação','aventura','estratégia','rpg','esporte','simulação']:
                genero = genero.capitalize()
            elif genero.lower() in ['acao','açao','estrategia','simulacao','simulaçao']:
                if genero.lower() == 'acao' or genero.lower == 'açao':
                    genero = 'Ação'
                elif genero.lower() == 'estrategia':
                    genero = 'Estratégia'
                else:
                    genero = 'Simulação'
            else:
                raise Exception
        except Exception:
            self._view.inputGen.delete(0,END)
            ShowView('Erro','Gênero incompatível')
            return 

        preco = self._view.inputPreco.get()

        try:
            preco = float(preco)
            if preco<=0 or preco >500:
                raise Exception
        except:
            self._view.inputPreco.delete(0,END)
            ShowView('Erro','Preço incompatível.\n O preço deve ser um número real entre 0 e 500')
            return 
        

        codigo = self._view.inputCod.get()
        titulo = self._view.inputTit.get()

        self._jogos.append(Jogo(codigo,titulo,console,genero,preco))
    
        self._view.destroy()
        ShowView('Cadastro','Cadastro realizado')