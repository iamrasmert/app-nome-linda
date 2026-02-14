import streamlit as st

st.title("Teste de nome")

nome = st.text_input("Digite seu nome:")

linda = ["leticia", "letícia", "Leticia", "Letícia", "lele", "lelê", "Lele", "Lelê"]

if nome:
    if nome in linda:
        st.success("Esse é o nome do amor da minha vida, a pessoa mais linda desse mundo que eu amo tanto!, te amo muito linda❤, se eu pudesse te dar o mundo eu daria, um dia vamos ter nossa família e seremos muito felizes junto, Eu Te Amo!")
    else:
        st.warning("Nomezinho mais ou menos 😅")
