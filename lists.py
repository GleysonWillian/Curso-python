familia = ["Gleyson", "Flávio", "Rosangela"]

#print(familia[0]) # retorna um índice
#print(familia[0:3]) #retorna vários índices
#print(familia[-2]) # retorna um índice de traz para frente

#Alterando o valor do índice
#print(familia)
#familia[1]= "Gleyson"
#print(familia)

#Incremento de outra lista (manualmente ou em arquivo)
#.extend: usa-se para adicionar vários registros (no final):
#familia.extend(["Tobby", "Akita"]) 
#print(familia)

#-----------------------------------------------------------------

#.append: usa-se para adicionar apenas um registro (no final):
#familia.append ("Garfield") 
#print(familia)

#.insert + número de índice desejado: usa-se para adicionar apenas um registro na posição do índice desejado:
#familia.insert(1,"Garfield")
#print(familia)

#Romoção de registros do final:
#familia.pop() #remoção da Akita
#familia.pop() #remoção do Tobby
#print(familia)

#Romoção de registros inserindo o nome:
#familia.remove("Garfield")
#print(familia)

#Limpando todos os registros:
#familia.clear()
#print(familia)

#Retorna ao índica com base no valor:
#print(familia.index("Gleyson"))

#Quanto registros do valor há dentro da lista:
#print(familia.count("Rosangela"))

#print(familia)

#----------------------------------------------------------------

#idade_familia = [23, 50, 32]
#print(idade_familia)

#.sort: coloca os números em ordem do menor para o maior:
#idade_familia.sort()
#print(idade_familia)

#.sort: colocar os membros da listas em ordem alfabética (A-Z):
#familia.sort()
#print(familia)

#idade_familia = [23, 50, 32]
#print(idade_familia)

#.sort: coloca os números em ordem do maior para o menor:
#idade_familia.reverse()
#print(idade_familia)

#.sort: colocar os membros da listas em ordem alfabética (Z-A):
#familia.reverse()
#print(familia)

#----------------------------------------------------------------

#Copia com ponto de referência:
#familia2 = familia
#print(familia2)

#familia.remove("Gleyson")
#print(familia2)

#---------------------------------------------------------------

#Copia:
#familia2 = familia.copy()
#familia.remove("Gleyson")
#print(familia)
#print(familia2)

#---------------------------------------------------------------

#Tuple (lista imutável):
#coordenadas = (-49, -36)
#print(coordenadas[0])
#print(coordenadas.count(-49))