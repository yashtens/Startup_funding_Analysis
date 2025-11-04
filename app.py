import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
startup=pd.read_csv('startup.csv')
startup['date']=pd.to_datetime(startup['date'],errors='coerce')
startup['month']=startup['date'].dt.month
startup['year']=startup['date'].dt.year
def overall_analysis():
    st.title('Overall Analysis')
    col1, col2,col3,col4 = st.columns(4)
    with col1:
        total = round(startup['amount'].sum())
        st.metric('Overall Amount', total)
    with col2:
        max_funding=startup.groupby('name')['amount'].max().sort_values(ascending=False).head(1).values[0]
        st.metric('Maximun Amount',max_funding)
    with col3:
        avg_funding = startup.groupby('name')['amount'].sum().mean()
        st.metric('Average Amount', avg_funding)
    with col4:
        data=startup['name'].nunique()
        st.metric('Number of Unique Values',data)

    st.header('Month on Month Graph')
    temp_df=startup.groupby(['year','month'])['amount'].sum().reset_index()
    temp_df['x_axis']=temp_df['month'].astype('str')+'-'+temp_df['year'].astype('str')
    temp_df[['amount','x_axis']]
    fig3, ax3  = plt.subplots()
    ax3.plot(temp_df['x_axis'],temp_df['amount'])
    ax3 .set_title('Overall investment of the month and the Year')
    ax3.set_xlabel('biggest investor')
    ax3.set_ylabel('Amount')
    ax3.legend()
    st.pyplot(fig3)
def investor_details(investors):
    st.title(investors)
    last_5_df=startup[startup['investor'].str.contains('investors')].head()[['date','name','vertical','City  Location','type','amount']]
    st.subheader('Most recent investor')
    st.dataframe(last_5_df)

    col1, col2 = st.columns(2)
    with col1:
        bigg = startup[startup['investor'].str.contains('investors')].groupby('name')['amount'].sum().sort_values(
            ascending=False).head(5)
        st.subheader('biggest investment')
        fig , ax=plt.subplots()
        ax.bar(bigg.index,bigg.values)
        ax.set_title('BIGGEST INVESTMENTS')
        ax.set_xlabel('biggest investor')
        ax.set_ylabel('Amount')
        ax.legend()
        st.pyplot(fig)
    with col2:
        stage=startup[startup['investor'].str.contains('investors')].groupby('vertical')['amount'].sum().sort_values(ascending=False)
        st.subheader('sector_investment')
        fig1, ax = plt.subplots()
        ax.pie(stage,labels=(stage.index),autopct='%0.1f%%')
        ax.set_title('Sector Investment')
        ax.set_xlabel('biggest investor')
        ax.set_ylabel('Amount')
        st.pyplot(fig1)
    startup['year']=startup['date'].dt.year
    year_series=startup[startup['investor'].str.contains('investors')].groupby('year')['amount'].sum().sort_values(ascending=False)
    st.subheader('yearly investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)
    st.pyplot(fig2)

st.sidebar.title("Startup Funding Analysis:")
option=st.sidebar.selectbox('select the option:',['Overall Analysis','Startup','Investor'])
if option=='Overall Analysis':
     btn3=st.sidebar.button('Overall Analysis')
     if btn3:
         overall_analysis()
elif option=='Startup':
     st.sidebar.selectbox('Select the Startup :',sorted(startup['name'].unique().tolist()))
     st.sidebar.  button("startup details")
elif option=='Investor':
     select_investor=st.sidebar.selectbox('select the Investor:',set(sorted(startup['investor'].str.split(',').sum())))
     btn2=st.sidebar.button("Investor details")
     if btn2:
         investor_details(select_investor)
     st.title("Investor details")

