# create wrapper class to access OMDb API
import requests

class Movie_req:

    def __init__(self):
        pass


    @staticmethod   
    def lookup_url():
        url="http://www.omdbapi.com/?t={}&apikey=5bbcc2a3"
        return url

