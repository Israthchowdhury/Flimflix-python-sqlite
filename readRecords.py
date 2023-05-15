from sqlConnect import *


def readRecords():
    # Retrieve the inserted record
    cursor.execute("SELECT * FROM tblFilms")  # select all items
    row = cursor.fetchall()  # fetch all records that was selected above
    # iterate and print all the records held in the row variable
    for record in row:
        print(record)


# readFilms()  # call he subroutine