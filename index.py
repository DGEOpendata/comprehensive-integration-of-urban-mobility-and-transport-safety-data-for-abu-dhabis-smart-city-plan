python
import pandas as pd

# Load datasets
transport_data = pd.read_csv('Public_Transportation_Usage_Abu_Dhabi_2025.csv')
traffic_data = pd.read_excel('Traffic_Accident-v3.0_Abu_Dhabi_2025.xlsx')

# Merge datasets on common columns such as date and location
merged_data = pd.merge(transport_data, traffic_data, left_on=['date', 'location'], right_on=['report_date', 'city'])

# Analyze combined data to find high-risk areas
high_risk_areas = merged_data.groupby(['location']).agg({'number_of_accidents': 'sum', 'number_of_users': 'sum'}).reset_index()

# Identify peak times for traffic accidents
peak_times = traffic_data.groupby('time').agg({'number_of_accidents': 'sum'}).sort_values('number_of_accidents', ascending=False)

# Output results
print('High Risk Areas:')
print(high_risk_areas)
print('\nPeak Times for Traffic Accidents:')
print(peak_times.head())

