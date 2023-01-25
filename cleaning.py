from datetime import datetime


def clean_to_int(r):
    try:
        r = int(r)
        return r
    except ValueError:
        raise Exception(f"The value {r} is not valid. It must be an int")


def convert_date(d):
    try:
        date_time_str = datetime.strptime(d, "%B %d, %Y ")
        new_format = date_time_str.strftime("%Y-%m-%d")
        return new_format
    except ValueError:
        raise Exception(f"Date entry error {d} is not valid.")


def track_clean(track):
    t = track.strip()
    return t


def special_clean(special):
    s = special.replace("(", "")
    s1 = s.replace(")", "")
    s2 = s1.lower().strip()
    return s2


def location_clean(location):
    l = location.split(',')
    new_l = []
    for each in l:
        each = each.strip()
        new_l.append(each)
    return new_l

