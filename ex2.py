nomes = []
cpfs = []

contador = 0

while contador < 4:
    nome = input(f"Digite o nome número {contador +1}: ")
    cpf = input(f"Digite o cpf número {contador +1}: ")
    nomes.append(nome)
    cpfs.append(cpf)
    contador += 1
print(nomes)
print(cpfs)