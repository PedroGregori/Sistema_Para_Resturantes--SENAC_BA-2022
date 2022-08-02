class Venda():
    def __init__(self, v_cod, data, prato, valor):
        self.v_cod = v_cod
        self.data = data
        self.prato = prato
        self.valor = valor
    def print(self):
        print(f'Código: {self.v_cod} || Data: {self.data}\nPrato: {self.prato} || Valor: {self.valor}')