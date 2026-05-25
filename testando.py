# Este código demonstra o uso da função integrada sorted() em Python, que retorna uma nova lista ordenada do menor ao maior a partir dos itens em um iterável.
# A função sorted() não modifica a lista original, mas sim cria uma nova lista ordenada. No exemplo, temos uma lista de tempos (time_list) e ao chamar sorted(time_list), obtemos uma nova lista ordenada, enquanto a lista original permanece inalterada.
time_list = [12, 2, 32, 19, 57, 22, 14] # Lista de tempos
print(sorted(time_list)) # Imprime a lista ordenada
print(time_list) # Imprime a lista original, que permanece inalterada
# OBS: Letras maiúsculas e minúsculas são ordenadas de forma diferente, com as maiúsculas sendo ordenadas antes das minúsculas. Por exemplo, 'A' vem antes de 'a' na ordem alfabética.