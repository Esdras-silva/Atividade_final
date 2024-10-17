def imprimir(database: list, i: int):
    exten = database[i]["extensão"]#coloca o item dentro da variavel
    if type(exten) == float:#verifica se a variavel é do tipo float
      print(f"{database[i]['nome']}\t extensão: {database[i]['extensão']:.3f} KM\t ano de criação: {database[i]['ano de criação']}")
    else:
           print(f"{database[i]['nome']}\t extensão: {database[i]['extensão']:.>5} KM\t ano de criação: {database[i]['ano de criação']}")
#se for int o numero é printado alinhado a direita
            #esse if tem objetivos simplesmente esteticos para um print padronizado