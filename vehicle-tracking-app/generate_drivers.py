import json
import requests
from faker import Faker


fake = Faker()

# Specify the number of records to generate
num_drivers = 1000

# API endpoint
api_url = "http://127.0.0.1:8000/api/v1/drivers/add"

# Generate driver data and send to the API
for _ in range(num_drivers):
    # Generate a single driver record
    driver = {
        "name": fake.name(),
        "license_number": fake.unique.random_number(digits=15),
        "contact_number": fake.unique.random_number(digits=10)
    }

    # Send POST request
    response = requests.post(api_url, json=driver)

    # Print response for debugging
    if response.status_code == 201:  # Assuming 201 is for successful creation
        print(f"Successfully added: {driver}")
    else:
        print(f"Failed to add: {driver}. Status Code: {response.status_code}, Response: {response.text}")
