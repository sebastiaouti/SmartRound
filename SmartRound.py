import streamlit as st
import random

def smartround_interface():
    st.title("🩺 SmartRound - Enfermaria")

    with st.form("form_evolucao"):
        nome = st.text_input("Nome do paciente")
        leito = st.text_input("Leito")
        sintomas = st.text_area("Sintomas / Queixas principais", height=150)
        lab = st.text_area("Exames laboratoriais", height=100)
        conduta = st.text_area("Conduta tomada", height=100)
        gerar_sinais = st.checkbox("Gerar sinais vitais genéricos", value=True)

        enviar = st.form_submit_button("Gerar Evolução")

        if enviar:
            sistolica = random.choice([120, 127, 133, 110])
            diastolica = random.choice([80, 83, 75, 80])
            fc = random.choice([60, 70, 80])
            fr = random.choice([16, 17, 18])

            sinais = f"PA: {sistolica}/{diastolica} mmHg, FC: {fc} bpm, FR: {fr} irpm" if gerar_sinais else "Sinais não informados."

            st.markdown(f"""
**Evolução de final de semana da Clínica Médica**

Paciente em acompanhamento pela equipe da clínica médica. Refere alimentação e sono preservados, diurese e evacuação mantidas. Nega febre, dispneia, náuseas ou outras queixas agudas no momento.

**Queixas**: {sintomas or "Sem queixas relevantes no momento."}
**Exames laboratoriais**: {lab or "Sem exames laboratoriais recentes ou sem alterações críticas."}

**Exame físico**:
BEG, orientado, afebril, corado, hidratado. {sinais}

**Conduta**:
{conduta or "Manter plano terapêutico vigente. Sem intercorrências no plantão."}

*By Sebastião Almeida*
""")
