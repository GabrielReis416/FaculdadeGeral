with open("notas.txt", "a") as arquivo:
    arquivo.write("Joao Aquino: 10\n")

with open("notas.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo atualizado do arquivo 'notas.txt':")
print(conteudo)