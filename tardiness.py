import pandas as pd


# read in flight traffic data
flight_traffic = pd.read_csv('7. flight_traffic_2017.csv')

flight_traffic.dropna()
flight_traffic = flight_traffic[flight_traffic['airline_id'].isin(['AA', 'AS', 'B6', 'DL', 'F9', 'G4', 'HA', 'NK', 'UA', 'WN'])]

flight_traffic['tardiness'] = flight_traffic['actual_arrival'] - flight_traffic['scheduled_arrival']
flight_traffic['late_takeoff'] = flight_traffic['actual_departure'] - flight_traffic['scheduled_departure']
flight_traffic.drop(['day', 'airline_delay', 'weather_delay', 'air_system_delay', 'security_delay', 'aircraft_delay', 'scheduled_departure', 'actual_departure', 'taxi_out', 'taxi_in', 'wheels_off', 'wheels_on', 'scheduled_arrival', 'actual_arrival', 'cancelled', 'actual_elapsed', 'scheduled_elapsed'], axis=1, inplace=True)

print(flight_traffic.head(20))

# get the flight data for carrier B6
flight_traffic_jb = flight_traffic[flight_traffic['airline_id'] == 'B6']

flight_traffic_jb.drop(['airline_id'], axis=1, inplace=True)
flight_traffic.drop(['airline_id'], axis=1, inplace=True)

flight_traffic_jb.to_csv('jb_flight_traffic_sans_id.csv', index=False)
flight_traffic.to_csv('all_flight_traffic_sans_id.csv', index=False)