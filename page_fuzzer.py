import requests

def getserverversion(url):
    r = requests.get(url)
    server = r.headers['Server']
    return server
    
def fuzzupdatepage(url):
    r = requests.get(url+'/updates.php')
    if r.status_code == 404:
        updatesphpnotfound = 'updates.php not avialible. Good Job!'
        print(updatesphpnotfound)
        return updatesphpnotfound
    if r.status_code == 200:
        updatesphpfound = 'updates.php is availible. This is not secure'
        print(updatesphpfound)
        return updatesphpfound

def fuzzinstallpage(url):
    r = requests.get(url+'/install.php')
    if r.status_code == 404:
        updatesphpnotfound = 'install.php not avialible. Good Job!'
        print(updatesphpnotfound)
        return updatesphpnotfound
    if r.status_code == 200:
        updatesphpfound = 'install.php is availible. This is not secure'
        print(updatesphpfound)
        return updatesphpfound
