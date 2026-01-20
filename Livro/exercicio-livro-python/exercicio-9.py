# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e 
# quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante 
# perderá. Exiba o total em dias. 

fumo = int(input("Informe a quantidade de cigarros fumados por dia: "))
idade = int(input("Quantos anos já fumou ? "))

dias_fumando = idade * 365
total_cigarros = fumo * dias_fumando

minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440

print(f"Você perdeu aproximadamente {dias_perdidos:.2f} dias de vida. ")