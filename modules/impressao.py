import sys

from utils.path import path_for_modules
sys.path.append(path_for_modules())

from modules.database import imprimir_por_filtro, imprimir_rodovias

def imprimir_todas():
    print("Todas as Rodovias: ")
    imprimir_rodovias()

def imprimir_trecho():
    inicio = int(input("Digite onde vai começar a impressão: "))
    final = int(input("Digite onde vai terminar a impressão: "))

    imprimir_por_filtro(inicio, final)