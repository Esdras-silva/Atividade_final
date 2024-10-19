def imprimir(database: list, i: int):
    extensao = database[i]["extensão"]#coloca o item dentro da variavel
    if extensao.is_integer():#Verifica se o numero float é inteiro ou quebrado( serve pra caso dê 340.0 pra não confundir com 340 mil)
      print(f"{database[i]['nome']}\t extensão: {int(extensao):>5} KM\t ano de criação: {database[i]['ano de criação']}")
    else:
      print(f"{database[i]['nome']}\t extensão: {extensao:.3f} KM\t ano de criação: {database[i]['ano de criação']}")#imprime 4.900 em vez de 4.9
