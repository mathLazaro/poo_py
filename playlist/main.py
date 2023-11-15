from typing import Any
import album as ab
import artista as at
import playlist as pl
import tkinter as tk
from model import *

class MainView:
    def __init__(self):
        self._root = tk.Tk()
        self._callbacks = {}
        self._menu_config()
        self._win_config()

    def _win_config(self):
        self._root.title('Playlist')
        self._root.geometry('300x200')
        self._root.config(bg='gainsboro',menu=self._menu)
        self._root.resizable(False,False)

    def _menu_config(self):
        self._menu = tk.Menu(self._root)
        self._artistaMenu = tk.Menu(self._menu)
        self._albumMenu = tk.Menu(self._menu)
        self._playlistMenu = tk.Menu(self._menu)

        self._menu.add_cascade(label='Artista',menu=self._artistaMenu)
        self._menu.add_cascade(label='Álbum',menu=self._albumMenu)
        self._menu.add_cascade(label='Playlist',menu=self._playlistMenu)

    def run(self):
        self._root.mainloop()

    def add_callback(self,key,method):
        self._callbacks[key] = method

    def bind_commands(self):
        self._artistaMenu.add_command(label='Cadastrar',command=self._callbacks['cad_art'])
        self._artistaMenu.add_command(label='Consultar',command=self._callbacks['cons_art'])
        self._albumMenu.add_command(label='Cadastar',command=self._callbacks['cad_alb'])
        self._albumMenu.add_command(label='Consultar',command=self._callbacks['cons_alb'])
        self._playlistMenu.add_command(label='Cadastar',command=self._callbacks['cad_play'])
        self._playlistMenu.add_command(label='Consultar',command=self._callbacks['cons_play'])


class MainController:
    def __init__(self, view: MainView):
        self._artistas = []
        self._playlists = []

        self._artistaControl = at.ArtistaControl(self)
        self._albumControl = ab.AlbumControl(self)
        self._playlistControl = pl.PlaylistControl(self)

        self._view = view

        self._add_callback()
        self._view.bind_commands()

        self._view.run()
    
    @property
    def artistas(self):
        return self._artistas
    
    @property
    def playlists(self):
        return self._playlists

    def _add_callback(self):
        self._view.add_callback('cad_art',self._artistaControl.mostrar_view)
        self._view.add_callback('cad_alb',self._albumControl.mostrar_view)
        self._view.add_callback('cad_play',self._playlistControl.mostrar_view)
        self._view.add_callback('cons_art',self._artistaControl.consultar)
        self._view.add_callback('cons_alb',self._albumControl.consultar)
        self._view.add_callback('cons_play',self._playlistControl.consultar)

    def add_artista(self, artista:Artista):
        self._artistas.append(artista)

    def att_albuns(self):
        for art in self._artistas:
            for alb in art.albuns:
                if len(alb.musicas) == 0:
                    print('teste')
                    aux = alb
                    art.albuns.remove(aux)
                    del aux

if __name__ == '__main__':
    MainController(MainView())