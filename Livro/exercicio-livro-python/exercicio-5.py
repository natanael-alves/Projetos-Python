# 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar.

preco = float(input("Informe o valor da mercadoria: R$ "))

desconto = float(input("Informe o valor do desconto: (%) "))

valor_desconto = (desconto / 100 ) * preco

pagar = preco - valor_desconto

print(f"O valor do desconto é de R$: {valor_desconto: .2f}")
print(f"O valor a ser pago é de: R$ {pagar: .2f}")