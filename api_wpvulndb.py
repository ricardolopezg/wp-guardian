#!/usr/bin/env python3

import json
import requests
from requests.compat import urljoin
from config import *
from wp_version_scanner import *

def wp_parser(wp_version_vulns):
    wpvulndb_api_data_dict = {}

    # for k, v in wpvulndb_api_data_dict:
    #     print(k,v)
    print("hello")



    # vulnerabilities = wp_version_vulns[wp_version]["vulnerabilities"]
    counter = 0

    # for vuln in vulnerabilities:
    #     vuln_title = wp_version_vulns[wp_version]["vulnerabilities"][counter]["title"]
    #     print("Vulnerability:\n" + vuln_title)
    #
    #     vuln_type = wp_version_vulns[wp_version]["vulnerabilities"][counter]["vuln_type"]
    #     print("\nVulnerability type:\n" + vuln_type)
    #
    #     references = wp_version_vulns[wp_version]["vulnerabilities"][counter]["references"]
    #
    #     for exp_type in references:
    #         counter2 = 0
    #         if exp_type == "url":
    #             print("\nReferences:")
    #             refs = wp_version_vulns[wp_version]["vulnerabilities"][counter]["references"]["url"]
    #             for exps in range(len(refs)):
    #                 print(refs[counter2])
    #                 counter2 += 1
    #
    #     counter += 1


def wp_ip_address(wp_version):
    # global wp_version
    global theme_name
    global plugin_name
    wordpress_version = wp_version.replace(".", "")
    # wp_version = wp_version_finder(soup) # function in wp_version_scanner.py
    # wordpress_version = wp_version.replace(".", "")
    # theme_name = "echelon"
    # plugin_name = "wp-symposium"

    # WPVULNDB api request
    base_url = "https://wpvulndb.com/api/v3/"
    api_token = {'Authorization': 'Token ' + wpvulndb_api_key}

    # WPVULNDB api call by asset type
    wordpress_path = "wordpresses/" + wordpress_version
    # theme_path = "themes/" + theme_name
    # plugin_path = "plugins/" + plugin_name

    # WPVULNDB api call
    wordpress_url = requests.get(urljoin(base_url, wordpress_path), headers = api_token)
    # theme_url = requests.get(urljoin(base_url, theme_path), headers = api_token)
    # plugin_url = requests.get(urljoin(base_url, plugin_path), headers = api_token)

    # output to object
    wordpress_path_json_object = json.loads(wordpress_url.text)
    # theme_version_json_object = json.loads(theme_url.text)
    # plugin_version_json_object = json.loads(plugin_url.text)

    # output prettified
    # wordpress_path_json_str = json.dumps(wordpress_path_json_object, indent=2)
    # theme_version_json_str = json.dumps(theme_version_json_object, indent=2)
    # plugin_version_json_str = json.dumps(plugin_version_json_object, indent=2)

    # print(wordpress_path_json_str)
    # print(wordpress_path_json_object)
    # print(theme_version_json_str)
    # print(plugin_version_json_str)

    # WP Version Function Data
    # with open('sample_output_obj.json', 'w') as outfile:
    #     json.dump(wordpress_path_json_object, outfile)
    # with open('sample_output_obj.json') as json_file:
        # wp_version_data = json.load(json_file)
    # wp_parser(wp_version_data)
    # wp_version_exploit_finder(wordpress_path_json_object)

    # WP Theme Function Data
    # with open('sample_output_theme_obj.json', 'w') as outfile:
    #     json.dump(theme_version_json_object, outfile)
    # with open('sample_output_theme_obj.json') as json_file:
    #     theme_data = json.load(json_file)
    # wp_theme_exploit_finder(theme_data)
    # wp_theme_exploit_finder(theme_version_json_object)

    # WP Plugin Function Data
    # with open('sample_output_plugin_obj.json', 'w') as outfile:
        # json.dump(plugin_version_json_object, outfile)
    # with open('sample_output_plugin_obj.json') as json_file:
    #     plugin_data = json.load(json_file)
    # wp_plugin_exploit_finder(plugin_data)
    # wp_plugin_exploit_finder(plugin_version_json_object)

wp_parser(wordpress_path_json_object)

# if __name__ == '__main__':
#     main()