import pandas as pd
import matplotlib.pyplot as plt



# # read in weather CSVs
# weather_2016 = pd.read_csv('6-1. weatherevents_2016.csv')
# weather_2017 = pd.read_csv('6-2. weatherevents_2017.csv')
# weather_2018 = pd.read_csv('6-3. weatherevents_2018.csv')
# weather_2019 = pd.read_csv('6-4. weatherevents_2019.csv')
# weather_2020 = pd.read_csv('6-5. weatherevents_2020.csv')
# weather_2021 = pd.read_csv('6-6. weatherevents_2021.csv')

# for df in [weather_2016, weather_2017, weather_2018, weather_2019, weather_2020, weather_2021]:
#     # delete columns Unnamed: 0, EventId, StartTime(UTC), EndTime(UTC)
#     df.drop(columns=['Unnamed: 0', 'EventId', 'StartTime(UTC)'], inplace=True)
#     # delete rows with NaN values
#     df.dropna(inplace=True)
#     df['ZipCode'] = df['ZipCode'].astype(int)
    
# #combine all weather dataframes into one
# weather_all = pd.concat([weather_2016, weather_2017, weather_2018, weather_2019, weather_2020, weather_2021], ignore_index=True)
# weather_all.to_csv('weather_all.csv')


weather_all = pd.read_csv('weather_all.csv')
print(weather_all.head())

# pivot table to get total precipitation for each state
precipitation_by_state = weather_all.pivot_table(index='State', values='Precipitation(in)', aggfunc='sum')
print(precipitation_by_state.head())

# save as csv
precipitation_by_state.to_csv('precipitation_by_state.csv')

# get number of weather events for each state that are 'Severe' severity
# filter the data frame to only include rows where 'severity' is 'severe'
severe_precipitation = weather_all[weather_all['Severity'] == 'Severe']

# group the data by 'state' column and get the count of events for each state
severe_precipitation_by_state = severe_precipitation.groupby('State').size().reset_index(name='count')
print(severe_precipitation_by_state.head())

# save as csv
severe_precipitation_by_state.to_csv('severe_precipitation_by_state.csv')