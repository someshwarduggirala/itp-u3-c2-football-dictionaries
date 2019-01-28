def players_as_dictionaries(squads_list):
    squads_list_dict=[]
    for player in squads_list:
        player_dict={ 'number': player[0],
                     'position': player[1],
                     'name': player[2],
                     'date_of_birth': player[3],
                     'caps': player[4],
                     'club': player[5],
                     'country': player[6],
                     'club_country': player[7],
                     'year': player[8],
                    }
        squads_list_dict.append(player_dict)
    return squads_list_dict
