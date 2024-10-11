from utils.limitar_lista import limitar_lista

import random

lista = [
    {"nome": "BR-101", "extensão": 4.772, "ano": 1950},
    {"nome": "BR-116", "extensão": 4.385, "ano": 1950},
    {"nome": "BR-230", "extensão": 4.223, "ano": 1972},
    {"nome": "BR-153", "extensão": 3.585, "ano": 1960},
    {"nome": "BR-262", "extensão": 2.170, "ano": 1962},
    {"nome": "BR-364", "extensão": 4.325, "ano": 1968},
    {"nome": "BR-381", "extensão": 1.200, "ano": 1958},
    {"nome": "BR-163", "extensão": 3.579, "ano": 1970},
    {"nome": "BR-040", "extensão": 1.178, "ano": 1955},
    {"nome": "BR-070", "extensão": 1.756, "ano": 1962},
    {"nome": "SP-280", "extensão": 442, "ano": 1961},
    {"nome": "RJ-116", "extensão": 180, "ano": 1972},
    {"nome": "MG-050", "extensão": 406, "ano": 1958},
    {"nome": "PR-151", "extensão": 320, "ano": 1975},
    {"nome": "RS-122", "extensão": 230, "ano": 1960},
    {"nome": "BA-099", "extensão": 217, "ano": 1973},
    {"nome": "SC-401", "extensão": 56, "ano": 1972},
    {"nome": "PE-060", "extensão": 245, "ano": 1969},
    {"nome": "CE-040", "extensão": 212, "ano": 1970},
    {"nome": "PA-150", "extensão": 695, "ano": 1976}]


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

def imprimir_parte():
    print("Existem {len(lista) rodovias cadastradas }")
    inicio = int(input("Qual o indice do numero inicial: "))
    final = int(input("Qual o indice do ultimo elemento a ser impress: "))

    for i in range(inicio-1,final):
        print(f"{lista[i]["nome"]}  {lista[i]["extensão"]}  {lista[i]["ano"]}")

busca()
imprimir_parte()
