import streamlit as st
import pandas as pd
import yfinance as yf
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------- Funções auxiliares -----------------------------
@st.cache_data
def carregar_dados(ticker="RENT3.SA", inicio="2023-01-01", fim="2025-06-25"):
    try:
        df = yf.download(ticker, start=inicio, end=fim)[['Open', 'Close']].dropna()
        df['target'] = (df['Open'] > df['Close']).astype(int)  # 1 = queda (abriu > fechou)
        df['pct_return'] = ((df['Close'] - df['Open']) / df['Open']) * 100
        df.index = pd.to_datetime(df.index)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

def treinar_modelo(df, anos_treino):
    train_df = df[df.index.year.isin(anos_treino)]
    test_df = df[df.index.year == 2025]

    X_train = train_df[['Open', 'Close']]
    y_train = train_df['target']
    X_test = test_df[['Open', 'Close']]
    y_test = test_df['target']

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    return model, y_test, y_pred, test_df

def calcular_metricas(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    return acc, cm, specificity, classification_report(y_test, y_pred, target_names=["0", "1"])

def calcular_retorno(test_df, y_pred):
    test_df = test_df.copy()
    test_df['pred'] = y_pred

    # Simulação de operação vendida: retorno é o negativo do pct_return
    test_df['retorno_simulado'] = -test_df['pct_return']

    acertos = test_df[(test_df['pred'] == 1) & (test_df['target'] == 1)]
    erros = test_df[(test_df['pred'] == 1) & (test_df['target'] == 0)]

    ganho_medio = acertos['retorno_simulado'].mean()
    perda_medio = erros['retorno_simulado'].mean()
    retorno_total = acertos['retorno_simulado'].sum() + erros['retorno_simulado'].sum()
    return ganho_medio, perda_medio, retorno_total

# ----------------------------- Interface -----------------------------
st.title("📊 Dashboard de Análise com KNN – RENT3.SA")

anos_treino = st.multiselect("Selecione os anos para Treinamento:", [2023, 2024], default=[2023, 2024])

df = carregar_dados()

if df.empty:
    st.warning("Nenhum dado disponível.")
else:
    # ---------- Gráficos ----------
    st.subheader("📈 Série Temporal – Preço de Abertura e Fechamento")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(df.index, df['Open'], label="Abertura", alpha=0.6)
    ax1.plot(df.index, df['Close'], label="Fechamento", alpha=0.6)
    ax1.set_ylabel("Preço (R$)")
    ax1.legend()
    st.pyplot(fig1)

    st.subheader("🔄 Distribuição das Classes (Target)")
    classe_pct = df['target'].value_counts(normalize=True) * 100
    fig2, ax2 = plt.subplots()
    classe_pct.plot(kind='bar', color=['skyblue', 'salmon'], ax=ax2)
    ax2.set_xticklabels(['0 (Fechamento ≥ Abertura)', '1 (Abertura > Fechamento)'], rotation=0)
    ax2.set_ylabel('Porcentagem (%)')
    st.pyplot(fig2)

    # ---------- Treinamento ----------
    model, y_test, y_pred, test_df = treinar_modelo(df, anos_treino)
    acc, cm, specificity, class_report = calcular_metricas(y_test, y_pred)
    ganho_medio, perda_medio, retorno_total = calcular_retorno(test_df, y_pred)

    # ---------- Métricas ----------
    st.subheader("📊 Métricas do Modelo")
    st.markdown(f"- **Acurácia:** `{acc:.2f}`")
    st.markdown(f"- **Especificidade:** `{specificity:.2f}`")
    st.text("Matriz de Confusão:")
    st.text(f"TN: {cm[0,0]}, FP: {cm[0,1]}, FN: {cm[1,0]}, TP: {cm[1,1]}")
    st.text("Relatório de Classificação:")
    st.text(class_report)

    # ---------- Financeiro ----------
    st.subheader("💰 Retorno Financeiro Simulado (Operação Vendida)")
    st.markdown(f"- **Ganho médio por acerto:** `{ganho_medio:.2f}%`")
    st.markdown(f"- **Perda média por erro:** `{perda_medio:.2f}%`")
    st.markdown(f"- **Retorno total líquido:** `{retorno_total:.2f}%`")