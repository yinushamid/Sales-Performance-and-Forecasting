SELECT product, price_each, SUM(quantity_ordered) AS 
unit_sold, sum(sales) as total_sales
FROM sales_data
GROUP BY product, price_each 