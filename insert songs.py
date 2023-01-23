import sqlite3
conn = sqlite3.connect('TaylorSwift.db')
cur = conn.cursor()


def parse_file(file_location):
    desired_list = []
    with open(file_location, "r") as f:
        lines = f.readlines()
        for line in lines:
            raw_column_values = line.split(",")
            # now we have the columns and can clean them up
            row_list = []
            for c in raw_column_values:
                row_list.append(c.strip())

            desired_list.append(row_list)
    return desired_list


a = parse_file("/Users/margaretschaub/Desktop/TS_songs.csv")


def convert_integers(name_of_list, index_value):
    for each in name_of_list:
        try:
            each[index_value] = int(each[index_value])
        except ValueError:
            print(f"Entry error at {each[1]}")


convert_integers(a, 3)


def create_list_of_tuples(nested_list):
    list_of_tuples = []
    for item in nested_list:
        list_of_tuples.append(tuple(item))
    return list_of_tuples


final_list = create_list_of_tuples(a)

cur.executemany("INSERT INTO songs (song, album, release_date, track_id) VALUES(?,?,?,?);", final_list)
conn.commit()

