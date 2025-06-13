select city, sum(sales) as total_sale
from sales_data
group by city
order by total_sale desc