import pandas as pd
import matplotlib.pyplot as plt


# read in flight_delay 
all_flight_delay = pd.read_csv('4. flight_delay_2016_2021.csv')
# read in flight traffic data
all_flight_traffic = pd.read_csv('7. flight_traffic_2017.csv')

# filter only carrier 'B6' for jetblue
flight_delay = all_flight_delay[all_flight_delay['carrier'] == 'B6']
flight_traffic = all_flight_traffic[all_flight_traffic['airline_id'] == 'B6']

# GET MOST-SERVICED AIRPORTS BY JETBLUE ######################################
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
airport_counts.to_csv('jb_airport_counts.csv', index=False)






# pivot table to get average delay for each year
carrier_delay = flight_delay.pivot_table(index='year', values='carrier_delay', aggfunc='mean')
carrier_delay.rename(columns={'carrier_delay': 'mins delayed'}, inplace=True)

#pivot table to get average carrier_ct for each year
carrier_ct = flight_delay.pivot_table(index='year', values='carrier_ct', aggfunc='mean')
carrier_ct.rename(columns={'carrier_ct': '# flights delayed on avg day'}, inplace=True)

#merge the two dataframes
carrier_delay_ct = pd.merge(carrier_delay, carrier_ct, how='outer', left_on='year', right_on='year')
# add year column
carrier_delay_ct['year'] = carrier_delay_ct.index
print(carrier_delay_ct.head(20))

# save to csv
carrier_delay_ct.to_csv('jb_delay_info.csv', index=False)






# pivot table to get the number of flights for each year, jb only
flight_traffic_year_jb = flight_delay.pivot_table(index='year', values='carrier_delay', aggfunc='count')
flight_traffic_year_jb.rename(columns={'carrier_delay': 'number of jb flights'}, inplace=True)

# pivot table to get the number of flights for each year, all
major_carriers_traffic = all_flight_delay[all_flight_delay['carrier'].isin(['AA', 'AS', 'B6', 'DL', 'F9', 'G4', 'HA', 'NK', 'UA', 'WN'])]
flight_traffic_year = major_carriers_traffic.pivot_table(index='year', values='carrier_delay', aggfunc='count')
flight_traffic_year.rename(columns={'carrier_delay': 'number of all airlines flights'}, inplace=True)

#merge the two dataframes
flight_traffic_year = pd.merge(flight_traffic_year_jb, flight_traffic_year, how='outer', left_on='year', right_on='year')
# add year column
flight_traffic_year['year'] = flight_traffic_year.index
print(flight_traffic_year.head(20))
# save to csv
flight_traffic_year.to_csv('all_flight_traffic.csv', index=False)
