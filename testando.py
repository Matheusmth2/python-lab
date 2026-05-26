# Utilizando o metodo de indices para acessar os elementos de uma lista
print("Hello".index("o")) # Retorna o indice do primeiro elemento encontrado
print("Hello".index("H")) # Python é case-sensitive, ou seja, diferencia maiúsculas de minúsculas
print("Hello".index("l")) # Retorna o indice do primeiro elemento encontrado

# Utilizando o metodo de contagem para contar quantas vezes um elemento aparece em uma lista
print("Hello".count("l")) # Retorna o número de vezes que o elemento aparece

# Utilizando o metodo de substituição para substituir um elemento por outro
print("Hello".replace("l", "x")) # Retorna uma nova string com as substituições feitas

# Utilizando o metodo de divisão para dividir uma string em uma lista de substrings
print("Hello World".split()) # Retorna uma lista de substrings, por padrão,

''' Strings imutáveis: As strings em Python são imutáveis, ou seja, não podem ser alteradas depois de criadas. Qualquer operação que pareça modificar uma string na verdade cria uma nova string.
s = "Hello"
s[0] = "h" # Isso causará um erro, pois strings são imutáveis '''