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

# takes in datastore and sortedcve list and creates data for md
def create_md(datastore,sortedcvelist):
    md_data= ''
    md_data += f'report #'
    md_data += f' {return_report_id(datastore)}\n\n'
    md_data += f'# {datastore[return_report_id(datastore)]["report title"]}\n\n'
    md_data += f'### {datastore[return_report_id(datastore)]["date"]}\n\n' 
    md_data += f'## Domain\n\n'
    md_data += f'{datastore[return_report_id(datastore)]["domain"]}\n\n' 
    md_data += f'## Summary \n\n' 
    md_data += f'> {datastore[return_report_id(datastore)]["summary"]}\n\n' 
    md_data += f'## Vulnerabilities  \n\n' 
    md_data += f'### Wordpress Version: '
    md_data += f'{datastore[return_report_id(datastore)]["assets"]["wordpress"]["version"]}\n\n'
    for information in sortedcvelist:
        md_data += f'\n --- \n ### **{information["id"]}**\n\n'
        md_data += f'**CVSS Score:** \n\n {information["cvss"]["score"]}\n\n'
        md_data += f'**CVSS Vector:** \n\n {information["cvss"]["vector"]}\n\n'
        md_data += f'>{information["description"]}\n\n'
        md_data += f'References:\n\n>{information["href"]}\n'
    return md_data

def writetomd(create_md,datastore):
    path_folder = './reports'
    # file_name="finalreport"
    with open(os.path.join(path_folder, f'wpg-{return_report_id(datastore)}.md'), mode='w') as md_file:
        md_file.write(create_md)

def jsontomd(filename):
    datastore = readjson(filename)
    reportid = return_report_id(datastore)
    cvelist = getcvelist(datastore,reportid)
    sortedcvelist = sortbycvss(cvelist)
    md_data = create_md(datastore,sortedcvelist)
    writetomd(md_data,datastore)

if __name__ == "__main__":
    filename = 'data_structure_design.json'
    jsontomd(filename)