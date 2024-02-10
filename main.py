import json
from time import sleep

from bs4 import BeautifulSoup
from WEB_SCRAPER_EASY.Easy_Web_Scraping import Operations

url_link = "https://dubailand.gov.ae/en/eservices/licensed-real-estate-brokers/licensed-real-estate-brokers-list#/"

program = Operations(url_link)

program.open_web()

i = 1
while i == 1:
    program.wait_for_all_element_on_website()
    visible_element = program.check_if_the_element_exists(
        '//*[@id="load-more"]/div/button'
    )
    if visible_element is True:
        program.scroll_to_down_page()
        sleep(1)
        program.click_on_button('//*[@id="load-more"]/div/button', "xpath")
    else:
        print("stop")
        i = 0


soup = BeautifulSoup(program.driver.page_source, "html.parser")
card_details = soup.find_all("div", class_="card-detail")

counter = 0
brokers_dict = {}
for i, card_detail in enumerate(card_details):
    card_detail.find()
    broker_name = card_detail.find("a", class_="custom-card-title").text.strip()
    broker_number = (
        card_detail.find(id=f"license-number-{i}").text.split(": ")[1].strip()
    )
    office_name = card_detail.find(id=f"office-name-{i}").text.strip()
    email = card_detail.find(id=f"email-{i}").find("a").text.strip()
    phone = card_detail.find(id=f"phone-{i}").find("a").text.strip()
    rating = card_detail.find(id=f"rank-{i}").text.strip().count("rating")

    counter += 1

    brokers_dict[f"{i}"] = {
        "name": broker_name,
        "number": broker_number,
        "office_name": office_name,
        "email": email,
        "phone": phone,
        "rating": rating,
    }

print(f"Brokers count: {counter}")
program.close_web()

for i, dane in brokers_dict.items():
    print(f"{i}: {dane}")

with open("DB_BROKERS.json", "w") as json_file:
    json.dump(brokers_dict, json_file)
