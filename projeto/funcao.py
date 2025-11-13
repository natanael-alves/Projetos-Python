# Funções 

# Funções são blocos de código reutilizáveis que realizam 
# uma tarefa específica em vez de escrever o mesmo código
# várias vezes, criamos uma função e apenas a chamamos sempre que necessário.

# Exemplo "real"
# Imagine que você tenha que calcular o imposto de vários produtos em uma loja.
# Em vez de repetir a conta várias vezes, você pode criar uma função 
# chamada calcular_imposto() e usá-la sempre que precisar.



# def saudacao(nome) :
#     print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

# saudacao("Natanael")



# retorno de valores

# def subtrair(a, b):
#     return a - b

# resultado = subtrair(900, 500)

# print(f"a subtração é : {resultado}")


#Função com vários parametros.

def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

# Chmando a função
resultado = calcular_media(10, 5, 8)
print(f"A média é: {resultado:.2f}")