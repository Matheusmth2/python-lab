# Este código calcula as raízes de uma equação quadrática usando a fórmula de Bhaskara.

# O usuário é solicitado a inserir o valor de a, que é o coeficiente do termo quadrático na equação.
a = int(input("Digite o valor de a: "))
# O usuário é solicitado a inserir o valor de b, que é o coeficiente do termo linear na equação.
b = int(input("Digite o valor de b: "))
# O usuário é solicitado a inserir o valor de c, que é o coeficiente do termo constante na equação.
c = int(input("Digite o valor de c: "))

# Calcula a primeira raiz usando a fórmula de Bhaskara e imprime o resultado.
x1 = (-b + (b**2 - 4*a*c) ** (1/2)) / (2*a)
print("O valor da primeira raiz é:", x1)

# Calcula a segunda raiz usando a fórmula de Bhaskara e imprime o resultado.
x2 = (-b - (b**2 - 4*a*c) ** (1/2)) / (2*a)
print("O valor da segunda raiz é:", x2)