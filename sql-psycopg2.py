import psycopg2


# connect to "chinook" DB
connection = psycopg2.connect(database="chinook")

# build a cursor object of the DB
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" colum  from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 5 - Select only albums with artistid of 51
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Tracks where the composer is Queen from the track table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 albums by kiss
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Kiss"])

# fetch the results (multiple)
results = cursor.fetchall()

# close the connection once results have been fetched
connection.close()

# print results
for result in results:
    print(result)
