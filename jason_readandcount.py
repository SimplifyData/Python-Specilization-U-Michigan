import urllib.request as urllib
import json

def jason_count():
    """
    this function pulls a url and reads the json and parses data, numbers and adds them from a key:value pair.
    :return:
    """

    try:
        url = input("Enter the url: ")

        web_page = urllib.urlopen(url).read()

    except:
        print("Enter a valid URL")

    data = json.loads(web_page.decode("utf-8"))

    print('User Counts', len(data["comments"]))

    print(json.dumps(data, indent = 4))

    sum_count = 0

    for count in range(len(data["comments"])):
        num_of_comments = data["comments"][count]["count"]

        sum_count = sum_count +  num_of_comments

    print (sum_count)


count_numbers = jason_count()

