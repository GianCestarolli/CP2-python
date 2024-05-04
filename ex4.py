usuario1 = []
usuario2 = []

for k in range(1, 6):
    jogo = int(input(f'Insira o valor do jogo número {k} comprado pelo usuário 1: '))
    usuario1.append(jogo)
for i in range(1, 6):
    jogo = int(input(f'Insira o valor do jogo número {i} comprado pelo usuário 2: '))
    usuario2.append(jogo)

soma1 = 0
soma2 = 0

for valor in usuario1:
    soma1 += valor


for valor in usuario2:
    soma2 += valor


media1 = sum(usuario1) / 5
media2 = sum(usuario2) / 5

print(f'O valor total da compra do usuário 1 é: {soma1}')
print(f'A média de preços do usuário 1 foi: {media1}')
print(f'O valor total da compra do usuário 2 é: {soma2}')
print(f'A média de preços do usuário 2 foi: {media2}')