#from DAO import Dao
import wrapper


class Movies:
    def __init__(self, title, year, runtime, genre):

        self.title=title
        self.year=year
        self.runtime=runtime
        self.genre=genre
       
   
    def get_movie_obj(self):

        movie_dict={'title': self.title,
                    'year': self.year,
                    'runtime': self.runtime,
                    'genre': self.genre
                    }
        
        return movie_dict

        


class Actors:
    def __init__(self, actors_names):
        self.actors_names=actors_names

    
    def get_actors_object(self):
        actors_dict={'actors':self.actors_names}

        return actors_dict
        


class Directors:
    def __init__(self, director_names):
        self.director_names=director_names
        

    def get_director_obj(self):
        direc_dict={'direcor': self.director_names}

        return direc_dict
