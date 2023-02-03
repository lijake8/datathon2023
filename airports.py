import pandas as pd
import matplotlib.pyplot as plt


# get most-visited airports by all airlines ##############################################################

# read in flight traffic data
flight_traffic = pd.read_csv('7. flight_traffic_2017.csv')

# from flight_traffic, get the number of flights for each origin_airport
flight_traffic_origin = flight_traffic.groupby(['origin_airport']).size().reset_index(name='flight_count')
# same thing with destination_airport
flight_traffic_dest = flight_traffic.groupby(['destination_airport']).size().reset_index(name='flight_count')

# merge the two dataframes to get total flights touching each airport
airport_counts = pd.merge(flight_traffic_origin, flight_traffic_dest, how='outer', left_on='origin_airport', right_on='destination_airport')
airport_counts['total_flights'] = airport_counts['flight_count_x'] + airport_counts['flight_count_y']
airport_counts.drop(['flight_count_x', 'flight_count_y', 'destination_airport'], axis=1, inplace=True)
airport_counts.dropna()
airport_counts.rename(columns={'origin_airport': 'airport'}, inplace=True)

print(airport_counts.head())

#save to csv
airport_counts.to_csv('busiest_airports.csv', index=False)




# # EXAMINE CHANGES YEAR OVER YEAR #####################################
print('blah---------------------------')
# get the flight data for 2016
flight_traffic_2016 = flight_traffic[flight_traffic['year'] == 2016]
print(flight_traffic_2016.head())
# from flight_traffic, get the number of flights for each origin_airport
flight_traffic_2016_origin = flight_traffic_2016.groupby(['origin_airport']).size().reset_index(name='flight_count')
# same thing with destination_airport
flight_traffic_2016_dest = flight_traffic_2016.groupby(['destination_airport']).size().reset_index(name='flight_count')
# merge the two dataframes to get total flights touching each airport
airport_counts_2016 = pd.merge(flight_traffic_2016_origin, flight_traffic_2016_dest, how='outer', left_on='origin_airport', right_on='destination_airport')

print(airport_counts_2016.head())
airport_counts_2016['total_flights_2016'] = airport_counts_2016['flight_count_x'] + airport_counts_2016['flight_count_y']
airport_counts_2016.drop(['flight_count_x', 'flight_count_y', 'destination_airport'], axis=1, inplace=True)
airport_counts_2016.dropna()
airport_counts_2016.rename(columns={'origin_airport': 'airport'}, inplace=True)
print(airport_counts_2016.head())

# get the flight data for 2021
flight_traffic_2021 = flight_traffic[flight_traffic['year'] == 2021]
# from flight_traffic, get the number of flights for each origin_airport
flight_traffic_2021_origin = flight_traffic_2021.groupby(['origin_airport']).size().reset_index(name='flight_count')
# same thing with destination_airport
flight_traffic_2021_dest = flight_traffic_2021.groupby(['destination_airport']).size().reset_index(name='flight_count')
# merge the two dataframes to get total flights touching each airport
airport_counts_2021 = pd.merge(flight_traffic_2021_origin, flight_traffic_2021_dest, how='outer', left_on='origin_airport', right_on='destination_airport')
airport_counts_2021['total_flights_2021'] = airport_counts_2021['flight_count_x'] + airport_counts_2021['flight_count_y']
airport_counts_2021.drop(['flight_count_x', 'flight_count_y', 'destination_airport'], axis=1, inplace=True)
airport_counts_2021.dropna()
airport_counts_2021.rename(columns={'origin_airport': 'airport'}, inplace=True)
print(airport_counts_2021.head())

#merge the two dataframes
airport_counts = pd.merge(airport_counts, airport_counts, how='outer', left_on='airport', right_on='airport')
airport_counts['change'] = airport_counts['total_flights_2021'] - airport_counts['total_flights_2016']
# airport_counts.drop(['total_flights_2016', 'total_flights_2021'], axis=1, inplace=True)
# airport_counts.dropna()
print(airport_counts.head())

