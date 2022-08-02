
class Funcionario():
    def __init__(self, cod, nome, funcao) -> None:
        self.cod = cod
        self.nome = nome
        self.funcao = funcao
    def print(self):
        print(f'Codigo: {self.cod} - Nome: {self.nome} - Função: {self.funcao}')