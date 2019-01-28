def players_by_country_and_position(squads_list):
    squads_dict_by_cntry_position={}
    for player in squads_list:
        country=player[6]
        position=player[1]
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
        squads_dict_by_cntry_position.setdefault(country,{})
        squads_dict_by_cntry_position[country].setdefault(position,[])
        squads_dict_by_cntry_position[country][position].append(player_dict)
        
    return squads_dict_by_cntry_position
