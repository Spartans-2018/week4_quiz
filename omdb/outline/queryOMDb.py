from wrapper import Movie_req
import requests
M=Movie_req()

class Query:

    def __init__(self):
        pass


    @staticmethod
    def search(search_name):
        
        url=M.lookup_url()
        response=requests.get(url.format(search_name))
        lookup_dict=response.json()
        return lookup_dict

#Query().search('rambo')