#Questão 18
'''
Leia um vetor contendo letras de uma frase inclusive os espaços em branco. Retirar os
espaços em branco do vetor e depois escrever o vetor resultante.

'''
frase = input("Digite uma frase: ")
nova_palavra = (frase .replace(" ", ""))
print(f" A frase {frase} retirando os espaços em branco é:\n {nova_palavra}")
 
