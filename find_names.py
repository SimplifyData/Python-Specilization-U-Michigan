
from bs4 import BeautifulSoup

import urllib.request as urllib

b_soup =  BeautifulSoup




def find_names():

    sum = 0
    url = input("Website: ")
    try:
        browser_counter = int(input("How many times to browser url?: "))

        if type(browser_counter) == int(browser_counter):
            browser_counter = int(browser_counter)

    except:

        print("Please write an integer for the browser loops")

        exit()

    name_list = list()


    for counter in range(browser_counter):

        print(counter)
        html = urllib.urlopen(url).read()

        file = b_soup(html)

        # retrieve span tags

        span_tags = file('a')

        name_counter  = 1

        for tag in span_tags:


            #print(tag.contents[0])

            #print (tag)

            #print (tag.get('href', None))


            if name_counter == 3:
                name_list.append(tag.contents[0])

                url = tag.get("href", None)

                break

            name_counter+=1

    return name_list


span_tags = find_names()

print(span_tags)