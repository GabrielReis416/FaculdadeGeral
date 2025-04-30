import csv

dados = [
    ["ID", "Produto", "Preço"],
    [1, "Produto A", 10.53],
    [2, "Produto B", 20.79],
    [3, "Produto C", 15.32]
]

with open("produtos.csv", "w", newline='', encoding="utf-8") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerows(dados)

print("Arquivo 'produtos.csv' criado com sucesso!")