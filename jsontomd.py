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

# format the sorted data
def format_sorted(vuln_list):
    formatted_cve_data = ''
    for vuln in vuln_list:                
        formatted_cve_data += f'---\n'
        formatted_cve_data += f'### **{vuln["title"]}**\n'
        formatted_cve_data += f'Vulnerability Type | Fixed In Version | \n'
        formatted_cve_data += f':--:|:--:'
        formatted_cve_data += f'\n{vuln["vuln_type"]} | {vuln["fixed_in"]}\n'
        url_list = vuln["references"]["url"]
        if 'cve' in vuln["references"]:
            cve_list = vuln["references"]["cve"]
            for cve_data in cve_list:
                formatted_cve_data += f'### **{cve_data["id"]}**\n'
                formatted_cve_data += f'CVSS Score | CVSS Vector |\n'
                formatted_cve_data += f':--:|:--:\n'
                formatted_cve_data += f'{cve_data["cvss"]["score"]} | {cve_data["cvss"]["vector"]} |\n'
                formatted_cve_data += f'**Description:**  \n>{cve_data["description"]}\n'
                url_list.append(cve_data["href"])
                formatted_cve_data += f'Reference URLs:\n'
                for urls in url_list:
                    formatted_cve_data += f'{urls}\n'
                    print(formatted_cve_data)
                    return formatted_cve_data

#TODO this function can probably be deleted
def cvelisttomd(cve_list):
    for information in cve_list:
        # print(information)
        cve_data=''
        cve_data += f'\n --- \n ### **{information["id"]}**\n\n'
        
        cve_data += f'**CVSS Score:** \n\n {information["cvss"]["score"]}\n\n'
        cve_data += f'**CVSS Vector:** \n\n {information["cvss"]["vector"]}\n\n'
        cve_data += f'>{information["description"]}\n\n'
        cve_data += f'References:\n\n>{information["href"]}\n'
        # print(cve_data)
    # return str(cve_list) # TODO formating for the list


# takes in datastore and sortedcve list and creates data for md
# This is the top part of the report <Report Header>
def create_md(datastore, sortedcvelist):
    report_id = return_report_id(datastore)
    md_header= ''
    md_header += f'report #'
    md_header += f' {report_id}\n\n'
    md_header += f'# {datastore[report_id]["report title"]}\n\n'
    md_header += f'### {datastore[report_id]["date"]}\n\n' 
    md_header += f'## Domain\n\n'
    md_header += f'{datastore[report_id]["domain"]}\n\n' 
    md_header += f'## Summary \n\n' 
    md_header += f'> {datastore[report_id]["summary"]}\n\n' 
    # md_header += f'## Vulnerabilities  \n\n' 
    md_header += f'### Wordpress Version: '
    md_header += f'{datastore[report_id]["assets"]["wordpress"]["version"]}\n\n'
    md_header += f'### Server Version:  '
    md_header += f' server-version '
    return md_header

def writetomd(create_md,datastore):
    path_folder = './reports'
    # file_name="finalreport"
    with open(os.path.join(path_folder, f'wpg-{return_report_id(datastore)}.md'), mode='w') as md_file:
        md_file.write(create_md)

def jsontomd(filename):
    datastore = readjson(filename)
    report = return_report_id(datastore)

    # get a sorted cve list
    # cvelist = getcvelist(datastore,report)
    # sortedcvelist = sortbycvss(cvelist)

    sortedcvelist = get_sorted_vuln_list(datastore, report)
    md_data = create_md(datastore,sortedcvelist)
    writetomd(md_data,datastore)

if __name__ == "__main__":
    filename = 'reports\\wpg-20200110-2484.json'
    # jsontomd(filename)
    datastore = readjson(filename)

    report = return_report_id(datastore)
    vuln_list = get_sorted_vuln_list(datastore, report)
    format_sorted(vuln_list)


    # fancy printing
    
    # for vuln in vuln_list:
    #     print(vuln['title'])
    #     if 'cve' in vuln['references']:
    #         print([(cve['id'], cve['cvss']) for cve in vuln['references']['cve']])