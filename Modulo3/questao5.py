import csv

dados_com_desconto = []

with open("produtos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    cabecalho = next(leitor)
    dados_com_desconto.append(cabecalho) 

    for linha in leitor:
        id_produto = linha[0]
        nome_produto = linha[1]
        preco = float(linha[2])
        preco_com_desconto = round(preco * 0.9, 2)  
        dados_com_desconto.append([id_produto, nome_produto, preco_com_desconto])

with open("produtos_desconto.csv", "w", newline='', encoding="utf-8") as novo_csv:
    escritor = csv.writer(novo_csv)
    escritor.writerows(dados_com_desconto)

print("Arquivo 'produtos_desconto.csv' criado com sucesso com 10% de desconto nos preços.")

with open("produtos_desconto.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
