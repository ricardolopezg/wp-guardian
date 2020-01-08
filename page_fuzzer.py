import requests

def getheader(url):
    r = requests.get('http://'+url)
    # print(r.headers)
    return r.headers
    
def fuzzupdatepage(url):
    r = requests.get('http://'+url+'/updates.php')
    if r.status_code == 404:
        updatesphpnotfound = 'updates.php not avialible. Good Job!'
        print(updatesphpnotfound)
        # return updatesphpnotfound
    if r.status_code == 200:
        updatesphpfound = 'updates.php is availible. This is not secure'
        print(updatesphpfound)
        # return updatesphpfound


def fuzzinstallpage(url):
    r = requests.get('http://'+url+'/install.php')
    if r.status_code == 404:
        updatesphpnotfound = 'install.php not avialible. Good Job!'
        print(updatesphpnotfound)
        # return updatesphpnotfound
    if r.status_code == 200:
        updatesphpfound = 'install.php is availible. This is not secure'
        print(updatesphpfound)
        # return updatesphpfound

# fuzzinstallpage('3.82.102.163/wordpress')