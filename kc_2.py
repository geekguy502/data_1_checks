import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt

arrivals = pd.read_csv('assets/arrivals.csv')
print(arrivals.head())

arrivals_tmp = arrivals.drop_duplicates()

"""

    id 
    carrier_code 
    flight_date 
    flight_number 
    tail_number
    origin
    sched_arr_time 
    act_arr_time 
    sch_elapsed
    act_elapsed
    arr_delay 
    wheels_on 
    taxi_in 
    delay_carrier
    delay_weather 
    delay_natavsys 
    delay_security
    delay_late_arrival

"""

arrivals_tmp.rename(columns={
    'ID' : 'id', 
    'Carrier Code' : 'carrier_code',
    'Date (MM/DD/YYYY)' : 'flight_date', 
    'Flight Number' : 'flight_number', 
    'Tail Number' : 'tail_number',
    'Origin Airport' : 'origin', 
    'Scheduled Arrival Time' : 'sched_arr_time', 
    'Actual Arrival Time' : 'act_arr_time',     
    'Scheduled Elapsed Time (Minutes)' : 'sch_elapsed', 
    'Actual Elapsed Time (Minutes)' : 'act_elapsed',   
    'Arrival Delay (Minutes)' : 'arr_delay', 
    'Wheels-on Time' : 'wheels_on', 
    'Taxi-In time (Minutes)' : 'taxi_in', 
    'Delay Carrier (Minutes)' : 'delay_carrier', 
    'Delay Weather (Minutes)' : 'delay_weather',
    'Delay National Aviation System (Minutes)'  : 'delay_natavsys',
    'Delay Security (Minutes)' : 'delay_security',
    'Delay Late Aircraft Arrival (Minutes)' : 'delay_late_arrival'
   
},inplace=True)