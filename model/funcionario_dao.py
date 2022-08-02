# DAO - Data Access Object
#       (Acesso ao dados dos objetos)

from model.funcionario import Funcionario as func

# Lista que armazena os objetos Funcionários
f_lst = []


def add(cod: int, nome: func, funcao: func):
    f = func(cod, nome, funcao)
    f_lst.append(f)
    return f_lst


def edit(cod: int, novoF: func):
    """1 - Encontrar o funcionário com de código fornecido
       2 - Substitui na lista pelo novoF"""
    pass


def excl(cod: int):
    """1 - encontrar o funcionário com de código fornecido
       2 - Exclui da lista  """
    pass


def getList() -> list:
    """ Retorna a lista de todos os funcionários"""
    return f_lst


def getFunc(cod: int) -> func:
    """ Varre a lista comparando o COD de cada objeto.
        SE existir um obj com o COD igual ao enviado, retorna o 
        objeto. Caso contrário retorna vazio (None) """
    for f in f_lst:
        if f.cod == cod:
            return f
        
    return None