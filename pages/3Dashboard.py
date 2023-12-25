import streamlit as st
import pandas as pd
import plotly.express as px

st.title(":signal_strength: :blue[ Let's take a look at the statistics of last 5 years]")
st.write("---")

df = pd.read_csv("data_csv.csv")   

ASD_traits_data=df["ASD_traits"].unique().tolist()
select_date=st.selectbox("ASD traits ?",ASD_traits_data)
df_up=df[df["ASD_traits"].isin(ASD_traits_data)]

sub_opt=df_up["Sex"].unique().tolist()
select_sub=st.multiselect("Gender",sub_opt)
df_up_sub=df_up[df_up["Sex"].isin(select_sub)]
st.write("---")
col1,col2=st.columns(2)
with col1:
    st.subheader("Jaundice statistics")
    with st.expander("See the plot"):     
        fig=px.bar(df_up_sub,x="Sex",color="Jaundice")
        fig.update_layout(height=500,width=200)
        st.write(fig)

with col2:
    st.subheader("Childhood Autism Rating Scale statistics")
    with st.expander("See the plot"):        
        fig=px.bar(df_up_sub,x="Sex",color="Childhood Autism Rating Scale")
        fig.update_layout(height=500,width=200)
        st.write(fig)
st.write("---")
col1,col2=st.columns(2)
with col1:
    st.subheader("Family member with ASD statistics")
    with st.expander("See the plot"):     
        fig=px.bar(df_up_sub,x="Sex",color="Family_mem_with_ASD")
        fig.update_layout(height=500,width=200)
        st.write(fig)

with col2:
    st.subheader("Social Responsiveness Scale statistics")
    with st.expander("See the plot"):        
        fig=px.bar(df_up_sub,x="Sex",color="Social_Responsiveness_Scale")
        fig.update_layout(height=500,width=200)
        st.write(fig)