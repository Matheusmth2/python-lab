# Criando uma função com parametros
# A variável failed_percentage é local à função calculate_fails() e não pode ser acessada fora dela. Para acessar o valor calculado, precisamos retornar a variável failed_percentage e armazená-la em uma variável global ou usá-la diretamente.
def calculate_fails(total_attempts, failed_attempts):
    failed_percentage = (failed_attempts / total_attempts) * 100
    return failed_percentage

# Criando a variavel global percentage
# Guardando a porcentagem de falhas calculada pela função calculate_fails() na variável global `percentage`
percentage = calculate_fails(4, 2) # Colocando argumentos para calcular a porcentagem de falhas (total_attempts=4, failed_attempts=2)
if percentage >= 50:
    print("Conta bloqueada")
#A porcentagem não é retornarda na tela, mas a mensagem "Conta bloqueada" será exibida, pois a porcentagem de falhas é maior ou igual a 50%.