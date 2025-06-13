import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
data = pd.read_csv(r"c:\Users\Hp\Desktop\my_first_project\mydata project\clean_sales_data.csv")
print(data)

cities_sale = data.groupby('City')['Sales'].sum().sort_values(ascending= False)

# plot
cities_sale.plot(kind= 'bar', figsize = (10, 6), color = 'skyblue')
plt.xlabel('city')
plt.ylabel('total_revenue')
plt.title('total revenue per city')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
