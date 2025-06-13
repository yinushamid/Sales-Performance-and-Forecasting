import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
sales_data = pd.read_excel(r'c:\Users\Hp\Desktop\my_first_project\mydata project\raw_sales_data.xlsx')
# copy the data for exploration
raw_sales_data  = sales_data.copy()


# clean the sales data 
raw_sales_data = raw_sales_data.drop_duplicates()

raw_sales_data = raw_sales_data.drop('Unnamed: 0', axis = 1)
clean_data = raw_sales_data.dropna()


# save the raw data
clean_data.to_csv(r'c:\Users\Hp\Desktop\my_first_project\mydata project\clean_data.csv', index= False)


