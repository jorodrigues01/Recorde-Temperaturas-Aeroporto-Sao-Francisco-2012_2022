import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from dataCleaning import df_MAX10y_byDay, df_MIN10y_byDay, df_MAX2022, df_MIN2022

plt.figure(figsize=(25,10))

observation_dates = pd.date_range('01-01-2023', periods=365, freq='D').to_series().dt.strftime('%d-%m')

plt.plot(observation_dates, df_MAX10y_byDay['TMAX'], '-', color='red', label='Max. daily temperatures 2012-2021')
plt.plot(observation_dates, df_MIN10y_byDay['TMIN'], '-', color='blue', label='Min. daily temperatures 2012-2021')


lower_2022 = list()
higher_2022 = list()

for i in range(0, 365):
    if df_MAX2022['TMAX'].iloc[i] > df_MAX10y_byDay['TMAX'].iloc[i]:
        higher_2022.append(df_MAX2022.iloc[i])
    if df_MIN2022['TMIN'].iloc[i] < df_MIN10y_byDay['TMIN'].iloc[i]:
        lower_2022.append(df_MIN2022.iloc[i])


higher_2015 = pd.DataFrame(higher_2022, index=np.arange(0, len(higher_2022), dtype='int'))
lower_2015 = pd.DataFrame(lower_2022, index=np.arange(0, len(lower_2022), dtype='int'))

plt.scatter(higher_2015['DAY OF YEAR']-1, higher_2015['TMAX'], s=20, color='black', label='Outlier Temperatures from 2022')
plt.scatter(lower_2015['DAY OF YEAR']-1, lower_2015['TMIN'], s=20, color='black')

plt.title('Daily Record Temperatures (2012-2021) in comparison with 2022', fontsize=25, pad=15)
plt.legend(title='Legend', loc=1)

ax = plt.gca()
ax.set_xlim((0, 364))
ax.fill_between(range(0, 365), df_MAX10y_byDay['TMAX'], df_MIN10y_byDay['TMIN'], facecolor='gray', alpha=0.2)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('Months')
ax.set_ylabel('Temperatures (°C)')

plt.show()