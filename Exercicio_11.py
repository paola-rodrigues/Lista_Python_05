#questão 11
nome = input("Digite um nome: ")
nome_rev = " ".join(reversed(nome))
print(f"Este nome de trás-para-frente é {nome_rev}")

#questão 11 outra forma
print(nome[::-1])
