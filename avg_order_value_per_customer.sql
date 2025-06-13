WITH cart_total AS (SELECT order_id, city, SUM(sales) AS total_order
FROM public.sales_data
GROUP BY order_id, city)
SELECT city, ROUND(AVG(total_order)::numeric, 2) AS average_cart_size
FROM cart_total
GROUP BY city
ORDER BY average_cart_size DESC;