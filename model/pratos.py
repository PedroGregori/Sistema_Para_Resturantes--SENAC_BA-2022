class Prato():
    def __init__(self, cod, nome, descricao, preco):
        self.cod = cod
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
    def print(self):
        print(f'Código: {self.cod}\nNome: {self.nome}\nDescrição: {self.descricao}\nPreço: {self.preco}')