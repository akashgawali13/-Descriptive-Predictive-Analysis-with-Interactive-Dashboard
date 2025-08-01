# -Descriptive-Predictive-Analysis-with-Interactive-Dashboard

This project combines **exploratory data analysis** and **machine learning** into a fully interactive dashboard using **Python**, designed to deliver both **insights and forecasts** from a sales dataset.

# Project Overview

This project showcases both Descriptive and Predictive Analytics using a sales dataset. The application is built with Streamlit and provides an interactive dashboard where users can explore key metrics, filter by region/product, and view future sales predictions using a machine learning model.

# Files

- **Model.py** - ML model training & prediction function  
- **app.py** - Main Streamlit app  
- **sales_data_sample.csv** - Sales dataset  
- **requirements.txt** - Libraries used  

# Features

- Monthly sales trend visualization  
- Country-wise sales distribution  
- Product line-wise total sales  
- Predict future sales using Linear Regression  
- Interactive filtering by Country and Product Line  


# Descriptive Analytics
- Total sales, average price, top categories/products
- Trends by time/category
- Interactive filters using Streamlit

# Predictive Analytics
- Machine Learning model (e.g., Linear Regression)
- Predict `Sales` or `Revenue` from input variables
- Trained model saved and reused for fast prediction

# Issues and Fixes
**Issue**
ORDERDATE not parsed	
**Fix **
Used pd.to_datetime(df["ORDERDATE"])
**Issue**
Future sales gave float output	
**Fix **
Converted predictions to int using .astype(int)
**Issue**
Path issues	
Used relative paths instead of full disk paths

 # Technologies Used

- **Python**
- **Pandas, NumPy, Matplotlib, Seaborn**
- **Scikit-learn** for model building
- **Streamlit** for dashboard UI

# Output
<img width="1919" height="889" alt="{0149FBE7-B231-4E9D-821E-D14D8BD6BEB3}" src="https://github.com/user-attachments/assets/e1237834-98d4-4346-94f7-9ac5f31b8b59" />
<img width="1916" height="1008" alt="{0D0B8C1F-D9D9-4EA8-923F-E10AAF90A5ED}" src="https://github.com/user-attachments/assets/97215792-204b-4588-b1bf-6806d1742b20"/>
<img width="1920" height="926" alt="{B880766B-5F7D-4FA5-8ED8-2EBE24C59965}" src="https://github.com/user-attachments/assets/cd6bbbeb-5317-450b-a046-1da738c6b9b4" />
