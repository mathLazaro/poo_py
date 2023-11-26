from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model import *

class CriarView(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('300x200')
        self.title('Criar Equipe')

        self._callbacks = {}
        

    def sel_curso(self,siglas):
        self.selCurso = Frame(self)

        self._frameCombo =Frame(self.selCurso)
        self._frameButton = Frame(self.selCurso)

        Label(self._frameCombo,text='Curso:',anchor=W).pack(fill='x')

        self.escolha = StringVar()

        self._cursos = ttk.Combobox(self._frameCombo,width=30,textvariable=self.escolha)
        self._cursos['values'] = siglas

        self._confirmar = Button(self._frameButton, text='Confirmar')
        self._cancelar = Button(self._frameButton, text='Cancelar')

        self._confirmar.bind('<Button>',self._callbacks['confirmar'])
        self._cancelar.bind('<Button>',self._callbacks['cancelar'])

        self._cursos.pack()
        self._cancelar.pack(side='left')
        self._confirmar.pack(side='left')

        self.selCurso.pack(fill='both',pady=50)
        self._frameCombo.pack(fill='x',padx=20,pady=10)
        self._frameButton.pack(side=RIGHT,padx=20)

    def sel_estudantes(self):
        self.selEstudantes = Frame(self)

        self._frameMat =Frame(self.selEstudantes)
        self._frameButton = Frame(self.selEstudantes)

        Label(self._frameMat,text='Estudante:',anchor=W).pack(fill='x')

        self.inputEstudante = Entry(self._frameMat,width=30)

        self._adicionar = Button(self._frameButton, text='Adicionar')
        self._voltar = Button(self._frameButton, text='Voltar')
        self._criar = Button(self._frameButton, text='Criar Equipe')

        self._criar.bind('<Button>',self._callbacks['criar'])
        self._adicionar.bind('<Button>',self._callbacks['adicionar'])
        self._voltar.bind('<Button>',self._callbacks['voltar'])

        self.inputEstudante.pack()
        self._voltar.pack(side='left')
        self._adicionar.pack(side='left')
        self._criar.pack(side='left')

        self.selEstudantes.pack(fill='both',pady=50)
        self._frameMat.pack(fill='x',padx=20,pady=10)
        self._frameButton.pack(side=RIGHT,padx=20)

    def add_callback(self,key,method):
        self._callbacks[key] = method


class CriarController:
    def __init__(self, main):
        self._main = main

        self._view = CriarView()
        self._add_callback()
        self._cursoView()

    def _cursoView(self):
        siglas = []
        cursosCadastrados = []
        
        for equ in self._main.equipes:
            cursosCadastrados.append(equ.siglaEquipe)


        for curso in self._main.cursos:
            if not curso.sigla in cursosCadastrados:
                siglas.append(curso.sigla)
        
        self._view.sel_curso(siglas)

    def _add_callback(self):
        self._view.add_callback('confirmar',self._confirmar)
        self._view.add_callback('cancelar',self._cancelar)
        self._view.add_callback('voltar',self._voltar)
        self._view.add_callback('adicionar',self._adicionar)
        self._view.add_callback('criar',self._criar)

    def _confirmar(self,event):
        self._cursoEscolhido = self._view.escolha.get()
        self._listEst = []

        self._view.selCurso.pack_forget()
        self._view.sel_estudantes()

    def _cancelar(self,event):
        self._view.destroy()
    
    def _adicionar(self,event):
        get = int(self._view.inputEstudante.get())

        for est in self._main.estudantes:
            if get == est.matricula:
                estudante = est
                break

        try:
            if estudante.curso.sigla == self._cursoEscolhido:
                if not estudante in self._listEst:
                    self._listEst.append(estudante)
                    messagebox.showinfo('Sucesso',f'Aluno \'{estudante.nome}\' adicionado na lista')
                else:
                    messagebox.showerror('Erro','O aluno já foi adicionado na lista')
            else:
                messagebox.showerror('Erro','O curso do aluno não é o mesmo do time')
        except:
            messagebox.showerror('Erro','Não há nenhum aluno com essa matrícula')

    def _voltar(self,event):
        self._view.selEstudantes.pack_forget()
        self._cursoView()
    
    def _criar(self,event):
        if len(self._listEst) != 0:
            for cur in self._main.cursos:
                if cur.sigla == self._cursoEscolhido:
                    self._main.equipes.append(Equipe(cur,self._listEst))
                    self._voltar(event)
                    messagebox.showinfo('Sucesso','Equipe criada')

        else:
            messagebox.showerror('Erro','A equipe deve conter pelo menos um aluno na lista')