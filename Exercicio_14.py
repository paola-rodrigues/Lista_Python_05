#Questão 14
import re
'''
14. Ler uma frase e contar quantos caracteres sao brancos. Lembre-se que uma frase ˜ e um ´
conjunto de caracteres (vetor).
'''
frase = input("Digite uma frase: ")
contador = 0

for letra in frase:
    if letra in " ":
        contador += 1
print(f"A frase '{frase}' tem {contador} caracteres em brancos.")        

