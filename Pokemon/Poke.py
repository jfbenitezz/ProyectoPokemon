import csv
import random
from numpy import rint
global customname
class Moves:
    def __init__(self, index: str, movename: str, type: str, power: float, acuracy: int, pp: int):
        self.movename = movename
        self.index = index
        self.movename= movename
        self.type= type
        self.power = power
        self.acuracy = acuracy
        self.pp = pp


class Pokemon:
    def __init__(self, name: str, type: str, max_hp: float, move1:Moves, move2:Moves, move3:Moves, move4:Moves, knocked = False):
        self.name = name
        self.type = type  # water, fire, grass
        self.max_hp = max_hp
        self.hp = max_hp
        self.knocked = knocked
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4 

    def showinfopoke(self):
        print("LISTA DE ATAQUES:\n1." +
        self.move1.movename +" ELEMENTO: "+ self.move1.type +" POWER: " + str(self.move1.power) + " ACURACY:" +  str(self.move1.acuracy) +"% PP: " + str(self.move1.pp) + "\n2." +
        self.move2.movename +" ELEMENTO: "+ self.move2.type +" POWER: " + str(self.move2.power) + " ACURACY:" +  str(self.move2.acuracy) +"% PP: " + str(self.move2.pp) + "\n3." +
        self.move3.movename +" ELEMENTO: "+ self.move3.type +" POWER: " + str(self.move3.power) + " ACURACY:" +  str(self.move3.acuracy) +"% PP: " + str(self.move3.pp) + "\n4." +
        self.move4.movename +" ELEMENTO: "+ self.move4.type +" POWER: " + str(self.move4.power) + " ACURACY:" +  str(self.move4.acuracy) +"% PP: " + str(self.move4.pp)+ "\n")
    
    def showlife(self):
        bar = self.hp/10
        strbar=""
        for b in range (int(bar)):
                strbar = f"{strbar}/"
        print (strbar) 

def assignmoves(ctype,list):
    fixedrow=[]
    with open('Moves.csv', 'r') as f:
        reader = csv.reader(f)
        n = 0
        while n < 4:
         rvalue = random.randint(1, 354)
         for row in reader:
            fixedrow.append(row[0].split(","))  #Separa el csv por fila
         for col in fixedrow: #Separa cada fila por columnas
              if ((rvalue ==  int(col[0])) & ((ctype == col[2]) or ((col[2] == "Normal") & (n < 3)))):
                  #Se escoge un index al azar si el tipo de ataque es igual al del Pokemon o a tipo normal se agrega a la lista de movimientos, se garantiza al menos un ataque unico de tipo
                  list.append(Moves(col[0], col[1], col[2], float(col[3]), int(col[4]), int(col[5])))
                  n = n +1


#Rivalpokemon1 = Pokemon("Venusaur", "water", 200, "Aeroblast", "Octazooka", "False Swipe","Crabhammer")

#Le corresponde al gimnasio
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


#Le corresponde al rival
def rivals():
    movelist=[]
    assignmovesrivals(movelist,"Aeroblast", "Octazooka", "False Swipe","Crabhammer")
    Rivalpokemon1 = Pokemon("Venusaur", "water", 200, movelist[0], movelist[1], movelist[2],movelist[3])

    assignmovesrivals(movelist,"Rock Slide", "Rock Throw", "AncientPower","Rock Tomb")
    Rivalpokemon2 = Pokemon("Serpentok", "rock", 200, movelist[0], movelist[1], movelist[2],movelist[3])
    
    assignmovesrivals(movelist,"Ember", "Flamethrower", "Fire Punch","Crush Claw")
    Rivalpokemon3 = Pokemon("Charmander", "fire", 200, movelist[0], movelist[1], movelist[2],movelist[3])

    assignmovesrivals(movelist,"Astonish", "Shadow Punch", "Night Shade","Shadow Ball")
    Rivalpokemon4 = Pokemon("Gengar", "ghost", 200, movelist[0], movelist[1], movelist[2],movelist[3])


