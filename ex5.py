
  
produtos_comprados = []
contador = 0

while contador < 5:
    produto = input(f"Digite o produto {contador + 1}: ").lower()
    produtos_comprados.append(produto)
    contador += 1

produtos_disponiveis = ["notebook", "ssd", "mouse", "teclado", "monitor"]
produtos_verificados = []

for produto in produtos_comprados:
    if produto in produtos_disponiveis:
        produtos_verificados.append(produto)


contagem_produtos = []
for produto in produtos_verificados:
  if produto not in contagem_produtos:
    contagem_produtos.append(produto)
    contagem_produtos.append(1)
  else:
    indice_produto = contagem_produtos.index(produto)
    contagem_produtos[indice_produto + 1] += 1


print("Contagem de produtos:")
for i in range(0, len(contagem_produtos), 2):
  produto = contagem_produtos[i]
  quantidade = contagem_produtos[i + 1]
  print(f"{produto}: {quantidade}")
