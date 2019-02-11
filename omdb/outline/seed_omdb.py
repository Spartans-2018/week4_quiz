import sqlite3
db='omdb1.db'
conn=sqlite3.connect(db)

conn.execute("DROP TABLE IF EXISTS movies")
conn.execute("DROP TABLE IF EXISTS actors")
conn.execute("DROP TABLE IF EXISTS directors")
conn.execute("DROP TABLE IF EXISTS movies_actors")
conn.execute("DROP TABLE IF EXISTS movies_directors")



conn.execute("""CREATE TABLE IF NOT EXISTS movies
                (movie_id INTEGER PRIMARY KEY,
                title VARCHAR,
                year VARCHAR,
                runtime VARCHAR,
                genre VARCHAR);
                """)
conn.execute("""CREATE TABLE IF NOT EXISTS actors
                (actor_id INTEGER PRIMARY KEY,
                first_name VARCHAR,
                last_name VARCHAR);
                """)

conn.execute("""CREATE TABLE IF NOT EXISTS directors
                (director_id INTEGER PRIMARY KEY,
                first_name VARCHAR,
                last_name VARCHAR)
                """)


conn.execute("""CREATE TABLE IF NOT EXISTS movies_actors
                (actor_id INTEGER,
                movie_id INTEGER,
                FOREIGN KEY(actor_id) REFERENCES actors(actor_id),
                FOREIGN KEY(movie_id) REFERENCES movies(movie_id))
                """)


conn.execute("""CREATE TABLE IF NOT EXISTS movies_directors
                (director_id INTEGER,
                movie_id INTEGER,
                FOREIGN KEY(director_id) REFERENCES directors(director_id),
                FOREIGN KEY(movie_id) REFERENCES movies(movie_id))
                """)




conn.commit()
conn.close()