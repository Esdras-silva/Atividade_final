import sys
from utils.path import path_for_modules
sys.path.append(path_for_modules('modules'))

from modules.database import buscar_rodovias
def messagem_pesquisa() -> str:
    return '''
 ---------------------- PESQUISA ----------------------
   Aqui você pode pesquisar as rodovias pelos seguintes
   campos: 
     Nome;
     Extensao;
     Ano de Criação.

'''

def pesquisa():
   
   try: 
     print(messagem_pesquisa())
     campo = input("Digite o em que campo você quer pesquisar: ").lower()
     if campo in ["nome", "extensão","ano de criação"] :
       termo = input(f"Digite o {campo} da Rodovia: ").lower()
       
       buscar_rodovias(campo,termo)
     else:
        raise Exception("Campo errado!!")
     
   except Exception as e:
      print(e) 
