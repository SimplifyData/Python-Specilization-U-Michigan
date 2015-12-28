
from bs4 import BeautifulSoup

import urllib.request as urllib

b_soup =  BeautifulSoup




def count_words():
    """
    This function parses the url html using beautiful soup.
    It counts the text value of a specific tag
    :return:
    """

    sum = 0
    url = input("Website: ")



    html = urllib.urlopen(url).read()

    file = b_soup(html)

    # retrieve span tags

    span_tags = file('span')

    for tag in span_tags:
        print tag
        sum = sum + int(tag.contents[0])

    return sum

span_tags = count_words()

print(span_tags)