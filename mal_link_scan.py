# TODO Find all paths of web page and 
# extract all links and scan check if 
# any of them have been reported as malicous
import re
import requests

def findlinks(linklist):
    urls = []
    for item in linklist:
        r = requests.get(item).text
        urls.append(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r))
    print(urls)
    return urls

if __name__ == "__main__":
    pass
    
    