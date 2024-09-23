import readchar
import os
import random

# CAMBIAR NOMBRE DE VARIABLE GLOBAL "PLAYER" PARA EL COMBATE, PORQUE JALA EL VALOR DE MAZE

###### Characters ######

### Enemies ###
fighters = {

    "Palmenido" : {
        "nickname" : ": El destructor de cubanos",
        "HP" : 100,
        "attacks" : {
            1 : {
                "name" : "Kalashnikov calibre 7.62 x 39mm",
                "description" : "",
                "damage" : 20
                },

            2 : {
                "name" : "Cuernito mutante",
                "description" : "",
                "damage" : 20
                },

            3 : {
                "name" : "Yo soy la bomba",
                "description" : "",
                "damage" : 21
                },

            4 : {
                "name" : "Nachos cubanos",
                "description" : " y perdió 10pts de vida porque le cayeron mal",
                "damage" : 10
                }
        }
    },
    
    "Patibio" : {
        "nickname" : ": El máximo mandilón",
        "HP" : 110,
        "attacks" : {
            1 : {
                "name" : "Navaja de cholo",
                "description" : "",
                "damage" : 20
                },

            2 : {
                "name" : "Ron con coca",
                "description" : ", el espíritu de José José lo ha poseído y ahora es imparable!",
                "damage" : 21
                 },
            
            3 : {
                "name" : "Java",
                "description" : "",
                "damage": 19
                },

            4 : {
                "name" : "Rusheada",
                "description" : " y lo balacearon los municipales ):",
                "damage" : 15
                }
        }
    },

    "Angelo" : {
        "nickname" : "",
        "HP" : 90,
        "attacks" : {
            1 : {
                "name" : "Clasismo",
                "description" : "",
                "damage" : 24
            },

            2 : {
                "name" : "Lectura mental",
                "description" : "",
                "damage" : 22
            },

            3 : {
                "name" : "Kraken divorciado",
                "description" : "y ha recuperado 15pts de vida!!",
                "damage" : 15
            },

            4 : {
                "name" : "Chai",
                "description" : " pero no le pusieron polvo de canela y perdió 10pts con el coraje",
                "damage" : 10
            }
        }
    },

    "Leo Deo" : {
        "nickname" : ": El ninja mas nalgón de todo el condado de Missuri",
        "HP" : 120,
        "attacks" : {
            1 : {
                "name" : "Remix",
                "description" : "",
                "damage" : 18
            },

            2 : {"name" : "Mirada juzgona",
                 "description" : "",
                 "damage" : 20
            },

            3 : {
                "name" : "Horario godín",
                "description" : "drenando horas de vida de su enemigo",
                "damage" : 22
            },

            4 : {
                "name" : "Lic. en Lenguas Hispánicas",
                "description" : " y como no consiguió chamba perdió 20pts de vida",
                "damage" : 20
            }
        }
    },

    "Skull Piko" : {
        "nickname" : ": El folla mamis",
        "HP" : 90,
        "attacks" : {
            1 : {
                "name" : "Telaraña de chavos",
                "description" : "",
                "damage" : 22
            },

            2 : {
                "name" : "Miopía laser",
                "description" : "sin apuntar",
                "damage" : 24
            },

            3 : {
                "name" : "Tattoo",
                "description" : "",
                "damage" : 21
            },

            4 : {
                "name" : "AMOPSA",
                "description" : "pero se perdió en el transporte público y perdió 11pts de vida.",
                "damage" : 11
            }
        }
    },

    "Tenebra" : {
        "nickname" : "modo Cybergoth",
        "HP" : 80,
        "attacks" : {
            1 : {
                "name" : "Ortometría",
                "description" : "para medir el orto del enemigo",
                "damage" : 25
            },

            2 : {
                "name" : "Cross Roads",
                "description" : "",
                "damage" : 30
            },

            3 : {
                "name" : "Tremenda piña",
                "description" : ": Tenebra te ha propinado tal ostia que ambos murieron!! (Tenebra -15pts de vida / enemigo -30pts de vida)",
                "damage" : 30
                },

            4 : {
                "name" : "Kosako",
                "description" : ": Oh no! Tenebra se puso ebria en el transporte público y perdió 15pts de vida",
                "damage" : 15
            }
        }
    },

    "Moon" : {
        "nickname" : ": The dragon princess",
        "HP" : 90,
        "attacks" : {
            1 : {
                "name" : "DDoS",
                "description" : "(Distributed Deny of Servicios-básicos)",
                "damage" : 24
            },
            
            2 : {
                "name" : "Racismo",
                "description" : "",
                "damage" : 20
            },

            3 : {
                "name" : "Ataque secreto",
                "description" : "",
                "damage" : 24
            },

            4 : {
                "name" : "Vaso de Starbucks",
                "description" : "pero se le rompió en el transporte y perdió 9pts de vida",
                "damage" : 9
            }
        }
    },

    "Kath" : {
        "nickname" : "\"La china\"",
        "HP" : 100,
        "attacks" : {
            1 : {
                "name" : "Chevrolet Beat",
                "description" : "para arrollarte sobre la banqueta!!",
                "damage" : 20
            },

            2 : {
                "name" : "Peda improvisada",
                "description" : "",
                "damage" : 20
            },

            3 : {
                "name" : "Clasismo",
                "description" : "",
                "damage" : 22
            },

            4 : {
                "name" : "Enrutamiento OSPF",
                "description" : "pero como olvidó declarar el identificador  perdió 10pts de vida",
                "damage" : 10
            }
        }
    }
}

