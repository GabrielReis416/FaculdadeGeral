import csv

with open("produtos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    
    next(leitor)  
    
    for linha in leitor:
        print(f"{linha[1]} - {linha[2]}")
