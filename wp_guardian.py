#!/usr/bin/env python3

import sys
import api_merge
from page_fuzzer import *

try:
    url = sys.argv[1]
except:
    exit('Usage: ')

print(getheader(url))
fuzzinstallpage(url)
fuzzupdatepage(url)