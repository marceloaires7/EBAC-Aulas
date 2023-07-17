# Importações de Pacotes.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Funções para Visualizar os Gráficos.
def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    st.pyplot(fig=plt)
    return None

# Layout da Página.
st.set_page_config(page_title= 'Análise SINASC (Módulo15Tarefa1)',
                   page_icon= 'https://s3.amazonaws.com/gupy5/production/companies/39637/career/92146/images/2022-08-23_17-33_logo.jpg',
                   layout= 'wide')
st.write('# Análise SINASC')

# read_csv 'SINASC_RO_2019.csv'.
sinasc = pd.read_csv('./MaterialExercicio/input_M15_SINASC_RO_2019.csv')

st.slider('Slide me', min_value=0, max_value=10)
