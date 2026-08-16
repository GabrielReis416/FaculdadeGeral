import pandas as pd
import matplotlib.pyplot as plt
import re
import statsmodels.api as sm

# ==========================================
# 1. CARREGAR O DATASET
# ==========================================

df = pd.read_csv("Sample-Data-CPU-Performance.csv")

print("Primeiras linhas do dataset:")
print(df.head())

print("\nDimensões do dataset:")
print(df.shape)

print("\nColunas:")
print(df.columns)


# ==========================================
# 2. PREPARAÇÃO DOS DADOS
# ==========================================

# A coluna CycleTime está no formato:
# Quantity[125, "Nanoseconds"]

# Extraindo apenas o número
df["CycleTime_ns"] = (
    df["CycleTime"]
    .str.extract(r"(\d+)")
    .astype(float)
)

# PublishedPerformance já é numérica
df["PublishedPerformance"] = pd.to_numeric(
    df["PublishedPerformance"]
)


# ==========================================
# 3. SELECIONAR AS VARIÁVEIS
# ==========================================

X = df["CycleTime_ns"]
Y = df["PublishedPerformance"]


# ==========================================
# 4. ESTATÍSTICAS DESCRITIVAS
# ==========================================

print("\nEstatísticas descritivas:")
print(df[["CycleTime_ns", "PublishedPerformance"]].describe())


# ==========================================
# 5. GRÁFICO DE DISPERSÃO
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(X, Y)

plt.xlabel("Tempo de ciclo (ns)")
plt.ylabel("Desempenho publicado")
plt.title("Tempo de ciclo × Desempenho do processador")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================
# 6. MODELO DE REGRESSÃO LINEAR
# ==========================================

# Adiciona o intercepto
X_modelo = sm.add_constant(X)

modelo = sm.OLS(Y, X_modelo).fit()

print("\n========== RESULTADO DA REGRESSÃO ==========")
print(modelo.summary())


# ==========================================
# 7. COEFICIENTES
# ==========================================

intercepto = modelo.params["const"]
coeficiente = modelo.params["CycleTime_ns"]
r2 = modelo.rsquared

print("\nIntercepto:", intercepto)
print("Coeficiente angular:", coeficiente)
print("R²:", r2)

print("\nEquação do modelo:")

print(
    f"Y = {intercepto:.4f} "
    f"{coeficiente:+.4f}X"
)


# ==========================================
# 8. VALORES ESTIMADOS
# ==========================================

df["Desempenho_Estimado"] = modelo.predict(X_modelo)

df["Residuo"] = (
    df["PublishedPerformance"]
    - df["Desempenho_Estimado"]
)

print("\nPrimeiros valores observados e estimados:")

print(
    df[
        [
            "CycleTime_ns",
            "PublishedPerformance",
            "Desempenho_Estimado",
            "Residuo"
        ]
    ].head(10)
)


# ==========================================
# 9. RETA DE REGRESSÃO
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(X, Y, label="Observações")

# Ordenar X para desenhar a reta corretamente
ordem = X.argsort()

plt.plot(
    X.iloc[ordem],
    df["Desempenho_Estimado"].iloc[ordem],
    label="Reta de regressão"
)

plt.xlabel("Tempo de ciclo (ns)")
plt.ylabel("Desempenho publicado")

plt.title(
    "Regressão linear: tempo de ciclo × desempenho"
)

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================
# 10. GRÁFICO DE RESÍDUOS
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Desempenho_Estimado"],
    df["Residuo"]
)

plt.axhline(
    0,
    linestyle="--"
)

plt.xlabel("Desempenho estimado")
plt.ylabel("Resíduos")

plt.title("Gráfico de resíduos")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================
# 11. CORRELAÇÃO
# ==========================================

correlacao = X.corr(Y)

print("\nCorrelação de Pearson:")
print(correlacao)
