import json
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_all_stats_df(website: str):
    """Gets all the stats from the webasite passed and 
    retuns a list of lists"""
    if 'https://footystats.org/clubs/' not in website:
        raise ValueError(f"Wrong website: {website}")
    path = '..\\chromedriver.exe'
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.get(website)

    containers = driver.find_elements(by='xpath', value='//tr[@class="row"]')
    all_stats_df = []
    
    for item in containers:
        tr_stat_list = []
        value_tr_container = item.find_elements(by='xpath', value='./td')

        for value in value_tr_container:
            value = value.text
            tr_stat_list.append(value)
        if '' not in tr_stat_list:
            all_stats_df.append(tr_stat_list)

    return all_stats_df


def get_desired_stats_dataframe(dataframe: List[list], config_json_file: str):
    """Returns the dataframe with stats that are enabled 
    on the config file"""
    enabled_stats = []
    desired_df = [["Stat", "Overall", "Local", "Away"]]
    
    with open(config_json_file, 'r') as f:
        stats_from_config = json.load(f)
    
    for key, value in stats_from_config.items():
        if value == "Enabled":
            enabled_stats.append(key)
    
    for stat in dataframe:
        if stat[0] in enabled_stats:
            desired_df.append(stat)
    
    return desired_df        
