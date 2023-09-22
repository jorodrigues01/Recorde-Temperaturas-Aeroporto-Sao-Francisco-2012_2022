import pandas as pd
import dateFunctions

df = pd.read_csv("C:/Users/JR/Downloads/USW00023234.csv", low_memory=False).sort_values('DATE').loc[:, ['DATE', 'TMAX', 'TMIN']]

df = df[(df['DATE'] >= '2012') & (df['DATE'] < '2023')]
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')
df['DAY OF YEAR'] = df['DATE'].apply(lambda date: dateFunctions.to_day_of_year(date))
df = df.drop(index=df[(df['DATE'] == '2012-02-29') |
                      (df['DATE'] == '2016-02-29') |
                      (df['DATE'] == '2020-02-29')].index).reset_index(drop=True)

df['TMAX'] = df['TMAX']/10
df['TMIN'] = df['TMIN']/10

df_MAX = pd.DataFrame(df[['DATE', 'DAY OF YEAR', 'TMAX']])
df_MIN = pd.DataFrame(df[['DATE', 'DAY OF YEAR', 'TMIN']])

df_MAX10y = df_MAX[df_MAX['DATE'] < '2022']
df_MAX10y_byDay = df_MAX10y.groupby(['DAY OF YEAR'], as_index=False)['TMAX'].max()
df_MAX10y_byDay['DATE'] = df_MAX10y_byDay.apply(lambda row: dateFunctions.get_historical_tmax_date(row, df_MAX10y.copy()), axis=1)

df_MIN10y = df_MIN[df_MIN['DATE'] < '2022']
df_MIN10y_byDay = df_MIN10y.groupby(['DAY OF YEAR'], as_index=False)['TMIN'].min()
df_MIN10y_byDay['DATE'] = df_MIN10y_byDay.apply(lambda row: dateFunctions.get_historical_tmin_date(row, df_MIN10y.copy()), axis=1)

df_MAX2022 = df_MAX[df_MAX['DATE'] >= '2022'].reset_index(drop=True)
df_MIN2022 = df_MIN[df_MIN['DATE'] >= '2022'].reset_index(drop=True)
