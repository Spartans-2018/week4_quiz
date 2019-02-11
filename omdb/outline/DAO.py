import sqlite3



class Dao:
   
    def __init__(self):
       pass

    @staticmethod
    def get_connection():
        conn = sqlite3.connect ("omdb1.db")
        return conn   

    @staticmethod
    def save_movie(title, year, runtime, genre):
        conn=Dao.get_connection()

        sql="INSERT INTO movies(title, year, runtime, genre) VALUES (?,?,?,?)"
        conn.execute(sql, (title, year, runtime, genre))
        conn.commit()
        conn.close()
        
        


    @staticmethod
    def save_actor(first_name, last_name):
        conn=Dao.get_connection()
        sql="INSERT INTO actors(first_name, last_name) VALUES (?,?)"
        conn.execute(sql, (first_name, last_name))
        conn.commit()
        conn.close()

    @staticmethod
    def save_directors(first_name, last_name):
        conn=Dao.get_connection()
        sql="INSERT INTO directors(first_name, last_name) VALUES (?,?)"
        conn.execute(sql, (first_name, last_name))
        conn.commit()
        conn.close()

    @staticmethod
    def save_actors_movies(actor_id, movie_id):
        conn=Dao.get_connection() 
        sql='INSERT INTO movies_actors (actor_id, movie_id) VALUES (?,?)'
        conn.execute(sql, (actor_id, movie_id))
        conn.commit()
        conn.close()
        

    @staticmethod
    def save_directors_movies(director_id, movie_id):
        conn=Dao.get_connection()
        sql='INSERT INTO movies_directors (director_id, movie_id) VALUES (?,?)'
        conn.execute(sql, (director_id, movie_id))
        conn.commit()
        conn.close()