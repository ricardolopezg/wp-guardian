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


    print(f'[+] Running report on {url}\n')
    soup = wvs.url_input(url)
    print(f'[+] Scanning WordPress version\n')
    wp_version = wvs.wp_version_finder(soup)
    print(f'[+] Scanning server version\n')
    server_version = page_fuzzer.getserverversion(url)
    print(f'[+] Fuzzing pages for data exposure\n')
    update_page = page_fuzzer.fuzzupdatepage(url)
    install_page = page_fuzzer.fuzzinstallpage(url)
    print(f'[+] Building vulnerability profile\n')
    filename = api_combined.report_builder(wp_version, url)
    print(f'[+] Creating report\n')
    jsontomd.jsontomd(filename,server_version,install_page,update_page)

    print(f'[+] WP GUARDIAN SCAN COMPLETE!\n\n++ Check your reports directory for your scan results in JSON and MD format. e.g. <date>-<time>.md ++')
    print('\n')

if __name__ == "__main__":
    main()