### Player ###
my_stats = {
    "player" : "Flamingo",
    "nickname" : "",
    "HP" : 115,
    "attacks" : {
        1 : {
            "name" : "Agarrada de nalga",
            "description" : "",
            "damage" : 20
        },

        2 : {
            "name" : "Hackerman",
            "description" : "para hackear el tiempo y traer a los laser-raptors",
            "damage" : 22
        },

        3 : {
            "name" : "Powerade azul",
            "description" : "para bajar la cruda y ganar 10pts de vida",
            "damage" : 10
        },

        4 : {
            "name" : "Ataque secreto",
            "description" : ": Oh no! Flamingo se puso a tomar con Patibio perdiendo 15pts de vida",
            "damage" : 15
        }
    }
}

###### MAZE ######
obstacle_definition="""\
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|        |        |                                            |
+  +--+  +  +--+--+  +--+--+--+--+--+--+--+--+--+  +--+--+--+  +
|     |     |        |     |     |              |     |        |
+--+  +  +--+  +--+--+  +  +  +  +  +--+--+--+  +--+  +  +--+--+
|     |  |     |        |     |  |        |  |  |     |     |  |
+  +--+  +  +--+  +--+--+--+--+--+--+  +--+--+  +--+--+--+  +--+
|  |     |  |  |  |              |  |  |     |        |  |     |
+  +--+--+  +--+  +  +--+--+--+  +  +  +  +  +--+  +  +--+--+  +
|        |  |     |     |     |     |     |     |  |           |
+  +--+  +  +  +--+--+  +--+  +  +--+--+--+--+  +  +--+--+--+--+
|  |     |  |        |     |  |              |  |           |  |
+  +  +--+  +--+--+--+--+  +  +--+--+--+--+  +  +--+  +--+  +--+
|  |  |                    |              |  |     |  |  |     |
+  +  +  +--+--+--+--+--+--+--+  +--+--+  +- +--+  +  +  +--+  +
|  |        |     |                    |  |     |  |     |     |
+  +--+--+  +  +  +  +--+  +--+--+  +--+--+  +  +  +--+  +  +--+
|  |        |  |  |     |        |  |        |  |  |  |  |     |
+  +  +--+--+  +  +--+  +  +--+--+--+  +--+--+--+  +  +  +--+  +
|  |  |        |     |  |     |     |           |  |     |  |  |
+  +  +  +--+--+--+--+  +--+  +  +--+--+--+--+  +  +--+--+--+  +
|  |                       |  |           |     |        |  |  |
+  +  +--+--+--+--+--+--+--+--+--+  +--+--+  +--+--+--+  +--+  +
|  |        |     |  |        |  |  |  |              |  |     |
+--+--+--+  +  +  +  +  +--+  +--+  +--+  +--+  +--+--+  +  +--+
|     |     |  |  |  |  |  |        |  |  |     |     |  |     |
+  +--+  +--+  +  +  +  +--+--+--+--+--+  +  +--+  +  +  +--+--+
|           |  |  |  |                 |  |  |     |  |        |
+--+--+--+  +--+  +  +--+--+--+--+--+  +  +  +--+--+--+--+--+  +
                  |                 |     |              |      
+-----+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+\
"""
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

