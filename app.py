import streamlit as st

st.set_page_config(
    
    page_title="Painel de Abito",
    page_icon="",
    layout="wide"

)

st.title("Painel de Abitos")
st.subheader("Registre e visualize o seus abitos diarios ")

#Barra lateral
st.sidebar.header("Seus abitos")
sono = st.sidebar.slider("Horas de sono", 0, 12 , 8)
agua = st.sidebar.slider("Copos de agua", 0, 10, 5)
exercicio = st.sidebar.selectbox("Exercico", ["Nenhum", "Leve", "Moderado", "Intenso"])

st.metric("Sono", f"{sono} horas")
st.metric("Agua", f"{agua} copos")
st.metric("Execicio", exercicio)

#colunas para visualização
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Detalhes do sono")
    st.write("Voce dormiu bem!" if sono >= 7 else "Tentar dormir mais")

with col2:
    st.header("Hidratação")
    st.write("Otimo voce estar mais Hidratado!" if agua >= 6 else "Beba mais agua!")

with col3:
    st.header("Exercicio")
    st.write("Parabens!" if exercicio != "nenhum" else "Tente se movimentar hoje")

with st.expander("Dicas rapidas"):
    st.write("- Durma pelo menos 7 horas")
    st.write("- Beba pelo menos 6 copos de Agua")
    st.write("- Faça algum exercico todos os dias ")

st.markdown("---")
st.markdown("Projeto com streamlit")

