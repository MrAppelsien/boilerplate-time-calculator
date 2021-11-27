import re


def heeft_geen_dag(how_much_day, new_hour, new_min, am_pm):
    if how_much_day > 1:
        new_time = f'{new_hour}:{new_min:02} {am_pm} ({how_much_day} days later)'
    elif how_much_day == 1:
        new_time = f'{new_hour}:{new_min:02} {am_pm} (next day)'
    else:
        new_time = f'{new_hour}:{new_min:02} {am_pm}'
    return new_time


def heeft_dag(how_much_day, new_hour, new_min, am_pm, day):
    if how_much_day > 1:
        new_time = f'{new_hour}:{new_min:02} {am_pm}, {day} ({how_much_day} days later)'
    elif how_much_day == 1:
        new_time = f'{new_hour}:{new_min:02} {am_pm}, {day} (next day)'
    else:
        new_time = f'{new_hour}:{new_min:02} {am_pm}, {day}'
    return new_time


def add_time(start, duration, day=None):
    start_hours, start_min, am_pm = re.match(r'(\d+):(\d+) (AM|PM)',start, flags=re.IGNORECASE).groups()
    duration_hours, duration_min = duration.split(":")
    new_min = int(start_min) + int(duration_min)
    new_hour = int(start_hours) + int(duration_hours)

    new_hour += new_min // 60
    new_min %= 60
    how_much_day = new_hour // 24
    new_hour %= 24

    name_of_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


    if am_pm == "PM":
        if new_hour > 12:
            new_hour %= 12
            how_much_day += 1
            am_pm = "AM"
        if new_hour == 12:
            how_much_day += 1
            am_pm = "AM"

    elif am_pm == "AM":
        if new_hour > 12:
            new_hour %= 12
            am_pm = "PM"
        if new_hour == 12:
            am_pm = "PM"

    if day:
        day = day.title()
        welke_dag = name_of_day[name_of_day.index(day) + how_much_day]
    if day == None:
        new_time = heeft_geen_dag(how_much_day, new_hour, new_min, am_pm)
    else:
        new_time = heeft_dag(how_much_day, new_hour, new_min, am_pm, welke_dag)

    print(new_time)
    return new_time


def test_do():
    assert add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)"
    assert add_time("3:00 PM", "3:10") == "6:10 PM"
    assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday"
    assert add_time("11:43 AM", "00:20") == "12:03 PM"
    assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)"
    assert add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)"