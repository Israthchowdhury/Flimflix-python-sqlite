from sqlConnect import *

def searchYear():
    filmflix = int(input("Enter a year to search for: "))
    cursor.execute(
        'select * from tblfilms where yearReleased='+"'"+str(filmflix)+"'")
    row = cursor.fetchall()
    for yearRecord in row:
        print(yearRecord)
# searchYear()