from ast import Break
import csv
import json
import random
class Moves:
    # power refers to the damage a move can deal
    # acuracy refers to how likely it is to hit
    # pp refers to how many uses a given attack has
    # if it reaches 0 the attack wont be available
    def __init__(self, index: str, movename: str, type: str, power: float, acuracy: int, max_pp: int):
        self.movename = movename
        self.index = index
        self.type= type
        self.power = power
        self.acuracy = acuracy
        self.max_pp = max_pp
        self.pp = max_pp


class Pokemon:
    def __init__(self, name: str, type: str, max_hp: float, move1:Moves, move2:Moves, move3:Moves, move4:Moves, knocked = False):
        self.name = name
        self.type = type  
        self.max_hp = max_hp
        self.hp = max_hp
        self.knocked = knocked
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4 

    # Displays info of the moves of the current pokemon
    def showinfopoke(self):
        print("LISTA DE ATAQUES:\n1." +
        self.move1.movename +" ELEMENTO: "+ self.move1.type +" POWER: " + str(self.move1.power) + " ACURACY:" +  str(self.move1.acuracy) +"% PP: " + str(self.move1.pp) + "\n2." +
        self.move2.movename +" ELEMENTO: "+ self.move2.type +" POWER: " + str(self.move2.power) + " ACURACY:" +  str(self.move2.acuracy) +"% PP: " + str(self.move2.pp) + "\n3." +
        self.move3.movename +" ELEMENTO: "+ self.move3.type +" POWER: " + str(self.move3.power) + " ACURACY:" +  str(self.move3.acuracy) +"% PP: " + str(self.move3.pp) + "\n4." +
        self.move4.movename +" ELEMENTO: "+ self.move4.type +" POWER: " + str(self.move4.power) + " ACURACY:" +  str(self.move4.acuracy) +"% PP: " + str(self.move4.pp)+ "\n")

    # Increases maximum health and resets current health
    def upgradelife(self):
        self.max_hp += 20
        self.hp = self.max_hp
        self.knocked = False
        
    # Display current health usings / to represent evey 10 health points
    def showlife(self):
        bar = self.hp/10
        strbar=""
        for b in range (int(bar)):
                strbar = f"{strbar}/"
        print (strbar) 

    # Creates moves extracting their info from moves.csv
    def assignmoves(ctype,list):
        fixedrow=[]
        with open('moves.csv', 'r') as f:
            reader = csv.reader(f)
            n = 0
            while n < 4:
                rvalue = random.randint(1, 354)
                for row in reader:
                    fixedrow.append(row[0].split(","))  #Separa el csv por fila
                for col in fixedrow:                    #Separa cada fila por columnas
                    if ((rvalue ==  int(col[0]))  & ((ctype == col[2]) or ((col[2] == "Normal") & (n < 2)))):
                        list.append(Moves(col[0], col[1], col[2], float(col[3]), int(col[4]), int(col[5])))
                        n = n +1   
                    # A random index is chosen, if the type of attack is equal to the type of Pokemon or a normal type, it is added
                    #to the list of moves, at least two unique type attacks are guaranteed
class Item:
    def __init__(self,name:str,cost:int, quan:int=0, flat_power:int=0, flat_hp:int=0, flat_acuracy:int=0, restore_pp:bool=False):
        self.name = name
        self.cost = cost
        self.quan = quan
        self.flat_power = flat_power
        self.flat_hp = flat_hp
        self.flat_acuracy = flat_acuracy
        self.restore_pp = restore_pp      
        
