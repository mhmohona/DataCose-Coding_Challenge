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
The project includes test cases for checking the functionality of the automation tool. The tests include:

* Test for successful GET request to the API endpoint /people/
* Test for successful POST request to the API endpoint /contacts/
* To run the tests, navigate to the project directory and run the following command:
` pytest test.py` 

## Dependencies
The project uses the following dependencies:

* requests
* dotenv

## Requirements
Python 3.x

## Environment Variables
The .env file contains the following environment variables:

* API_URL: API endpoint URL
* PEOPLE_URL: API endpoint /people/ URL
* CONTACTS_URL: API endpoint /contacts/ URL
* API_KEY: API key for fetching data from /people/ endpoint
* API_USERNAME: API basic auth username for posting data to /contacts/ endpoint
* API_PASSWORD: API basic auth password for posting data to /contacts/ endpoint
