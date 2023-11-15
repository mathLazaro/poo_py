class Artista:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__musicas = []
        self.__albuns = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
    
    @property
    def albuns(self):
        return self.__albuns
    
    def add_musica(self, musica):
        self.__musicas.append(musica)
    
    def add_album(self, album):
        self.__albuns.append(album)


class Album:
    def __init__(self, titulo: str, ano: int, artista: Artista):
        self.__titulo = titulo
        self.__ano = ano
        self.__artista = artista
        self.__musicas = []
        
        self.__artista.add_album(self)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def musicas(self):
        return self.__musicas
    
    def add_musica(self, musica):
        self.__musicas.append(musica)

    def __del__(self):
        print('album removido')


class Musica:
    def __init__(self, titulo: str, nroFaixa: int, album: Album):
        self.__titulo = titulo
        self.__nroFaixa = nroFaixa
        self.__artista = album.artista
        self.__album = album

        self.__artista.add_musica(self)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def nroFaixa(self):
        return self.__nroFaixa
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def albuns(self):
        return self.__album


class Playlist:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
    
    def add_musica(self, musica: Musica):
        self.__musicas.append(musica)
    
    def __del__(self):
        print('playlist removida')