import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.title(":blue[GTRI MERMAID]")
st.write("The buoy of the future")


df = pd.DataFrame([[32.78171,-117.24964]])
df.columns = ["LAT", "LON"]
print(df)

with open("my_map.html","r") as f:
    html_data = f.read()

st.components.v1.html(html_data,height=500)
st.map(df)