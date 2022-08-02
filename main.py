""" Arquivo principal """
# importa a classe funcionário para dentro do main.py
import os
from model.funcionario import Funcionario
from model.pratos import Prato
from model.vendas import Venda
import model.funcionario_dao as f_dao
import model.pratos_dao as p_dao
import model.vendas_dao as v_dao

op = 0

while op != 6:
    os.system('cls')
    print('::::::::::::|Sistema para Restaurantes|::::::::::::')
    print('|-------------------------------------------------|')
    print('| [1] - Mostrar Menu                              |')
    print('| [2] - Realizar uma venda                        |')
    print('|-------------------------------------------------|')
    print('| [3] - Gerenciamento de Funcionários             |')
    print('| [4] - Gerenciamento de Pratos                   |')
    print('| [5] - Gerenciamento de vendas                   |')
    print('| [6] - Sair                                      |')
    print('+-------------------------------------------------+')
    op = int(input('Digite o número da opção desejada: '))
    
    if op == 1:
        """MOSTRAR MENU"""
        os.system('cls')
        print('::::::::::::|MENU|::::::::::::')
        pratos = p_dao.getList()
        for p in pratos:
            p.print()
            print('------------------------------')
    
    elif op == 2:
        """REALIZAR VENDA"""
        p_cod = int(input('Insira o código do prato: '))
        data =  input('Data: ')
        venda = v_dao.addVenda()
        
        
    
    elif op == 3:
        """GERENCIAMENTO DE FUNCIONÁRIOS"""
        while op != 4:
            os.system('cls')
            print('::::::::::|Gerenciamento de Funcionários|::::::::::')
            print('|-------------------------------------------------|')
            print('| [1] - Adicionar                                 |')
            print('| [2] - Editar                                    |')
            print('| [3] - Excluir                                   |')
            print('| [4] - Lista de Funcionários                     |')
            print('| [5] - Voltar ao menu principal                  |')
            print('+-------------------------------------------------+')           
            op = int(input('Digite o número da opção desejada: '))
            
            if op == 1:
                os.system('cls')
                print('::::::::::::::|Adicionar Funcionário|::::::::::::::')
                n = str(input('Digite o nome: '))
                cod = int(input('Digite o codigo: '))
                funcao = ''
                print('===============|Funções disponíveis|===============')
                print('[1] - Gerente\n[2] - Recepcionista\n[3] - Serviços Gerais')
                print('===================================================')
                funcao_op = int(input('Digite o número conrrespondente a função: '))
                print('---------------------------------------------------')
                if funcao_op == 1:
                    funcao = 'Gerente'
                elif funcao_op == 2:
                    funcao = 'Recepcionista'
                elif funcao_op == 3: 
                    funcao = ' Serviços Gerais'
                f_cod = f_dao.getFunc(cod)
                if f_cod == None:
                    func = f_dao.add(cod, n, funcao)
                else:
                    print(f'ERRO!! o código {cod} corresponde ao funcionário abaixo, tente outro')
                    f_cod.print()
                    
                
                input('Aperte ENTER para continuar')
                
            
            elif op == 2:
                pass
            
            elif op == 3:
                pass
            
            elif op == 4:
                os.system('cls')
                print(':::::::::::::|Lista de Funcionários|:::::::::::::')
                for f in func:
                    f.print()
            
            elif op == 5:
                break
    
    elif op == 4:
        """GERENCIAMENTO DE PRATOS"""
        op = 0
        while op != 4:
            os.system('cls')
            print('::::::::::|Gerenciamento de Pratos|::::::::::')
            print('|-------------------------------------------|')
            print('| [1] - Adicionar                           |')
            print('| [2] - Editar                              |')
            print('| [3] - Excluir                             |')
            print('| [4] - Voltar ao menu principal            |')
            print('+-------------------------------------------+')  
            op = int(input('Digite o número da opção desejada: ')) 
            
            if op == 1:
                os.system('cls')
                print(':::::::::::::::|Adicionar Prato|:::::::::::::::')
                n = input('Digite o nome: ')
                cod = int(input('Digite o código: '))
                desc = input('Digite a descrição: ')
                preco = float(input('Digite o preço: '))
                p_cod = p_dao.getPrato(cod)
                if p_cod == None:
                    prato = p_dao.add(cod, n, desc, preco)
                else:
                    print('---------------------------------------------------------------')
                    print(f'ERRO!! o código {cod} corresponde ao prato abaixo, tente outro')
                    print('---------------------------------------------------------------')
                    p_cod.print()
                    print('---------------------------------------------------------------')
            
            elif op == 2:
                pass
            
            elif op == 3:
                pass
            elif op == 4:
                break
            
            input('Aperte ENTER para continuar')
    
        
        
    
    elif op == 5:
        """GERENCIAMENTO DE VENDAS"""
        pass
    input('Aperte ENTER para continuar')
    os.system('cls')
print('Obrigado por usar o sistema :D')