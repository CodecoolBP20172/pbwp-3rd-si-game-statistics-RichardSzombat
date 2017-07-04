
# Report functions
def count_games(file_name):
    with open (file_name,"r") as game_stats:
        number = 0
        for line in game_stats:
            number += 1
        return number

def decide(file_name,year):
    import csv
    years = [x[2] for x in csv.reader(open(file_name,'r'),delimiter='\t')]
    for game in years :
        if str(game)==str(year):
            return True
    return False
    
def get_latest(file_name):
    import csv 
    titles = [x[0] for x in csv.reader(open(file_name,'r'),delimiter='\t')]
    years = [x[2] for x in csv.reader(open(file_name,'r'),delimiter='\t')]
    latest_game_index=int(years.index(max(years)))
    return titles[latest_game_index]









stat="game_stat.txt"
print(count_games(stat))
print (decide(stat,1997))
get_latest(stat)
