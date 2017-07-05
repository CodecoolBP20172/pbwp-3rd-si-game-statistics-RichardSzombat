import reports
# Printing functions
stat = "game_stat.txt"
print(reports.get_most_played(stat))
print(reports.sum_sold(stat))
print(reports.get_selling_avg(stat))
print(reports.count_longest_title(stat))
print(reports.get_date_avg(stat))
print(reports.get_game(stat, "Minecraft"))
print(reports.count_grouped_by_genre(stat))
print(reports.get_date_ordered(stat))