# I decided that the rivals were fixed, that is, their pokemon and movements are already defined
# In this class is the information that is passed to create the pokemon objects that correspond to the rival
class Rival:
    def __init__(self,cn:int, name="Panchito"):
        movelist=[]
        self.name = name
        # Motion instances are created according to the name and pokemon to be assigned as attributes
        if(cn == 0):
            Gym.assignmovesrivals(movelist,"Aeroblast", "Octazooka", "False Swipe","Crabhammer")
            self.rivalpokemon1 = Pokemon("Mega Blastoise", "Water", 200, movelist[0], movelist[1], movelist[2],movelist[3])

            Gym.assignmovesrivals(movelist,"Rock Slide", "Rock Throw", "AncientPower","Rock Tomb")
            self.rivalpokemon2 = Pokemon("Serpentok", "Rock", 200, movelist[0], movelist[1], movelist[2],movelist[3])
        
            Gym.assignmovesrivals(movelist,"Ember", "Flamethrower", "Fire Punch","Crush Claw")
            self.rivalpokemon3 = Pokemon("Charmander", "Fire", 200, movelist[0], movelist[1], movelist[2],movelist[3])

            Gym.assignmovesrivals(movelist,"Astonish", "Shadow Punch", "Night Shade","Shadow Ball")
            self.rivalpokemon4 = Pokemon("Gengar", "Ghost", 200, movelist[0], movelist[1], movelist[2],movelist[3]) 

        if(cn == 1):
             Gym.assignmovesrivals(movelist,"Karate Chop", "Submission", "Meteor Mash","ViceGrip")
             self.rivalpokemon1 = Pokemon("Lucario", "Fighting", 200, movelist[0], movelist[1], movelist[2],movelist[3])

             Gym.assignmovesrivals(movelist,"DragonBreath", "Dragon Claw", "Dragon Rage","Pay Day")
             self.rivalpokemon2 = Pokemon("Garchomp", "Dragon", 200, movelist[0], movelist[1], movelist[2],movelist[3])

             Gym.assignmovesrivals(movelist,"Bite", "Faint Attack", "Crunch","Endeavor")
             self.rivalpokemon3 = Pokemon("Darkrai", "Dark", 200, movelist[0], movelist[1], movelist[2],movelist[3])

             Gym.assignmovesrivals(movelist,"Razor Leaf", "Giga Drain", "Leaf Blade","Mach Punch")
             self.rivalpokemon4 = Pokemon("Rillaboom", "Grass", 200, movelist[0], movelist[1], movelist[2],movelist[3])

        if(cn == 2):
            Gym.assignmovesrivals(movelist,"Steel Wing", "Doom Desire", "BubbleBeam","Cut")
            self.rivalpokemon1 = Pokemon("Empoleon", "Steel", 200, movelist[0], movelist[1], movelist[2],movelist[3])

            Gym.assignmovesrivals(movelist,"Blizzard", "Aurora Beam", "Wing Attack","Scratch")
            self.rivalpokemon2 = Pokemon("Articuno", "Ice", 200, movelist[0], movelist[1], movelist[2],movelist[3])

            Gym.assignmovesrivals(movelist,"Earthquake", "Dig", "Magnitude","Rock Tomb")
            self.rivalpokemon3 = Pokemon("Golurk", "Ground", 200, movelist[0], movelist[1], movelist[2],movelist[3])

            Gym.assignmovesrivals(movelist,"Megahorn", "Signal Beam", "Air Cutter","Crush Claw")
            self.rivalpokemon4 = Pokemon("Scizor", "Bug", 200, movelist[0], movelist[1], movelist[2],movelist[3])

# Predefined rival list
rival_list =["Cindy","Brock","Doroty"]

# The n_rival is used to indicate how many battles there should be
class Gym:
    def __init__(self,gymname:str, list, n_rival=0):
        self.gymname = gymname
        self.n_rival = n_rival   
        for i in list:
            self.n_rival +=  1

    def deletelastrival(list): 
         del list[len(list)-1]

