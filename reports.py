import csv


def load_list(file_name, index):
    properties = []
    reader = open(file_name, "r")
    game_stats = csv.reader(reader, delimiter="\t")
    for row in game_stats:
        properties.append(row[index])
    reader.close()
    return properties


def sort_list(list_name):
    for item in range(len(list_name) - 1, 0, -1):
        for i in range(item):
            if list_name[i].upper() > list_name[i + 1].upper():
                list_name[i], list_name[i + 1] = list_name[i + 1], list_name[i]
    return list_name
# 1


def count_games(file_name):
    games = load_list(file_name, 1)
    return len(games)
# 2


def decide(file_name, year):
    years = load_list(file_name, 2)
    for game in years:
        if str(game) == str(year):
            return True
    return False
# 3


def get_latest(file_name):
    titles = load_list(file_name, 0)
    years = load_list(file_name, 2)
    latest_game_index = int(years.index(max(years)))
    return titles[latest_game_index]

# 4


def count_by_genre(file_name, genre):
    import operator
    genres = load_list(file_name, 3)
    number_of_games = genres.count(genre)
    return number_of_games
# 5


def get_line_number_by_title(file_name, title):
    titles = load_list(file_name, 0)
    while True:
        try:
            line_number = titles.index(title) + 1
            return line_number
        except ValueError:
            return "Title not found"
            break
# 6


def sort_abc(file_name):
    titles = load_list(file_name, 0)
    return sort_list(titles)
# 7


def get_genres(file_name):
    genres = load_list(file_name, 3)
    sorted_genre = list(set(genres))
    return sort_list(sorted_genre)
# 8


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
            return "Genre not found"
        finally:
            data.close()
