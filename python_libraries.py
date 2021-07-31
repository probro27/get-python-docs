import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import lxml

serviceurl = "https://docs.python.org/3/library/"

lib = input("Enter Library Name - ")
url = serviceurl + f"{lib}.html"
request = requests.get(url)

alturi = f"https://pypi.org/project/{lib}/"

if request.status_code == 200:
    print("Module need not be installed")
    fhand = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(fhand, 'lxml')

    # print(soup.prettify())

    description = soup.find('div', attrs={'id': f'module-{lib}'})

    print(description.text.strip())
    # for lines in description:
    #     content = lines.find('p')
else:
    print("Module needs to be installed")
    handler = urllib.request.urlopen(alturi)
    soup1 = BeautifulSoup(handler, 'lxml')

    command = soup1.find('span', attrs={'id':'pip-command'})
    description = soup1.find('div', {'class':'project-description'})
    print("Install command")
    print(command.text.strip())
    print("Project Description")
    print(description.text.strip())
# for line in fhand:
#     print(line.decode().strip())