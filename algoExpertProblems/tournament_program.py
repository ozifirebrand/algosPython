def tournament_game(competitions, results):
    away_player_index = 1
    home_player_index = 0
    additional_point = 3
    max_value = 0
    max_key = ""
    points = 0
    players_dict = {}
    for index in range(len(competitions)):
        score_per_round = results[index]
        players_per_round = competitions[index]

        if score_per_round == 0:
            player = players_per_round[away_player_index]
            points = players_dict[player]
            players_dict[player] = points + additional_point
        if score_per_round == 1:
            player = players_per_round[home_player_index]
            points = players_dict[player]
            players_dict[player] = points + additional_point

        for key in players_dict.keys():
            if players_dict[key] > max_value:
                max_value = players_dict[key]
                max_key = key
        return max_key