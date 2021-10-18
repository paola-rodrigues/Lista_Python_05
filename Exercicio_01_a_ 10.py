print("Questão 1º")
'''
1.Faça um programa que então leia uma string e a imprima
'''
nome = input("Digite seu nome: ")
print(f"Seu nome é {nome}\n")


print("Questão 2º")
'''
2. Crie um programa que imprima o comprimento de uma string
'''
print("O tamanho do nome é {}\n".format(len(nome)))

print("Questão 3º")
'''
FaÇA um programa para converter uma letra maiuscula em letra minúscula. Use a tabela ´
ASCII para resolver o problema
'''
letra = input("Escreva uma letra maiúscula: ")
Ascii = ord(letra)
Ascii+= 32
print("A letra maiúscula {}, onde sua letra minúscula é {}\n".format(letra, chr(Ascii)))

print("Questão 4º")
'''
Crie um programa que compara duas strings
'''
senha = input("Digite uma senha: ")
senha_cadastro = input("Digite novamente a senha: ")
verificar = senha == senha_cadastro 
print(f"Sua senha está {verificar}\n")


print("Questão 5º")
'''
FaÇA um programa que leia um nome e imprima as 4 primeiras letras do nome.

'''
nome1 = input("Digite seu nome: ")
nome_primeiras = nome1[0:4]
print(f"As 4 primeiras letras é: {nome_primeiras}\n")


print("Questão 6º")
'''
Digite um nome, calcule e retorne quantas letras tem esse nome
'''
nome_novo = input("Digite um nome: ")
quantidade_letras = len(nome_novo)
print(f"Esse nome tem {quantidade_letras} letras\n") 


print("Questão 7º")
'''
Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25, imprime o nome da
pessoa e a palavra “ACEITA”, caso contrario imprimir “NÃO ACEITA”
'''
nome1 = input("Digite seu nome: ")
sexo = input("Qual o seu sexo: ")
idade = int(input("Digite sua idade: "))

if ((sexo == "feminino") and (idade < 25)):
            x = "ACEITA"
else:
            x = "NÃO ACEITA"

print(f"{nome1}, {x}\n")


print("Questão 8º")
'''
Faça um programa que conte o numero de 1’s que aparecem em um string. Exemplo: ´
0011001 -> 3
'''
nome_num = input("Digite uma letra: ")            
x = ' '.join(format(ord(x), 'b') for x in nome_num)
print(x)
y = x.count("1")
print(f"A letra digitada equivale a número {x}em binário e soma dos número 1 neste binário é {y}")

print("Questão 8 outa forma com 1")
num = input("Digite um número que contém 1:")
x = num.count("1")
print(f"O soma dos números um é {x}\n")


print("Questão 9º")
'''
Escreva um programa que substitui as ocorrencias de um caractere 0 em uma string por ˆ
outro caractere 1
'''
r = input("Digite um número com vários digitos que tenha 0 para ser substituído por 1: ") 
print(r.replace("0", "1"))



print("Questão 10º")
'''
Entre com um nome e imprima o nome somente se a primeira letra do nome for “a”
(maiuscula ou min ´ uscula). 
'''
nome = input("Digite seu nome:")
print("Seu nome é {}".format(nome.capitalize()))






