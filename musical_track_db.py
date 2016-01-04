import xml.etree.ElementTree as ET

import sqlite3

def musical_track_load():
    """
    This function parses XML itunes data and stores the track information into sqlite.
    :return:
    """

    conn  = sqlite3.connect(
        "D:\\Box Sync\\Python Projects\\Python-Specilization-U-Michigan\\SQL lite\\musical_track_db.sqlite")

    cur = conn.cursor()

    cur.executescript('''

        DROP TABLE IF EXISTS Artist;
        DROP TABLE IF EXISTS Album;
        DROP TABLE IF EXISTS Track;

        CREATE TABLE Artist (

            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,

            name    TEXT UNIQUE

            );

        CREATE TABLE Album (

            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,

            artist_id  INTEGER,

            title   TEXT UNIQUE

            );

        CREATE TABLE Track (

            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,

            title TEXT  UNIQUE,

            album_id  INTEGER,

            len INTEGER, rating INTEGER, count INTEGER

             );

        ''')

    try:
        xml_file = input("What is your music XML file path?: ")

        if len(xml_file) > 1: print("file loaded")

    except:
        print("Please enter a valid file")

    music_tree = ET.parse(xml_file)

    return music_tree

    # lets look for the keys

    # <key>Track ID</key><integer>369</integer>
    # <key>Name</key><string>Another One Bites The Dust</string>
    # <key>Artist</key><string>Queen</string>

def look_up(entry,key):
    """
    This function finds the values of the keys from the XML tree node entry
    :param entry:
    :param key:
    :return:
    """
    found = False

    for child in entry:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True

    return None


def musical_track():
    """
    This fucntion to actual process and store the music track
    :return:
    """

    file = musical_track_load()

    all_nodes = file.findall('/dict/dict/dict')

    print('Dict count:', len(all_nodes))

    for nodes in all_nodes:
        if (look_up(nodes,'Track ID') is None): continue

        song_title = lookup(nodes, 'Name')

        artist = lookup(nodes, 'Artist')

        album = lookup(nodes, 'Album')

        count = lookup(nodes, 'Play Count')

        rating = lookup(nodes, 'Rating')

        length = lookup(nodes, 'Total Time')

        if title is None or artist is None or album is None:
            continue

        print(title,artist,album,count,rating,length)

    conn = sqlite3.connect(
        "D:\\Box Sync\\Python Projects\\Python-Specilization-U-Michigan\\SQL lite\\musical_track_db.sqlite")

    cur = conn.cursor()

    cur.execute(''' INSERT OR IGNORE INTO Artist (name) VALUES (?) ''', (artist,))

    cur.execute(''' SELECT id FROM Artist WHERE Artist.name = ?''', (artist,))

    artist_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?,?)''',(artist_id,album))

    cur.execute(''' SELECT id FROM Album WHERE title = ?''',(album))

    album_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR IGNORE INTO Track(title, album_id , len, rating, count) VALUES

                (?,?,?,?,?)''',(song_title, album_id, length, rating, count))

    conn.commit()








