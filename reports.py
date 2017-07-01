
# Report functions
def count_games(file_name):
    with open (file_name,"r") as game_stats:
        number = 0
        for line in game_stats:
            number += 1
        return number

def decide(file_name,year):
    with open(file_name,"r") as game_stat:
        game_stat_list=[line.strip().split("\t") for line in game_stat]
       # print (game_stat_list)
        for game in game_stat_list:
            print(game)
            if str(game[2])==str(year):
                return True
            else:
                return False










stat="game_stat.txt"
print(count_games(stat))
print (decide(stat,2000))
