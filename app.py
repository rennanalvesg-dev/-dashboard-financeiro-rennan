import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Dashboard Financeiro Rennan",
    layout="wide"
)

# =====================================
# DADOS
# =====================================

receita = 8063
gastos = 2064
aporte = 5000
patrimonio = 113679

gastos_categoria = pd.DataFrame({
    "Categoria":[
        "Alimentação",
        "Mercado",
        "Transporte",
        "Lazer",
        "Farmácia",
        "Compras",
        "Outros"
    ],
    "Valor":[661,413,310,248,165,145,122]
})

ativos = pd.DataFrame({
    "Ativo":[
        "Caixinhas (Nubank)",
        "FGTS",
        "Cripto (Bybit)",
        "Bolsa / Tesouro",
        "Conta Itaú"
    ],
    "Valor":[83607,16299,9500,700,3573]
})

evolucao = pd.DataFrame({
    "Mes":["Dez/25","Jan/26","Fev/26","Mar/26","Abr/26","Mai/26"],
    "Valor":[2490,2780,2930,3250,2880,2064]
})

# =====================================
# ESTILO
# =====================================

st.markdown("""
<style>

.stApp {
    background-color: #070B14;
    color: #F9FAFB;
}

.block-container {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

.card {
    background: linear-gradient(145deg,#111827,#0B1220);
    border-radius: 22px;
    padding: 22px;
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0 0 30px rgba(124,58,237,0.08);
    margin-bottom: 20px;
}

.metric-title {
    color: #9CA3AF;
    font-size: 14px;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 10px;
}

.green {
    color: #22C55E;
}

.red {
    color: #EF4444;
}

.blue {
    color: #3B82F6;
}

.purple {
    color: #A855F7;
}

.section-title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 0px;
    color: white;
}

.section-subtitle {
    color: #9CA3AF;
    margin-top: -5px;
    margin-bottom: 25px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# CABEÇALHO
# =====================================

st.markdown("""
<div class="section-title">
Visão Geral
</div>

<div class="section-subtitle">
Resumo da sua vida financeira
</div>
""", unsafe_allow_html=True)

# =====================================
# CARDS
# =====================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">
            Receita Mensal
        </div>

        <div class="metric-value green">
            R$ {receita:,.0f}
        </div>

        <div class="metric-title">
            Total líquido
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">
            Gastos no Período
        </div>

        <div class="metric-value red">
            R$ {gastos:,.0f}
        </div>

        <div class="metric-title">
            25,6% da receita
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">
            Aporte / Investimentos
        </div>

        <div class="metric-value blue">
            R$ {aporte:,.0f}
        </div>

        <div class="metric-title">
            62% da receita
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="metric-title">
            Patrimônio Total
        </div>

        <div class="metric-value purple">
            R$ {patrimonio:,.0f}
        </div>

        <div class="metric-title green">
            +2,35% no mês
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =====================================
# LINHA 1
# =====================================

col1,col2 = st.columns([1.1,1])

with col1:

    fig_gastos = px.pie(
        gastos_categoria,
        names="Categoria",
        values="Valor",
        hole=0.58,
        color_discrete_sequence=px.colors.sequential.Plasma
    )

    fig_gastos.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font_color="#F9FAFB",
        title="Gastos por Categoria",
        height=450
    )

    st.plotly_chart(
        fig_gastos,
        use_container_width=True
    )

with col2:

    fig_evolucao = go.Figure()

    fig_evolucao.add_trace(
        go.Scatter(
            x=evolucao["Mes"],
            y=evolucao["Valor"],
            mode="lines+markers+text",
            text=evolucao["Valor"],
            textposition="top center",
            line=dict(color="#9333EA", width=4),
            marker=dict(size=10)
        )
    )

    fig_evolucao.update_layout(
        title="Evolução dos Gastos",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font_color="#F9FAFB",
        height=450
    )

    st.plotly_chart(
        fig_evolucao,
        use_container_width=True
    )

st.write("")
st.write("")

# =====================================
# LINHA 2
# =====================================

col3,col4 = st.columns([1.1,1])

with col3:

    fig_ativos = px.pie(
        ativos,
        names="Ativo",
        values="Valor",
        hole=0.58,
        color_discrete_sequence=px.colors.sequential.Viridis
    )

    fig_ativos.update_layout(
        title="Alocação de Ativos",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font_color="#F9FAFB",
        height=450
    )

    st.plotly_chart(
        fig_ativos,
        use_container_width=True
    )

with col4:

    st.markdown("""
    <div class="card">
    """, unsafe_allow_html=True)

    st.subheader("Metas Financeiras")

    st.write("🏠 Compra da Casa")
    st.progress(84)
    st.caption("R$ 83.607 / R$ 100.000")

    st.write("📈 Aporte Mensal")
    st.progress(100)
    st.caption("R$ 5.000 / R$ 5.000")

    st.write("💳 Gastos Mensais")
    st.progress(69)
    st.caption("R$ 2.064 / R$ 3.000")

    st.write("")
    st.metric(
        "Patrimônio Atual",
        f"R$ {patrimonio:,.0f}"
    )

    st.markdown("</div>", unsafe_allow_html=True)
