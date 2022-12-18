from cs50 import SQL


# Open favorites.db using SQLite tech
db = SQL('sqlite:///favorites.db')
fav = input('Fav prob: ')

# do NOT use f-strings as placeholders because of SQL-injections
rows = db.execute('SELECT COUNT(*) AS n FROM favorites WHERE problem = ?', fav)
print(rows[0]['n'])