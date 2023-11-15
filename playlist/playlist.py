from model import *
from tkinter import *
from tkinter import ttk
from auxiliar import ShowView

class PlaylistView(Toplevel):
    def __init__(self, cad):
        Toplevel.__init__(self)
        self.ctr = True
        self._callbacks = {}
        self.cad = cad

        # window config
        self.title('Cadastrar Playlist')
        self.geometry('300x240')
        self.resizable(False,False)
    
    def GUI_nome(self):
        self._nameField = Frame(self,height=120,bg='gainsboro')
        self._buttonField = Frame(self,height=50,bg='gainsboro')

        Label(self._nameField,text='Nome da playlist:',bg='gainsboro',anchor=W).place(x=50,y=60)
        self.inputNome = Entry(self._nameField,width=25)
        self.inputNome.place(x=50,y=90)

        self._botaoVoltar = Button(self._buttonField,text='Voltar',width=3)
        self._botaoLimpar = Button(self._buttonField,text='Limpar',width=3)
        self._botaoCad = Button(self._buttonField,text='Cadastrar',width=5)

        self.labelDenied = Label(self,text='Insira um nome para a playlist',fg='red')

        self._nameField.pack(fill='x')
        self._buttonField.pack(fill='x')

    def GUI_musicas(self):
        self._nameField.pack_forget()
        self._buttonField.pack_forget()

        self._artistField = Frame(self,height=40,bg='gainsboro')
        self._musicField = Frame(self,height=140,bg='gainsboro')

        # artista (COMBOBOX)
        self.escolha = StringVar()
        Label(self._artistField,text='Escolha o artista:',bg='gainsboro',anchor=W).place(x=50,y=0)
        self._boxArt = ttk.Combobox(self._artistField,width=25,textvariable=self.escolha)
        self._boxArt['values'] = self._listNomeArt
        self._boxArt.place(x=50,y=20)
        self._boxArt.bind('<<ComboboxSelected>>',self._callbacks['mudarLista'])

        # musica (LISTBOX)
        Label(self._musicField,text='Escolha a música:',bg='gainsboro',anchor=W).place(x=50,y=0)
        self.boxMusic = Listbox(self._musicField,width=25)
        self.boxMusic.place(x=50,y=20)

        self._artistField.pack(fill='x',pady=10)
        self._musicField.pack(fill='x')
        self._buttonField.pack(fill='x')

    def interface_mostrar(self):
        self._playlistField = Frame(self,height=120,bg='gainsboro')
        self._buttonField = Frame(self,height=80,bg='gainsboro')

        Label(self._playlistField,text='Buscar playlist:',bg='gainsboro',anchor=W).place(x=50,y=60)
        self.escolha = StringVar()
        self._checkPlay = ttk.Combobox(self,width=25,textvariable=self.escolha)
        self._checkPlay['values'] = self._listPlaylist

        self._checkPlay.place(x=50,y=90)

        self._botaoVoltar = Button(self._buttonField,text='Voltar',width=3)
        self._botaoCad = Button(self._buttonField,text='Procurar',width=5)

        self._playlistField.pack(fill='x')
        self._buttonField.pack(fill='x')

    def add_callback(self,key,method):
        self._callbacks[key] = method

    def bind_commands(self):
        if self.cad:
            print(self.ctr)
            if self.ctr:
                self._botaoCad.config(command=self._callbacks.get('cadastrar'))
                self._botaoLimpar.config(command=self._callbacks.get('limpar'))
                self._botaoVoltar.config(command=self._callbacks.get('voltar'))

                self._botaoCad.place(x=185,y=20,anchor=W)
                self._botaoLimpar.place(x=130,y=20,anchor=W)
                self._botaoVoltar.place(x=75,y=20,anchor=W)
            else:
                self._botaoLimpar.place_forget()
                self._botaoVoltar.place_forget()

                self._botaoCad.config(command=self._callbacks.get('cadastrar'))
                self._botaoVoltar.config(command=self._callbacks.get('voltar'))

                self._botaoCad.place(x=185,y=20,anchor=W)
                self._botaoVoltar.place(x=130,y=20,anchor=W)
        else:
            self._botaoCad.config(command=self._callbacks.get('mostrar'))
            self._botaoVoltar.config(command=self._callbacks.get('voltar'))

            self._botaoCad.place(x=185,y=20,anchor=W)
            self._botaoVoltar.place(x=130,y=20,anchor=W)

    def set_combobox(self, artistas):
        self._listNomeArt = artistas

    def set_listBox(self,lista):
        self.boxMusic.delete(0,END)
        i = 0
        for l in lista:
            self.boxMusic.insert(i,l)
            i+=1

    def set_playlists(self,playlists):
        self._listPlaylist = playlists

    def att_listBox(self,adicionado):
        for ad in adicionado.musicas:
            i=0
            for ele in self.boxMusic.get(0,END):
                if ad.titulo == ele:
                    self.boxMusic.delete(i)
                i+=1

    
