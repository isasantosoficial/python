# Receber um número inteiro
numero = int(input("Digite um número inteiro: "))

# Exibir a tabuada do número fornecido
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")