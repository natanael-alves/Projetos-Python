# Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado pelo usuário, assim como a quantidade de dias 
# pelos os quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0.15 por Km rodado.

distancia = float(input("Informe a quantidade de Km percorrido: "))
diaria = float(input("Informe a quantidade de dias que ficou com o carro: "))

pagamento = (distancia * 0.15) + (diaria * 60)

print(f"O preço a pagar é de: {pagamento:.2f}")