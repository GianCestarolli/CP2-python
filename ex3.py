salarios = [1800, 2500, 3200, 4200, 5000]
salario_10 = []
salario_20 = []
salario_30 = []

for salario in salarios:
    if salario <= 2000:
        salario_final = salario - (salario * 0.1)
        salario_10.append(salario_final)
    elif salario <= 4000:
        salario_final = salario - (salario * 0.2)
        salario_20.append(salario_final)
    else:
        salario_final = salario - (salario * 0.3)
        salario_30.append(salario_final)

print("Salários líquidos com desconto de 10%:", salario_10)
print("Salários líquidos com desconto de 20%:", salario_20)
print("Salários líquidos com desconto de 30%:", salario_30)
