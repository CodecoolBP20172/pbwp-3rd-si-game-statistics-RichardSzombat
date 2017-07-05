import csv


def load_list(file_name, index):
    properties = []
    reader = open(file_name.strip(), "r")
    game_stats = csv.reader(reader, delimiter="\t")
    for row in game_stats:
        properties.append(row[index])
    reader.close()
    return properties

#   1


def get_most_played(file_name):
    titles = load_list(file_name, 0)
    copies = load_list(file_name, 1)
    copies = [float(x) for x in copies]
    most_copies_index = copies.index(max((copies)))
    return str(titles[most_copies_index])
#   2


def sum_sold(file_name):
    copies = load_list(file_name, 1)
    copies = [float(x) for x in copies]
    sum_of_copies = sum(copies)
    return sum_of_copies
#   3


def get_selling_avg(file_name):
    copies = load_list(file_name, 1)
    copies = [float(x) for x in copies]
    avg_sell = sum(copies) / len(copies)
    return avg_sell
#   4


def count_longest_title(file_name):
    titles = load_list(file_name, 0)
    count_title = [len(x) for x in titles]
    return max(count_title)
#   5


def get_date_avg(file_name):
    years = load_list(file_name, 2)
    years = [float(x) for x in years]
    avg_years = sum(years) / len(years)
    return round(avg_years)
#   6


def get_game(file_name, title):
    titles = load_list(file_name, 0)
    copies = load_list(file_name, 1)
    copies = [float(x) for x in copies]
    years = load_list(file_name, 2)
    years = [int(x) for x in years]
    genre = load_list(file_name, 3)
    publisher = load_list(file_name, 4)
    while True:
        try:
            g_index = titles.index(title)
            properties = [titles[g_index], copies[g_index], years[g_index], genre[g_index], publisher[g_index]]
            return properties
        except ValueError:
            return "Game not found"
#   7


def count_grouped_by_genre(file_name):
    genre = load_list(file_name, 3)
    genres_dict = {}
    for game in genre:
        if game in genres_dict.keys():
            genres_dict[game] += 1
        else:
            genres_dict[game] = 1
    return genres_dict
#   8


def get_date_ordered(file_name):
    import operator
    game_dict = {}
    years = load_list(file_name, 2)
    titles = load_list(file_name, 0)
    years = [int(x)for x in years]
    for num, title in enumerate(titles):
        game_dict[title] = years[num]
    sorted_game_list = sorted(game_dict.items(), key=lambda x: (-x[1], x[0]))
    sorted_game_list = [x[0] for x in sorted_game_list]
    return sorted_game_list
