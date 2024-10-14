from utils.limitar_lista import limitar_lista
from utils.imprimir import imprimir

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
        elif termo in str(database[i]["ano"]) and campo == 'ano':
            print(database[i])
        elif termo in str(database[i]["extensao"]):
            print(database[i])

def imprimir_rodovias():
    for i in range(len(database)):
        imprimir(database,i)
            
def imprimir_por_filtro(inicio, final):
        for i in range(inicio-1,final):
            imprimir(database,i)



