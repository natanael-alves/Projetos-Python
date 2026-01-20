# 3.12 Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada
# para a viagem. 

distancia = float(input("Distância a pecorrer (Km): "))
velocidade = float(input("Informe a velocidade (Km/h): "))

tempo = distancia / velocidade

print(f"O tempo de viagem é de: {tempo:.2f} horas")