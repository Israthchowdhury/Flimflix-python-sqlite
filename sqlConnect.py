import sqlite3  # import the SQLite Library

"create a conn variable and pass sqlite connect method to it"
"creeate dbb if it doesn't exist, if it does use it "
# conn = sqlite3.connect("folderpath/folderpath/folderpath/fileName.dbExtension")
conn = sqlite3.connect("flimFlix.db")
# cursor method ierate through database/tables
cursor = conn.cursor()
