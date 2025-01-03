#String é qualquer tipo de texto dentro de aspas duplas ""

minha_string = "qualquer texto"

print(f"contatenar {minha_string} em string") #utiliza-se f para concatenar uma string com outra

#Funções com strings

print(minha_string.upper()) #Tudo em maiúsculo
print(minha_string.lower()) #Tudo em minúsculo
print(minha_string.capitalize()) #Primeira letra fica maiúscula
print(minha_string.isupper()) #Virifica se é maiúsculo (retorna dado booleano)
print(minha_string.islower()) #Verifica se é minúsculo 
print(minha_string.strip()) #Remove espaços antes e depois do texto (se tiver)
print(minha_string.replace("qualquer", "meu")) #Substitui uma palavra ou texto por outro (necessário inserir contéudo dentro dos parênteses)
print(len(minha_string)) #Conta as letras
print(minha_string.index("r")) #Procura e mostra o índice da palavra ou texto

#Formula para verificar se o texto/palavra/letra existe ou não (comparação)
x = "texto" in minha_string
print(x) 

#Texto com múltiplas linhas:

minha_string1 = """linha 1,
linha 2,
linha 3,
linha 4.
"""
print(minha_string1)

#Caracter de scape (\n). Criando texto com várias linhas:

minha_string2 = "linha 1,\nlinha 2,\nlinha 3."

print(minha_string2)

#Como adicionar aspas duplas dentro do texto impresso:
minha_string3 = "adiciona entre \"aspas\" no texto"

print(minha_string3)