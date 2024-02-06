aluno_maior_media = ""
maior_media = 0

anterior = float(input("Digite o primeiro número inteiro: "))
while anterior != int(anterior):
    print("Por favor, digite um número inteiro.")
    anterior = float(input("Digite o primeiro número inteiro: "))

for i in range(2, 4):  # Começar do segundo número, já que o primeiro já foi lido
    numero = float(input(f"Digite o {i}º número inteiro: "))

    # Verificar se o número atual é menor que o anterior
    while numero < anterior or numero != int(numero):
        print(f"O número {numero} não é inteiro ou é menor que o anterior. Tente novamente.")
        numero = float(input(f"Digite o {i}º número inteiro: "))

    anterior = numero  # Atualizar o número anterior

    # Restante do código (pode ser adaptado conforme necessário)
    nome = input(f"Digite o nome do {i}º aluno: ")

    prova1 = float(input("Digite a nota da primeira prova: "))
    while prova1 < 0 or prova1 > 10:
        prova1 = float(input("Digite o valor de 0-10 para a prova1: "))

    prova2 = float(input("Digite a nota da segunda prova: "))
    while prova2 < 0 or prova2 > 10:
        prova2 = float(input("Digite o valor de 0-10 para a prova2: "))

    trabalho = float(input("Digite a nota do trabalho: "))
    while trabalho < 0 or trabalho > 10:
        trabalho = float(input("Digite o valor de 0-10 para o trabalho: "))

    media = prova1 * 0.35 + prova2 * 0.35 + trabalho * 0.3
    if media >= 5.0:
        situacao = "Aprovado"
    elif 3.5 < media < 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"O aluno {nome} teve a média final {media}. Situação: {situacao}\n")

    # Atualizar o aluno com a maior média
    if media > maior_media:
        maior_media = media
        aluno_maior_media = nome

print(f"O aluno com a maior média foi {aluno_maior_media} com média {maior_media}.")
