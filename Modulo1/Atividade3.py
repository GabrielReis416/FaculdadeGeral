# Entrada de Dados

altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")

# Calculo 

if sexo == "m":
    peso_ideal = 72.7 * altura - 58
    print(f"O peso ideal para um homem de {altura}m de altura é: {peso_ideal:.2f} kg")
elif sexo == "f":
    peso_ideal = 62.1 * altura - 44.7
    print(f"O peso ideal para uma mulher de {altura}m de altura é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido! Por favor, digite 'M' para masculino ou 'F' para feminino.")