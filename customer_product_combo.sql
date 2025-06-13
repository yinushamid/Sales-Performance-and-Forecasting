WITH orders_with_multiple_products AS 
(SELECT order_id, STRING_AGG(Product, ', ' ORDER BY Product) AS Product_Combo
FROM public.sales_data
GROUP BY order_id
HAVING COUNT(DISTINCT Product) > 1),
product_combos AS 

(SELECT Product_Combo, COUNT(*) AS Frequency
FROM orders_with_multiple_products
GROUP BY Product_Combo)

SELECT Product_Combo, Frequency
FROM product_combos
WHERE Frequency > 1
ORDER BY Frequency DESC