#!/usr/bin/env python3

import sys
# import api_merge
from page_fuzzer import *
# from api_wpvulndb import *
from api_combined import *
from wp_version_scanner import *

try:
    url = sys.argv[1]
except:
    exit('Usage: python3 <file> <ip>')

# print(getheader(url))
# fuzzinstallpage(url)
# fuzzupdatepage(url)
soup = url_input(url)
wp_version = wp_version_finder(soup)

# api_combined.py function
wpvulndb(wp_version)
