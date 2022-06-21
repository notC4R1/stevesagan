import requests
###
server = "https://api.opendota.com/api/"
test_match_id = 5840046424
notcarl_id="88018253"
juggz_id = "5181820"
mike_walsh_id="188812207"

##Get Kills of Last 10 Games
def get_player_kills():
    response = requests.get(server+"players/"+mike_walsh_id+"/matches")
    r = response.json()
    player_kills=[]

    for i in range(10):
        player_kills.append(r[i]["kills"])

    return player_kills
        
##Get Deaths of Last 10 Games
def get_player_deaths():
    response = requests.get(server+"players/"+mike_walsh_id+"/matches")
    r = response.json()
    player_deaths=[]

    for i in range(10):
        player_deaths.append(r[i]["deaths"])

    return player_deaths

##Get Hero IDs of Last 10 Games
def get_player_hero_ids():
    response = requests.get(server+"players/"+mike_walsh_id+"/matches")
    r = response.json()
    player_hero_ids=[]

    for i in range(10):
        player_hero_ids.append(r[i]["hero_id"])

    return player_hero_ids

#Get hero name with Hero ID
def get_hero_name(player_hero_ids):
    player_hero_ids = player_hero_ids
    r_hero_list = requests.get(server+"heroes")
    hero_list = r_hero_list.json()
    player_hero_names = []
    x=0
    while len(player_hero_names) <= len(player_hero_ids) and len(player_hero_names) != len(player_hero_ids):
        for z in range(len(hero_list)):
            if hero_list[z]["id"] == player_hero_ids[x]:
                player_hero_names.append(hero_list[z]["localized_name"])
                x+=1
                break
                    
    return player_hero_names

#Roasts the player
def spit_fire(player_kills,player_deaths,player_hero_names):
    player_kills=player_kills
    player_deaths=player_deaths
    player_hero_names=player_hero_names
    print("Mike's most recent games of DOTA:")
    for i in range(len(player_hero_names)):
        if player_kills[i] < player_deaths[i]:
            print (str(player_hero_names[i])+": "+ str(player_kills[i])+ "/" + str(player_deaths[i]) + ". Looks like he's feeding")
        else:
            print (str(player_hero_names[i])+": "+str(player_kills[i])+ "/" + str(player_deaths[i]))



player_kills = get_player_kills()
player_deaths = get_player_deaths()
player_hero_ids = get_player_hero_ids()
player_hero_names = get_hero_name(player_hero_ids)
spit_fire(player_kills, player_deaths,player_hero_names)