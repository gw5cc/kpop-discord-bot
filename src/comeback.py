# pulled from https://hackersandslackers.com/scraping-urls-with-beautifulsoup/

import requests
from bs4 import BeautifulSoup
import re 

# def comeback_by_title

# def list all comebacks this month? 


def comeback_by_group(group_name):

    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    url = "https://kpopping.com/calendar"
    req = requests.get(url, headers)
    # second param tells us that this is an HTML documents
    soup = BeautifulSoup(req.content, 'html.parser')

    artist_info = {}
    for artists in soup.find_all("div", class_="data"):

        # Succesfully found artist
        # May need to consider when there's more than one artist
        if artists.find_all("span",class_="star", text=re.compile(F"{group_name}")):
            artist_name = artists.find_all("span",class_="star", text=re.compile(F"{group_name}"))
            artist_info["Artist"] = group_name
            
            # For now just assume there's only 1 artist/month for comeback
            artist_metadata = artist_name[0].parent.parent.parent
            artist_info["Title"] = artist_metadata.find("h4", class_="title").get_text()
            artist_info["Type"] = artist_metadata.find("div", class_="type").get_text()
            
            # Calendar date
            comeback_date = artist_metadata.parent.parent.parent.parent
            artist_info["Comeback Date"] = comeback_date.find("div", class_="date").find(text=True, recursive=False).strip()
            print(artist_info)
        

    # if you don't find the artist 
    if len(artist_info) == 0: 
        print(F"{group_name} does not exist or have a comeback this month.")
        return F"{group_name} does not exist or have a comeback this month."
    else:
        return artist_info