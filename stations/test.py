from requests import get
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',}
response = get("https://www.google.com/search?q=latitude+longitude+of+75270+postal+code+paris+france",headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
a = soup.find("div", class_= "Z0LcW").text
print(a)

# import requests
# from bs4 import BeautifulSoup as soup
# import re

# url = "https://www.google.cl/maps/place/Hernando+de+Magallanes+958,+Las+Condes"
# resp=requests.request(method="GET",url=url)

# soup_parser = soup(resp.text, "html.parser")

# html_content = soup_parser.html.contents[1]

# print(html_content.find_all("script")[7].text)
# _script = html_content.find_all("script")[7]

# matches=re.findall("(-\d+\.\d{7})",_script.text)
# print(matches[0],matches[1])