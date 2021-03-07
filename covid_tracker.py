import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)
    return r.text
    
myurl ="https://covid-19tracker.milkeninstitute.org/"

htmldata = getdata(myurl)

soup = BeautifulSoup(htmldata,'html.parser')

myclass = "is_h5-2 is_developer w-richtext"

result = str(soup.find_all("div",class_=myclass))

print("No 1" + result[46:86])

print("No  2" + result[139:226])
       
print("No  3" + result[279:305])
       
print("No  4" + result[358:375])
       
print("No  5" + result[428:437] + " " + result[490:550])
                                     