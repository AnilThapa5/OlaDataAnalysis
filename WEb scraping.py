from bs4 import BeautifulSoup
import requests
import pandas as pd


'''

#get the url
urls = "https://quotes.toscrape.com/"
req = requests.get(urls)
#print(req)

##parsing the html page

soul1 = BeautifulSoup(req.text,'html.parser')
#print(soul1)

#finding data

name = soul1.find("span", class_="text")
#print(name)

## finding all data

data = []
name1 = soul1.find_all("span", class_="text")
for q in name1:
    data.append(q.text)

df = pd.DataFrame(data, columns=["NAME"])
df.to_csv("data.csv", index=False)

'''


### Finding THe author for html

'''
url = "https://quotes.toscrape.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text,'html.parser')

table = soup.find("small", class_="author")
print(table)

'''

'''
## FInding the tags

url = "https://quotes.toscrape.com"
req = requests.get(url)
urs_pars = BeautifulSoup(req.text, "html.parser")
tags = urs_pars.find("div", class_="tags")
for t in tags:
    print(t.text)


'''

'''

## Finding all Data into dataframe including text author and tags

url = "https://quotes.toscrape.com"
get_url = requests.get(url)
soup = BeautifulSoup(get_url.text, "html.parser")
table = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    auth = quote.find("small", class_="author").text
    tags = ", ".join([tag.text for tag in quote.find_all("a", class_="tag")])
    table.append({
        "Text": text,
        "Author": auth,
        "Tags": tags
    })
    df = pd.DataFrame(table)
    print(df)
    df.to_csv("All_DATA.csv", index="False")


'''


