import json
import requests
from faker import Faker
from random import uniform

# Initialize Faker instance
fake = Faker()

# Specify the number of records to generate
num_routes = 1000

# API endpoint for adding routes
api_url = "http://127.0.0.1:8000/api/v1/routes/add"

# Generate route data and send to the API
for _ in range(num_routes):
    # Generate a random start and end location
    start_location = fake.city()
    end_location = fake.city()
    while start_location == end_location:  # Ensure start and end locations are different
        end_location = fake.city()

    # Generate random distance (in kilometers) and duration (in hours)
    distance = round(uniform(5.0, 1000.0), 2)  # Distance between 5km and 1000km
    duration = round(distance / uniform(40.0, 120.0), 2)  # Duration assuming speed between 40-120 km/h

    # Generate a single route record
    route = {
        "start_location": start_location,
        "end_location": end_location,
        "distance": distance,
        "duration": duration
    }

    # Send POST request
    response = requests.post(api_url, json=route)

    # Print response for debugging
    if response.status_code == 201:  # Assuming 201 is for successful creation
        print(f"Successfully added: {route}")
    else:
        print(f"Failed to add: {route}. Status Code: {response.status_code}, Response: {response.text}")
