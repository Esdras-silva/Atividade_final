from utils.imprimir import imprimir

from utils.limitar_lista import limitar_lista



database = []

def adicionar_rodovia(rodovia: dict) -> str:
     if limitar_lista(database):
       database.append(rodovia)
       return "Adicionada com sucesso!"
     else:
        return "Armazenamento cheio!"

def buscar_rodovias(campo: str, termo: str):
    
    for i in range(len(database)):
        if termo in database[i]["nome"] and campo == 'nome' :
            print(database[i])
        elif termo in str(database[i]["ano de criação"]) and campo == 'ano de criação':
            print(database[i])
        elif termo in str(database[i]["extensão"]):
            print(database[i])
        else:
            print(f"Não tem nenhuma rodovia com {'essa' if campo == 'extensão' else 'esse'} {campo}!!")

def imprimir_rodovias():
    for i in range(len(database)):
        imprimir(database,i)
            
def imprimir_por_filtro(inicio, final):
        for i in range(inicio-1,final):
            imprimir(database,i)



