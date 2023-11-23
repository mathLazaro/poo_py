from tkinter import *
from model import *
from datetime import date



notaConfig = {
    'bg': 'lemon chiffon',
    'font': ('TimesNewToman',11)
}



class PrintNotaFiscal(Toplevel):
    def __init__(self, root, nota:NotaFiscal):
        Toplevel.__init__(self, root)
        self._nf = nota

        self.config(bg='lemon chiffon')
        self.title('')
        self.det_geometry()

        self._head = Frame(self,bg='lemon chiffon')
        self._nota = Frame(self,bg='lemon chiffon')
        self._cliente = Frame(self,bg='lemon chiffon')
        self._produto = Frame(self,bg='lemon chiffon')
        self._total = Frame(self,bg='lemon chiffon')


        Label(self._head, text='Nota Fiscal',font=('TimesNewRoman',14,'bold'),cnf=notaConfig).pack(fill='x')
        Label(self._head, text='Açougue SA',cnf=notaConfig).pack(fill='x')

        Label(self._nota,text='- - - - - - - - - - - - - - - - - - - - - - - - - - -'\
              ,font=('TimesNewRoman',12,'bold'),cnf=notaConfig).pack(fill='x')
        Label(self._nota,text='Identificador: '+str(self._nf.identificador)\
              ,cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
        Label(self._nota,cnf=notaConfig,anchor=W,text='Data: '+str(self._nf.data.day)\
              +' / '+str(self._nf.data.month)+' / '+str(self._nf.data.year)).pack(fill='x',padx=27)

        Label(self._cliente,text='- - - - - - - - - - - - - - - - - - - - - - - - - - -',\
              font=('TimesNewRoman',12,'bold'),cnf=notaConfig).pack(fill='x')
        Label(self._cliente,text='Cliente: '+str(self._nf.cliente.nome),cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
        Label(self._cliente,text='CPF: '+str(self._nf.cliente.cpf),cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
        Label(self._cliente,text='Email: '+str(self._nf.cliente.email),cnf=notaConfig,anchor=W).pack(fill='x',padx=27)


        for prod in self._nf.produtos.keys():
            Label(self._produto,text='- - - - - - - - - - - - - - - - - - - - - - - - - - -',\
                  font=('TimesNewRoman',12,'bold'),cnf=notaConfig).pack(fill='x')
            Label(self._produto,text=str(prod.codigo)+' - '+str(prod.nome),\
                  cnf=notaConfig,anchor=W).pack(fill='x',padx=27)
            Label(self._produto,text='R$'+str('%.2f' % prod.precoKg)+' * '+str(self._nf.get_qtdProduto(prod.codigo))+\
                  'kg = R$'+str('%.2f' % self._nf.calcular_valorProduto(prod.codigo)),cnf=notaConfig,anchor=E).pack(fill='x',padx=27)

        Label(self._total,text='- - - - - - - - - - - - - - - - - - - - - - - - - - -',\
                  font=('TimesNewRoman',12,'bold'),cnf=notaConfig).pack(fill='x')
        Label(self._total,text='Valor total da nota: R$'+ str('%.2f' % self._nf.calcular_valorNota()),cnf=notaConfig,anchor=E).pack(fill='x',padx=27)


        self._head.pack(fill='both')
        self._nota.pack(fill='both')
        self._cliente.pack(fill='both')
        self._produto.pack(fill='both')
        self._total.pack(fill='both')

    def det_geometry(self):
        tam = len(self._nf.produtos.keys())
        if tam < 3:
            self.geometry('300x410')
        elif tam < 5:
            self.geometry('300x540')
        elif tam < 7:
            self.geometry('300x670')
        elif tam < 9:
            self.geometry('300x800')
        elif tam < 11:
            self.geometry('300x930')

# def teste():
#     nf = NotaFiscal(Cliente('matheus','email',11392508681),date(2023,11,22),'1232')
#     nf.add_produto(Produto('123','carne',23.5),1.2)
#     nf.add_produto(Produto('2233','busca',32),0.80)
#     PrintNotaFiscal(root,nf)

# root = Tk()
# root.geometry('300x200')
# Button(root,command=teste).pack()
# root.mainloop()s