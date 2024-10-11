from utils.limitar_lista import limitar_lista

import random

lista = []

def cadastro():
    nome = input("Digite o nome da rodovia: ")
    extensao = float(input("Digite a Extensão dela: "))
    ano = int(input("Digite o ano de criação dela: "))

    if limitar_lista(lista):
      print("Armazenamento cheio")
    else:
         lista.append({
        "nome": nome,
        "extensao": extensao,
        "ano":  ano
    })

def busca():
    termo = input("digite a rodovia que deseja pesquisar: ").upper()#pega o termo digitado para busca e transforma em maiusculo
    for i in range(len(lista)):
        if termo in lista[i]["nome"] or termo in str(lista[i]["ano"]) or termo in str(lista[i]["extensão"]):#Transforma os numeros em str para poder inteirar
            print(lista[i])
def imprimir():
    for i in range(len(lista)):
        print

def imprimir_parte():
    print("Existem {len(lista) rodovias cadastradas }")
    inicio = int(input("Qual o indice do numero inicial: "))
    final = int(input("Qual o indice do ultimo elemento a ser impress: "))

    for i in range(inicio-1,final):
        print(f"{lista[i]["nome"]}  {lista[i]["extensão"]}  {lista[i]["ano"]}")

busca()
imprimir_parte()