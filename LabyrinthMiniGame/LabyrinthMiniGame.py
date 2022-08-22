

map = [["|-|","-|","-|","-|","F|"],
       ["|-|","-|","-|","-|","-|"],
       ["|-|","-|","-|","-|","-|"],
       ["|-|","-|","-|","-|","-|"],
       ["|-|","-|","-|","-|","-|"],
       ["|x|","-|","-|","-|","-|"]]

def showMap():
    for r in map:
     for c in r:
      print(c,end="")
     print()


def choice2dr(dir1, dir2):
    decision = input ("You have two choses - " + dir1 + " or " + dir2 + "." + " Chose!\n ")
    return decision

def choice3dr(dir1, dir2, dir3):
    decision = input ("You have three choses - " + dir1 + ", " + dir2 + " or " + dir3 + "." + " Chose!\n ")
    return decision



def mapUpdate (direction,cordX,cordY):
    
    if direction == "up":
        if cordY < 4:
            map[cordX-1][cordY] = "|*|"
        else:
            map[cordX-1][cordY] = "*|"
       
    elif direction == "right":
        map[cordX][cordY + 1] = "*|"

    elif direction == "down":
        map[cordX + 1][cordY] = "*|"

    elif direction == "left":
        map[cordX][cordY - 1] = "*"



def removePath (direction,cordX,cordY):
    
    if direction == "up":
        if cordY < 4:
            map[cordX-1][cordY] = "| |"
        else:
            map[cordX-1][cordY] = " |"
       
    elif direction == "right":
        if cordX == 2 and cordY == -1:
            map[cordX][cordY + 1] = "|  "
        else:
            map[cordX][cordY + 1] = "  "

    elif direction == "down":
        map[cordX + 1][cordY] = " |"

    elif direction == "left":
        map[cordX][cordY - 1] = "  |"


    
class Move:
    cordX = 5
    cordY = 0
    def up(decision, correct):
        if decision == correct:
            mapUpdate(decision, Move.cordX, Move.cordY)
            removePath(decision,Move.cordX + 1, Move.cordY)
            showMap()
            Move.cordX = Move.cordX - 1
            

    def right(decision, correct):
        if decision == correct:
            mapUpdate(decision, Move.cordX, Move.cordY)
            removePath(decision,Move.cordX, Move.cordY - 1)
            showMap()
            Move.cordY = Move.cordY + 1

    def down(decision, correct):
        if decision == correct:
            mapUpdate(decision, Move.cordX, Move.cordY)
            removePath(decision,Move.cordX - 1, Move.cordY)
            showMap()
            Move.cordX = Move.cordX + 1

    def left(decision, correct):
        if decision == correct:
            mapUpdate(decision, Move.cordX, Move.cordY)
            removePath(decision,Move.cordX, Move.cordY + 1)
            showMap()
            Move.cordY = Move.cordY - 1
            
        


print(" You woke up in mysterious place.\n Everything around you seems familiar yet unknown.\n All you know is that you take one step at a time,\n if it is right one - good, if not - you are no more\n")

for r in map:
 for c in r:
  print(c,end="")
 print()



choice = choice2dr("up","right")
Move.up(choice, "up")

choice = choice2dr("up","right")
Move.up(choice, "up")

choice = choice2dr("up","right")
Move.up(choice, "up")

choice = choice2dr("up","right")
Move.right(choice, "right")

choice = choice3dr("up","right", "down")
Move.right(choice, "right")

choice = choice3dr("up","right", "down")
Move.down(choice, "down")

choice = choice3dr("left","right", "down")
Move.right(choice, "right")

choice = choice2dr("up","down")
Move.down(choice, "down")

choice = choice3dr("left","right", "down")
Move.right(choice, "right")

choice = choice3dr("up","right", "down")
Move.up(choice, "up")

choice = choice2dr("up","up")
Move.up(choice, "up")

choice = choice2dr("up","left")
Move.up(choice, "up")

choice = choice2dr("left","up")
Move.left(choice, "left")    

choice = choice3dr("left","up", "down")
Move.up(choice, "up")

choice = choice2dr("left","right")
Move.right(choice, "right")

