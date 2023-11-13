# Using the NBA_Player_Microsevice

This microservice provides a random, active NBA player's data using Flask and retrieved from an NBA API. 
Note: this microservice is intended to be run locally on a temporary, local URL. 

Required dependencies needed to run the microservice include: 
1. Python 3.7+
2. NBA API `pip install nba_api`
3. Requests `pip install requests`
4. Flask `pip install Flask`


## Requesting Data from the microservice
In order to make a request from the microservice, you will need to define a function in your main program to make an HTTP get request. In Python, that call could look like this: 
```
  import requests

  def get_random_player():
      url = "http://127.0.0.1:5000/player_data"
      response = requests.get(url)
  
      if response.status_code == 200:
          return response.json()
      else:
          print("Error:", response.status_code)
          return None

random_player = get_random_player()
```

**To request data from the microservice:**
1. start the Flask server by running microservice.py
2. Once the server is running, the `get_random_player()` function in the main program will now be able to call on the microservice to determine the requested data.


## Receiving Data from the microservice

When you call the `get_random_player()` function in the main program, the microservice handles the request and returns a JSON object with the random player's data in the following format:

```
{
    'id': player_id,
    'full_name': full_name,
    'first_name': first_name,
    'last_name': last_name,
    'is_active': True or False
}
```
This object can then be used as the user sees fit to search the NBA API for additional information on the player using the player ID or name. 

## UML Sequence Diagram 
![image](https://github.com/Brandie-M/NBA_Player_Microsevice/assets/103692387/d7c6714c-7139-4fac-985e-79a6bb7b9a36)

