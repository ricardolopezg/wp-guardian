import json
import os
import api_combined
import page_fuzzer

#Takes in json file name from api combined
def readjson(filename):
    # filename = 'data_structure_design.json'
    with open(filename, 'r') as f:
        datastore = json.load(f)
    return datastore

# takes in the all the data and returns the report id
def return_report_id(datastore):
    for report in datastore:
        return report

# takes in datastore and reportid returns cvelist
def getcvelist(datastore,reportid): 
    wp = datastore[reportid]['assets']['wordpress']
    cvelist=[]
    for vuln in wp['vulnerabilities']:
        if 'cve' in vuln['references']:
            for cve in vuln['references']['cve']:
                cvelist.append(cve)
    return cvelist

# takes in cve list and returns sorted cvelist
def sortbycvss(cvelist):
    sortedcvelist = sorted(cvelist, key=lambda item: item['cvss']['score'],reverse=True)
    return sortedcvelist

def get_sorted_vuln_list(datastore, report_id):
    # fetch the list of vulnerabilities for this report id
    vuln_list = datastore[report_id]['assets']['wordpress']['vulnerabilities']
    
    # define a key function that extracts the 
    # largest CVSS_CVE for a single vulnerability
    def get_key(vuln):
        if 'cve' in vuln['references']:
            # get the list of CVEs
            cves = vuln['references']['cve']
            # construct a list of {CVSS}_{CVE_ID} for all of the CVEs
            cvss_list = [f'{c["cvss"]["score"]}_{c["id"]}' for c in cves]
            # choose the largest value
            m = max(cvss_list)
            # print(cvss_list, m)
            return m
        else:
            # There are no CVEs, sort this as the lowest
            return " " # sort to bottom
            # return "_" # sort to top

    sorted_list = sorted(vuln_list, key=get_key, reverse=True)
    return sorted_list

# format the sorted cve data
def format_sorted(vuln_list):
    formatted_cve_data = ''
    for vuln in vuln_list:                
        formatted_cve_data += f'---\n'
        formatted_cve_data += f'### **{vuln["title"].strip()}**\n'
        url_list = vuln["references"]["url"]
        if 'cve' in vuln["references"]:
            cve_list = vuln["references"]["cve"]
            for cve_data in cve_list:
                url_list.append(cve_data["href"])
                formatted_cve_data += f'\n### {cve_data["id"]}\n\n'
                formatted_cve_data += f'  Vulnerability Type   |   Fixed In Version   |  CVSS Score  |  CVSS Vector\n'
                formatted_cve_data += f':--:|:--:|:--:|:--:'
                formatted_cve_data += f'\n  {vuln["vuln_type"]} | {vuln["fixed_in"]}  | {cve_data["cvss"]["score"]} | {cve_data["cvss"]["vector"]}\n\n'
                # formatted_cve_data += f'  CVSS Score  |  CVSS Vector  | \n'
                # formatted_cve_data += f':--:|:--:'
                # formatted_cve_data += f'\n{cve_data["cvss"]["score"]} | {cve_data["cvss"]["vector"]} |\n\n'
                formatted_cve_data += f'**Description:** \n\n'
                formatted_cve_data += f'>{cve_data["description"]}\n\n'
                
                formatted_cve_data += f'**References:** \n\n'
                for urls in url_list:
                    formatted_cve_data += f'>{urls}\n\n'
                    
    # print(formatted_cve_data)
    return formatted_cve_data

# takes in datastore and sortedcve list and creates data for md
# This is the top part of the report <Report Header>
def create_md(datastore, sortedcvelist,server_version,install_page,update_page):
    report_id = return_report_id(datastore)
    md_header= ''
    md_header += f'Report #'
    md_header += f' {report_id}\n\n'
    md_header += f'# {datastore[report_id]["report title"]}\n\n'
    md_header += f'### {datastore[report_id]["date"]}\n\n' 
    md_header += f'## Domain\n\n'
    md_header += f'{datastore[report_id]["domain"]}\n\n' 
    md_header += f'## Summary \n\n' 
    md_header += f'> {datastore[report_id]["summary"]}\n\n'
    md_header += f'\n\n{install_page}\n\n{update_page}\n\n'

    md_header += f'#### Wordpress Version: '
    md_header += f'{datastore[report_id]["assets"]["wordpress"]["version"]}\n\n'
    md_header += f'#### Server Version: {server_version}\n\n '
    return md_header

def writetomd(md_header,format_sorted,datastore):
    create_md = md_header + format_sorted
    path_folder = './reports'
    with open(os.path.join(path_folder, f'wpg-{return_report_id(datastore)}.md'), mode='w') as md_file:
        md_file.write(create_md)

def jsontomd(filename,server_version,install_page,update_page):
    datastore = readjson(filename)
    report = return_report_id(datastore)
    vuln_list = get_sorted_vuln_list(datastore, report)
    sortedcvelist = get_sorted_vuln_list(datastore, report) 
    md_data = create_md(datastore,sortedcvelist,server_version,install_page,update_page)
    data_body = format_sorted(vuln_list)
    writetomd(md_data,data_body,datastore)

if __name__ == "__main__":
    filename = 'reports\\wpg-20200110-2484.json'
    datastore = readjson(filename)
    # report = return_report_id(datastore)
    # vuln_list = get_sorted_vuln_list(datastore, report)
    # sortedcvelist = get_sorted_vuln_list(datastore, report)  
    # data_header = create_md(datastore,sortedcvelist)
    # data_body = format_sorted(vuln_list)
    # writetomd(data_header,data_body,datastore)
