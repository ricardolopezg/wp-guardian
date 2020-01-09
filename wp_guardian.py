#!/usr/bin/env python3

import sys
# import api_merge
from page_fuzzer import *
# from api_wpvulndb import *
from api_combined import *
from wp_version_scanner import *
print('test2')

try:
    url = sys.argv[1]
except:
    exit('Usage: python3 <file> <ip>')

print(url)
# print(getheader(url))
# fuzzinstallpage(url)
# fuzzupdatepage(url)
soup = url_input(url)
print(soup)
wp_version = wp_version_finder(soup)
wpvulndb(wp_version)
