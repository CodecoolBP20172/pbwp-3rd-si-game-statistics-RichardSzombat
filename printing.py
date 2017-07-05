import reports

stat = "game_stat.txt"
print(reports.count_games(stat))
print(reports.decide(stat, 1997))
print(reports.get_latest(stat))
print(reports.count_by_genre(stat, "First-person shooter"))
print(reports.get_line_number_by_title(stat, "World of Warcraft"))
print(reports.sort_abc(stat))
print(reports.get_genres(stat))
print(reports.when_was_top_sold_fps(stat))
