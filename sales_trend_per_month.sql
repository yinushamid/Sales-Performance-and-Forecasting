select product, sum(sales), month
from public.sales_data
group by product, month