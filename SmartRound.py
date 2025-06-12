import streamlit as st
import openai
from docx import Document
from io import BytesIO


def gerar_evolucao(nome: str, leito: str, sintomas: str, lab: str, conduta: str) -> str:
    """Gera texto de evolução médica usando a API da OpenAI."""
    prompt = (
        f"Escreva uma evolução médica resumida para o paciente {nome} no leito {leito}. "
        f"Sintomas/queixas: {sintomas}. Exames laboratoriais: {lab}. Conduta tomada: {conduta}."
    )
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
        )
        texto = resposta.choices[0].message["content"].strip()
    except Exception as e:
        texto = f"Erro ao gerar evolução: {e}"
    return texto


def criar_docx(texto: str) -> BytesIO:
    doc = Document()
    doc.add_paragraph(texto)
    buf = BytesIO()
    doc.save(buf)
    buf.seek(0)
    return buf


def smartround_interface():
    st.title("🩺 SmartRound - Enfermaria")

    with st.form("form_evolucao"):
        nome = st.text_input("Nome do paciente")
        idade = st.text_input("Idade")
        leito = st.text_input("Leito")
        sintomas = st.text_area("Sintomas / Queixas principais", height=150)
        lab = st.text_area("Exames laboratoriais", height=100)
        conduta = st.text_area("Conduta tomada", height=100)
        enviar = st.form_submit_button("Gerar Evolução")

    if enviar:
        texto = gerar_evolucao(nome, leito, sintomas, lab, conduta)
        st.subheader("Evolução Gerada")
        st.markdown(texto)

        docx_data = criar_docx(texto)
        st.download_button(
            label="Baixar DOCX",
            data=docx_data,
            file_name="evolucao.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
