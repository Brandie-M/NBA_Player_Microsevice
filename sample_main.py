import requests


def get_random_player():
    url = "http://127.0.0.1:5000/player_data"
    response = requests.get(url)

    if response.status_code == 200:
        # print for testing only.
        # print("Response Received. Random Player Dictionary Returned.")
        return response.json()
    else:
        print("Error:", response.status_code)
        return None



####################################
### Test                         ###
####################################
# random_player = get_random_player()
# if random_player:
#     print(random_player)
####################################