import requests
import io

def getserverversion(url):
    r = requests.get(url)
    server = r.headers['Server']
    return server
    
def fuzzupdatepage(url):
    r = requests.get(url+'/updates.php')
    if r.status_code == 404:
        updatesphpnotfound = f' - [x] updates.php is not accessible'
        # print(updatesphpnotfound)
        return updatesphpnotfound
    if r.status_code == 200:
        updatesphpfound = f'updates.php is accessible. This is not secure'
        # print(updatesphpfound)
        return updatesphpfound

def fuzzinstallpage(url):
    r = requests.get(url+'/install.php')
    if r.status_code == 404:
        updatesphpnotfound = f' - [x] install.php is not accessible'
        # print(updatesphpnotfound)
        return updatesphpnotfound
    if r.status_code == 200:
        updatesphpfound = f'install.php is accessible. This is not secure'
        # print(updatesphpfound)
        return updatesphpfound

# Fuzz all directories from list
def fuzzcommondir(url):
    dirlist=[]
    with open('./db/commonfile.txt') as dp:
        line = dp.readline()
        while line:
            combined=url+line.strip()
            r = requests.get(combined)
            if r.status_code == 200:
                pagefound=f'Found {combined} {r}. This may have some data over exposure.'
                dirlist.append(pagefound)
                
            # if r.status_code != 200:
            #     pagenotfound=f'NOT Found {combined} {r}. No data overexposure here.'
            #     dirlist.append(pagenotfound)
            
            line = dp.readline()
        
        print(dirlist)
        return dirlist

        
if __name__ == "__main__":
    url = 'https://www.cmohq.agency/'
    fuzzcommondir(url)