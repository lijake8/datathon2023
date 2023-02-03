import pandas as pd
import matplotlib.pyplot as plt


# read in flight_delay csv file and store in pandas dataframe
all_flight_delay = pd.read_csv('4. flight_delay_2016_2021.csv')
print(all_flight_delay.head())


# compare average flight delay for each airline ##########################################

# all_flight_delay_pcts = all_flight_delay
# # convert arr_del15, carrier_ct, weather_ct, nas_ct, security_ct, late_aircraft_ct, arr_diverted, arr_cancelled to percentages of the value in arr_flights
# all_flight_delay_pcts['arr_del15'] = all_flight_delay['arr_del15'] / all_flight_delay['arr_flights']
# all_flight_delay_pcts['carrier_ct'] = all_flight_delay['carrier_ct'] / all_flight_delay['arr_flights']
# all_flight_delay_pcts['weather_ct'] = all_flight_delay['weather_ct'] / all_flight_delay['arr_flights']
# all_flight_delay_pcts['nas_ct'] = all_flight_delay['nas_ct'] / all_flight_delay['arr_flights']
# all_flight_delay_pcts['security_ct'] = all_flight_delay['security_ct'] / all_flight_delay['arr_flights']
# all_flight_delay_pcts['late_aircraft_ct'] = all_flight_delay['late_aircraft_ct'] / all_flight_delay['arr_flights']
# all_flight_delay_pcts['arr_diverted'] = all_flight_delay['arr_diverted'] / all_flight_delay['arr_flights']
# all_flight_delay_pcts['arr_cancelled'] = all_flight_delay['arr_cancelled'] / all_flight_delay['arr_flights']
# all_flight_delay_pcts.drop(columns=['year', 'month', 'airport_name', 'arr_delay', 'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'], inplace=True)
# print(all_flight_delay_pcts.head())

# carriers = pd.DataFrame()

# # base delay: what percentage of flights are late on average, per carrier
# # pivot table to get average arr_del15 for each carrier
# carriers['pct_delayed_total'] = all_flight_delay_pcts.pivot_table(index='carrier', values='arr_del15', aggfunc='mean')

# # system and congestion delay: what percentage of flights are late due to airport
# # pivot table to get average nas_ct for each carrier
# carriers['pct_delayed_cuz_airport'] = all_flight_delay_pcts.pivot_table(index='carrier', values='nas_ct', aggfunc='mean')

# # weather delay: what percentage of flights are late due to weather
# # pivot table to get average weather_ct for each carrier
# carriers['pct_delayed_cuz_weather'] = all_flight_delay_pcts.pivot_table(index='carrier', values='weather_ct', aggfunc='mean')

# # crew delay: what percentage of flights are late due to crew
# # pivot table to get average carrier_ct for each carrier
# carriers['pct_delayed_cuz_crew'] = all_flight_delay_pcts.pivot_table(index='carrier', values='carrier_ct', aggfunc='mean')

# # airline compounding delay: what percentage of flights are late due to previous flight
# # pivot table to get average late_aircraft_ct for each carrier
# carriers['pct_delayed_cuz_previous'] = all_flight_delay_pcts.pivot_table(index='carrier', values='late_aircraft_ct', aggfunc='mean')

# # cancellations: what percentage of flights are cancelled
# # pivot table to get average arr_cancelled for each carrier
# carriers['pct_cancelled'] = all_flight_delay_pcts.pivot_table(index='carrier', values='arr_cancelled', aggfunc='mean')

# # remove all rows where carrier is not one of the major airlines: ['AA', 'AS', 'B6', 'DL', 'F9', 'G4', 'HA', 'NK', 'UA', 'WN']
# carriers = carriers[carriers.index.isin(['AA', 'AS', 'B6', 'DL', 'F9', 'G4', 'HA', 'NK', 'UA', 'WN'])]

# print(carriers.head(20))

# # export to csv
# carriers.to_csv('carriers_pcts_delays.csv')

##################################################################################################################




# # filter only carrier 'B6' for jetblue
# flight_delay = all_flight_delay[all_flight_delay['carrier'] == 'B6']
# print(flight_delay.head())

# # pivot table to get average carrier_delay for each year
# carrier_delay = flight_delay.pivot_table(index='year', values='carrier_delay', aggfunc='mean')

# print(carrier_delay.head(20))



# get the average nas_delay and arr_delay for each airport (shows congestion at each airport)
airport_delays = all_flight_delay.pivot_table(index='airport', values=['nas_delay', 'arr_delay'], aggfunc='mean')

# airport_codes = pd.read_csv('1a. Airports.csv')
# airport_codes.rename(columns={'Code': 'airport'}, inplace=True)
# # for the description column, remove the airport name and keep only the city and state
# airport_codes['Location'] = airport_codes['Description'].str.split(':').str[0]
# airport_codes.drop(columns=['Description'], inplace=True)

# # merge airport_codes and airport_congestion_delays
# airport_congestion_delays = pd.merge(airport_codes, airport_congestion_delays, on='airport')
print(airport_delays.head(20))

# save airport_congestion_delays to csv
airport_delays.to_csv('airport_delays.csv')










# EXAMINE CHANGES IN CONGESTION YEAR OVER YEAR #####################################
# get the flight data for 2016
flights_by_airport_2016 = all_flight_delay[all_flight_delay['year'] == 2016]
#get the total number of arriving flights for each airport
flights_by_airport_2016 = flights_by_airport_2016.pivot_table(index='airport', values='arr_flights', aggfunc='sum')
flights_by_airport_2016.rename(columns={'arr_flights': 'arr_flights_2016'}, inplace=True)
print(flights_by_airport_2016.head(10))

# get the flight data for 2021
flights_by_airport_2021 = all_flight_delay[all_flight_delay['year'] == 2019]
#get the total number of arriving flights for each airport
flights_by_airport_2021 = flights_by_airport_2021.pivot_table(index='airport', values='arr_flights', aggfunc='sum')
flights_by_airport_2021.rename(columns={'arr_flights': 'arr_flights_2021'}, inplace=True)
print(flights_by_airport_2021.head(10))

#merge the two dataframes
airport_flights_2016_2021 = pd.merge(flights_by_airport_2016, flights_by_airport_2021, on='airport')
airport_flights_2016_2021['no_flights_change'] = airport_flights_2016_2021['arr_flights_2021'] - airport_flights_2016_2021['arr_flights_2016']
print(airport_flights_2016_2021.head(50))

# save airport_congestion_delays to csv
airport_flights_2016_2021.to_csv('airport_numflights_change_2016_to_2021.csv')