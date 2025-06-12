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

        # Exemplo simplificado de parser de exames
        resultados = [
            {"Exame": "Hb", "Valor": "10,7", "Alterado": True},
            {"Exame": "Ht", "Valor": "33,0", "Alterado": True},
            {"Exame": "Cr", "Valor": "1,4", "Alterado": True},
        ]
        df = pd.DataFrame(resultados)
        st.subheader("Resumo do Exame:")
        st.table(df)
        st.info("Interpretação sugestiva: Anemia discreta. Avaliar em conjunto com quadro clínico.")
