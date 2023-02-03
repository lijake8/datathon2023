import pandas as pd
import matplotlib.pyplot as plt



# read in flight traffic data
all_flight_traffic = pd.read_csv('7. flight_traffic_2017.csv')

# filter only carrier 'nk' for spirit
flight_traffic = all_flight_traffic[all_flight_traffic['airline_id'] == 'NK']

# GET MOST-SERVICED AIRPORTS BY spirit ######################################
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

# save to csv
airport_counts.to_csv('spirit_airport_counts.csv', index=False)

