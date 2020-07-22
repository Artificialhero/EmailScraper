import re
import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urlsplit


inpUrl = ("http://sneakycorp.htb/team.php") #input('Please enter an URL ')
urlResponse = requests.get("http://sneakycorp.htb/team.php")

print("Checking site status:")
print(urlResponse.status_code) 

unscraped = deque([inpUrl])
scraped = set()
emails = set()

#emailExt = input("What top-level domain? e.g .com: add this to the regex")

#Start of scraping
while len(unscraped):
    url = unscraped.popleft()   
    scraped.add(url)
    
    urlParts = urlsplit(url)
    print(urlParts)
    
    baseUrl = "{0.scheme}://{0.netloc}".format(urlParts)
    if '/' in urlParts.path:
        path = url[:url.rfind('/')+1]
    else:
        path = urllib
        
    #Send HTTP GET Request to the site
    print("Checking URL %s" % url)
    try:
        urlResponse
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue
    
    #Getting emails, might need to change regex
    newMails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", 
                              urlResponse.text, re.I))
    emails.update(newMails)
    
for i in emails:
    print(i)
    #Output to .txt file
