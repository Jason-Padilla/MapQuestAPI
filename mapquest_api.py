#  Jason Padilla 20502573.  ICS 32 Lab.  Project #3

import json
import urllib.parse
import urllib.request

API_KEY = 'Fmjtd%7Cluu821ub21%2C7l%3Do5-94aagw'

BASE_URL = 'http://www.mapquestapi.com/directions/v2/route?key=' 

def encode_locations(locations_to: list):
    '''
        This takes a list and encodes all the characters inside the list
        and puts them into a new list. Then all the characters in the list
        get added up
    '''
    encoded_list =[]
    for location in locations_to:
        query_parameters = [('to', location)]
        encoded ='&' + urllib.parse.urlencode(query_parameters)
        encoded_list.append(encoded)
    encoded_result = ''.join(encoded_list)
    return encoded_result 

def build_url(location_from: list, encoded_locations_to: list) -> str:
    '''
        This takes two lists, one that indicates from and the other that
        indicates to, and encodes the first one. This then returns a URL that
        can be used to access the directions from and to 
    '''

    query_parameters = [('from', location_from)]
    complete_url = BASE_URL + API_KEY +'&'+ urllib.parse.urlencode(query_parameters) + encoded_locations_to
    return complete_url


def json_response(url: str) -> 'json':
    ''' This takes a built url and returns the json response'''
    
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()


    