import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Média de preço por categoria de livros")

uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    sorted_data = data.groupby('category')['price'].mean().sort_values(ascending=True)
    
    sorted_data.plot(xlabel = 'Categoria', ylabel = 'Preço médio', kind = 'bar', figsize=(10,4))

    st.title("Média de preço")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()