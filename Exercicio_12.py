import re
#Questão 12
'''
12. Faça um programa que receba do usuario uma string. O programa imprime a string sem ´
suas vogais.
'''
x = input("Digite um nome: ")
sem_vogais = re.sub("[AEIOUaeiou]","",x)
print(sem_vogais)
