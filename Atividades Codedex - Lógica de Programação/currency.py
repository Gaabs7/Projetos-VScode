
pesos = int(input("Quanto você tem em pesos?"))
solas = int(input("Quando você tem em solas?"))
reais = int(input("Quanto você tem em reais?"))

//pegar o valor que o usuário me der, e multiplicar pelos decimais (esse vai ser o valor de USD)

total = pesos *0.00031 + solas * 0.29 + reais * 0.20

print (total)

