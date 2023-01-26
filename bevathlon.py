"""Simple Travelling Salesperson Problem (TSP) for BEVATHLON"""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

import requests
import json
import urllib.request
import urllib.parse
import pickle
import math
import copy


ADDRESSES = ['112-114 The Parade, Leamington Spa CV32 4AQ, Warwickshire, England', # depot
                       'The White Horse, Warwickshire, 4-6 Clarendon Ave, Leamington Spa CV32 5PZ',
                       '34 Clemens St, Leamington Spa CV31 2DN, Warwickshire, England',
                       'Fizzy Moon Brewhouse and Grill, 35 Regent St, Leamington Spa CV32 5EE, Warwickshire, England',
                       'The Drawing Board, 18 Newbold St, Leamington Spa CV32 4HN, Warwickshire, England',
                       'The Greyhound, 35, Kennedy Square, Leamington Spa CV32 4SY, Warwickshire, England',
                       'T Js Bar, 45-47 Bath St, Leamington Spa CV31 3AG, Warwickshire, England',
                       'The Clarendon, 44-46 Clarendon Ave, Leamington Spa CV32 4RZ',
                       'Tesco Express, 22-24 Parade, Leamington Spa CV32 4DN',
                       'Railway Inn, 12 Clemens St, Leamington Spa CV31 2DL, Warwickshire, England',
                       'The Old Library, 11 Bath St, Leamington Spa CV31 3AF, Warwickshire, England',
                       '41-43 Warwick St, Leamington Spa CV32 5JX',
                       'Hope Tavern, 2 Court St, Leamington Spa CV31 1NH, Warwickshire, England',
                       'Murphys Bar, 33 Regent St, Leamington Spa CV32 5EJ, Warwickshire, England',
                       'The star and garter, 4-6 Warwick St, Leamington Spa CV32 5LL, Warwickshire, England',
                       'Woodland Tavern, 3 Regent St, Leamington Spa CV32 5HW, Warwickshire, England',
                       'The Town House, 2 George St, Leamington Spa CV31 1ET, Warwickshire, England',
                       'Pig and Fiddle, 45 High St, Leamington Spa CV31 1LN, Warwickshire, England',
                       'The Bowling Green Inn, 18-20 New St, Leamington Spa CV31 1HP, Warwickshire, England',
                       'The White Horse, 4-6 Clarendon Ave, Leamington Spa CV32 5PZ, Warwickshire, England'
                      ]
PUBS_PER_DIRECTION_URL = 10 # Max is 10
API_KEY = 'ENTER API KEY' # https://developers.google.com/maps/documentation/distance-matrix/start#get-a-key


def create_data(ADDRESSES):
  """Creates the data."""
  data = {}
  ### TODO: ENTER API KEY
  data['API_key'] = ''
  data['addresses'] = ADDRESSES
  return data

def create_distance_matrix(data):
  addresses = data["addresses"]
  API_key = data["API_key"]
  # Distance Matrix API only accepts 100 elements per request, so get rows in multiple requests.
  max_elements = 100
  num_addresses = len(addresses) # 16 in this example.
  # Maximum number of rows that can be computed per request (6 in this example).
  max_rows = max_elements // num_addresses
  # num_addresses = q * max_rows + r (q = 2 and r = 4 in this example).
  q, r = divmod(num_addresses, max_rows)
  dest_addresses = addresses
  distance_matrix = []
  # Send q requests, returning max_rows rows per request.
  for i in range(q):
    origin_addresses = addresses[i * max_rows: (i + 1) * max_rows]
    response = send_request(origin_addresses, dest_addresses, API_key)
    distance_matrix += build_distance_matrix(response)

  # Get the remaining remaining r rows, if necessary.
  if r > 0:
    origin_addresses = addresses[q * max_rows: q * max_rows + r]
    response = send_request(origin_addresses, dest_addresses, API_key)
    distance_matrix += build_distance_matrix(response)
  return distance_matrix

