
from bs4 import BeautifulSoup

import urllib.request as urllib

b_soup =  BeautifulSoup




def find_names():

    sum = 0
    url = input("Website: ")



    html = urllib.urlopen(url).read()

    file = b_soup(html)

    # retrieve span tags

    span_tags = file('a')

    for tag in span_tags:
        print (tag)




span_tags = find_names()

print(span_tags)