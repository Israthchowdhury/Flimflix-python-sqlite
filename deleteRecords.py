from sqlConnect import *
import readRecords
from time import sleep


def deleteRecords():
    # filmID of the record to be deleted
    idField = input("Enter the filmID to be deleted : ")

    cursor.execute(f"DELETE FROM tblFilms WHERE filmID={idField}")
    conn.commit()
    print(f"filmID {idField} deleted from tblFilms table")  # return the deleted filmID

    sleep(3)
    readRecords.readRecords()  # call the readSongs methiod from the readData python file


# deleteFilms()  # call the deleteSongs
