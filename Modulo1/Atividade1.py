# Entrada de Dados
valorConta = float(input("Digite o valor da conta: R$ "))
percentualDesconto = float(input("Digite o percentual de desconto: "))

# cálculo
desconto = valorConta * (percentualDesconto / 100)
valorFinal = valorConta - desconto

# Resultado 
print(f"O valor da conta após o desconto de {percentualDesconto}% é: R$ {valorFinal:.2f}")