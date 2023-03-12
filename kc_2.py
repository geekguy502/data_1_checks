import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt

data = pd.read_csv('assets/SouthwestArrivals.csv')

data['date'] = pd.to_datetime(data[['year', 'month']].assign(day=1))
data = data.groupby(['date'])['total'].sum().reset_index()
data.plot(x='date', y='total', kind='line')
plt.xlabel('Year-Month')
plt.ylabel('Total')
plt.title('Southwest Total SDF arrivals by Year-Month')
plt.show()