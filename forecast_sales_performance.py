import pandas as pd
from prophet import Prophet

# Load your dataset
df = pd.read_csv(r'c:\Users\Hp\Desktop\my_first_project\mydata project\clean_data.csv')

# Convert to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Aggregate revenue by month
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].dt.to_timestamp()

# Prophet expects columns 'ds' and 'y'
df_prophet = monthly_sales.rename(columns={'Month': 'ds', 'Sales': 'y'})

# Initialize and fit the model
model = Prophet()
model.add_seasonality(name='monthly', period=12, fourier_order=5)
model.fit(df_prophet)

# Make future predictions
future = model.make_future_dataframe(periods=12)  # Forecasting for the next 12 months

# Generate forecast
forecast = model.predict(future)

# Plot the forecast
model.plot(forecast)

# Forecast the next 6 months
future = model.make_future_dataframe(periods=6, freq='M')
forecast = model.predict(future)

# Keep only relevant columns
forecast_result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

forecast_result.to_csv(r'c:\Users\Hp\Desktop\my_first_project\python codes\revenue_forecast.csv', index=False)

