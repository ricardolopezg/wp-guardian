#!/usr/bin/env python3

import json
import requests
from requests.compat import urljoin
from config import *
from wp_version_scanner import *
import vulners

def wp_version_exploit_finder(wp_version_vulns):
    wp_version_vuln_dict = wp_version_vulns
    vulnerabilities = wp_version_vuln_dict[wp_scanner_version]["vulnerabilities"]
    counter = 0

    for vuln in vulnerabilities:
        vuln_title = wp_version_vuln_dict[wp_scanner_version]["vulnerabilities"][counter]["title"]
        print("Vulnerability:\n" + vuln_title)

        vuln_type = wp_version_vuln_dict[wp_scanner_version]["vulnerabilities"][counter]["vuln_type"]
        print("\nVulnerability type:\n" + vuln_type)

        references = wp_version_vuln_dict[wp_scanner_version]["vulnerabilities"][counter]["references"]

        for exp_type in references:
            counter2 = 0
            if exp_type == "url":
                print("\nReferences:")
                refs = wp_version_vuln_dict[wp_scanner_version]["vulnerabilities"][counter]["references"]["url"]
                for exps in range(len(refs)):
                    print(refs[counter2])
                    counter2 += 1
            if exp_type == "metasploit":
                print("\nMetasploit:")
                exploits = wp_version_vuln_dict[wp_scanner_version]["vulnerabilities"][counter]["references"]["metasploit"]
                for exps in range(len(exploits)):
                    print(exploits[counter2])
                    counter2 += 1
            if exp_type == "cve":
                print("\nCVE:")
                exploits = wp_version_vuln_dict[wp_scanner_version]["vulnerabilities"][counter]["references"]["cve"]
                for exps in range(len(exploits)):
                    print(exploits[counter2])
                    counter2 += 1
            if exp_type == "exploitdb":
                print("\nExploitDB:")
                exploits = wp_version_vuln_dict[wp_scanner_version]["vulnerabilities"][counter]["references"]["exploitdb"]
                for exps in range(len(exploits)):
                    print(exploits[counter2])
                    counter2 += 1
        counter += 1
        print("\n###########################################################\n")

def wpvulndb(wpversion):
    global wp_scanner_version
    # wp_scanner_version = wp_version_finder(soup) # function in wp_version_scanner.py
    wp_scanner_version = wpversion
    print(wpversion)
    wordpress_version = wpversion.replace(".", "") # ~~~> wordpress version must not include periods

    base_url = "https://wpvulndb.com/api/v3/"
    api_token = {'Authorization': 'Token ' + wpvulndb_api_key}

    # WPVULNDB type of api call
    wordpress_path = "wordpresses/" + wordpress_version
    # WPVULNDB API call
    wordpress_url = requests.get(urljoin(base_url, wordpress_path), headers = api_token)
    # # output dictionary/object
    wordpress_path_json_object = json.loads(wordpress_url.text)
    # output prettified
    # wordpress_path_json_str = json.dumps(wordpress_path_json_object, indent=2)
    # print(wordpress_path_json_str)
    # print(wordpress_path_json_object)

    # WP Version Function Data
    # with open('sample_output_obj.json', 'w') as outfile:
    #     json.dump(wordpress_path_json_object, outfile)
    # with open('sample_output_obj.json') as json_file:
    #     wp_version_data = json.load(json_file)
    # wp_version_exploit_finder(wp_version_data)
    wp_version_exploit_finder(wordpress_path_json_object)

def vulners_cve_parser(cve_info):
    cve_vuln_dict = cve_info
    counter = 0

    for vuln in cve_vuln_dict:
        print(vuln + ":")

        description = cve_vuln_dict[cve_list_input[counter]]["description"]
        print("\nDescription:\n" + description)

        CVSS_score = cve_vuln_dict[cve_list_input[counter]]["cvss"]["score"]
        print("\nCVSS Score:\n" + str(CVSS_score))

        CVSS_vector = cve_vuln_dict[cve_list_input[counter]]["cvss"]["vector"]
        print("\nCVSS Vector:\n" + str(CVSS_vector))

        reference = cve_vuln_dict[cve_list_input[counter]]["href"]
        print("\nReference:\n" + str(reference))

        counter += 1
        print("\n###########################################################\n")

    with open('vulnerability_data.json', 'w') as outfile:
        json.dump(vulnerability_data_json_object, outfile)

def vulners():
    global cve_list_input
    global multiple_cve
    cve_list_input = ["CVE-2014-8810", "CVE-2014-8809"]

    vulners_api = vulners.Vulners(api_key=vulners_api_key)

    # Search multiple CVE's
    multiple_cve = vulners_api.documentList(cve_list_input)
    # print(type(CVE_DATA)) # type: dictionary
    multiple_cve_json_str = json.dumps(multiple_cve, indent=2)
    print(multiple_cve_json_str)

    vulners_cve_parser(multiple_cve)

