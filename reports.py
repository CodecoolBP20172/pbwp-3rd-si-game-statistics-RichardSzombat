import csv


# Report functions
def count_games(file_name):
    with open (file_name,"r") as game_stats:
        number = 0
        for line in game_stats:
            number += 1
        return number

def decide(file_name,year):
    years = [x[2] for x in csv.reader(open(file_name,'r'),delimiter='\t')]
    for game in years :
        if str(game)==str(year):
            return True
    return False
    
def get_latest(file_name):
    titles = [x[0] for x in csv.reader(open(file_name,'r'),delimiter='\t')]
    years = [x[2] for x in csv.reader(open(file_name,'r'),delimiter='\t')]
    latest_game_index=int(years.index(max(years)))
    return titles[latest_game_index]


def count_by_genre(file_name,genre):
    import operator    
    genres = [x[3] for x in csv.reader(open(file_name,'r'),delimiter='\t')]
    number_of_games=genres.count(genre)
    return number_of_games

def get_line_number_by_title(file_name,title):
    titles=[x[0] for x in csv.reader(open(file_name,"r"),delimiter="\t")]
    while True:
        try:
            line_number=titles.index(title)+1
            return line_number
        except ValueError:
            break







stat="game_stat.txt"
print(count_games(stat))
print (decide(stat,1997))
get_latest(stat)
print(count_by_genre(stat,"Survival game"))
print(get_line_number_by_title(stat,"World of Warcraft"))
