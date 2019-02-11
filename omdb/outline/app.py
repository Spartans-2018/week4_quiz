
from models import Movies, Actors, Directors

from queryOMDb import Query

from omdb_controller import Controller

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# example code in README
@app.route('/search-movie/<movie>/<search_type>', methods=['GET', 'POST'])
def search_movie(movie, search_type):
    
    if search_type=='1':
        '''
        Call on the models to retreive the movie title from db
        '''
        movie_dict=Controller().search_db(movie)
        
        
        movie_title=jsonify(Movie=movie_dict)
        return movie_title


    elif search_type=='2':
        '''
        Call on queryOMDb to search for the movie title on OMDb API
        '''
        movie_dict=Query().search(movie)
        Controller().handle_api_data(movie_dict)
        Controller().handle_actors(movie_dict)
        Controller().handle_director(movie_dict)
        Controller().handle_movies_actors(movie_dict)
        Controller().handle_movies_directors(movie_dict)
        movie_data=jsonify(movie_dict)
        return movie_data
    else:
        response = jsonify(error="choose 1 or 2 as search type")
        response.status_code = 404
        return response



if __name__ == "__main__":
    app.run(debug=True)