import requests

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
