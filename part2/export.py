import reports
# Export functions
stat = "game_stat.txt"

with open("export.txt", "w") as export_file:
    export_file.write(str(reports.get_most_played(stat)) + "\n")
    export_file.write(str(reports.sum_sold(stat)) + "\n")
    export_file.write(str(reports.get_selling_avg(stat)) + "\n")
    export_file.write(str(reports.count_longest_title(stat)) + "\n")
    export_file.write(str(reports.get_date_avg(stat)) + "\n")
    export_file.write(str(reports.get_game(stat, "Minecraft")) + "\n")
    export_file.write(str(reports.count_grouped_by_genre(stat)) + "\n")
    export_file.write(str(reports.get_date_ordered(stat)) + "\n")
