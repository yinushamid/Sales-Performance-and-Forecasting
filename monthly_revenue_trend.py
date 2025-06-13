import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
data = pd.read_csv(r"c:\Users\Hp\Desktop\my_first_project\mydata project\clean_data.csv")
print(data)

revenue_per_month  = data.groupby('Month')['Sales'].sum().sort_values(ascending= False)

# plot
revenue_per_month.plot(kind= 'bar', figsize = (10, 6), color = 'skyblue')
plt.xlabel('months')
plt.ylabel('total_sales')
plt.title('total sold per month')
plt.show()