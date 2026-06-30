import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# dataset berasal dari Power BI
df = dataset.copy()

# pastikan bertipe datetime
df['Date'] = pd.to_datetime(df['Date'])

# Hitung Revenue
df['Revenue'] = df['Unit_Price'] * df['Units_Sold']

# Agregasi revenue per bulan
monthly = df.groupby(pd.Grouper(key='Date', freq='MS'))['Revenue'].sum().reset_index()

monthly = monthly.set_index('Date')

# Model Holt-Winters
model = ExponentialSmoothing(
    monthly['Revenue'],
    trend='add',
    seasonal='add',
    seasonal_periods=12
)

fit = model.fit()

# Forecast 6 bulan
forecast = fit.forecast(6)

# Plot
plt.figure(figsize=(10,5))

plt.plot(
    monthly.index,
    monthly['Revenue'],
    label='Actual Revenue',
    linewidth=2
)
plt.plot(
    forecast.index,
    forecast,
    label='Forecast',
    linewidth=2,
    linestyle='--'
)
plt.title("Sales Revenue Forecast")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
