import xml.etree.ElementTree as ET
import urllib.request as urllib

def find_content():
    """
    this function finds the element node "content" and its value, using xml and urllib
    :return:
    """

    try:
        url = input("what is the website?: ")

        html = urllib.urlopen(url).read()

    except:
        print("Please enter a valid website url")

    tree = ET.fromstring(html)

    counts = tree.findall('.//count')

    #print ((counts))

    count_num = 0

    for count in counts:
        #print (type(count))

        count_text = count.text

        count_num = int(count_text) + count_num

        #print(count_num)


        #count_num = count_num + int(count.txt)

        #print (count_num)

    return count_num

xml_xount = find_content()

print(xml_xount)