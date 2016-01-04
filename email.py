import bs4

b_soup = bs4.BeautifulSoup

import sqlite3

import urllib.request as urlreq

import re
def store_email():
    """
    This function counts the name of org from a text file and stores in SQL lite
    :return:
    """

    conn = sqlite3.connect("D:\\Box Sync\\Python Projects\\Python-Specilization-U-Michigan\SQL lite\\emaildb.sqlite")

    cur = conn.cursor()

    try:
        cur.execute(''' DROP TABLE IF EXISTS Counts''')
    except:
        print("continue")

    cur.execute(''' CREATE TABLE Counts (org TEXT, count INTEGER)''')

    try:
        url = input("Enter the url: ")

        web_page = urlreq.urlopen(url).read()

    except:
        print("Enter a valid url")

    #print(web_page)

    web_page = web_page.decode('utf-8')


    #print (web_page)

    email_count = re.findall("From .*@(.\S+)", web_page)

    #print(email_count)

    """
    for line in (web_page):

        email = re.findall("From .* @(./S+)",line)

        print (email)

        if len(email) > 0:
            print (email)

            """

    for org in email_count:
        cur.execute(' SELECT count FROM Counts where org = ? ', (org,) )

        row = cur.fetchone()

        if row is None:
            cur.execute(''' INSERT INTO Counts (org,count) VALUES (?,1) ''', (org,))

        else:
            cur.execute('UPDATE Counts SET count = count + 1 where org = ?', (org,))

    conn.commit()

    sqlstr = cur.execute("SELECT org,count from Counts ORDER BY count DESC ")
    print("Counts:")
    for row in sqlstr:
        print(str(row[0]),str(row[1]))

    cur.close()