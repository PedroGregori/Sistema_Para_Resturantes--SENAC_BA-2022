from model.pratos import Prato

p_lst = []

def add(cod: int, nome: Prato, desc: Prato, preco: float):
    p = Prato(cod, nome, desc, preco)
    p_lst.append(p)
    return p_lst

def edit():
    pass

def excl():
    pass

def getList():
    return p_lst

def getPrato(cod: int):
    for p in p_lst:
        if p.cod == cod:
            return p
    return None