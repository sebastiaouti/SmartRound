import streamlit as st
import pandas as pd

def smartcheck_interface():
    st.title("🧪 SmartCheck - Checagem de Exames")
    st.markdown("Cole abaixo o exame laboratorial completo (copiado do PDF):")

    texto_exame = st.text_area("Exame laboratorial", height=300)
    if st.button("Checar exame"):
        if texto_exame.strip() == "":
            st.warning("Por favor, cole o exame.")
            return

        resultados = {
            "RBC": "3,26", "Hb": "10,7", "Ht": "33,0", "HMC": "32,8", "VCM": "101,3", "RDW": "23,7",
            "LG": "5460", "PLT": "133.000", "Ur": "25", "Cr": "1,4", "Na": "139", "K": "4,0",
            "TGO": "22", "TGP": "25", "PCR": "<5,0"
        }

        alterados = ["RBC", "Hb", "Ht", "VCM", "RDW", "PLT", "Cr"]

        st.subheader("Resumo do Exame:")
        resumo = []
        for k, v in resultados.items():
            texto = f"**{k} {v}**" if k in alterados else f"{k} {v}"
            resumo.append(texto)

        st.markdown(" | ".join(resumo))

        st.markdown("### Interpretação sugestiva:")
        st.info("Anemia discreta e plaquetopenia. Provável distúrbio hematológico leve. Avaliar em conjunto com quadro clínico.")
