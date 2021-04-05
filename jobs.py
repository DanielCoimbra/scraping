from bs4 import BeautifulSoup
import requests
from time import gmtime, strftime

TIME = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())



url = 'https://www.freelancer.com/jobs/s-web-security-web-development-python-internet-security-computer-security-golang-java-javascript-network-security/1/?cl=l-en-pt'

response = requests.get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

soup = html_soup.find_all('a', class_='JobSearchCard-primary-heading-link')

with open(f'{TIME}.txt', 'w') as f:
    f.write(str(soup))
    f.write('\n\n\n************************************************\n\n\n')

    url = 'https://www.freelancer.com/jobs/?cl=l-en-pt&keyword=python'

    response2 = requests.get(url)

    html_soup2 = BeautifulSoup(response2.text, 'html.parser')

    soup2 = html_soup2.find_all('div', class_='JobSearchCard-item')

    f.write(str(soup2))

print('done')

