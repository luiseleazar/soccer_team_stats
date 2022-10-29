import json
import logging
from typing import List

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger('Team Stats')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

def get_arguments(filename: str):
    with open(filename, 'r') as f:
            arguments = json.load(f)

    return arguments

def get_first_link(team: str):
    url = 'https://www.google.com/search'
    headers = {
        'Accept' : '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': team + " footystats"}
    content = requests.get(url, headers = headers, params = parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    search = soup.find(id = 'search')
    first_link = search.find('a')
    url = first_link['href']

    if '/es/' in url:
        url = url.replace('/es/','/')
    return url

def create_all_disabled_config_file(all_stats_list: List[list]):
    stats_dict = {}
    for item in all_stats_list[1:]:
        stats_dict.update({item[0]:"Disabled"})
    
    with open("stats.json", "w") as f:
        json.dump(stats_dict, f)


# Implement setup logging() right here