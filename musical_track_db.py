import xml.etree.ElementTree as ET

import sqlite3

def musical_track_load():
    """
    This function parses XML itunes data and stores the track information into sqlite.
    :return:
    """

    conn  = sqlite3.connect(
        "musical_track_db.sqlite")

    cur = conn.cursor()

    try:

        cur.executescript('''

            DROP TABLE IF EXISTS Artist;
            DROP TABLE IF EXISTS Album;
            DROP TABLE IF EXISTS Track;

            CREATE TABLE Artist (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name    TEXT UNIQUE
            );

            CREATE TABLE Genre (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name    TEXT UNIQUE
            );

            CREATE TABLE Album (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            artist_id  INTEGER,
            title   TEXT UNIQUE
            );

            CREATE TABLE Track (
            id  INTEGER NOT NULL PRIMARY KEY
            AUTOINCREMENT UNIQUE,
            title TEXT  UNIQUE,
            album_id  INTEGER,
            genre_id  INTEGER,
            len INTEGER, rating INTEGER, count INTEGER
            );

            ''')

        print('table created')

    except:
        print("continue")

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

        song_title = look_up(nodes, 'Name')

        artist = look_up(nodes, 'Artist')

        album = look_up(nodes, 'Album')

        count = look_up(nodes, 'Play Count')

        rating = look_up(nodes, 'Rating')

        length = look_up(nodes, 'Total Time')

        genre = look_up(nodes, 'Genre')

        if song_title is None or artist is None or album is None:
            continue

        #print(song_title,artist,album,count,rating,length)

        conn = sqlite3.connect(
            "musical_track_db.sqlite")

        cur = conn.cursor()

        #print(artist)

        cur.execute(''' INSERT OR IGNORE INTO Artist (name) VALUES (?) ''', (artist,))

        cur.execute(' SELECT id FROM Artist WHERE name = ?', (artist,))

        #conn.commit()

        artist_id = cur.fetchone()[0]

        #print(artist_id)

        cur.execute(''' INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?,?)''',(artist_id,album))

        cur.execute(' SELECT id FROM Album WHERE title = ?',(album,))

        album_id = cur.fetchone()[0]

        cur.execute(''' INSERT OR IGNORE INTO Genre (name) VALUES (?)''',(genre))

        print(genre)

        cur.execute(''' SELECT id FROM Genre WHERE name =?''',(genre))

        genre_id = cur.fetchone()[0]

        cur.execute(''' INSERT OR IGNORE INTO Track(title, album_id ,genre_id, len, rating, count) VALUES

                    (?,?,?,?,?,?)''',(song_title, album_id, genre_id,length, rating, count))

        conn.commit()

    conn.close()

musical_track = musical_track()


D:\\Box Sync\\Python Projects\\Python-Specilization-U-Michigan\\data\\tracks\tracks\\Library.xml




