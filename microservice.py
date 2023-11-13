import random
from flask import Flask
from nba_api.stats.library.data import players
from nba_api.stats.library.data import (
    player_index_id,
    player_index_full_name,
    player_index_first_name,
    player_index_last_name,
    player_index_is_active,
)


def _get_player_dict(player_row):
    return {
        "id": player_row[player_index_id],
        "full_name": player_row[player_index_full_name],
        "first_name": player_row[player_index_first_name],
        "last_name": player_row[player_index_last_name],
        "is_active": player_row[player_index_is_active],
    }


def get_active_players():
    players_list = []
    for player in players:
        if player[player_index_is_active]:
            players_list.append(_get_player_dict(player))
    return players_list


def determine_random_player():
    active_players = get_active_players()
    random_number = random.randrange(len(active_players))
    random_player = active_players[random_number]
    return random_player


app = Flask(__name__)


@app.route('/player_data', methods=['GET'])

def return_player_data():
    # print for testing only
    # print("Request received, sending response.")
    return determine_random_player()


if __name__ == "__main__":
    app.run(port=5000)
