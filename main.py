import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DATE_COLUMN = 'date'

@st.cache
def load_data(File):
    data1 = pd.read_csv(File)
    lowercase = lambda x: str(x).lower()
    data1.rename(lowercase, axis='columns', inplace=True)
    data1[DATE_COLUMN] = pd.to_datetime(data1[DATE_COLUMN])
    return data1

df_tsla = load_data("TSLA.csv")
df_f = load_data("F.csv")

df1 = df_tsla[["date", "close"]]
df2 = df_f[["date", "close"]]

fig, ax = plt.subplots(figsize=(25, 25))
ax.plot(df1["date"], df1["close"], label="Tesla")
ax.plot(df2["date"], df2["close"], label="Ford")
ax.legend(loc=2, prop={'size': 30})
plt.xlabel('Date', fontsize=18)
plt.ylabel('Price', fontsize=18)

st.subheader("The best vs The worst car maker")
st.pyplot(fig)
