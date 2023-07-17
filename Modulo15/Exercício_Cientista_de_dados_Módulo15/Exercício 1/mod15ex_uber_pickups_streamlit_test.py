#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import time

st.set_page_config(page_title='Ebac - Módulo 15 - Tarefa 01',
                   layout='wide',
                   page_icon='https://ebaconline.com.br/favicon.ico')

st.title("Módulo 15 - Tarefa 01")
st.markdown("#### Acesse os links abaixo, leia o conteúdo e crie uma aplicação com streamlit reproduzindo pelo menos 20 códigos extraídos das páginas.")
st.markdown('''https://docs.streamlit.io/en/stable/getting_started.html <br>
            https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html
            https://docs.streamlit.io/en/stable/advanced_concepts.html
            https://docs.streamlit.io/en/stable/caching.html
            https://docs.streamlit.io/en/stable/api.html
            https://docs.streamlit.io/en/stable/session_state_api.html
            https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py''')

st.markdown("##### Exemplo 01")
st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

st.markdown("##### Exemplo 02")
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

st.markdown("##### Exemplo 03")
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.markdown("##### Exemplo 04")
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.markdown("##### Exemplo 05")
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

st.markdown("##### Exemplo 05")
st.subheader('st.latex')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.markdown("##### Exemplo 06")
st.subheader('st.code')
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.markdown("##### Exemplo 07")
st.subheader('st.table')
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

st.markdown("##### Exemplo 08")
st.subheader('st.metric')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.markdown("##### Exemplo 09")
st.subheader('st.area_chart')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

st.markdown("##### Exemplo 10")
st.subheader('st.bar_chart')
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.markdown("##### Exemplo 11")
st.subheader('st.pyplot')
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.markdown("##### Exemplo 12")
st.subheader('st.altair_chart')
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

st.markdown("##### Exemplo 13")
st.subheader('st.button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.markdown("##### Exemplo 14")
st.subheader('st.checkbox')
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

st.markdown("##### Exemplo 15")
st.subheader('st.file_uploader')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


st.markdown("##### Exemplo 16")
st.subheader('st.info')
st.info('This is a purely informational message', icon="ℹ️")

st.markdown("##### Exemplo 17")
st.subheader('st.progress')
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

st.markdown("##### Exemplo 18")
st.subheader('st.exception')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

st.markdown("##### Exemplo 19")
st.subheader('st.warning')
st.warning('This is a warning', icon="⚠️")

st.markdown("##### Exemplo 20")
st.subheader('st.success')
st.success('This is a success message!', icon="✅")

