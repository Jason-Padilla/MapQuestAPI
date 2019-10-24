class Directions:
    def __init__(self, json):
        self._json = json

    def map_action(self):
        '''
            This takes in a json response and returns only the directions
            for the route
        '''
        print('\nDIRECTIONS:')
    
        for location in self._json['route']['legs']:
            print("")
            for direction in location['maneuvers']:
                print("   ",direction['narrative'])

class Distance:
    def __init__(self, json):
        self._json = json

    def map_action(self):
        '''
            This takes in a json rsponse and returns only the total
            distance of the route in miles
        '''
        miles = int(self._json['route']['distance'])
        print('\nTOTAL DISTANCE: ' + str(miles) + ' miles')
            
class Time:
    def __init__(self, json):
        self._json = json

    def map_action(self):
        '''
            This takes in a json response and returns only the total time
            of the route in minutes
        '''
        time = int(self._json['route']['time'])
        print('\nTOTAL TIME: ' + str(round(time/60)) + ' minutes')
   
        
class Latlong:
    def __init__(self, json):
        self._json = json

    def map_action(self):
        '''
            This takes in a json response and returns the latitude and the
            the longitude with their corresponding N,S,W, or E
        '''

        print("\nLATITUDE/LONGITUDE:\n")
        for location in self._json['route']['locations']:
            latitude = (location['latLng']['lat'])
            if latitude > 0:
                n = '{0:.2f}'.format(latitude)
                n = str(n)
                print("   " + location['adminArea5'] + ": " + n + 'N', end = ' ')
            else:
                latitude = latitude * -1
                s = '{0:.2f}'.format(latitude)
                s = str(s)
                print("   " + location['adminArea5'] + ": " + 'S',end = ' ')
                
            longitude = (location['latLng']['lng'])    
            if longitude > 0:
                e = '{0:.2f}'.format(longitude)
                e = str(e)
                print(e + 'E',end = '\n')
            else:
                longitude = longitude * -1
                w = '{0:.2f}'.format(longitude)
                w = str(w)
                print(w + 'W',end = '\n')
                   
