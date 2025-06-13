select month, sum(sales) as total_sale
from public.sales_data
group by month
order by total_sale desc