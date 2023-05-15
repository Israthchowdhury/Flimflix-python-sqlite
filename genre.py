from sqlConnect import *

def searchGenre():
    filmflix = input("Enter a genre to search for: ").strip()
    cursor.execute('SELECT * FROM tblfilms WHERE Genre='+"'"+filmflix+"'")
    row = cursor.fetchall()
    for genreRecord in row:
        print(genreRecord)

# searchGenre()