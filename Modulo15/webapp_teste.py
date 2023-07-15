import streamlit as st

st.title('Título')

st.header('Header')

st.subheader('SubHeader')

st.markdown('----')


st.markdown('# Isso é um texto com markdown e um [#]')
st.markdown('## Isso é um texto com markdown e um [##]')
st.markdown('### Isso é um texto com markdown e um [###]')

st.markdown('----')

st.markdown('Markdown normal')

st.markdown('_Markdown itálico_')
st.markdown('*Markdown itálico*')

st.markdown('__Markdown negrito__')
st.markdown('**Markdown negrito**')

st.markdown('***Markdown negrito itálico***')
st.markdown('*__Markdown negrito itálico__*')
st.markdown('_**Markdown negrito itálico**_')

st.markdown('----')

st.markdown('Isso é um link pro [google](https://www.google.com.br/)')

st.markdown("<h1 style='text-align: center; color: red;'>Título em vermelho</h1>", unsafe_allow_html=True)

st.markdown('Olá, mundo :sunglasses:')
st.markdown('Olá, mundo :100:')

st.markdown('----')


st.markdown('''
            MARKDOWN | PEQUENO | GRANDE
             ---     | ---     |  ---
            *ITÁLICO*| `CODE`  | **NEGRITO**
            ''')

st.markdown('----')


st.write('Bem-vindo')