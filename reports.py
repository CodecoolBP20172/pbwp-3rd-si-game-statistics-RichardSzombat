import csv
# Report functions

# 1


def count_games(file_name):
    with open(file_name, "r") as game_stats:
        number = 0
        for line in game_stats:
            number += 1
        return number
# 2


def decide(file_name, year):
    years = load_list(stat, 2)
    for game in years:
        if str(game) == str(year):
            return True
    return False
# 3


def get_latest(file_name):
    titles = load_list(stat, 0)
    years = load_list(stat, 2)
    latest_game_index = int(years.index(max(years)))
    return titles[latest_game_index]

# 4


def count_by_genre(file_name, genre):
    import operator
    genres = load_list(stat, 3)
    number_of_games = genres.count(genre)
    return number_of_games
# 5


def get_line_number_by_title(file_name, title):
    titles = load_list(stat, 0)
    while True:
        try:
            line_number = titles.index(title) + 1
            return line_number
        except ValueError:
            break
# 6


def sort_abc(file_name):
    titles = load_list(stat, 0)
    return sort_list(titles)
# 7


def get_genres(file_name):
    genres = load_list(stat, 3)
    sorted_genre = list(set(genres))
    return sort_list(sorted_genre)


def load_list(file_name, index):
    list_type = []
    reader = open(file_name, "r")
    target_reader = csv.reader(reader, delimiter="\t")
    for row in target_reader:
        list_type.append(row[index])
    reader.close()
    return list_type


def sort_list(list_name):
    for item in range(len(list_name) - 1, 0, -1):
        for i in range(item):
            if list_name[i].upper() > list_name[i + 1].upper():
                list_name[i], list_name[i + 1] = list_name[i + 1], list_name[i]
    return list_name


def when_was_top_sold_fps(file_name):
    data = open(file_name)
    game_stats = csv.reader(data, delimiter="\t")
    years = []
    copies = []
    while True:
        try:
            for game in game_stats:
                if game[3] == "First-person shooter":
                    years.append(int(game[2]))
                    copies.append(float(game[1]))
            top_fps_index = copies.index(max(copies))
            return years[top_fps_index]
        except ValueError:
            print("Genre not found")
            break
        finally:
            data.close()


stat = "game_stat.txt"
count_games(stat)
decide(stat, 1997)
get_latest(stat)
count_by_genre(stat, "First-person shooter")
get_line_number_by_title(stat, "World of Warcraft")
sort_abc(stat)
get_genres(stat)
when_was_top_sold_fps(stat)
