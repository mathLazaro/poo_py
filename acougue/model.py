from datetime import date
from copy import copy


class CpfInvalido(Exception):
    def __del__(self):
        print('CPF INVÁLIDO')



class PrecoInvalido(Exception):
    def __del__(self):
        print('PREÇO INVÁLIDO')



class QuantidadeInvalida(Exception):
    def __del__(self):
        print('QUANTIDADE INVÁLIDA')



class CodigoProdutoInvalido(Exception):
    def __del__(self):
        print('CÓDIGO DO PRODUTO INVÁLIDO')



class Produto:
    def __init__(self, codigo:str, nome:str, precoKg:float):
        try:
            self.__cod = codigo
            self.__nome = nome
            self.__precoKg = float(precoKg)
            self.__qtdVendida = 0
        except:
            raise PrecoInvalido

    @property
    def codigo(self):
        return self.__cod
    
    @property
    def nome(self):
        return self.__nome
        
    @property
    def precoKg(self):
        return self.__precoKg ## '%.2f' %
    
    @property
    def qtdVendida(self):
        return self.__qtdVendida
    
    @precoKg.setter
    def precoKg(self,newPreco:float):
        try:
            self.__precoKg = newPreco
        except:
            PrecoInvalido
        
    # a qtd vedida de produto é adicionada automaticamente ao adicionar na nota
    def _add_qtdVendida(self, qtd:float):
        self.__qtdVendida += qtd

    # def calcular_faturamento(self) -> float:
    #     return self.__qtdVendida * self.__precoKg
    


class Cliente:
    def __init__(self, nome:str, email:str, cpf:int):
        if not self._validar_cpf(str(cpf)): # valida o cpf
            raise CpfInvalido
        else:
            self.__nome = nome
            self.__email = email
            self.__cpf = str(cpf)
            self.__compras = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def cpf(self) -> str:
        return self.__cpf[0:3] + '.' + self.__cpf[3:6] + '.' + self.__cpf[6:9] + '-' + self.__cpf[9:11]

    # valida o cpf passado como parâmetro
    def _validar_cpf(self, cpf: str) -> bool:
        # retorna falso a quantidade de números é incompatível
        if len(cpf) != 11:
            return False
        
        cpfValida = cpf[0:9]
        i = 10
        soma = 0

        for num in cpfValida:
            soma += int(num) * i
            i -= 1

        soma %= 11
        soma = 11 - soma

        if soma >= 10:
            cpfValida += '0'
        else:
            cpfValida += str(soma)

        soma = 0
        i = 11

        for num in cpfValida:
            soma += int(num) * i
            i -= 1
        
        soma %= 11
        soma = 11 - soma

        if soma >= 10:
            cpfValida += '0'
        else:
            cpfValida += str(soma)

        
        # retorna true caso bater o dígito verficador e falso caso contrário
        if cpfValida == cpf:
            return True
        else:
            return False

    # todas as notas são adicionadas automaticamente ao cliente em seu contrutor
    def _add_compra(self, nota):
        self.__compras



class NotaFiscal:
    def __init__(self, cliente:Cliente, data:date, identificador:int):
        self.__cliente = cliente
        self.__data = data
        self.__identificador = identificador

        self.__produtos = {} # key -> produto | value -> quantidade
        self.__cliente._add_compra(self)

    @property
    def cliente(self):
        return self.__cliente
    
    ## retorna o dicionário com as quantidades vendidas
    @property
    def produtos(self):
        return self.__produtos

    @property
    def data(self):
        return self.__data

    @property
    def identificador(self):
        return self.__identificador
    
    @property
    def cliente(self):
        return self.__cliente
    
    # adiciona produto na nota
    def add_produto(self, produto:Produto, qtd:float):
        if qtd < 0:
            raise QuantidadeInvalida
        else:
            self.__produtos[copy(produto)] = qtd
            produto._add_qtdVendida(qtd)

    # retorna a quantidade de produto vedido naquela nota
    # retorna erro se não houver tal produto
    def get_qtdProduto(self, cod:str) -> float:
        for prod in self.__produtos.keys():
            if prod.codigo == cod:
                return self.__produtos[prod]
            
        raise CodigoProdutoInvalido

    # calcular o valor de um certo produto de acordo com o código
    # retorna erro se não houver tal produto
    def calcular_valorProduto(self, cod:str) -> float:
        for prod in self.__produtos.keys():
            if prod.codigo == cod:
                return self.__produtos[prod] * prod.precoKg
            
        raise CodigoProdutoInvalido
        
    # calcular o valor total da nota
    def calcular_valorNota(self) -> float:
        soma = 0
        for prod in self.__produtos.keys():
            soma += self.calcular_valorProduto(prod.codigo)

        return soma
    

if __name__=='__main__':
    prod1 = Produto('123','carne',23)

    nota = NotaFiscal(Cliente('matheus','mail',11392508681),date(2323,2,2),'23')

    nota.add_produto(prod1,1)

    print(nota.calcular_valorProduto('123'))

    prod1.precoKg = 2

    print(nota.calcular_valorProduto('123'))