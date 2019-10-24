import mapquest_actions
import mapquest_api

def start_interface():
    locations = input_of_locations()
    location_from = locations[0]
    locations_to = locations[1:]

    num_actions = number_of_actions()
    list_of_actions = name_of_actions(num_actions)
    
    url = mapquest_api.build_url(location_from, mapquest_api.encode_locations(locations_to))
    json_result = mapquest_api.json_response(url)

    output_mapquest_actions(list_of_actions,json_result)

    print("\nDirection Provided by MapQuest API.\n")

def input_of_locations() -> [str]:
    '''
        This function takes in an integer as an input to indicate how
        many lines of input to provide next and appends them to a list
    '''
    list_of_locations = []
    while True:
        try:
            number_of_locations = int(input("Please enter the number of locations being traveled: "))
            if number_of_locations >= 2:
                location_from = input("Enter starting location: ")
                list_of_locations.append(location_from)
                for locations in range(number_of_locations - 1):
                    if (number_of_locations - 1) >= 2:
                        location_to = input("Enter the name of location " + str(locations+1) + " to travel to: ")
                    else:
                        location_to = input("Enter the name of the location being traveled to: ")
                    list_of_locations.append(location_to)
                return list_of_locations                
            else:
                print('\nPlease Enter An Integer Greater than 1')
    
        except:
            print('\nPlease Enter An Integer')
    

def number_of_actions() -> int:
    '''
        This function takes in an integer as an input to indicate how many
        lines of input to provide next and appends the lines(steps) to a list
    '''
    number_of_actions = 0
    while True:
        try:
            number_of_actions = int(input("Enter the number of actions to be provided: "))
            if number_of_actions >= 1:
                return number_of_actions
            else:
                print("\nPlease enter a number greater than 0")
        except: 
            print("\nPlease enter a number")
            
def name_of_actions(number_of_actions:int) -> [str]:
    list_of_actions = []
    while True:
        try:
            for action in range(number_of_actions):
                action_name = input("Enter the name of action " + str(action+1) + " [DIRECTIONS,DISTANCE,TIME,LONGITUDE]:").upper()
                if(action_name not in ["DIRECTIONS","DISTANCE","TIME","LONGITUDE"]):
                    raise Exception("\nPlease choose from one of the actions [DIRECTIONS,DISTANCE,TIME,LONGITUDE]")
                else:
                    list_of_actions.append(action_name)
            return list_of_actions
        except Exception as e: print(e) 

def output_mapquest_actions(actions:list, json_result:'json') -> str:
    '''
        This function takes in a list of characters and returns DIRECTIONS,
        TOTALDISTANCE, TOTALTIME and LATLONG if the character within the list
        matches any of the 4
    '''
    for action in actions:
        if action == 'DIRECTIONS':
            mapquest_actions.Directions(json_result).map_action()
            
        if action == 'DISTANCE':
            mapquest_actions.Distance(json_result).map_action()
        
        if action == 'TIME':
            mapquest_actions.Time(json_result).map_action()
            
        if action == 'LONGITUDE':
            mapquest_actions.Latlong(json_result).map_action()
        

if __name__ == '__main__':
    start_interface()

    
