# Este código calcula as raízes de uma equação quadrática usando a fórmula de Bhaskara.

# O usuário é solicitado a inserir o valor do cateto a
a = int(input("Digite o cateto a: "))
# O usuário é solicitado a inserir o valor do cateto b
b = int(input("Digite o cateto b: "))

# O cálculo da hipotenusa, onde c é a hipotenusa, a é o cateto oposto e b é o cateto adjacente.
c = (a ** 2 + b ** 2) ** (1/2)

print("A hipotenusa é:", c)