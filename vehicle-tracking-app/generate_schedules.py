import json
import requests
from faker import Faker
from random import randint
from datetime import datetime, timedelta

# Initialize Faker instance
fake = Faker()

# Specify the number of records to generate
num_schedules = 1000

# API endpoint for adding schedules
api_url = "http://127.0.0.1:8000/api/v1/schedules/add"

# Assuming you already have IDs for vehicles, drivers, and routes
# Replace these with appropriate API calls if dynamic fetching is needed
vehicle_ids = list(range(1, 101))  # Example vehicle IDs (1 to 100)
driver_ids = list(range(1, 201))   # Example driver IDs (1 to 200)
route_ids = list(range(1, 50))     # Example route IDs (1 to 50)

# Generate schedule data and send to the API
for _ in range(num_schedules):
    # Generate a random departure time
    departure_time = fake.date_time_this_month()
    # Generate arrival time, ensuring it's after the departure time
    arrival_time = departure_time + timedelta(hours=randint(1, 5))

    # Generate a single schedule record
    schedule = {
        "vehicle_id": fake.random_element(vehicle_ids),
        "driver_id": fake.random_element(driver_ids),
        "route_id": fake.random_element(route_ids),
        "departure_time": departure_time.isoformat(),  # Format as ISO 8601
        "arrival_time": arrival_time.isoformat()
    }

    # Send POST request
    response = requests.post(api_url, json=schedule)

    # Print response for debugging
    if response.status_code == 201:  # Assuming 201 is for successful creation
        print(f"Successfully added: {schedule}")
    else:
        print(f"Failed to add: {schedule}. Status Code: {response.status_code}, Response: {response.text}")
