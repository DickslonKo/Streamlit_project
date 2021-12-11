import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df_sales = pd.read_csv("Tesla_car_sales.csv")

with st.form("my_form"):
    st.write("Display Option")
    report_type = st.radio('Which year car sales', ('2015', "2016", "2017", "2018", "2019", "2020", "2021"))

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Year",report_type)

if report_type =="2015":
    st.write(df_sales.iloc[0,1:].sum())

if report_type =="2016":
    st.write(df_sales.iloc[1,1:].sum())

if report_type =="2017":
    st.write(df_sales.iloc[2,1:].sum())

if report_type =="2018":
    st.write(df_sales.iloc[3,1:].sum())

if report_type =="2019":
    st.write(df_sales.iloc[4,1:].sum())

if report_type =="2020":
    st.write(df_sales.iloc[5,1:].sum())

if report_type =="2021":
    st.write(df_sales.iloc[6,1:].sum())

DATE_COLUMN = 'date'

@st.cache
def load_data(File):
    data1 = pd.read_csv(File)
    lowercase = lambda x: str(x).lower()
    data1.rename(lowercase, axis='columns', inplace=True)
    data1[DATE_COLUMN] = pd.to_datetime(data1[DATE_COLUMN])
    return data1

df_tsla = load_data("TSLA.csv")
# df_sales["Year"] = pd.to_datetime(df_sales["Year"])
# df_sales["Total"] = df_sales["Q1"] + df_sales["Q2"] + df_sales["Q3"] + df_sales["Q4"]
df1 = df_tsla[["date", "close"]]
df2 = df_sales
df2 = pd.melt(df2, id_vars=['Year'], value_vars=['Q1', "Q2", "Q3", "Q4"])
# df2 = df_sales[["Year", "Total"]]
labels = ["2015", "2016", "2017", "2018", "2019", "2020", "2021"]
x = np.arange(len(labels))
barWidth = 0.25

fig, ax = plt.subplots(2, figsize=(25, 25))
ax[0].plot(df1["date"], df1["close"], label="Tesla")
ax[1] = sns.barplot(x="Year", y="value", hue="variable", data=df2)
# ax[1].bar_label(Q1, padding=3)
# ax[1].bar_label(Q2, padding=3)
# ax[1].bar_label(Q3, padding=3)
# ax[1].bar_label(Q4, padding=3)
# ax.legend(loc=2, prop={'size': 30})
ax[0].set_xlabel('Date', fontsize=18)
ax[0].set_ylabel('Price', fontsize=18)
ax[1].set_xlabel('Year', fontsize=18)
ax[1].set_ylabel('Car_sales', fontsize=18)
# ax[1].set_xticks(x, labels)
st.subheader("The greatest company in the world")
st.pyplot(fig)

