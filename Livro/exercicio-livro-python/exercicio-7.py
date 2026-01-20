# 3.13 Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é: 9 x C
#                                                                                                           -------  +  32
#                                                                                                               5

c = float(input("Informe a temperatura em celsius : "))
f = (9 * c) / 5 + 32

print(f"A temperatura em ºF é: {f}")
