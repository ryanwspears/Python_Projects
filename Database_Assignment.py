# Imports the SQLite module
import sqlite3

# Connects to the Database 'files.db'
conn = sqlite3.connect('files.db')

with conn:
    curr = conn.cursor()
    # Creates a table called 'tblFiles' and adds 2 columns
    curr.execute('CREATE TABLE IF NOT EXISTS tblFiles(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                colFileName STRING)')
    # Commits the data to the database
    conn.commit()

conn = sqlite3.connect('files.db')

# Creates a multi-tuple with 7 entries
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Loops through the above tuple to find and display files with the .txt extension
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            curr = conn.cursor()
            curr.execute('INSERT INTO tblFiles (colFileName) VALUES (?)', (x,))
            print(x)

# Closes the database
conn.close()
