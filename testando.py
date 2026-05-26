# Acessando elementos de uma lista usando índices
my_list = ["banana", "maçã", "laranja", "uva"]
print(my_list[0])  # Acessa o primeiro elemento da lista
print(my_list[1])  # Acessa o segundo elemento da lista
print(my_list[2])  # Acessa o terceiro elemento da lista
print(my_list[3])  # Acessa o quarto elemento da lista

# Concatenando listas
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Concatena as duas listas

# Diferente de strings, as listas são mutáveis, ou seja, seus elementos podem ser alterados após a criação da lista.
# Mundando o valor de um elemento da lista
my_list[1] = 7  # Altera o segundo elemento da lista
print(my_list)  # Imprime a lista atualizada

# Utilizando o método de inserção para adicionar um elemento em uma posição específica da lista
my_list.insert(2, "abacaxi")  # Insere "abacaxi" na posição 2 da lista
print(my_list)  # Imprime a lista atualizada

# Utilizando o método de remoção para remover um elemento específico da lista
my_list.remove("laranja")  # Remove "laranja" da lista
print(my_list)  # Imprime a lista atualizada