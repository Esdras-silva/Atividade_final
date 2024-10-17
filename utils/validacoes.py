
from utils.timer import timer

def validar_entrada(messagem) -> int :
    while True:
        try:
            return int(input(messagem))
        except ValueError:
            print("Entrada invalida! Por favor, insira um número válido.")
            timer()
        

def confirmar_saida():
    while True:
        sair = validar_entrada("Você tem certeza que quer sair do programa? (1 - Sim, 2 - Não): ")
        
        if sair == 1:
            return True
        elif sair == 2:
            return False
        