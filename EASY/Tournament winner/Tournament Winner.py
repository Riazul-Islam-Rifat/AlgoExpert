def tournamentWinner(competitions, results):
    current_best_team = ''
    winner_tracker = {current_best_team:0}

    for item in range(len(results)):
        if results[item]==0:
            winner = competitions[item][1]
        else:
            winner = competitions[item][0]

        if winner not in winner_tracker:
            winner_tracker[winner]=3
        else:
            winner_tracker[winner]+=3

        if winner_tracker[winner]>winner_tracker[current_best_team]:
            current_best_team=winner

    return current_best_team
