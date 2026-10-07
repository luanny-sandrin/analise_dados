#------ RODE python -m streamlit run pathdoseuarquivo.py Path(H:\Python\3°etapa\streamlit_aula1\st_aula1.py) ou RelativePath(st_aula1.py)

import pandas as pd
import streamlit as st 

idade = 19
nome = "Luanny"
st.write("Olá ", nome, idade)

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# }) (Mude os valores para Português, Matemática, Python e Frame, e na segunda coluna para 5, 9, 7, 10)

df = pd.DataFrame({
    'first column': ["Português", "Matemática", "Python", "Frame"],
    'second column': [5, 9, 7, 10]
})
df

st.title("Meu primeiro dash")
st.subheader("Luanny")
