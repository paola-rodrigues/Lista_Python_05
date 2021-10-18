#Questão 13
import re
'''
13. Faça um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui
essa palavra. Entre com um caractere (vogal ou consoante) e substitua todas as vogais
da palavra dada por esse caractere.
'''
palavra = input("Digite uma palavra: ")
contador = 0

for letra in palavra:
    if letra in "aeiouAEIOU":
        contador += 1
print(f"A palavra '{palavra}' tem {contador} vogais.")        

nova_letra = input("Digite um caractere 'vogal' ou 'consoante' : ")
sem_vogais = re.sub("[AEIOUaeiou]",nova_letra,palavra)
print(sem_vogais)