###### Global variables ######

### Fighters ###
FIGHTER = random.choice(list(fighters.keys()))
FIGHTER_NICKNAME = fighters[FIGHTER]["nickname"]
ENEMY_HP_ABSOLUTE = fighters[FIGHTER]["HP"]
enemy_hp = ENEMY_HP_ABSOLUTE

### Player ###
PLAYER_NAME = my_stats["player"]
PLAYER_NICKNAME = my_stats["nickname"]
PLAYER_HP_ABSOLUTE = my_stats["HP"]
player_hp = PLAYER_HP_ABSOLUTE

### Maze ###
POS_X, POS_Y = 0, 1
MAP_WIDTH, MAP_HEIGHT, NUM_MAP_OBJECTS = len(obstacle_definition[0]), len(obstacle_definition), 40
OBJECT_LIMIT_X, OBJECT_LIMIT_Y = MAP_WIDTH -1, MAP_HEIGHT -1
PLAYER = "⛧"
TAIL_PIECE = "𓃵"
OBJECT = "𖤍"

game_over, dead = False, False
my_position = [0, 29]
tail_length = 0
tail = []

###### FIGHT Functions ######
def hp_bars():
    global FIGHTER, PLAYER_NAME, ENEMY_HP_ABSOLUTE, PLAYER_HP_ABSOLUTE, enemy_hp, player_hp

    # Never show negative numbers, when it downs under zero, set in zero
    if enemy_hp < 0: enemy_hp = 0

    if player_hp < 0: player_hp = 0

    temp_enemy_hp = ENEMY_HP_ABSOLUTE - enemy_hp
    temp_player_hp = PLAYER_HP_ABSOLUTE - player_hp

    hp_enemy_bar = ("{}: ".format(FIGHTER) + "[" + ("|"*enemy_hp) + ("-"*temp_enemy_hp) + "]", "{}%".format(enemy_hp))

    hp_player_bar = ("{}: ".format(PLAYER_NAME) + "[" + ("|"*player_hp) + ("-"*temp_player_hp) + "]", "{}%".format(player_hp))

    return hp_enemy_bar, hp_player_bar

def game():
    global FIGHTER, PLAYER_NAME, FIGHTER_NICKNAME, PLAYER_NICKNAME, enemy_hp, player_hp, fighters, dead, game_over

    while enemy_hp > 0 and player_hp > 0:
        
        random_index_attack = random.randint(1,4) # Index to select a random Fighter's attack
        enemy_attack = fighters[FIGHTER]["attacks"][random_index_attack] # Search the attack
        enemy_attack_name = enemy_attack["name"]
        enemy_attack_description = enemy_attack["description"]
        enemy_attack_damage = enemy_attack["damage"]

        input("Presiona \"Enter\" para continuar...") # Enemy's turn
        os.system("cls")
        
        print("Turno de {}...".format(FIGHTER))
        print("{} {} ha utilizado: {} {}!!".format(FIGHTER, FIGHTER_NICKNAME, enemy_attack_name, enemy_attack_description))

        if FIGHTER == "Angelo": # Special IF for Angeloo (Kraken attack)

            if random_index_attack == 3: enemy_hp += enemy_attack_damage # Restore health

            elif random_index_attack == 4: enemy_hp -= enemy_attack_damage

            else: player_hp -= enemy_attack_damage
        
        elif FIGHTER == "Tenebra": # Special IF for Tenebra (Piña attack)

            if random_index_attack == 3: # Damage both players
                player_hp -= enemy_attack_damage
                enemy_hp -= int(enemy_attack_damage/2)

            elif random_index_attack == 4: enemy_hp -= enemy_attack_damage

            else: player_hp -= enemy_attack_damage
        
        else:
            if random_index_attack == 4: enemy_hp -= enemy_attack_damage

            else: player_hp -= enemy_attack_damage

        bars = hp_bars()
        print(bars[0])
        print(bars[1])

        input("Presiona \"Enter\" para continuar...")
        os.system("cls")

        if enemy_hp == 0: break

        print("Turno de {}...".format(PLAYER_NAME)) # Player's turn
        selection = None # Index
        while selection not in [1, 2, 3, 4]:
            try:
                selection = int(input("""
                                Selecciona un ataque:
                               [1] Agarrada de nalga
                               [2] Hackerman
                               [3] Powerade azul
                               [4] Ataque Secreto
                               : """))
            
            except: print("Opción inválida, inténtalo de nuevo.")

        player_attack = my_stats["attacks"][selection]
        player_attack_name = player_attack["name"]
        player_attack_description = player_attack["description"]
        player_attack_damage = player_attack["damage"]
        
        print("{} {} ha utilizado: {} {}!!".format(PLAYER_NAME, PLAYER_NICKNAME, player_attack_name, player_attack_description)) # Cambiar name por description
        
        if selection == 3: player_hp += player_attack_damage # The thirth attack increase the health
        
        elif selection == 4: player_hp -= player_attack_damage # The fourth attack always damage itself

        else: enemy_hp -= player_attack_damage
        
        bars = hp_bars()
        print(bars[0])
        print(bars[1])

    if enemy_hp > player_hp:
        os.system("cls")
        print(bars[0])
        print(bars[1])
        print("{} Le hizo un chavo a {}".format(FIGHTER, PLAYER_NAME))
        dead, game_over = True, True

    else:
        os.system("cls")
        print(bars[0])
        print(bars[1])
        print("{} murió porque no era de la talla de {}".format(FIGHTER, PLAYER_NAME))

    enemy_hp = ENEMY_HP_ABSOLUTE
    player_hp = PLAYER_HP_ABSOLUTE

