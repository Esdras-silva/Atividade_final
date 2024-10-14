from utils.limitar_lista import limitar_lista
from assets.menssages import * 

import random

lista = []

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

def imprimir(i):
    exten = lista[i]["extensão"]#coloca o item dentro da variavel
    if type(exten) == float:#verifica se a variavel é do tipo float
        print(f"{lista[i]["nome"]}\t extensão: {lista[i]["extensão"]:.3f} KM\t ano de criação: {lista[i]["ano"]}")#se a variavel for float usa :.3f
    else:
            print(f"{lista[i]["nome"]}\t extensão: {lista[i]["extensão"]:>5} KM\t ano de criação: {lista[i]["ano"]}")#se for int o numero é printado alinhado a direita
            #esse if tem objetivos simplesmente esteticos para um print padronizado

def imprimir_tudo():
    print("Todas as rodovias")
    for i in range(len(lista)):
        imprimir(i) # tava compreguiça de escrever duas vezes por isso transformei em função

def imprimir_parte():
    print(f"Existem {len(lista)} rodovias cadastradas ")
    inicio = int(input("Qual o indice da primeira rodovia a ser impressa: "))
    final = int(input("Qual o indice do ultimo elemento a ser impressa: "))

    for i in range(inicio-1,final):
        imprimir(i)

