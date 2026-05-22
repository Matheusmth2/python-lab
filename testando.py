# Conversor de moedas: pesos, soles e reais para dólar

# O programa solicita ao usuário a quantidade de pesos, soles e reais que ele possui, e então converte esses valores para dólares usando as taxas de conversão atuais.
pesos = float(input("Digite quantos pesos você tem: "))
soles = float(input("Digite quantos soles você tem: "))
reais = float(input("Digite quantos reais você tem: "))

# As taxas de conversão hoje 22-05-2026 são: 1 peso = 0.00027 dólar, 1 sol = 0.29 dólar, e 1 real = 0.20 dólar.
dolar = (pesos * 0.00027) + (soles * 0.29) + (reais * 0.20)

# Por fim,o programa exibe o valor total em dólares.
print("O seu dinheiro em dólar é:", dolar)