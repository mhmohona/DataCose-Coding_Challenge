import requests
import json
import re
from datetime import datetime

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
base_url = os.getenv("BASE_URL")
people_endpoint = os.getenv("PEOPLE_ENDPOINT")
contacts_endpoint = os.getenv("CONTACTS_ENDPOINT")
bearer_token = os.getenv("BEARER_TOKEN")
auth = (os.getenv("AUTH_USERNAME"), os.getenv("AUTH_PASSWORD"))

def test_create_contacts():
    # Get People objects
    headers = {
    'Authorization': 'Bearer ' + bearer_token
    }
    people_response = requests.get(base_url + people_endpoint, headers=headers)
    people = people_response.json()

    if people_response.status_code == 200:
        people = people_response.json()
        for person in people:
            # Create a "Contact" object with the cleaned and transformed data
            contact = {
                "first_name": re.sub(r'^\s+|\s+$', '', person['fields']['firstName']),
                "last_name": re.sub(r'^\s+|\s+$', '', person['fields']['lastName']),
                "birthdate": datetime.strptime(person['fields']['dateOfBirth'], '%d-%m-%Y').strftime('%Y-%m-%d'),
                "email": person['fields']['email'],
                "custom_properties": {
                    "airtable_id": person['id'],
                    "lifetime_value": float(person['fields'].get('lifetimeValue', '$0.00')[1:])
                }
            }

            # POST the "Contact" object to the API
            contacts_response = requests.post(base_url + contacts_endpoint, auth=auth, json=contact)

            assert contacts_response.status_code == 200
    else:
        assert False, f"Failed to get a list of people with status code {people_response.status_code}"
