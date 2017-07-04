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

def sort_abc(file_name):
    titles=[x[0] for x in csv.reader(open(file_name,"r"),delimiter="\t")]
    csv
    return sort_list(titles)

def get_genres(file_name):
    genres=[x[3] for x in csv.reader(open(file_name,"r"),delimiter="\t")]
    sorted_genre=list(set(genres))
    return sort_list(sorted_genre)

def sort_list(list_name):
    for item in range(len(list_name)-1,0,-1):
        for i in range(item):
            if list_name[i].upper() >list_name[i+1].upper():
                list_name[i],list_name[i+1]=list_name[i+1],list_name[i]
    return list_name

def when_was_top_sold_fps(file_name):
    while True:
        try:
            game_stat=open(file_name)
            copies=[x[1] for x in csv.reader(open(file_name,"r"),delimiter="\t") if x[3]=="First-person shooter"]
            copies=[float(i) for i in copies]
            top_sold_index=copies.index(max(copies))
            print(top_sold_index)
            years=[x[2] for x in csv.reader(open(file_name,"r"),delimiter="\t") if x[3]=="First-person shooter"]
            years=[int(i)for i in years]
            return years[top_sold_index]
        except ValueError:
            print("Genre not found.")
            break

   



stat="game_stat.txt"
print(count_games(stat))
print (decide(stat,1997))
get_latest(stat)
print(count_by_genre(stat,"First-person shooter"))
print(get_line_number_by_title(stat,"World of Warcraft"))
print(sort_abc(stat))
print(get_genres(stat))
print(when_was_top_sold_fps(stat))
