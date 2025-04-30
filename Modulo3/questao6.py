import pandas as pd

dados = {
    "Aluno": ["João", "Maria", "José", "Ana"],
    "Nota 1": [7.5, 8.2, 6.9, 9.1],
    "Nota 2": [8.0, 7.5, 6.5, 9.5]
}

df = pd.DataFrame(dados)

print("DataFrame completo:")
print(df)

print("\nColuna 'Aluno':")
print(df["Aluno"])

print("\nPrimeira linha do DataFrame:")
print(df.iloc[0])

jose = df[df["Aluno"] == "José"]
media_jose = (jose["Nota 1"].values[0] + jose["Nota 2"].values[0]) / 2
print(f"\nMédia das notas do aluno José: {media_jose:.2f}")