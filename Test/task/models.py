import sqlite3 as sq


with sq.connect("Profile.db") as con:
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Cookie_Profile(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        created_at TIMESTAMP NOT NULL,
        cookie TEXT,
        launch_date TIMESTAMP, 
        launch_count INTEGER DEFAULT 0
    );""")
