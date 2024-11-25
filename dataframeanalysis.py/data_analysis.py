import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

try:
    # Fetching data from the API for drivers
    driver_api = requests.get("http://127.0.0.1:8000/api/v1/drivers")
    driver_api.raise_for_status() 
    driver_api_data = driver_api.json() 
    
    # Fetching data from the API for schedules
    schedule_api = requests.get("http://127.0.0.1:8000/api/v1/schedules")
    schedule_api.raise_for_status()  
    schedule_api_data = schedule_api.json() 
    
    # Convert the data to DataFrames
    driver_df = pd.DataFrame(driver_api_data)
    schedule_df = pd.DataFrame(schedule_api_data)
    
   
    
    # pd.DataFrame(driver_api_data['id'])
    # pd.DataFrame(schedule_api_data['id'])
    
    
    # Combine the driver and schedule dataframes
    combined_df = pd.merge(driver_df, schedule_df, on='id', how='inner')
    
    print(combined_df.shape)
    
    print(combined_df.isnull().sum())
    
    print(combined_df.dtypes)
    
    combined_df['departure_time'] =pd.to_datetime(combined_df['departure_time']) 
    
    combined_df.ffill(inplace= True)
    print(combined_df)
    
    #feature  engineering 

    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
