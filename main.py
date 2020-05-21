#!/usr/bin/env python3
from bs4 import BeautifulSoup; # for web scraping
import requests;
import urllib.request;
from urllib.request import urlopen;
import re;
import sys;

# sets the destination URL and returns parsed webpage as BeautifulSoup object
# to be used in other functions
def choose_vehicle_class(choice):
    url = "https://www.hitachi-rail.com/delivery/rail_vehicles/{}/index.html".format(choice)
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# prints delivery speed record data scraped from Hitachi website
def print_speed_records(choice):
    """pulls train delivery speed records and prints based on user selection"""
    soup = choose_vehicle_class(choice)
    counter = 0 # counter to track when a table has been iterated over
    train_tables = soup.find_all('table', {'class':'TableStyle3'}) # grab all tables of trains with style class TableStyle3...
    for tr in train_tables:                                   # ... for each <tr> train tables...
        rows = tr.find_all('tr')                              # find all <tr> and assign to var rows
        if counter == 0:
            for td in rows:                                     # ... for each <td> found in <tr>...
                removed_tags = td.get_text()                    # ... format HTML tags out, print, and update counter
                print(removed_tags)
                counter = 1
        else:
            print("------------------------------------------")  # ... else print table delimiter and update counter
            counter = 0

def main():
    running = True
    while running:
        print(
        "TYPE: High Speed Trains KEY: 'high_speed'\nTYPE: Intercity Trains KEY: 'intercity'\nTYPE: Commuter/Metro Trains KEY: 'commuter'\nTYPE: High Speed Lightweight Bolsterless Bogie Trains KEY: 'bogie'\n")
        print("To exit program type '0'")
        user_choice = input("To see delivery records for desired train class please type key value and press Enter: ")
        if user_choice == 0: # regardless if 0 is entered program is terminating on any input other than defined KEYS
            running = False
            break
        else:
            print_speed_records(user_choice)

if __name__ == "__main__":
    main()