def send_request(origin_addresses, dest_addresses, API_key):

  """ Build and send request for the given origin and destination addresses."""
  def build_address_str(addresses):
    # Build a pipe-separated string of addresses
    address_str = ''
    for i in range(len(addresses) - 1):
      address_str += addresses[i] + '|'
    address_str += addresses[-1]
    return address_str

  request = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric'
  origin_address_str = build_address_str(origin_addresses)
  dest_address_str = build_address_str(dest_addresses)
  request = request + '&origins=' + origin_address_str + '&destinations=' + \
                       dest_address_str + '&key=' + API_key
  jsonResult = urllib.request.urlopen(request).read()
  response = json.loads(jsonResult)
  return response



def build_distance_matrix(response):
  distance_matrix = []
  for row in response['rows']:
    row_list = [row['elements'][j]['distance']['value'] for j in range(len(row['elements']))]
    distance_matrix.append(row_list)
  return distance_matrix


def main_distance_matrix(ADDRESSES):
  """Entry point of the program"""
  # Create the data.
  data = create_data(ADDRESSES)
  addresses = data['addresses']
  for i in range(len(addresses)):
    addresses[i] = urllib.parse.quote_plus(addresses[i])


  API_key = data['API_key']
  distance_matrix_store = create_distance_matrix(data)
  print(distance_matrix_store)
  return distance_matrix_store





def create_data_model(distance_matrix_store):
    """Stores the data for the problem."""
    data = {}

    data['distance_matrix'] = distance_matrix_store
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {:.3f} kilometres'.format(solution.ObjectiveValue()/1000))
    index = routing.Start(0)
    plan_output = 'Route for vehicle 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Route distance: {}metres\n'.format(route_distance)


def main(distance_matrix_store):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(distance_matrix_store)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)
        # print(solution)

    routes = get_routes(solution, routing, manager)
    return(routes[0])

def get_routes(solution, routing, manager):
  """Get vehicle routes from a solution and store them in an array."""
  # Get vehicle routes and store them in a two dimensional array whose
  # i,j entry is the jth location visited by vehicle i along its route.
  routes = []
  for route_nbr in range(routing.vehicles()):
    index = routing.Start(route_nbr)
    route = [manager.IndexToNode(index)]
    while not routing.IsEnd(index):
      index = solution.Value(routing.NextVar(index))
      route.append(manager.IndexToNode(index))
    routes.append(route)
  return routes    


if __name__ == '__main__':

    y = input("Get distance matrix? y/n \n:")
    if y == 'y':
        ADDRESSES_copy = copy.deepcopy(ADDRESSES)
        # GET DISTANCE MATRIX
        distance_matrix_store = main_distance_matrix(ADDRESSES_copy)
        # print(distance_matrix_store)
        with open('data.pickle', 'wb') as f:
            pickle.dump(distance_matrix_store, f, pickle.HIGHEST_PROTOCOL)


    with open('data.pickle', 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
        distance_matrix_store = pickle.load(f)


    

    route = main(distance_matrix_store)
    print("Route Index:")
    print(str(route) + "\n")
    print("Addresses:")
    for i in range(len(ADDRESSES) + 1):
        print(str(i + 1) + ": " + ADDRESSES[route[i]])

    # Create Direction Maps:
    addresses_url = copy.deepcopy(ADDRESSES) 
    for i in range(len(addresses_url)):
      addresses_url[i] = urllib.parse.quote_plus(addresses_url[i])

    addresses_url_ordered = []
    for i in range(len(ADDRESSES) + 1):
      addresses_url_ordered.append(urllib.parse.quote_plus(addresses_url[route[i]]))

    # print("\nUrl Addresses")
    # for i in range(len(addresses_url_ordered)):
    #   print(str(i + 1) + ": " + addresses_url_ordered[i])
    
    input("\nPress Enter to see Google Map Directions:")
    
    links_num = math.ceil((len(addresses_url) + 1) / PUBS_PER_DIRECTION_URL)
    links = []
    for link_index in range(links_num):
      link_url = 'https://www.google.com/maps/dir/'
      for address_url in range(PUBS_PER_DIRECTION_URL):
        if ((address_url + link_index*PUBS_PER_DIRECTION_URL) == len(addresses_url_ordered)): 
          break
        link_url += addresses_url_ordered[address_url + link_index*PUBS_PER_DIRECTION_URL] + '/'
        
      links.append(link_url)
      print(link_url)
