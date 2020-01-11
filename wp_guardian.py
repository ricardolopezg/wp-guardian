#!/usr/bin/env python3

import sys
import api_combined
import wp_version_scanner as wvs
import jsontomd

def main():
    url = sys.argv[1]
    if len(url) < 1:
        exit('Usage:wp_guardian.py http(s)://www.example.com(/wordpress)')

    soup = wvs.url_input(url)
    wp_version = wvs.wp_version_finder(soup)
    filename = api_combined.report_builder(wp_version, url)
    jsontomd.jsontomd(filename)

if __name__ == "__main__":
    main()