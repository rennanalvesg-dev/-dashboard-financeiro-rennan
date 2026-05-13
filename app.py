import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Financeiro Rennan",
    layout="wide"
)

# =========================
# DADOS
# =========================

patrimonio_total = 113679
liquidez = 92000
meta_aporte = 5000
meta_gastos = 3000

gastos = pd.DataFrame({
    "Categoria": [
        "Alimentação",
        "Delivery",
        "Transporte",
        "Farmácia",
        "Compras",
        "Parcelamentos",
        "Viagens"
    ],
    "Valor": [800,600,500,300,400,700,250]
})

ativos = pd.DataFrame({
    "Ativo":[
        "Nubank",
        "FGTS",
        "Cripto",
        "Ações",
        "Conta Itaú"
    ],
    "Valor":[83607,16299,9500,700,3573]
})

# =========================
# ESTILO
# =========================

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

[data-testid="stMetric"] {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================

st.title("💰 Dashboard Financeiro - Rennan")

st.markdown("### Visão geral financeira")

# =========================
# CARDS
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Patrimônio Total",
    f"R$ {patrimonio_total:,.0f}"
)

col2.metric(
    "Liquidez",
    f"R$ {liquidez:,.0f}"
)

col3.metric(
    "Meta Investimento",
    f"R$ {meta_aporte:,.0f}"
)

col4.metric(
    "Limite Gastos",
    f"R$ {meta_gastos:,.0f}"
)

st.divider()

# =========================
# GRÁFICOS
# =========================

col5, col6 = st.columns(2)

with col5:

    fig_gastos = px.pie(
        gastos,
        names="Categoria",
        values="Valor",
        hole=0.55,
        title="Gastos por Categoria",
        color_discrete_sequence=px.colors.sequential.Plasma
    )

    fig_gastos.update_layout(
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        font_color="white"
    )

    st.plotly_chart(
        fig_gastos,
        use_container_width=True
    )

with col6:

    fig_ativos = px.pie(
        ativos,
        names="Ativo",
        values="Valor",
        hole=0.55,
        title="Distribuição Patrimonial",
        color_discrete_sequence=px.colors.sequential.Viridis
    )

    fig_ativos.update_layout(
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        font_color="white"
    )

    st.plotly_chart(
        fig_ativos,
        use_container_width=True
    )

# =========================
# EVOLUÇÃO PATRIMONIAL
# =========================

evolucao = pd.DataFrame({
    "Mes":["Jan","Fev","Mar","Abr","Mai"],
    "Patrimonio":[65000,78000,92000,105000,113679]
})

fig_evolucao = px.line(
    evolucao,
    x="Mes",
    y="Patrimonio",
    markers=True,
    title="Evolução Patrimonial"
)

fig_evolucao.update_layout(
    paper_bgcolor="#1e293b",
    plot_bgcolor="#1e293b",
    font_color="white"
)

st.plotly_chart(
    fig_evolucao,
    use_container_width=True
)

# =========================
# TABELA
# =========================

st.subheader("Resumo dos Gastos")

st.dataframe(
    gastos,
    use_container_width=True
)