class PlaylistControl:
    def __init__(self,main):
        self._main = main

    def _add_callback(self):
        self._view.add_callback('mostrar',self._mostrar)
        self._view.add_callback('cadastrar',self._cadastrar)
        self._view.add_callback('voltar',self._voltar)
        self._view.add_callback('limpar',self._limpar)
        self._view.add_callback('mudarLista',self._mudar_lista)

    def _set_view_art(self):
        lista = []
        for art in self._main.artistas:
            lista.append(art.nome)
        self._view.set_combobox(lista)
    
    def _set_view_play(self):
        lista = []
        for play in self._main.playlists:
            lista.append(play.nome)
        self._view.set_playlists(lista)

    def _set_view_mus(self,art:Artista):
        lista = []
        for mus in art.musicas:
            lista.append(mus.titulo)
        self._view.set_listBox(lista)
        self._view.att_listBox(self._playlistObject)

    def _mostrar(self):
        selecionado = self._view.escolha.get()
        if len(selecionado) != 0:
            for play in self._main.playlists:
                if play.nome == selecionado:
                    playSelect = play
                
            texto = 'Nome da playlist: ' + str(playSelect.nome) + '\n'
            for mus in playSelect.musicas:
                texto += ' . ' + str(mus.titulo) + ' - ' + str(mus.artista.nome) + '\n'
            
            self._view.destroy()
            ShowView('Pesquisa por playlist', texto)
        else:
            self._view.destroy()
            ShowView('Erro','Nenhuma playlist criada ou selecionada')

    def _cadastrar(self):
        if self._view.ctr:
            try:
                nome  = self._view.inputNome.get()
                if len(nome) != 0:
                    self._view.ctr = False
                    self._playlistObject = Playlist(nome)
                    self._view.GUI_musicas()
                    self._view.bind_commands()
                else:
                    raise Exception
            except Exception:
                self._limpar()
                self._view.labelDenied.pack()
        else:
            nomeMusica = self._view.boxMusic.get(ACTIVE)
            for art in self._main.artistas:
                control = False
                for mus in art.musicas:
                    if mus.titulo == nomeMusica:
                        self._playlistObject.add_musica(mus)
                        self._view.att_listBox(self._playlistObject)
                        control = True
                        break
                if control:
                    break
  
    def _limpar(self):
        self._view.labelDenied.pack_forget()
        self._view.inputNome.delete(0,END)

    def _voltar(self):
        if not self._view.ctr and self._view.cad:
            print('teste1')
            if len(self._playlistObject.musicas) == 0:
                del self._playlistObject
                self._view.destroy()
            else:
                print('teste2')
                self._main.playlists.append(self._playlistObject)
                self._view.destroy()
                ShowView('Sucesso','Playlist cadastrada')
        else:
            self._view.destroy()
    
    def _mudar_lista(self,event):
        selecionado = self._view.escolha.get()

        for art in self._main.artistas:
            if art.nome == selecionado:
                self._set_view_mus(art)

    def mostrar_view(self):
        self._main.att_albuns()
        self._view = PlaylistView(True)
        self._add_callback()
        self._set_view_art()
        self._view.GUI_nome()
        self._view.bind_commands()

    def consultar(self):
        self._main.att_albuns()
        self._view = PlaylistView(False)
        self._add_callback()
        self._set_view_play()
        self._view.interface_mostrar()
        self._view.bind_commands()