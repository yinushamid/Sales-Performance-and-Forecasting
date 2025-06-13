# customer behavior, sales insight and forecasting

## table of content
- [project overview](#project-overview)

### project overview
To help the business understand who our customers are and what they buy, track how well we're selling our products, and predict how much money we'll make in the future, all to make smarter decisions and grow the business

### data source
 sales data: the primary dataset used for this analysis is the "sales_data.csv" file, from kaggle, containing detailed information about each sale made by the company

### tools
- python - data cleaning and prediction 
- postgresql - data analysis
- power Bi - creating reports

### data cleaning and preparation
in the initial data preparation phase we perform the following tasks:
1. data loading and inspection
2. handling missing values
3. data cleaning and formatting

### exploratory data analysis
EDA involved exploring the sales data to answer key questions such as
- what is the overall sales trend?
- which products are top sellers?
- what are the peak sales product?

### results
the analysis results are summarised as follows
## customer behavior
1. Atlanta ($196.13) and New York City ($195.59) have the highest average cart sizes, while Boston ($150) has the lowest.
2. "Vareebadd Phone, Wired Headphones" and "USB-C Charging Cable, Wired Headphones" are the most frequent pairings, suggesting customers often buy accessories with their main devices.
3. There are specific times (e.g., 07 PM, 12 PM) that show higher "Sales" indicating potential peak purchasing windows.

## sale insight
1.  The total sales are 34.49 Million, with 185.9K orders
2.  San Francisco and Los Angeles are significant contributors to overall sales, with Dallas and Chicago also showing strong performance. New York appears lower in comparison.
3.   "20in Monitor" consistently contributes across months, while others might have peak months (e.g., "ThinkPad Laptop" showing strong numbers in April and May).
4.   "MacBook Pro Laptop" and "ThinkPad Laptop" are leading in sum of sales, followed by "20in 4K Gaming Monitor"
5.    sales appear to pick up from March to July, then possibly decline again towards the end of the year

## forecast
1. chart clearly shows past revenue performance, indicating periods of growth and fluctuation (e.g., a dip around early 2019, followed by recovery and growth into 2020).
2. The forecast generally appears to follow the historical trend, suggesting a reasonable projection based on past performance.

### recommendation
base on the analysis we recommend the following action:
##customer behavior
1. Based on popular product combinations create specific product bundles or discount offers to encourage larger purchases.
2.  For cities with lower average cart sizes, considerfree shipping thresholds to encourage customers to add more items to their carts.
3. consider increasing marketing spend or customer service availability during those specific times to maximize conversion

## sales insight
1. Allocate sales and marketing resources strategically based on city performance
2. Given the high value of laptops, train sales teams to cross-sell accessories
3. Analyze monthly sales trends to anticipate peak and trough periods
4. For products with declining or stagnant sales, investigate reasons (e.g., competition, pricing, marketing) and consider strategies such as bundling or discounts

## forecast
1. Regularly compare actual sales revenue against the forecasted figures. Significant deviations (either positive or negative) should trigger further investigation to understand underlying causes and adjust strategies.

### limitations
The dataset primarily contains transactional sales data. It may lack deeper customer demographic information (e.g., age, income, gender) or external factors (e.g., marketing spend, competitor activity, economic indicators) that could provide richer insights or explain sales fluctuations more thoroughly

### references
This project utilized the 'Sales Data' dataset, which was sourced from Kaggle



