import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





#Title
st.title("Mehmet Koc Makine Öğrenmesi Deneme")





#Image
st.image("yapayzekaegitimlogo.png",width=500) 





data = sns.load_dataset("tips")
st.write("Shape of a dataset",data.shape)





menu = st.sidebar.radio("Menu",["Tips","Tips2"])
if menu=="Tips":
    st.header("Tips")
    if st.checkbox("Tips"):
        st.table(data.head(50))
        
        
    st.title("Graphs")
    graph=st.selectbox("Different types of graphs",["Scatter Plot","Bar Graph","Histogram"])
    if graph=="Scatter Plot":
        fig,ax=plt.subplots()
        sns.scatterplot(data=data,x="total_bill",y="tip",hue="sex")
        st.pyplot(fig)
        
    if graph=="Bar Graph":
        fig,ax=plt.subplots()
        sns.barplot(x="tip",y=data.sex.index,data=data)
        st.pyplot(fig)
    if graph=="Histogram":
        fig,ax=plt.subplots()
        sns.distplot(data.total_bill,kde=True)
        st.pyplot(fig)
    

