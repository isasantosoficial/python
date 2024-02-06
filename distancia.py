#programa distancia
nome = input("Seu nome: ")
origem = input("Cidade de origem: ")
destino = input("Cidade de destino: ")
distancia = float(input("Qual a distâcia em km? "))
velocidade = float(input("Quantos km/h irá viajar? "))
tempo = distancia/velocidade

print(f"{nome}, o tempo estimado entre {origem} e {destino} é de {tempo} horas.")