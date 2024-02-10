# Dubai Brokers Scraper

## Description

Dubai Brokers Scraper is an advanced data extraction tool that automatically retrieves and processes information about licensed real estate brokers from the official Dubai Land Department website.
https://dubailand.gov.ae/en/eservices/licensed-real-estate-brokers/licensed-real-estate-brokers-list#/

## Features

- Automatically scrolls the webpage and clicks the "Load More" button to retrieve all available data.
- Extracts and processes broker data such as name, license number, office name, email, phone, and rating.
- Saves the collected data to a JSON file.

## Requirements

- Python 3.6 or newer
- `WEB_SCRAPER_EASY` library - a custom library created for easy web scraping.
- BeautifulSoup
- json
- time

## Installation

1. Clone the repository to your local environment.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the script using `python main.py`.

## WEB_SCRAPER_EASY Library

The `WEB_SCRAPER_EASY` library is a key component of this project. 
It is a custom library created for easy web scraping. 
It can be downloaded from this GitHub repository: https://github.com/Markowian22/WEB_SCRAPER

## Author

Marek Budzicz
