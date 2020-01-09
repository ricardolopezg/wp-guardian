#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import urllib.request
# from wp_guardian import *

def url_input(website):
    wp_page = urllib.request.urlopen(website+'/wordpress').read()
    soup = BeautifulSoup(wp_page,"html.parser")
    return soup

def wp_version_finder(soup):
    for tag in soup.find_all("meta"):
        if tag.get("name", None) == "generator":
            version = tag.get("content", None).split(' ')
            return version[1]

# if __name__ == "__main__":
#     wp_version_finder(soup)
    # print(wp_version_finder(soup))