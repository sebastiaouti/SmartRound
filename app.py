
import streamlit as st

# Login simples
def login():
    st.title("SmartRound")
    st.subheader("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if username == "sebastiao.junior" and password == "107242":
            st.session_state["autenticado"] = True
        else:
            st.error("Usuário ou senha incorretos")

# Evolução médica
def formulario():
    st.title("SmartRound - Evolução Médica")
    nome = st.text_input("Nome do paciente")
    leito = st.text_input("Leito")
    queixa = st.text_area("Queixa principal / motivo da avaliação")
    sinais_auto = st.checkbox("Gerar sinais vitais automaticamente", value=True)

    pa = st.text_input("PA", placeholder="Ex: 120/80")
    fc = st.text_input("FC", placeholder="Ex: 70")
    fr = st.text_input("FR", placeholder="Ex: 16")

    if st.button("Gerar evolução"):
        st.subheader("Texto gerado:")
        st.markdown(f"""**Evolução de final de semana da Clínica Médica**

Paciente {nome}, leito {leito}, em acompanhamento. Queixa principal: {queixa or "não referida"}. 
PA: {pa or "127/83"} | FC: {fc or "70"} | FR: {fr or "17"}

Sem outras intercorrências no plantão.""")

if "autenticado" not in st.session_state:
    login()
elif st.session_state["autenticado"]:
    formulario()
