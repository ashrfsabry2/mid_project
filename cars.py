import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st
df = pd.read_csv('car_analysis.csv')
df.drop(columns=['Item URL'], inplace=True)
df.drop(columns=['Unnamed: 0'],inplace= True)
df.drop(columns=['Date Displayed'],inplace = True)
df.drop(columns=['day'],inplace = True)
def full(row):
    if row["Automatic Transmission"] == "Yes" and row["Air Conditioner"] == "Yes" and row["Power Steering"] == "Yes" and row["Remote Control"] == "Yes":
        return "Yes"
    else:
        return "No"
df["full_option"] = df.apply(full, axis=1)

pages = st.sidebar.radio("Select Page", ["Learn About data", "EDA"])

if pages == 'Learn About data':
    st.image('https://i.pinimg.com/736x/54/ad/9a/54ad9a34c53c93a999983e99f98b843e.jpg')
    st.write(df[:10])
    st.header('Data row and columns')
    st.write(df.shape)
   
    st.header("Data Columns")
    st.write('''
                Name: The name or title of the car.
                
                Price: The price of the car in Egyptian pounds.
                
                Color: The color of the car.
                
                Mileage: The mileage of the car in kilometers.
                
                Make: The brand or manufacturer of the car.
                
                Model: The model of the car.
                
                City: The city where the car is located.
                
                Automatic Transmission: Indicates whether the car has an automatic transmission (Yes/No).
                
                Air Conditioner: Indicates whether the car has an air conditioner (Yes/No).
                
                Power Steering: Indicates whether the car has power steering (Yes/No).
                
                Remote Control: Indicates whether the car has remote control features (Yes/No).
                
                year: The year of the car.
                
                month: The month of the car listing.
                
                full_option: all option available''')














if pages == "EDA":

    tab1, tab2 = st.tabs(["Statistics For Categorical", "Statistics For Numerical "])
    with tab1:
        st.dataframe(df.describe(include="O"))
        st.header("Value Counts For Each Categorical Column")
        categoricals = df.describe(include="O").columns

        for cat in categoricals:
            st.write(f"Value Counts For {cat} :")
            dff = pd.DataFrame(df[cat].value_counts()[:10])
            dff.reset_index(inplace=True)
            dff.rename(columns={"index":cat,cat:f"count of {cat}"}, inplace=True)
            st.dataframe(dff)
            if cat == 'Name':
                st.title('top  names of cars ')
                name_car = px.bar(df['Name'].value_counts().sort_values(ascending = False)[:10])
                st.plotly_chart(name_car )
            if cat=='Color':
                st.title('what is the top  colors of cars ')
                car_color = px.scatter(df['Color'].value_counts()[:10])
                st.plotly_chart(car_color)
                

            if cat=='Make':
                st.title('top make of cars ')
                top_make= px.bar(df['Make'].value_counts().sort_values(ascending = False)[:10])

                st.plotly_chart(top_make)
            if cat=='Model':
                st.title('top  brand of cars ')
                top_model = px.bar(df['Model'].value_counts().sort_values(ascending = False)[:10])
                st.plotly_chart(top_model)
                
            if cat=='Automatic Transmission':
                st.title(' count of manual and automatic cars')
                car_auto =px.pie(df, names='Automatic Transmission' )

                st.plotly_chart(car_auto)
            if cat=='Air Conditioner':
                st.title('Top cars has Air Conditioner or no ')
                car_air = px.pie(df, names='Air Conditioner' )
                st.plotly_chart(car_air)

            if cat=='Power Steering':
                st.title('Top cars has power steering or no ')
                car_power= px.pie(df, names='Power Steering' )
                st.plotly_chart(car_power)




            if cat=='Remote Control':
                st.title('Top cars has remote control or no ')
                car_remote= px.pie(df, names='Remote Control' )
                st.plotly_chart(car_remote)
            if cat == 'City':
                st.title('Top cities in used markets ')
                top10_city = px.line(df['City'].value_counts().sort_values(ascending = False)[:10])
                st.plotly_chart(top10_city)
            
            if cat =='full_option':
                st.header('is most cars have full option') 
                full_car = px.bar(df,x='full_option')
                st.plotly_chart(full_car)
    with tab2:
        st.dataframe(df.describe())
        st.header("Value Counts For Each Numerical Column")
        numericals = df.describe().columns
        for num in numericals:
            dff = pd.DataFrame(df[num].value_counts())
            dff.reset_index(inplace=True)
            dff.rename(columns={"index":num,num:f"count of {num}"}, inplace=True)
            st.dataframe(dff)

            if num == 'month':
                st.header('The most month of publication')
                month_car = px.pie(df , names = 'month')
                st.plotly_chart(month_car)
            if num=='Price':
                
                st.header('what is range price')
                st.title('the mean price')
                st.write(df['Price'].mean())
                st.title('The most expensive cars')
                max_with_price = px.scatter(df.nlargest(15,'Price'),x = 'Name',y='Price')
                st.plotly_chart(max_with_price)
                st.title('price cars')
                min_with_price = px.histogram(df, x = 'Price',nbins= 100)
                st.plotly_chart(min_with_price)

            if num =='Mileage':
                st.header('what is the range of mileage')
                st.title('the mean mileage')
                st.write(df['Mileage'].mean())
                st.title('is there a relation between price and mileage')
                mileage_price = px.scatter(df,x='Price',y = 'Mileage')
                st.plotly_chart(mileage_price)
                
