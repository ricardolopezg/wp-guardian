import json
import os

filename = 'report_data.json'
with open(filename, 'r') as f:
    datastore = json.load(f)

def sortbycvss(cvelist):
    sortedcvelist = sorted(cvelist, key=lambda item: item['cvss']['score'],reverse=True)
    return sortedcvelist

def getcvelist(item):
    reportid = return_report_id(datastore)
    wp = item[reportid]['assets']['wordpress']
    cvelist=[]
    for vuln in wp['vulnerabilities']:
        if 'cve' in vuln['references']:
            for cve in vuln['references']['cve']:
                cvelist.append(cve)
                # print("ite")
    return cvelist

def return_report_id(datastore):
    for report in datastore:
        return report

vulnslist = getcvelist(datastore)
sortedvulnslist = sortbycvss(vulnslist)
# print(sortedvulnslist)

def print_sorted_vulns_list(sortedvulnslist):
    alldata = ''
    for information in sortedvulnslist:
        # alldata += '\n' +'CVE-'+ information['id'] +'\n' + '\n' + information['description'] + '\n' +information['href']
        alldata += f'\n --- \n ### **{information["id"]}**\n\n'
        alldata += f'**CVSS Score:** \n\n {information["cvss"]["score"]}\n\n'
        alldata += f'**CVSS Vector:** \n\n {information["cvss"]["vector"]}\n\n'
        alldata += f'>{information["description"]}\n\n'
        alldata += f'References:\n\n>{information["href"]}\n'
        # print(alldata)
    return alldata

# print_sorted_vulns_list(sortedvulnslist)
md_data= ''
md_data += f'report #{return_report_id(datastore)}\n\n'
md_data += f'# {datastore[return_report_id(datastore)]["report title"]}\n\n'
md_data += f'### {datastore[return_report_id(datastore)]["date"]}\n\n' 
md_data += f'## Domain\n\n{datastore[return_report_id(datastore)]["domain"]}\n\n' 
md_data += f'## Summary \n\n\n > {datastore[return_report_id(datastore)]["summary"]}\n\n' 
md_data += f'## Vulnerabilities  \n\n' 
md_data += f'### *Wordpress Version: {datastore[return_report_id(datastore)]["assets"]["wordpress"]["version"]}*\n\n' 
md_data += f'{print_sorted_vulns_list(sortedvulnslist)}\n\n' 

path_folder = 'C:/Users/anon/Desktop/wp-guardian/'
file_name="finalreport"
with open(os.path.join(path_folder, f'{file_name}.md'), mode='w') as md_file:
    md_file.write(md_data)