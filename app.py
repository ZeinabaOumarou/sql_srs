import streamlit as st
import pandas as pd
import duckdb as db

st.write("Hello World")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label="Entrez votre code")
    result = db.query(sql_query).df()
    st.write(result)
    # st.dataframe(df)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlitio/examples/dog.jpg", width=200)

with tab3:
    st.header("An owL")
