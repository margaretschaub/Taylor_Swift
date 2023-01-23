from cleaning import *
import sqlite3

conn = sqlite3.connect('TaylorSwift.db')
cur = conn.cursor()


def parse_file(file_location):
    desired_list = []
    with open(file_location, "r") as x:
        lines = x.readlines()
        for line in lines:
            raw_column_values = line.split(",")
            # now we have the columns and can clean them up
            row_list = []
            for y in raw_column_values:
                row_list.append(y.strip())

            desired_list.append(row_list)
    return desired_list


setlist = parse_file('/Users/margaretschaub/Desktop/test_clean.csv')
print(setlist)

for each in setlist:
    counter = each[0]
    r = clean_to_int(counter)   # returns r
    song = each[1]
    t = track_clean(song)   # returns t
    special = each[2]
    s = special_clean(special)  # returns s
    date = each[3]
    new_format = convert_date(date)  # returns new_format
    performance_list = each[4]
    new_list = location_clean(performance_list)  # return new_list
    for item in new_list:
        if len(performance_list) == 4:
            venue = item[0]
            city = item[1]
            state = item[2]
            country = item[3]
        elif len(performance_list) == 3:
            venue = item[0]
            city = item[1]
            country = item[2]
            state = ''

    a = f"INSERT OR IGNORE INTO set_list (concert, order_played, song) VALUES('{concert_id}','{r}','{song_id}')"
    b = f"INSERT OR IGNORE INTO special (song, details) VALUES('{song_id}','{s})"
    c = f"INSERT OR IGNORE INTO performances (date, venue, city, state, country) VALUES('{new_format}','{venue}'," \
        f"'{city}','{state}','{country}')"
    d = f"INSERT OR IGNORE INTO songs (song) VALUES ('{t}')"
    e = f'select id from songs where song = "{t}" COLLATE NOCASE'
    f = f'select id from performances where venue = "{venue}" and date = "{new_format} COLLATE NOCASE'

    res1 = cur.execute(e)
    song_id = res1.fetchone()

    if song_id is None:
        create_new_song = cur.execute(d)
        conn.commit()
        res1 = cur.execute(e)
        song_id = res1.fetchone()

    res2 = cur.execute(f)
    concert_id = res2.fetchone()
    if concert_id is None:
        create_new_concert = cur.execute(c)
        conn.commit()
        res2 = cur.execute(f)
        concert_id = res2.fetchone()

    insert_set_list = cur.execute(a)
    insert_special = cur. execute(b)
    conn.commit()
