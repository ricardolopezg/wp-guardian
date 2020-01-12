#!/usr/bin/env python3

import json
import requests
from requests.compat import urljoin
from config import *
import vulners
# import random
from datetime import datetime
import pprint
import os

pp = pprint.PrettyPrinter(indent=2)

def report_builder(scanned_wp_version, url):
    now = datetime.now()
    # report_num = now.strftime("%Y%m%d%H%M%S") + str(random.randint(1000,9999))
    report_num = now.strftime("%Y%m%d%H%M%S")
    report_data = {}

    report_data[report_num] = {}
    report_data[report_num]["report title"] = "WP Guardian Vulnerability Scan"
    report_data[report_num]["date"] = now.strftime("%d/%m/%Y %H:%M:%S")
    report_data[report_num]["domain"] = url
    # report_data[report_num]["summary"] = ""
    report_data[report_num]["assets"] = {}
    report_data[report_num]["assets"]["wordpress"] = {}
    report_data[report_num]["assets"]["wordpress"]["version"] = scanned_wp_version
    report_data[report_num]["assets"]["wordpress"]["vulnerabilities"] = wpvulndb_api(scanned_wp_version)
    write_summary(report_data, report_num)

    # Make sure to create a reports directory to save report files
    #TODO refactor to its own function
    reports_dir = "./reports"
    if not os.path.isdir('./reports'):
        os.mkdir(reports_dir)
    #TODO refactor to its own function
    report_json_file_name = f'./reports/wpg-{report_num}.json'
    with open(report_json_file_name, 'w') as outfile:
        json.dump(report_data, outfile)

    return report_json_file_name

def wp_version_exploit_finder(wp_version_vulns, wp_scanner_version):
    vulnerabilities = wp_version_vulns[wp_scanner_version]["vulnerabilities"]
    vuln_list = []

    for vuln in vulnerabilities:
        report_vulns = {}

        vuln_id = vuln["id"]
        report_vulns["id"] = vuln_id

        vuln_title = vuln["title"]
        report_vulns["title"] = vuln_title

        vuln_type = vuln["vuln_type"]
        report_vulns["vuln_type"] = vuln_type

        references = vuln["references"]
        report_vulns["references"] = references

        if 'cve' in references:
            cve_list = references['cve'] #extract cves and add to list
            var = vulners_api(cve_list)
            report_vulns['references']['cve'] = var

        fixed_in = vuln["fixed_in"]
        report_vulns["fixed_in"] = fixed_in

        vuln_list.append(report_vulns)

    return vuln_list

def wpvulndb_api(wpversion):
    remove_version_periods = wpversion.replace(".", "")

    base_url = "https://wpvulndb.com/api/v3/"
    api_token = {'Authorization': 'Token ' + wpvulndb_api_key}

    # WPVULNDB type of api call
    wordpress_path = "wordpresses/" + remove_version_periods
    # WPVULNDB API call
    wordpress_url = requests.get(urljoin(base_url, wordpress_path), headers = api_token)
    wordpress_path_json_object = json.loads(wordpress_url.text)

    if "error" in wordpress_path_json_object:
        raise Exception(wordpress_path_json_object['error'] + " --> Change API Key")

    vuln_list = wp_version_exploit_finder(wordpress_path_json_object, wpversion)
    return vuln_list

def vulners_cve_parser(cve_info):
    list_of_cves_dict = []

    for cve_id in cve_info:
        cve_dict = {}
        cve_id_for_report_data = cve_id.replace("CVE-", "")

        id = cve_info[cve_id]["id"]
        cve_dict["id"] = id

        description = cve_info[cve_id]["description"]
        cve_dict["description"] = description

        CVSS_score = cve_info[cve_id]["cvss"]["score"]
        cve_dict["cvss"] = {}
        cve_dict["cvss"]["score"] = CVSS_score

        CVSS_vector = cve_info[cve_id]["cvss"]["vector"]
        cve_dict["cvss"]["vector"] = CVSS_vector

        href = cve_info[cve_id]["href"]
        cve_dict["href"] = href

        list_of_cves_dict.append(cve_dict)

    return list_of_cves_dict

def write_summary(full_scan_report_data, report_num):
    report_base = full_scan_report_data[report_num]
    num_vulns = len(report_base["assets"]["wordpress"]["vulnerabilities"])

    report_base["summary"] = f'WP Guardian ran a WordPress vulnerability scan and generated a report on {report_base["date"]} for {report_base["domain"]}. {num_vulns} vulnerabilities were found for WordPress {report_base["assets"]["wordpress"]["version"]}. The most critical vulnerabilities are presented first and scale down by CVSS score.'

def vulners_api(cve_list):
    cve_list = [f'CVE-{cve}' for cve in cve_list]

    vulners_api = vulners.Vulners(api_key=vulners_api_key)
    # Search multiple CVE's
    multiple_cve = vulners_api.documentList(cve_list)

    return vulners_cve_parser(multiple_cve)