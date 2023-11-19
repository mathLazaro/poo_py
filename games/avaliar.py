from tkinter import *
from tkinter import ttk
from auxiliar import ShowView
from model import *


class FrameAvaliacao(Frame):
    def __init__(self,root,callbacks):
        Frame.__init__(self,root)

        self.config(width=300,height=200)

        self._head = Frame(self)
        self._ava = Frame(self)
        self._button = Frame(self)

        self._labelHead: Label

        self.escolha = StringVar()
        self._avaliacoes = ttk.Combobox(self._ava,width=30,textvariable=self.escolha)
        self._avaliacoes['values'] = [1,2,3,4,5]

        self._voltar = Button(self._button, text='Voltar')
        self._adicionar = Button(self._button, text='Adicionar')

        self._voltar.bind('<Button>',callbacks['voltar'])
        self._adicionar.bind('<Button>',callbacks['adicionar'])

        self._avaliacoes.pack(pady=20)
        self._voltar.pack(side='left')
        self._adicionar.pack(side='left')

        self._head.pack(fill='x')
        self._ava.pack()
        self._button.pack(side='right',ipadx=20)

    def add_label(self,cod:str):
        try:
            self._labelHead.pack_forget()
        except:
            pass
        finally:
            self._labelHead = Label(self._head,text=str('O código do jogo avaliado é \'' + cod + '\''),anchor=W)
            self._labelHead.pack()



class FrameCodigo(Frame):
    def __init__(self,root,callbacks):
        Frame.__init__(self,root)

        self.config(width=300,height=200)
        
        self._cod = Frame(self)
        self._button = Frame(self)

        Label(self._cod,text='Código do jogo',anchor=W).pack(fill='x')
        
        self.inputCod = Entry(self._cod,width=30)
        self.inputCod.pack()

        self._voltar = Button(self._button, text='Voltar')
        self._limpar = Button(self._button, text='Limpar')
        self._avaliar = Button(self._button, text='Avaliar')
        
        self._voltar.bind('<Button>',callbacks['destroy'])
        self._limpar.bind('<Button>',callbacks['limpar'])
        self._avaliar.bind('<Button>',callbacks['avaliar'])

        self._voltar.pack(side='left')
        self._limpar.pack(side='left')
        self._avaliar.pack(side='left')

        self._cod.pack()
        self._button.pack(ipadx=0,pady=20,side='right',fill='x')
        


class AvaliarView(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Avaliar Jogo')
        self.geometry('300x200')
        self.resizable(FALSE,FALSE)

        self._callbacks = {}

        Frame(self,height=50).pack(fill='both')

    def instace_frame(self):
        self.frameCod = FrameCodigo(self,self._callbacks)
        self.frameAva = FrameAvaliacao(self,self._callbacks)

    def add_callback(self,key,method):
        self._callbacks[key] = method



class AvaliarController:
    def __init__(self, jogos:list):
        self._jogos = jogos

        self._view = AvaliarView()
        self._pass_callbacks()
        self._view.instace_frame()
        self._view.frameCod.pack()

    def _pass_callbacks(self):
        self._view.add_callback('voltar',self._voltar)
        self._view.add_callback('destroy',self._destroy)
        self._view.add_callback('limpar',self._limpar)
        self._view.add_callback('avaliar',self._avaliar)
        self._view.add_callback('adicionar',self._adicionar)

    def _voltar(self,event):
        self._view.frameAva.pack_forget()
        self._view.frameCod.pack()

    def _destroy(self,event):
        self._view.destroy()

    def _limpar(self,event):
        self._view.frameCod.inputCod.delete(0,END)

    def _avaliar(self,event):
        codigo = self._view.frameCod.inputCod.get()
        
        if len(codigo):
            for jg in self._jogos:
                if jg.codigo == codigo:
                    self._jogoSel = jg
                    self._view.frameCod.pack_forget()
                    self._view.frameAva.add_label(codigo)
                    self._view.frameAva.pack()
                    return
                
            ShowView('Erro','Não há nenhum jogo cadastrado com esse código')
            self._limpar('limpar')
    
    def _adicionar(self,event):
        sel = self._view.frameAva.escolha.get()

        if len(sel) != 0:
            sel = int(sel)
            if sel == 1 or sel == 2 or sel == 3 or sel == 4 or sel == 5:
                self._jogoSel.add_avaliacoes(Avaliacao(int(sel)))
                ShowView('Sucesso',str('Avaliação adicionada para o jogo de código \''\
                                        + self._jogoSel.codigo + '\''))