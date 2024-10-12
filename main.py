from utils.limitar_lista import limitar_lista
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
  

def buscar(campo: str ,valor):

    def filtro_da_lista(item):
        return item == valor
    nova_lista = list(lista[i][campo] for i in range(len(lista)))


    lista_filtrada = list(filter(filtro_da_lista, nova_lista))

    print(lista_filtrada)


for _ in range(2):
    cadastro()

buscar("ano", 2000)