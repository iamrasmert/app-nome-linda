import streamlit as st

st.set_page_config(page_title="💖 Teste de Beleza 💖", page_icon="💖")

# Fundo rosa
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💖 Teste de Beleza 💖")
st.write("Descubra se você é a pessoa mais linda do mundo 👀✨")

# Música romântica (YouTube embed)
st.markdown(
    """
    <iframe width="0" height="0" src="https://www.youtube.com/embed/izGwDsrQ1eQ?autoplay=1&loop=1&playlist=izGwDsrQ1eQ"></iframe>
    """,
    unsafe_allow_html=True
)

nome = st.text_input("Digite seu nome:")

linda = ["leticia", "letícia", "Leticia", "Letícia", "lele", "lelê"]

if nome:
    if nome in linda:
        st.balloons()
        st.success("💖 A pessoa mais linda desse mundo que eu amo tanto! Te amo muito linda! ❤😍")
        st.markdown("### 🌹 Você é simplesmente perfeita 🌹")
        
        st.image(
            "https://i.imgur.com/4M7IWwP.png",
            caption="💞 Para a pessoa mais linda 💞"
        )
    else:
        st.warning("😅 Nomezinho mais ou menos...")
        st.markdown("Mas ainda assim é especial 💫")
