# exercicio 3.8 : Escreva um programa que leia um valor em metros e exiba convertido em milímetros.

metros = float(input("Informe a metragem: "))
milimetro = 1000

convert = metros * milimetro 

print(f"metragem em milímetros é:  {convert: .2f}")