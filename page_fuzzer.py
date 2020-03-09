import requests
import io
import mal_link_scan

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
def fuzzthemes(url):
    dirlist=[]
    with open('./db/wp-themes.fuzz.txt') as dp:
        line = dp.readline()
        while line:
            combined=url+line.strip()
            r = requests.get(combined)
            if r.status_code == 200:
                pagefound=f'Theme found; {combined} {r.status_code}'
                print(pagefound)
                dirlist.append(pagefound)
            line = dp.readline()
        
        print(dirlist)
        return dirlist

def fuzzplugins(url):
    dirlist=[]
    with open('./db/wp-plugins.fuzz.txt') as dp:
        line = dp.readline()
        while line:
            combined=url+line.strip()
            r = requests.get(combined)
            if r.status_code == 200:
                pagefound=f'Plugin Found; {combined} {r.status_code}'
                # print(pagefound)
                dirlist.append(pagefound)
            line = dp.readline()
        
        # print(dirlist)
        return dirlist        
def fuzzallpages(url):
    dirlist=[]
    with open('./db/wordpress.fuzz.txt') as dp:
        line = dp.readline()
        while line:
            combined=url+line.strip()
            r = requests.get(combined)
            if r.status_code == 200:
                pagefound=f'Page Found; {combined} {r.status_code}'
                # print(r.text)
                # print(pagefound)
                dirlist.append(combined)
            line = dp.readline()
            return dirlist

if __name__ == "__main__":
    url = 'https://www.cmohq.agency/'
    linklist = fuzzallpages(url)
    mal_link_scan.findlinks(linklist)
    # fuzzplugins(url)
    # fuzzcommondir(url)
    # fuzzthemes(url)