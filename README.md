# Automation-Engineer-Candidate-Challenge


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

A screenshort of a short summary of test results from the test file "test.py" - 

<img width="838" alt="image" src="https://user-images.githubusercontent.com/14244685/216645670-26ad0d3b-032c-4221-be19-6bb8dd11e04a.png">

The test results indicate that three tests have failed and three tests have passed. The failed tests are "test_missing_required_field", "test_invalid_email_address", and "test_non_numeric_lifetime_value". The failure was due to an assertion error, as the expected result (422) did not match the actual result (400).

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


