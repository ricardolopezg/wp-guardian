#!/usr/bin/env python3

import sys
import api_combined
import wp_version_scanner as wvs
import jsontomd
import page_fuzzer
def main():
    url = sys.argv[1]
    if len(url) < 1:
        exit('Usage:wp_guardian.py http(s)://www.example.com(/wordpress)')

    print('\n')
    print('██╗    ██╗██████╗      ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ █████╗ ███╗   ██╗')
    print('██║    ██║██╔══██╗    ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║')
    print('██║ █╗ ██║██████╔╝    ██║  ███╗██║   ██║███████║██████╔╝██║  ██║██║███████║██╔██╗ ██║')
    print('██║███╗██║██╔═══╝     ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██║██╔══██║██║╚██╗██║')
    print('╚███╔███╔╝██║         ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║  ██║██║ ╚████║')
    print(' ╚══╝╚══╝ ╚═╝          ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝')
    print('\n')
    print('IS BUILDING YOUR REPORT. PLEASE WAIT...')
    print('\n')


    soup = wvs.url_input(url)
    wp_version = wvs.wp_version_finder(soup)
    filename = api_combined.report_builder(wp_version, url)
    server_version = page_fuzzer.getserverversion(url)
    update_page = page_fuzzer.fuzzupdatepage(url)
    install_page = page_fuzzer.fuzzinstallpage(url)
    jsontomd.jsontomd(filename,server_version,install_page,update_page)
    print("WP GUARDIAN SCAN COMPLETE! Check your reports directory.")
    print('\n')

if __name__ == "__main__":
    main()