from model.vendas import Venda
from model.pratos import Prato
import pratos_dao as p_dao

v_lst = []

def addVenda(p_cod: int, data: Venda, pago: Venda ):
    """Terminar o sistema de verificação e confirmação de venda"""
    prato = p_dao.getPrato(p_cod)
    preco = prato.preco
    if preco > pago:
        falta = preco - pago
    
    
    if prato != None:
        if pago > preco:
            troco = pago - preco
            venda = Venda(v_cod, data, prato, preco)
    


def getList():
    pass

def getLucro():
    pass

def getCod():
    pass