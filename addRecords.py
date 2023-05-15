from sqlConnect import *
from time import sleep

def addRecords():
    tblFilms = []
    title = input("Enter Title: ")
    yearReleased = int(input("Enter Released Year: "))
    rating = input("Enter Rating: ")
    duration = int(input("Enter Duration: "))
    genre = input("Enter Genre: ")

    tblFilms.append(title)
    tblFilms.append(yearReleased)
    tblFilms.append(rating)
    tblFilms.append(duration)
    tblFilms.append(genre)

    cursor.execute("INSERT INTO tblfilms VALUES (NULL,?,?,?,?,?) ", tblFilms)
    conn.commit()
    print("Record added")

    sleep(2)
    cursor.execute("SELECT * FROM tblfilms ")
    row = cursor.fetchall()
    for records in row:
        print(records)




 #addRecords()