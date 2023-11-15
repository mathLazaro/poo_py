from model import *
from tkinter import *
from tkinter import ttk
from auxiliar import ShowView


class AlbumView(Toplevel):
    def __init__(self,cad:bool):
        Toplevel.__init__(self)
        self.cad = cad
        self.albumControl = True # TRUE - cria o album - FALSE - add musica
        self._callbacks = {}

        self.geometry('300x200')
        self.resizable(False,False)

        if cad:
            self.title('Cadastrar Álbum')
            self._GUI_album()
        else:
            self.title('Mostrar álbuns')

    def _GUI_album(self):
        
        self._insertField = Frame(self,height=140,bg='gainsboro')
        self._buttonField = Frame(self,height=40,bg='gainsboro')

        Label(self._insertField,text='Título do álbum:',bg='gainsboro',anchor=W).place(x=50,y=11)
        Label(self._insertField,text='Nome do artista:',bg='gainsboro',anchor=W).place(x=50,y=51)
        Label(self._insertField,text='Ano do álbum:',bg='gainsboro',anchor=W).place(x=50,y=91)
        
        self.inptAlbumNome = Entry(self._insertField,width=25)
        self.inptArtNome = Entry(self._insertField,width=25)
        self.inptAlbumAno = Entry(self._insertField,width=25)

        self.inptAlbumNome.place(x=50,y=30)
        self.inptArtNome.place(x=50,y=70)
        self.inptAlbumAno.place(x=50,y=110)

        self._botaoVoltar = Button(self._buttonField,text='Voltar',width=3)
        self._botaoLimpar = Button(self._buttonField,text='Limpar',width=3)
        self._botaoCad = Button(self._buttonField,text='Cadastrar',width=5)

        self.artistaDenied = Label(self,text='Artista desconhecido',fg='red')
        self.anoDenied = Label(self,text='Insira um número para o ano',fg='red')

        self._insertField.pack(fill='x')
        self._buttonField.pack(fill='x')

    def GUI_musica(self):
        self.artistaDenied.pack_forget()
        self.anoDenied.pack_forget()
        self._insertField.pack_forget()
        self._buttonField.pack_forget()

        self._insMusField = Frame(self,height=120,bg='gainsboro')

        Label(self._insMusField,text='Nome da música:',bg='gainsboro',anchor=W).place(x=50,y=31)
        Label(self._insMusField,text='Número da faixa:',bg='gainsboro',anchor=W).place(x=50,y=71)
        
        self.inptMusicaNome = Entry(self._insMusField,width=25)
        self.inptFaixa = Entry(self._insMusField,width=25)

        self.musicaConfirm = Label(self,text='Música adicionada',fg='green')
        self.musicaDenied = Label(self,text='Insira um número para a faixa',fg='red')

        self.inptMusicaNome.place(x=50,y=50)
        self.inptFaixa.place(x=50,y=90)

        self._insMusField.pack(fill='x')
        self._buttonField.pack(fill='x')

    def interface_mostrar(self):
        self._titulo = Frame(self,height=120,bg='gainsboro')
        self._buttonField = Frame(self,height=80,bg='gainsboro')

        Label(self._titulo,text='Buscar músicas por álbum:',bg='gainsboro',anchor=W).place(x=50,y=60)
        self.escolha = StringVar()
        self._checkAlb = ttk.Combobox(self,width=25,textvariable=self.escolha)
        self._checkAlb['values'] = self._listaAlbum

        self._checkAlb.place(x=50,y=90)

        self._botaoVoltar = Button(self._buttonField,text='Voltar',width=3)
        self._botaoCad = Button(self._buttonField,text='Procurar',width=5)

        self._titulo.pack(fill='x')
        self._buttonField.pack(fill='x')

    def add_callback(self,key,method):
        self._callbacks[key] = method

    def bind_commands(self):
        if self.cad:
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

    def set_listaAlbum(self,lista):
        self._listaAlbum = lista


class AlbumControl:
    def __init__(self, main):
        self._main = main

    def _add_callback(self):
        self._view.add_callback('mostrar',self._mostrar) #procurar
        self._view.add_callback('cadastrar',self._cadastrar)
        self._view.add_callback('voltar',self._voltar)
        self._view.add_callback('limpar',self._limpar)

    # funções dos botões

    def _mostrar(self):
        escolha = self._view.escolha.get()

        if len(escolha) != 0:
            album = 'a'
            
            for art in self._main.artistas:
                aux = False
                for alb in art.albuns:
                    if escolha == alb.titulo:
                        album = alb
                        break
                if aux:
                    break

            texto = 'Nome do artista: ' + str(album.artista.nome) + '\n'
            texto += 'Título do álbum: ' + str(album.titulo) + '\n'
            texto += 'Ano de lançamento: ' + str(album.ano) + '\n'

            for mus in album.musicas:
                texto += ' . faixa ' + str(mus.nroFaixa) + ' - ' + mus.titulo + '\n'

            self._view.destroy()
            ShowView('Pesquisa de álbum por título',texto)

    def _cadastrar(self):
        if self._view.albumControl: # cria o album
            artista = self._view.inptArtNome.get()
            for art in self._main.artistas:
                if art.nome == artista:
                    anoAlbum = self._view.inptAlbumAno.get()
                    try:
                        anoAlbum = int(anoAlbum)
                        nomeAlbum = self._view.inptAlbumNome.get()
                        self._album = Album(nomeAlbum,anoAlbum,art)
                        self._view.albumControl = False
                        self._view.GUI_musica()
                        return
                    except Exception:
                        self._limpar()
                        self._view.anoDenied.pack()
                        return
                
            self._limpar()
            self._view.artistaDenied.pack()
        else:
            nome = self._view.inptMusicaNome.get()
            faixa = self._view.inptFaixa.get()
            try:
                faixa = int(faixa)
                self._album.add_musica(Musica(nome,faixa,self._album))
                self._limpar()
                self._view.musicaConfirm.pack()
            except Exception:
                self._limpar()
                self._view.musicaDenied.pack()

    def _voltar(self):
        if self._view.cad and not self._view.albumControl:
            if len(self._album.musicas) == 0:
                ShowView('AVISO','O álbum deve conter no mínimo 1 música')
            else:
                self._view.destroy()
                ShowView('Sucesso','Álbum cadastrado com sucesso')
        else:
            self._view.destroy()

    def _limpar(self):
        if self._view.albumControl:
            self._view.artistaDenied.pack_forget()
            self._view.anoDenied.pack_forget()
            self._view.inptArtNome.delete(0,END)
            self._view.inptAlbumAno.delete(0,END)
            self._view.inptAlbumNome.delete(0,END)
        else:
            self._view.musicaConfirm.pack_forget()
            self._view.musicaDenied.pack_forget()
            self._view.inptMusicaNome.delete(0,END)
            self._view.inptFaixa.delete(0,END)

    # ************************

    def mostrar_view(self):
        self._view = AlbumView(True)
        self._add_callback()
        self._view.bind_commands()

    def consultar(self):
        self._main.att_albuns()
        lista = []

        for art in self._main.artistas:
            for alb in art.albuns:
                lista.append(alb.titulo)

        self._view = AlbumView(False)
        self._view.set_listaAlbum(lista)
        self._view.interface_mostrar()
        self._add_callback()
        self._view.bind_commands()