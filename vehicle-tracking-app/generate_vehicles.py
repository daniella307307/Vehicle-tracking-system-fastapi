import json
import requests
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Specify the number of records to generate
num_vehicles = 1000

# API endpoint for adding vehicles
api_url = "http://127.0.0.1:8000/api/v1/vehicles/add"

# Generate vehicle data and send to the API
for _ in range(num_vehicles):
    # Generate a single vehicle record
    vehicle = {
        "name": fake.random_element(elements=["Toyota Hiace", "Ford Transit", "Mercedes Sprinter", "Nissan NV200"]),
        "plate_number": fake.unique.license_plate(),
        "capacity": fake.random_int(min=2, max=50)  # Random capacity between 2 and 50 passengers
    }

    # Send POST request
    response = requests.post(api_url, json=vehicle)

    # Print response for debugging
    if response.status_code == 201:  # Assuming 201 is for successful creation
        print(f"Successfully added: {vehicle}")
    else:
        print(f"Failed to add: {vehicle}. Status Code: {response.status_code}, Response: {response.text}")
