import reports
# Export functions
stat="game_stat.txt"

with open("export.txt","w") as export_file:
    export_file.write(str(reports.count_games(stat))+"\n")
    export_file.write(str(reports.decide(stat,1997))+"\n")
    export_file.write(str(reports.get_latest(stat))+"\n")
    export_file.write(str(reports.count_by_genre(stat,"First-person shooter"))+"\n")
    export_file.write(str(reports.get_line_number_by_title(stat,"World of Warcraft"))+"\n")
    export_file.write(str(reports.sort_abc(stat))+"\n")
    export_file.write(str(reports.get_genres(stat))+"\n")
    export_file.write(str(reports.when_was_top_sold_fps(stat))+"\n")
    