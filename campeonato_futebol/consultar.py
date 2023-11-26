from tkinter import *
from tkinter import messagebox

class ConsultarView(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('300x200')
        self.title('Consultar equipes')

        self._callbacks = {}
        
    def get_sigla(self):
        self.getSigla = Frame(self)

        self._frameSigla =Frame(self.getSigla)
        self._frameButton = Frame(self.getSigla)

        Label(self._frameSigla,text='Sigla equipe:',anchor=W).pack(fill='x')

        self.inputSilga = Entry(self._frameSigla,width=30)

        self._consultar = Button(self._frameButton, text='Consultar')
        self._cancelar = Button(self._frameButton, text='Cancelar')

        self._consultar.bind('<Button>',self._callbacks['consultar'])
        self._cancelar.bind('<Button>',self._callbacks['cancelar'])

        self.inputSilga.pack()
        self._cancelar.pack(side='left')
        self._consultar.pack(side='left')

        self.getSigla.pack(fill='both',pady=50)
        self._frameSigla.pack(fill='x',padx=20,pady=10)
        self._frameButton.pack(side=RIGHT,padx=20)

    def add_callback(self,key,method):
        self._callbacks[key] = method


class ConsultarController:
    def __init__(self, main):
        self._main = main

        self._view = ConsultarView()
        self._add_callback()
        
        self._view.get_sigla()

    def _add_callback(self):
        self._view.add_callback('consultar',self._consultar)
        self._view.add_callback('cancelar',self._cancelar)

    def _consultar(self,event):
        entry = (self._view.inputSilga.get()).upper()

        for cur in self._main.cursos:
            if cur.sigla == entry:
                curso = cur

        try:
            if curso == curso:
                for eq in self._main.equipes:
                    if eq.siglaEquipe == entry:
                        text = 'Sigla da equipe: ' + str(eq.siglaEquipe)
                        text += '\nEquipe:'
                        print('teste')
                        for est in eq.equipe:
                            print(str(est.nome))
                            text += '\n . ' + str(est.nome)

                        messagebox.showinfo('Consulta',text)
                        return
                messagebox.showerror('Erro','Não existe equipe desse curso')
        except:
            messagebox.showerror('Erro','Esta sigla do curso não existe')

    def _cancelar(self,event):
        self._view.destroy()