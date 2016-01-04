import bs4

b_soup = bs4.BeautifulSoup

import sqlite3

import urllib.request as urlreq

def store_email():
    """
    This function counts the name of org from a text file and stores in SQL lite
    :return:
    """

    conn = sqlite3.connect("D:\\Box Sync\\Python Projects\\Python-Specilization-U-Michigan\\SQL lite\\firstsqllite.db")

    url = input("Name of the file")

    html = urlreq.urlopen(url)

    print (html)

