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
headers = {
'Authorization': 'Bearer ' + bearer_token
}

def get_people():
    people_response = requests.get(base_url + people_endpoint, headers=headers)
    if people_response.status_code == 200:
        people = people_response.json()
        return people
    else:
        raise Exception(f"Failed to get people data. Response code: {people_response.status_code}")

def test_people_endpoint_success():
    people = get_people()
    for person in people:
        fields = person["fields"]

        first_name = fields.get("firstName", "")
        last_name = fields.get("lastName", "")
        birthdate = fields.get("dateOfBirth", "")
        email = fields.get("email", "")

        assert first_name, "firstName field is empty"
        assert last_name, "lastName field is empty"
        assert birthdate, "dateOfBirth field is empty"
        assert email, "email field is empty"
def test_create_contacts():
    # Get People objects
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

def test_failed_authentication():
    # Test authentication failure by passing in incorrect auth credentials
    incorrect_auth = ("incorrect", "credentials")
    contacts_response = requests.post(base_url + contacts_endpoint, auth=incorrect_auth, json={})

    assert contacts_response.status_code == 401

def test_missing_required_field():
    # Test with a Contact object missing a required field
    contact = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "custom_properties": {
            "airtable_id": "abc123"
        }
    }

    contacts_response = requests.post(base_url + contacts_endpoint, auth=auth, json=contact)

    assert contacts_response.status_code == 400

def test_invalid_email_address():
    # Test with an invalid email address
    contact = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "notanemailaddress",
        "birthdate": "2000-01-01",
        "custom_properties": {
            "airtable_id": "abc123"
        }
    }

    contacts_response = requests.post(base_url + contacts_endpoint, auth=auth, json=contact)

    assert contacts_response.status_code == 400

def test_non_numeric_lifetime_value():
    # Test with a non-numeric value for the lifetime_value property
    contact = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "birthdate": "2000-01-01",
        "custom_properties": {
            "airtable_id": "abc123",
            "lifetime_value": "not a number"
        }
    }

    contacts_response = requests.post(base_url + contacts_endpoint, auth=auth, json=contact)

    assert contacts_response.status_code == 400
