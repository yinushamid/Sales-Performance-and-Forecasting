import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
data = pd.read_csv(r"c:\Users\Hp\Desktop\my_first_project\mydata project\clean_data.csv")
print(data)

products_sale = data.groupby('Product')['Sales'].sum().sort_values(ascending= False)

# plot
products_sale.plot(kind= 'bar', figsize = (10, 6), color = 'skyblue')
plt.xlabel('product')
plt.ylabel('total_sales')
plt.title('total sales per product')
plt.show()