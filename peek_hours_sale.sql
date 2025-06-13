select hour, sum(sales) as total_sale
from public.sales_data
group by hour
order by total_sale desc