# Since the movements are already defined, the list is simply traversed in search of its information.
    def assignmovesrivals(list,move1,move2,move3,move4):
        fixedrow=[]
        list.clear()
        with open('Moves.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                fixedrow.append(row[0].split(","))  
            for col in fixedrow:  
                if(move1 == col[1]):
                    list.append(Moves(col[0], col[1], col[2], float(col[3]), int(col[4]), int(col[5])))
                if(move2 == col[1]):
                    list.append(Moves(col[0], col[1], col[2], float(col[3]), int(col[4]), int(col[5])))
                if(move3 == col[1]):
                    list.append(Moves(col[0], col[1], col[2], float(col[3]), int(col[4]), int(col[5])))    
                if(move4 == col[1]):
                    list.append(Moves(col[0], col[1], col[2], float(col[3]), int(col[4]), int(col[5])))         
    
class Player:
    def __init__(self, name="juan", money:int = 200):
        self.name = name
        self.money = money

    # This is the initial screen of the game where the player is allowed to create their pokemon and assign them as his attributes   
    def createteam(self):
        print("BIENVENIDO A POKEMON ")
        print("Primero armemos nuestro equipo ")
        for n in range(4):
            movelist=[]
            mascotname = input("\nInserte el nombre de su Pokemon: ")
            print("***************************************\n"+
            "Normal *** Psychic *** Fighting\nGrass *** Water *** Fire\nGround *** Dark *** Flying"+
            "\nIce *** Ghost *** Poison *** Bug \nElectric *** Rock *** Steel *** Dragon"+
            "\n***************************************\n")
            matches = ["Normal","Psychic","Fighting","Grass","Water","Fire","Ground","Dark","Flying","Ice"
            , "Ghost", "Poison","Bug","Electric","Rock","Steel","Dragon"]

            customtype = input("Inserte su tipo de Pokemon: ")
            customtype = customtype.capitalize()
            while not any(x in customtype for x in matches):
                customtype = input("TIPO NO ENCONTRADO INTENTE NUEVAMENTE\nInserte su tipo de Pokemon: ")
                customtype = customtype.capitalize()
            else:
                max_hp = 200
                Pokemon.assignmoves(customtype.capitalize(), movelist)
                if(n==0):
                 self.mypokemon1 = Pokemon(mascotname, customtype, max_hp, movelist[0], movelist[1], movelist[2], movelist[3])
                 customname = self.mypokemon1
                if(n==1):
                 self.mypokemon2 = Pokemon(mascotname, customtype, max_hp, movelist[0], movelist[1], movelist[2], movelist[3])
                 customname = self.mypokemon2
                if(n==2):
                 self.mypokemon3 = Pokemon(mascotname, customtype, max_hp, movelist[0], movelist[1], movelist[2], movelist[3])    
                 customname = self.mypokemon3    
                if(n==3):
                 self.mypokemon4 = Pokemon(mascotname, customtype, max_hp, movelist[0], movelist[1], movelist[2], movelist[3])
                 customname = self.mypokemon4
            print("\n****POKEMON CREADO EXITOSAMENTE****")    
            print("NOMBRE " + customname.name + "\nTIPO: " + customname.type)
            customname.showinfopoke()
            print("***********************************")    
        print("****EQUPO COMPLETO HORA DE RETAR AL GIMNASIO****\n")
        print("****HORA DE LA BATALLA****\n")     

# The available items are created
heart = Item("Heart",75,1,0,150) 
sight = Item("Sight",75,0,0,0,10)
charge = Item("Charge",75,1,15)
assault_focus = Item ("assault focus",100,0,8,0,8)
recovery = Item("Rrecovery",150,0,0,50,0,True)

class Match:  
    def __init__(self):
        gym = Gym("Alola",rival_list)
        user = Player()
        user.createteam()
        cont = 0
        self.effectiveness = 1
        # For each rival that belongs to the gym there will be a fighT
        for i in rival_list:
            rival = Rival(cont,i)
            # This is for the purpose of abbreviating when calling each pokemon
            rivalpokemon1 = rival.rivalpokemon1
            rivalpokemon2 = rival.rivalpokemon2
            rivalpokemon3 = rival.rivalpokemon3
            rivalpokemon4 = rival.rivalpokemon4
            mypokemon1 = user.mypokemon1
            mypokemon2 = user.mypokemon2
            mypokemon3 = user.mypokemon3
            mypokemon4 = user.mypokemon4

            # Variables neccesary for the while cycles in each fight
            # turnsw indicates if it is the turn of the Player or the Rival(npc)
            # battlesw indicates if a particular fight is over
            turnsw=0
            battlesw = 0

            # Info of the rival is shown 
            print("****TU RIVAL ES: " + rival.name +"****\n")
            print( rival.name + " elige a su " + rivalpokemon1.name + " del tipo " + rivalpokemon1.type + "\n")

            # From now on the program will be working  with customname wich is refering to the active Player pokemon
            # And  objetivename wich is refering to the active Rival pokemon
            # Active meaning is the one that is currently affected by attacks, bonuses, whose info is used to perform actions

            # User must choose an avalaible starting pokemon
            while True:
                po = input("***ESCOGE TU POKEMON INICAL****\n1."+ mypokemon1.name + "\n2."+ 
                mypokemon2.name + "\n3."+ mypokemon3.name + "\n4."+ mypokemon4.name + "\n")
                if(po=="1"):
                    customname = mypokemon1
                if(po=="2"):
                    customname = mypokemon2
                if(po=="3"):   
                    customname = mypokemon3  
                if(po=="4"):
                    customname = mypokemon4 
                if((0<int(po)<=4)):
                    break

            print("Eliges a " + customname.name)
            # rival will always start with is first assigned pokemon
            objetivename = rivalpokemon1

            while(battlesw == 0):
                # player turn
                if(turnsw == 0):
                    print("\nTU TURNO\n")
                    print("**** MENU OPCIONES ****\n")
                    print("**** 1.ATACAR ****\n")
                    print("**** 2.INVENTARIO ****\n")
                    print("**** 3.CAMBIAR POKEMON****\n")
                    print("**** 4.HUIR****\n")
                    op = input("¿Que haras?\n")
                    # Regardless of what action is taken the turn changes to the Rival
                    turnsw = 1
                    # Attack option choosen now avalaible attacks are displayed
                    if(op=="1"):
                        customname.showinfopoke()

                        # Checkyng if chosen attack is valid
                        # If the selected attack has run out of uses it cant be choosen
                        while True:
                            a = input("\nElija un ataque\n")
                            if((0<int(a)<=4) & (self.checkpp(customname,a)== True)):
                                break 
                        print("--------------------------------")
                        # The method is called with the Player pokemon being the attacker and Rival pokemon the defender
                        self.attack_pokemon(customname,objetivename,a) 

                        # Once all rival pokemons are defeated the fight is over and the next rival is selected, since cont changed
                        if(rivalpokemon1.knocked == True & rivalpokemon2.knocked == True 
                        & rivalpokemon3.knocked == True & rivalpokemon4.knocked == True  ):
                            print("\nFELICIDADES HAS GANADO ESTA BATALLA")  
                            cont += 1
                            battlesw=1   

                        # If a Rival pokemon is defeated the Rival must select one of his remaining Pokemons to continue the fight
                        while((objetivename.knocked == True) & (battlesw==0)):                    
                            po = str(random.randint(1, 4))
                            if(po=="1"):
                                objetivename = rivalpokemon1
                            if(po=="2"):
                                objetivename = rivalpokemon2
                            if(po=="3"):   
                                objetivename = rivalpokemon3
                            if(po=="4"):
                                objetivename = rivalpokemon4
                            if(objetivename.knocked == False):
                                print(rival.name + " CAMBIA DE POKEMON A: " + objetivename.name + " DE TIPO " + objetivename.type)      

                    # Bonus menu is displayed
                    if(op=="2"):
                        self.bonusmenu(customname)    
                    
                    # Changes active pokemon using customname 
                    # This pokemon will be hit inmediatly since the turn passes to the Rival
                    if(op=="3"):
                        while True:
                            po = input("***ESCOGE TU POKEMON DE REMPLAZO***\n1."+ mypokemon1.name + "\n2."+ 
                            mypokemon2.name + "\n3."+ mypokemon3.name + "\n4."+ mypokemon4.name + "\n")
                            if(po=="1"):
                                customname = mypokemon1
                            if(po=="2"):
                                customname = mypokemon2
                            if(po=="3"):   
                                customname = mypokemon3  
                            if(po=="4"):
                                customname = mypokemon4 
                            if((0<int(po)<=4)):
                                break       
                    # Player exits the game, made sure to check decission              
                    if(op=="4"):
                        if ("Y")in(input("presiona Y para abandonar la batalla")):
                            print("BATALLA ABANDONADA RECUERDA QUE SIEMPRE ESTAREMOS LISTOS PARA UNA REVANCHA")
                            battlesw=1
                            exit()                  
                        else: turnsw=0

                # Rivals turn     
                if(turnsw == 1 & (battlesw==0)):
                        print("--------------------------------")
                        print("\nTURNO DE TU RIVAL")  
                        a = str(random.randint(1, 4))
                        # A random move is choosen
                        # The method is called with the Rival pokemon being the attacker and Player pokemon the defender

                        self.attack_pokemon(objetivename,customname,a) 
                        print("--------------------------------")

                        # If all player pokemon are defeated the game ends
                        if(mypokemon1.knocked == True & mypokemon2.knocked == True 
                        & mypokemon3.knocked == True & mypokemon4.knocked == True ):
                            print("\nMALA SUERTE HAS PERDIDO ESTA BATALLA RECUERDA QUE SIEMPRE ESTAREMOS LISTOS PARA UNA REVANCHA")
                            exit()                        
                        #If a Player pokemons is defeated, he select one of his remaining Pokemons to continue the fight
                        while((customname.knocked == True) & (battlesw==0)):
                            po =input("Tu Pokemon ha sido noqueado escoge a su remplazo\n1."+ mypokemon1.name + "\n2."+ 
                            mypokemon2.name + "\n3."+ mypokemon3.name + "\n4."+ mypokemon4.name + "\n")
                            if(po=="1"):
                                customname = mypokemon1
                            if(po=="2"):
                                customname = mypokemon2
                            if(po=="3"):   
                                customname = mypokemon3  
                            if(po=="4"):
                                customname = mypokemon4     
                        turnsw = 0 
            # This menu is shown once at least one Rival has been defeated           
            if(cont != 0):
                print("HORA DE RETAR AL SIGUIENTE OPONENTE\n")   
                print("VIDA MAXIMA DE TU EQUIPO AUMENTADA\n")
                print("VIDA DE EQUIPO RESTAURADA\n")
                mypokemon1.upgradelife()
                mypokemon2.upgradelife()
                mypokemon3.upgradelife()
                mypokemon4.upgradelife()
                print("GANAS 100 CREDITOS") 
                user.money += 100
                self.tienda(user)
            # If all Rival of the Gym have been defeated a modest congratulations message is displayed
            if(cont == gym.n_rival):
                for n in range(5):
                    print("\n***********FELICIDADES HAS GANADO LA MEDALLA DE GIMNASIO***********") 
                exit() 


    def tienda(self,user:Player):
        # Checks if the user has enough money to buy a Item
        # Adds one to the .quan atribute of the Item, so it can be once more
        while(True):
            print("\nDinero actual: " + str(user.money))
            i = input("***Elige un item a comprar***\n1.Heart "+ str(heart.cost) +"\n2.Sight "+ str(sight.cost) +"\n3.charge "+ str(charge.cost) 
            +"\n4.assault_focus "+ str(assault_focus.cost) +"\n5.Recovery "+ str(recovery.cost)+"\n6.Salir tienda\n")
            if((i=="1") & ((user.money - heart.cost) >= 0)):
                heart.quan += 1 
                user.money -= heart.cost
            if((i=="2") & ((user.money - sight.cost) >= 0)):
                sight.quan += 1 
                user.money -= sight.cost
            if((i=="3") & ((user.money - charge.cost) >= 0)):
                charge.quan += 1 
                user.money -= charge.cost
            if((i=="4") & ((user.money - assault_focus.cost) >= 0)):
                assault_focus.quan += 1 
                user.money -= assault_focus.cost
            if((i=="5") & ((user.money - recovery.cost) >= 0)):
                recovery.quan += 1 
                user.money -= recovery.cost
            if(i=="6"):
                break

    def bonusmenu(self, customname):
        # Checks if selected item is availabe, only one item can be used per turn
        while(True):
            i = input("***Elige un item para usar***\n1.Heart "+ str(heart.quan) +"\n2.Sight "+ str(sight.quan) +"\n3.charge "+ str(charge.quan) 
            +"\n4.assault_focus "+ str(assault_focus.quan) +"\n5.Recovery "+ str(recovery.quan)+"\n")

            # heart heals the active Player pokemon 
            if((i=="1") & (heart.quan > 0)):
                heart.quan -= 1 
                if((customname.hp + heart.flat_hp) > customname.max_hp):
                    customname.hp = customname.max_hp
                else:
                    customname.hp += heart.flat_hp
                print("Vida recuperada")
                break
            # sight improves the acuracy of two moves of the active Player pokemon 
            if((i=="2") & (sight.quan > 0)):
                sight.quan -= 1 
                customname.move1.acuracy += sight.flat_acuracy
                customname.move2.acuracy += sight.flat_acuracy
                print("Precision mejorada")
                break
            # charge improves the power of two moves of the active Player pokemon 
            if((i=="3") & (charge.quan > 0)):
                charge.quan -= 1 
                customname.move1.power += charge.flat_power
                customname.move2.power += charge.flat_power
                print("Daño mejorado")
                break  
            # assault_focus improves the power and acuracy of two moves of the active Player pokemon 
            if((i=="4") & (assault_focus.quan > 0)):
                assault_focus.quan -= 1 
                customname.move1.acuracy += assault_focus.flat_acuracy
                customname.move2.acuracy += assault_focus.flat_acuracy
                customname.move1.power += assault_focus.flat_power
                customname.move2.power += assault_focus.flat_power
                print("Daño y precision mejorado")
                break  
            # recovery restores pp of all moves of the active pokemon, being the only way to do so
            # and heals  heals the active Player pokemon 
            if((i=="5") & (recovery.quan > 0)):
                recovery.quan -= 1
                customname.hp += heart.flat_hp
                customname.move1.pp = customname.move1.max_pp
                customname.move2.pp = customname.move2.max_pp
                customname.move3.pp = customname.move3.max_pp
                customname.move4.pp = customname.move4.max_pp
                print("pp de equipo recuperado")
                break

    # Method returns true if the selected move still has uses and false if it does not
    def checkpp(self,customname: Pokemon, a):
        if(a=="1"): 
           move = customname.move1
        if(a=="2"): 
           move = customname.move2
        if(a=="3"): 
           move = customname.move3  
        if(a=="4"): 
           move = customname.move4              
        move.pp -= 1
        if(move.pp < 0):
           print("Ha gastada el maximo de usos de este movimiento")
           return False
        else:
            return True   

    # Takes the type of the move selected by the attacker and compares how effective it is against the pokemon type of the defender
    # It will change the atribute effectiveness that is used when calculating damage done
    def geteffectiveness(self, customove:Moves, objetivename:Pokemon):
        attacker = customove.type
        defender = objetivename.type

    # To acomplish this we have a json that lists all the possible relations between types     
        for type in data: 
            if(type == attacker): 
                effectiveness = [data[attacker][defender]]
                self.effectiveness = float(effectiveness[0])
        if(self.effectiveness==2):
            print("El ataque fue muy efectivo daño*2")
        if(self.effectiveness==0):
            print("El ataque fue completamente negado daño=0")
        if(self.effectiveness==0.5):
            print("El ataque fue poco efectivo daño*0.5")    

    # In this case we take customname as the attacker and objetivename as defender 
    # and deal a certain amount of damage meaning substracting said damage from the defenders hp
    # the amount of damage depends on the moves power and in how effective it is

    # for example if we choose a electric type move with 100 power against a water type defender
    # the damage will be (power*effectiveness) = (100*2) = 200, sice electric is strong against water

    def attack_pokemon(self,customname: Pokemon, objetivename: Pokemon, a: int):
        print("Atacando a " + objetivename.name + " su vida actual es " + str(objetivename.hp))
        objetivename.showlife()

        # A random value between 0 and a 100 is created and if 
        # it is in range of the moves acuracy the attack is valid if not the attack is a miss
        chvalue = random.randint(0, 100)
        startinghp = objetivename.hp
        if(a=="1"):          
            if(chvalue <= customname.move1.acuracy):
                print(customname.name + " usa " + customname.move1.movename )
                self.geteffectiveness(customname.move1,objetivename)
                objetivename.hp = objetivename.hp - customname.move1.power*self.effectiveness
        if(a=="2"):
            if(chvalue <= customname.move2.acuracy):
                print(customname.name + " usa " + customname.move2.movename )
                self.geteffectiveness(customname.move2,objetivename)
                objetivename.hp = objetivename.hp - customname.move2.power*self.effectiveness
        if(a=="3"):
            if(chvalue <= customname.move3.acuracy):
                print(customname.name + " usa " + customname.move3.movename )
                self.geteffectiveness(customname.move3,objetivename)
                objetivename.hp = objetivename.hp - customname.move3.power*self.effectiveness
        if(a=="4"):
            if(chvalue <= customname.move4.acuracy):
                print(customname.name + " usa " + customname.move4.movename ) 
                self.geteffectiveness(customname.move4,objetivename)
                objetivename.hp = objetivename.hp - customname.move4.power*self.effectiveness                       

        if(startinghp == objetivename.hp):
            print("Mala suerte Ataque fallido\n") 
        else:
             # If the attack is valid the updated health of the defender is displayed
            print("Ataque exitoso\nVida restante de "+ objetivename.name + ": " + str(objetivename.hp)) 
            objetivename.showlife()
        if(objetivename.hp <= 0):
            objetivename.knocked = True
            print ("POKEMON NOCKEADO\n")

# The json is loaded once
f = open('type-chart.json')
data = json.load(f)
# Creates a Match instance starting the game
torneo = Match()

# I do not know why organizing the modules didnt work if this comment is gone then its solved