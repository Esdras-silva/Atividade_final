from utils.limitar_lista import limitar_lista
from assets.menssages import * 


lista = [{
    "nome": "Arthur Bernades",
    "extensao": 45.7,
    "ano": 2024
}, 
{
    "nome": "Julio cesar",
    "extensao": 32.4,
    "ano": 2000
},{
    "nome": "Perimetral",
    "extensao": 24,
    "ano": 2000
},{
    "nome": "Arthur",
    "extensao": 15,
    "ano": 2004
}]






def cadastro():
    nome = input("Digite o nome da rodovia: ")
    extensao = float(input("Digite a Extensão dela: "))
    ano = int(input("Digite o ano de criação dela: "))

    if limitar_lista(lista):
       lista.append({
        "nome": nome,
        "extensao": extensao,
        "ano":  ano
        })
    else:
        print("Armazenamento cheio")
  

def busca():
    termo = input("digite a rodovia que deseja pesquisar: ").upper()#pega o termo digitado para busca e transforma em maiusculo
    for i in range(len(lista)):
        if termo in lista[i]["nome"] or termo in str(lista[i]["ano"]) or termo in str(lista[i]["extensao"]):#Transforma os numeros em str para poder inteirar
            print(lista[i])


def imprimir():
   
    print(opcao_imprimir())
    
    opcao = int(input("Escolha uma opção: "))

   
    if opcao == 1 :
      print_imprimir(lista)
       
            
    elif opcao == 2:
        
        trecho = input("Digite um o trecho que você quer imprimir (Separe por espaço ex: 1 5): ")
        trecho_formatado = list(map(int, trecho.split()))
        
        print_imprimir(lista[trecho_formatado[0]-1:trecho_formatado[1]])
      
    else:
        raise Exception("Opção errada")
    

