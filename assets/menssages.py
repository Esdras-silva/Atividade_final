def opcao_menu():
    return '''
---------------- SISTEMA DE CADASTRO - RODOVIAS ----------------
                    
                    1 - Cadastrar
                    2 - Buscar
                    3 - Imprimir
                    4 - Sair

'''

def opcao_imprimir() -> str:
    return '''
    ----------------------- IMPRIMIR -----------------------
                        1 - Imprimir tudo
                        2 - Imprimir trecho

    '''

def print_imprimir(lista) -> str:
    msg = '''
     ----------------------- IMPRIMIR -----------------------
     
    
    '''

    for i in range(len(lista)):
        msg += f'''

                    Rod. {lista[i]["nome"]}
                    Extensão: {lista[i]["extensao"]} Km
                    Inaugurada em: {lista[i]["ano"]}

                    '''
    return print(msg) 