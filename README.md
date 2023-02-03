# Automation-Engineer-Candidate-Challenge

## Arther
[Mahfuza Humayra Mohona](https://www.linkedin.com/in/mhmohona/)\
email - mhmohona@gmail.com

## Introduction
This project is an automation tool that fetches the data from the API endpoint /people/, cleans and transforms the data to match the "Contact" object schema, and then posts each "Contact" object to the API endpoint /contacts/. The project includes the following components:

* .env file containing environment variables
* setup.py file for project dependencies
* requirements.txt file for project dependencies
* code for fetching, cleaning and posting data to the API
* code for testing the project functionality

## Usage
Run the automation tool
`python main.py`


## Data Cleaning
The data fetched from the API endpoint /people/ is cleaned in the following ways:

* Leading and trailing spaces are removed from first and last names
* The date of birth is transformed from "dd-mm-yyyy" to "yyyy-mm-dd" format
* Lifetime value is transformed from "$xx.xx" to float

## Test
 To run the tests, navigate to the project directory and run the following command:
` pytest test.py` 
The project includes test cases for checking the functionality of the automation tool. The tests include:

1. test_people_endpoint_success: This test verifies that the "People" endpoint is working correctly by checking that it returns data with the expected fields, i.e. firstName, lastName, dateOfBirth, and email.

2. test_create_contacts: This test verifies that the "Contacts" endpoint is working correctly by creating "Contact" objects from the "People" data and POSTing it to the API. It verifies that the API returns a 200 status code, which indicates success.

3. test_failed_authentication: This test verifies that the API's authentication mechanism is working correctly by passing incorrect credentials. It verifies that the API returns a 401 status code, which indicates an authentication error.

4. test_missing_required_field: This test verifies that the API is correctly handling a missing required field by sending a "Contact" object missing the birthdate field. It verifies that the API returns a 400 status code, which indicates a client error.

5. test_invalid_email_address: This test verifies that the API is correctly handling an invalid email address by sending a "Contact" object with an invalid email. It verifies that the API returns a 400 status code, which indicates a client error.

6. test_non_numeric_lifetime_value: This test verifies that the API is correctly handling a non-numeric value for a custom property. It verifies that the API returns a 400 status code, which indicates a client error.

## Dependencies
The project uses the following dependencies:

* requests
* dotenv

## Requirements
* Python 3.x

## Environment Variables
The .env file contains the following environment variables:

* API_URL: API endpoint URL
* PEOPLE_URL: API endpoint /people/ URL
* CONTACTS_URL: API endpoint /contacts/ URL
* API_KEY: API key for fetching data from /people/ endpoint
* API_USERNAME: API basic auth username for posting data to /contacts/ endpoint
* API_PASSWORD: API basic auth password for posting data to /contacts/ endpoint