def main():

    print("BIENVENIDO A POKEMON ")
    print("Primero armemos nuestro equipo ")
    for n in range(4):
        movelist=[]
        mascotname = input("Inserte el nombre de su Pokemon: ")
        print("****************************\n"+
        "Normal *** Psychic *** Fighting\nGrass *** Water *** Fire\nGround *** Dark *** Flying"+
        "\nIce *** Ghost *** Poison *** Bug \nElectric *** Rock *** Steel *** Dragon"+
        "\n****************************\n")
        matches = ["Normal","Psychic","Fighting","Grass","Water","Fire","Ground","Dark","Flying","Ice", "Ghost", "Poison","Bug","Electric","Rock","Steel","Dragon"]
        customtype = input("Inserte su tipo de Pokemon: ")
        while not any(x in customtype.capitalize() for x in matches):
            customtype = input("TIPO NO ENCONTRADO INTENTE NUEVAMENTE\nInserte su tipo de Pokemon: ")
        else:
            max_hp = 200
            assignmoves(customtype.capitalize(), movelist)
            if(n==0):
                Mypokemon1 = Pokemon(mascotname, customtype, max_hp, movelist[0], movelist[1], movelist[2], movelist[3])
                customname = Mypokemon1
            if(n==1):
                Mypokemon2 = Pokemon(mascotname, customtype, max_hp, movelist[0], movelist[1], movelist[2], movelist[3])
                customname = Mypokemon2
            if(n==2):
                Mypokemon3 = Pokemon(mascotname, customtype, max_hp, movelist[0], movelist[1], movelist[2], movelist[3])    
                customname = Mypokemon3    
            if(n==3):
                Mypokemon4 = Pokemon(mascotname, customtype, max_hp, movelist[0], movelist[1], movelist[2], movelist[3])
                customname = Mypokemon4
        print("****POKEMON CREADO EXITOSAMENTE****")    
        print("NOMBRE " + customname.name + "\nTIPO: " + customname.type)
        customname.showinfopoke()

    print("****EQUPO COMPLETO HORA DE RETAR AL GIMNASIO****\n")
    print("****HORA DE LA BATALLA****\n")
    
    #SE MUESTRA INFO BASICA DEL OPONENTE, MUESTRA NOMBRE Y TIPO POKEMON OPONETNE
    rivals()# Crea los rivales
    movelist=[]
    assignmovesrivals(movelist,"Aeroblast", "Octazooka", "False Swipe","Crabhammer")
    Rivalpokemon1 = Pokemon("Venusaur", "water", 200, movelist[0], movelist[1], movelist[2],movelist[3])
    turnsw=0
    battlesw = 0

    print("Tu rival elige a su " + Rivalpokemon1.name + " del tipo " + Rivalpokemon1.type + "\n")
    op = input("***ESCOGE TU POKEMON INICAL****\n1."+ Mypokemon1.name + "\n2."+ Mypokemon2.name + "\n3."+ Mypokemon3.name + "\n4."+ Mypokemon4.name + "\n")
    if(op=="1"):
        customname = Mypokemon1
    if(op=="2"):
        customname = Mypokemon2
    if(op=="3"):   
        customname = Mypokemon3  
    if(op=="4"):
        customname = Mypokemon4 
    print("Eliges a " + customname.name)
#Haz la comprobacion de poner numero validos
    while(battlesw == 0):
        if(turnsw == 0):
            print("\n**** MENU OPCIONES ****\n")
            print("**** 1.ATACAR ****\n")
            print("**** 2.INVENTARIO ****\n")
            print("**** 3.CAMBIAR POKEMON****\n")
            print("**** 4. HUIR****\n")
            op = input("¿Que haras?\n")
            if(op=="1"):
                objetivename = Rivalpokemon1
                attack_pokemon(customname,objetivename)

   
#Le corresponde al entrenador
def attack_pokemon(customname: Pokemon, objetivename: Pokemon):
    print("Atacando a " + objetivename.name + " su vida actual es " + str(objetivename.hp))
    objetivename.showlife()
    customname.showinfopoke()
    a = input("\nElija un ataque\n")
    chvalue = random.randint(0, 100)
    startinghp = objetivename.hp
    if(a=="1"):
        if(chvalue <= customname.move1.acuracy):
            objetivename.hp = objetivename.hp - customname.move1.power
    if(a=="2"):
        if(chvalue <= customname.move2.acuracy):
            objetivename.hp = objetivename.hp - customname.move2.power
    if(a=="3"):
        if(chvalue <= customname.move3.acuracy):
            objetivename.hp = objetivename.hp - customname.move3.power
    if(a=="4"):
        if(chvalue <= customname.move4.acuracy):
            objetivename.hp = objetivename.hp - customname.move4.power                        

    if(startinghp == objetivename.hp):
        print("Mala suerte Ataque fallido\n") 
    else:
        print("Ataque exitoso\nVida restante de "+ objetivename.name + ": " + str(objetivename.hp)) 
        objetivename.showlife()
    if(objetivename.hp <= 0):
         objetivename.knocked = True
         print ("POKEMON ENEMIGO NOCKEADO\n") 
         


  #cuando implemente player implemento perdida pp
  #Cuando pones un ataque con numero no valido saldra como fallido

main()




