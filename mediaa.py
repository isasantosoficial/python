aluno_maior_media = ""
maior_media = 0

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")

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