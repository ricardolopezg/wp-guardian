#!/usr/bin/env python3

from config import *
import vulners
import api_wpvulndb
import json

def cve_parser(cve_info):
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

        refrence = cve_vuln_dict[cve_list_input[counter]]["href"]
        print("\nReference:\n" + str(refrence))

        counter += 1
        print("\n###########################################################\n")

    with open('vulnerability_data.json', 'w') as outfile:
        json.dump(vulnerability_data_json_object, outfile)

def main():
    global cve_list_input
    global multiple_cve
    cve_list_input = ["CVE-2017-14174", "CVE-2016-1175"]

    vulners_api = vulners.Vulners(api_key=vulners_api_key)

    # Search multiple CVE's
    multiple_cve = vulners_api.documentList(cve_list_input)
    # print(type(CVE_DATA)) # type: dictionary
    multiple_cve_json_str = json.dumps(multiple_cve, indent=2)
    # print(multiple_cve_json_str)

    cve_parser(multiple_cve)

if __name__ == '__main__':
    main()