import streamlit as st, pandas as pd, plotly.express as px
st.set_page_config(page_title="Tourism Dashboard",layout="wide")
st.title("Tourism Data Analysis Dashboard")
df=pd.read_excel("../dataset/Tourism_Cleaned_Preprocessed.xlsx")
dest=st.sidebar.multiselect("Destination",sorted(df.destination.unique()),default=sorted(df.destination.unique()))
yr=st.sidebar.multiselect("Year",sorted(df.year.unique()),default=sorted(df.year.unique()))
d=df[df.destination.isin(dest)&df.year.isin(yr)]
c1,c2,c3=st.columns(3)
c1.metric("Bookings",len(d)); c2.metric("Avg Spend (USD)",round(d.spend_usd.mean(),1)); c3.metric("Avg Rating",round(d.rating.mean(),2))
m=d.groupby(["year","month"]).size().reset_index(name="bookings"); m["period"]=m.year.astype(str)+"-"+m.month.astype(str).str.zfill(2)
st.plotly_chart(px.line(m,x="period",y="bookings",title="Monthly Trend"),use_container_width=True)
a,b=st.columns(2)
a.plotly_chart(px.bar(d.destination.value_counts().reset_index(),x="destination",y="count",title="Top Destinations"),use_container_width=True)
b.plotly_chart(px.pie(d,names="origin_country",title="Origin Countries"),use_container_width=True)
