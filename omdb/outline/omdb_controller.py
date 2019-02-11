#import app
from models import Movies, Actors, Directors
import sqlite3
from flask import Flask, jsonify
from DAO import Dao


class Controller:
    def __init__(self):
        pass

    @staticmethod
    def get_connection():
        conn = sqlite3.connect ("omdb1.db")
        return conn 

    def search_db(self, movie):
        conn=Controller.get_connection()
        c=conn.cursor()
      
        sql="SELECT * FROM movies WHERE title LIKE  (?)"
        movie_cur=c.execute(sql, ('%'+movie+'%',))
        md=movie_cur.fetchone()
        
        movie_id=str(md[0])
        title=md[1]
        year=md[2]
        runtime=md[3]
        genre=md[4]
        movie_dict= Movies(title, year, runtime, genre).get_movie_obj()
        #self.search_actor_db(movie_id)
        sql1="SELECT * FROM movies_actors WHERE movie_id=?;"
        actor_cur=c.execute(sql1, (movie_id,))
        ad=actor_cur.fetchall()
        actors_list=[]
        for pair in ad:
            actors_list.append(str(pair[0]))

        sql2="SELECT * FROM actors WHERE actor_id=(?);"
        actors_names=[]
        for actor in actors_list:
            v=c.execute(sql2, (actor,))
            row1=v.fetchone()[1:]
            actors_names.append(row1)
        actors_dict=Actors(actors_names).get_actors_object()

        sql3="SELECT * FROM movies_directors WHERE movie_id=?;"
        direct_cur=c.execute(sql3, (movie_id,))
        dd=direct_cur.fetchone()
        dir_id=str (dd[0])
        sql4="SELECT * FROM directors WHERE director_id=(?);"
        dir_id_cur=c.execute(sql4, (dir_id,))
        direct_names=dir_id_cur.fetchone()[1:]
        director_dict=Directors(direct_names).get_director_obj()
        conn.close()


        return movie_dict, actors_dict, director_dict

    # def search_actor_db(self, movie_id):
    #     conn=Controller.get_connection()
    #     c=conn.cursor()
    #     sql1="SELECT * FROM movies_actors WHERE movie_id=?;"
    #     actor_cur=c.execute(sql1, movie_id)
    #     ad=actor_cur.fetchall()
    #     actors_list=[]
    #     for pair in ad:
    #         actors_list.append(pair[0])

    #     sql3="SELECT * FROM actors WHERE actor_id=(?);"
    #     actors_names=[]
    #     for actor in actors_list:
    #         v=c.execute(sql3, actor)
    #         row1=v.fetchone()[1:]
    #         actors_names.append(row1)
    #     actors_dict=Actors(actors_names).get_actors_object()
        
    #     return actors_dict


    def handle_api_data(self, movie_dict):
        title= movie_dict['Title']
        year=movie_dict['Year']
        runtime= movie_dict['Runtime']
        genre= movie_dict['Genre']
        Dao.save_movie(title, year, runtime, genre)


    def handle_director(self, movie_dict):
        if movie_dict["Director"]!='N/A':
            direct_list=movie_dict['Director'].split()
            first_name=direct_list[0]
            last_name=direct_list[1]
            

        else:
            first_name="N/A"
            last_name="N/A"

        Dao.save_directors(first_name, last_name)

    def handle_actors(self, movie_dict):

        if movie_dict["Actors"]!='N/A':
            actors_list=movie_dict["Actors"].split(',')
            for actor in actors_list:
                first_name=actor.split()[0]
                last_name=actor.split()[1]
                Dao.save_actor(first_name, last_name)
        else:
            first_name='N/A'
            last_name='N/A'
            Dao.save_actor(first_name, last_name)

    def handle_movies_actors(self, movie_dict):
        conn=Controller.get_connection()
        c=conn.cursor()
        sql="SELECT movie_id FROM movies WHERE title= ?"
        sql1="SELECT actor_id FROM actors WHERE first_name= ? AND last_name=?"
        title= movie_dict['Title']
        movie_cur= c.execute(sql, (title,))
        movie_id=movie_cur.fetchone()[0]
        c.close()
        if movie_dict["Actors"]!='N/A':
            
            actors_list=movie_dict["Actors"].split(',')
            for actor in actors_list:
                conn=Controller.get_connection()
                c=conn.cursor()
                first_name=actor.split()[0]
                last_name=actor.split()[1]
                
                actor_cur=c.execute(sql1, (first_name, last_name))
                actor_id=actor_cur.fetchone()[0]
                c.close()
                Dao.save_actors_movies(str(actor_id), str(movie_id))

    def handle_movies_directors(self, movie_dict):

        conn=Controller.get_connection()
        c=conn.cursor()
        sql="SELECT movie_id FROM movies WHERE title= ?"
        sql1="SELECT director_id FROM directors WHERE first_name= ? AND last_name=?"
        title= movie_dict['Title']
        movie_cur= c.execute(sql, (title,))
        movie_id=movie_cur.fetchone()[0]
        c.close()
        if movie_dict["Director"]!='N/A':
            conn=Controller.get_connection()
            c=conn.cursor()
            direct_list=movie_dict['Director'].split()
            first_name=direct_list[0]
            last_name=direct_list[1]
                
            direct_cur=c.execute(sql1, (first_name, last_name))
            director_id=direct_cur.fetchone()[0]
            c.close()
            Dao.save_directors_movies(str(director_id), str(movie_id))





    @staticmethod
    def test_func():
        return "Welcome"








