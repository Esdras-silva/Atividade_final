import sys
from utils.path import path_for_modules
sys.path.append(path_for_modules())


from utils.validacoes import confirmar_saida, validar_entrada
from utils.timer import timer
from modules.cadastrar import cadastrar
from modules.impressao import imprimir_todas, imprimir_trecho
from modules.pesquisa import pesquisa

def messagem_inicial() -> str :
    return '''
-------------------- BEM VINDO(A) AO REGISTRADOR DE RODOVIAS --------------------
            Esse programa foi criado como proposta de trabalho final
            de algoritmos da Profª Regiane Kawasaki. Por isso nos esforçamos
            criar um ótimo programa, tentando seguir ao máximo as boas práticas
            de programaçao.


            By Antonio Silva e João Paulo Santos



'''

def opção_menu():
    return '''
-------------------- MENU --------------------

                 1 - Cadastrar
                 2 - Pesquisar
                 3 - Imprimir
                 4 - Sair

'''

def opção_imprimir():
    return '''
-------------------- IMPRIMIR --------------------
                
                1 - Impprimir Tudo
                2 - Imprimir Trecho
                3 - Sair

'''

def menu_imprimir():
    opt_imprimir = 0
    while opt_imprimir != 3:
        print(opt_imprimir())
        opt_imprimir = validar_entrada("Escolha uma opção: ")
        if opt_imprimir == 1:
            imprimir_todas()
        elif opt_imprimir == 2:
            imprimir_trecho()
        elif opt_imprimir == 3:
            print("Voltando...")
            timer()
    

def menu_principal():
    
    print(messagem_inicial())
    opt = None
    while opt != 5:
        try:
            timer()
            print(opção_menu())
            opt = validar_entrada("Escolha uma opção: ")

            if opt == 1:
                cadastrar()
            
            elif opt == 2:
                pesquisa()
            elif opt == 3:
                menu_imprimir()
            elif opt == 4:
                if confirmar_saida():
                    opt = 5
                    print("Saindo....")
                    timer()
                else:
                    opt = None
        except KeyboardInterrupt:
            print("\n Você não popde interromper o programa pelo teclado. Para sair, escolha a opção 4.")
            continue
          