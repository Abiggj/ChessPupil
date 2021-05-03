import chessdotcom
import os


def getgames_from_username(username):
    dates = []
    archives = chessdotcom.get_player_game_archives(username).json['archives']
    for url in archives:
        date = list(map(int, url[-7:].split('/')))
        dates.append(date)

    for year, month in dates:
        count = 1
        data = chessdotcom.get_player_games_by_month_pgn(username, year, month).json['pgn']['pgn']
        pgn_list = data.split('\n\n\n')
        for pgn in pgn_list:
            filename = os.getcwd()+"/Database/{}/{}/{}".format(username, year, month)
            os.makedirs(filename, exist_ok=True)
            file_addr = '/'+str(count)+".pgn"
            with open(filename+file_addr, 'w') as file:
                file.write(pgn)
                count += 1
