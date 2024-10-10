lista = []


def cadastro():
    nome = input("Digite o nome da rodovia: ")
    extensao = float(input("Digite a Extensão dela: "))
    ano = int(input("Digite o ano de criação dela: "))

    lista.append({
        "nome": nome,
        "extensao": extensao,
        "ano":  ano
    })

for i in range(2):
    cadastro()

print(lista)