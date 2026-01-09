import streamlit as st
import pandas as pd 
import httpx

data = httpx.get("http://127.0.0.1:8000/books").json()

df = pd.DataFrame(data)

st.markdown("# Book dashboard")
st.markdown("This dashboard gives an overview statistics about our book")

st.markdown("# Book KPI's")

cols = st.columns(4)

with cols[0]:
    st.metric("total books", len(df))
with cols[1]:
    st.metric("old books", len(df.query("year < 1860")))
with cols[2]:
    st.metric("newer books", len(df.query("year > 1860")))
with cols[3]:
    st.metric("unique authors", len(df["author"].unique()))


st.markdown("# Year distrubution")
ax = df["year"].plot(
    kind="hist",
    xlabel="year",
    ylabel="count",
    title="Year distrubution for all availables books",
    bins=20
)

fig = ax.get_figure()

st.pyplot(fig)

st.markdown("## All available books")

st.dataframe(df)