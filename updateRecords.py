from sqlConnect import *
import readRecords
from time import sleep

def updateRecords():
    # FilmID of the record
    idRecordField = input("Enter ID to be updated: ")

    fieldRecord = input("Which field you want to update: (Title, yearReleased, Rating, Duration, Genre): ").title()

    # Enter the value for the field
    newFieldValue = input(f"Enter the new value for: {fieldRecord} ")
    print(f"The value entered is: {newFieldValue} ")

    newFieldValue = "'" + newFieldValue + "'"
    print(f" The value entered is:{newFieldValue} ")
    
    cursor.execute(f"UPDATE tblfilms SET {fieldRecord} = {newFieldValue} WHERE FilmID = {idRecordField}")
    conn.commit
    # return the updated FilmID
    print(f"Film Record {idRecordField} updated ")  

    sleep(2)
    readRecords.readRecords()
# updateRecord()