#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import urllib.request
import sys

url = 'http://3.82.102.163/wordpress' # refactor to get input from wp_guardian.py

wp_page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(wp_page,"html.parser")

def wp_version_finder(webpage):
    for tag in soup.find_all("meta"):
        if tag.get("name", None) == "generator":
            version = tag.get("content", None).split(' ')
            return version[1]

# if __name__ == "__main__":
#     wp_version_finder(soup)
    # print(wp_version_finder(soup))