###### SNAKE ######

def objects():
    global NUM_MAP_OBJECTS, OBJECT_LIMIT_X, OBJECT_LIMIT_Y, my_position
    object_list = []

    for i in range(NUM_MAP_OBJECTS):

        while True:
            temp_object = [random.randint(0, OBJECT_LIMIT_X), random.randint(0, OBJECT_LIMIT_Y)]

            if temp_object in object_list or temp_object == my_position: pass

            else: break

        object_list.append(temp_object)
    
    return object_list

map_objects = objects()

def new_objects():
    global OBJECT_LIMIT_X, OBJECT_LIMIT_Y, my_position, tail, map_objects

    while True:
        new_object = [random.randint(0, OBJECT_LIMIT_X), random.randint(0, OBJECT_LIMIT_Y)]
        
        if new_object not in map_objects and new_object not in tail and new_object != my_position:
            map_objects.append(new_object)
            break

        else: pass

def maze():
    global POS_X, POS_Y, MAP_WIDTH, MAP_HEIGHT, PLAYER, OBJECT, TAIL_PIECE, my_position, tail_length, game_over, dead

    combat = False

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None

            try:

                for map_object in map_objects:

                    if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                        char_to_draw = OBJECT
                        object_in_cell = map_object

            except: continue

            for tail_piece in tail:

                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = TAIL_PIECE

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = PLAYER

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                    # Despues de dibujar el laberinto, comprobará si hay un combate
                    combat = True
                    new_objects()

                if my_position in tail: game_over, dead = True, True

            if obstacle_definition[coordinate_y][coordinate_x] == "+": char_to_draw = "+" # PISTA

            elif obstacle_definition[coordinate_y][coordinate_x] == "-": char_to_draw = "-"

            elif obstacle_definition[coordinate_y][coordinate_x] == "|": char_to_draw = "|"

            print(" {} ".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    if combat == True: os.system("cls"), game() # Cleans screen and starts the game
    

def position():
    global direction, my_position

    if my_position[POS_X] < 0: my_position[POS_X] = OBJECT_LIMIT_X
    
    elif my_position[POS_X] > OBJECT_LIMIT_X: my_position[POS_X] = 0

    elif my_position[POS_Y] < 0: my_position[POS_Y] = OBJECT_LIMIT_Y

    elif my_position[POS_Y] > OBJECT_LIMIT_Y:  my_position[POS_Y] = 0

while game_over == False:

    maze()
    print("¿A que casilla te quieres move? [WASD]")
    direction = readchar.readchar()
    new_position = None
    
    os.system("cls")

    if direction == "w": new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s": new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a": new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d": new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q": game_over = True

    else: print("Opción inválida!!")

    if new_position:
        
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] not in ["+", "-", "|"]:
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

        position()

    if game_over == True and dead == True: print("HAZ MUERTO!!")

    elif game_over == True and dead == False: print("HASTA LUEGO!!")

#ilusionó y lo ghostearon