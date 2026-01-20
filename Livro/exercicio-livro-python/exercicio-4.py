# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o 
# valor do aumento e do novo salário.

salario = float(input("Informe o salário: "))
aumento = float(input("Informe o aumento (%): "))

novo_provento = salario * aumento / 100
novo_salario = salario + novo_provento

print(f"Você teve um aumeto  de: R$ {novo_provento}")
print(f"Seu novo salário é: R$ {novo_salario}")
