import limitar_lista
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

