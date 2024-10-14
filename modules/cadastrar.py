from modules.database import adicionar_rodovia

def cadastrar():
     nome = input("Digite o nome da rodovia: ")
     extensao = float(input("Digite a Extensão dela: "))
     ano = int(input("Digite o ano de criação dela: "))

     print(adicionar_rodovia({
          "nome": nome,
          "extensao": extensao,
          "ano": ano
     }))

cadastrar()