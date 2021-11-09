#Questão 15
'''
Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da
palavra. Imprima a string resultante.
'''

cont = 0
letra = list(input("Digite uma palavra : ")) #transformado em lista

while cont <= (len(letra))- 1 :
    letra[cont] = chr(ord(letra[cont]) + 1)
    cont+=1
    nova_palavra = ''.join(letra)
    if cont == (len(letra)):
        print(f" A palavra com a soma de +1  em cada caractere é '{nova_palavra}'")
 

