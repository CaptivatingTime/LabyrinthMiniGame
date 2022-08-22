import sys, os


def main():

    print(" You woke up in mysterious place.\n Everything around you seems familiar yet unknown.\n All you know is that you take one step at a time,\n if it is right one - good, if not - you are out of lives.\n")

    again = True
    reason = "Wrong move,"

    while again == True:
        try:
            Map.show()
            choice = choice2dr("up","right")
            Move.up(choice, "up")
            if Move.isSafe != True: sys.exit(1)

            choice = choice2dr("up","right")
            Move.up(choice, "up")
            if Move.isSafe != True: sys.exit(1)

            choice = choice2dr("up","right")
            Move.up(choice, "up")
            if Move.isSafe != True: sys.exit(1)

            choice = choice2dr("up","right")
            Move.right(choice, "right")
            if Move.isSafe != True: sys.exit(1)

            choice = choice3dr("up","right", "down")
            Move.right(choice, "right")
            if Move.isSafe != True: sys.exit(1)

            choice = choice3dr("up","right", "down")
            Move.down(choice, "down")
            if Move.isSafe != True: sys.exit(1)

            choice = choice3dr("left","right", "down")
            Move.right(choice, "right")
            if Move.isSafe != True: sys.exit(1)

            choice = choice2dr("up","down")
            Move.down(choice, "down")
            if Move.isSafe != True: sys.exit(1)

            choice = choice3dr("left","right", "down")
            Move.right(choice, "right")
            if Move.isSafe != True: sys.exit(1)

            choice = choice3dr("up","right", "down")
            Move.up(choice, "up")
            if Move.isSafe != True: sys.exit(1)

            choice = choice2dr("up","up")
            Move.up(choice, "up")
            if Move.isSafe != True: sys.exit(1)

            choice = choice2dr("up","left")
            Move.up(choice, "up")
            if Move.isSafe != True: sys.exit(1)

            choice = choice2dr("left","up")
            Move.left(choice, "left") 
            if Move.isSafe != True: sys.exit(1)

            choice = choice3dr("left","up", "down")
            Move.up(choice, "up")
            if Move.isSafe != True: sys.exit(1)

            choice = choice2dr("left","right")
            Move.right(choice, "right")
            if Move.isSafe != True: sys.exit(1)

            print("\nYou actualy did it!\n")
            print("|-|-|-|$|$|\n\
    |-|-|-|$|$|\n\
    |$|$|$|-|$|\n\
    |$|-|$|$|$|\n\
    |$|-|-|$|$|\n\
    |x|-|-|-|-|\n")
            Move.isSafe = False
            reason = "You did it! "
            if Move.isSafe != True: sys.exit(1)
  
        except:
           yorn = input(reason + "Try again? (y/n)\n")
           if yorn == "y":
               restart()
           else:
               again = False
               print("We will meet soon enough again!")

class Map:
    update = [["|-|","-|","-|","-|","F|"],
      ["|-|","-|","-|","-|","-|"],
      ["|-|","-|","-|","-|","-|"],
      ["|-|","-|","-|","-|","-|"],
      ["|-|","-|","-|","-|","-|"],
      ["|x|","-|","-|","-|","-|"]]
    def show():
     for r in Map.update:
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
            Map.update[cordX-1][cordY] = "|*|"
        else:
            Map.update[cordX-1][cordY] = "*|"
       
    elif direction == "right":
        Map.update[cordX][cordY + 1] = "*|"

    elif direction == "down":
        Map.update[cordX + 1][cordY] = "*|"

    elif direction == "left":
        Map.update[cordX][cordY - 1] = "*"



def removePath (direction,cordX,cordY):
    
    if direction == "up":
        if cordY < 4:
            Map.update[cordX-1][cordY] = "| |"
        else:
            Map.update[cordX-1][cordY] = " |"
       
    elif direction == "right":
        if cordX == 2 and cordY == -1:
            Map.update[cordX][cordY + 1] = "|  "
        else:
            Map.update[cordX][cordY + 1] = "  "

    elif direction == "down":
        Map.update[cordX + 1][cordY] = " |"

    elif direction == "left":
        Map.update[cordX][cordY - 1] = "  |"


    
class Move:
    isSafe = True
    cordX = 5
    cordY = 0
    def up(decision, correct):
        if decision == correct:
            mapUpdate(decision, Move.cordX, Move.cordY)
            removePath(decision,Move.cordX + 1, Move.cordY)
            Map.show()
            Move.cordX = Move.cordX - 1
        else:
           Move.isSafe = False
            

    def right(decision, correct):
        if decision == correct:
            mapUpdate(decision, Move.cordX, Move.cordY)
            removePath(decision,Move.cordX, Move.cordY - 1)
            Map.show()
            Move.cordY = Move.cordY + 1
        else:
            Move.isSafe = False

    def down(decision, correct):
        if decision == correct:
            mapUpdate(decision, Move.cordX, Move.cordY)
            removePath(decision,Move.cordX - 1, Move.cordY)
            Map.show()
            Move.cordX = Move.cordX + 1
        else:
            Move.isSafe = False

    def left(decision, correct):
        if decision == correct:
            mapUpdate(decision, Move.cordX, Move.cordY)
            removePath(decision,Move.cordX, Move.cordY + 1)
            Map.show()
            Move.cordY = Move.cordY - 1
        else:
            Move.isSafe = False
            
        
def restart():
    Move.cordX = 5
    Move.cordY = 0
    Move.isSafe = True
    Map.update = [["|-|","-|","-|","-|","F|"],
      ["|-|","-|","-|","-|","-|"],
      ["|-|","-|","-|","-|","-|"],
      ["|-|","-|","-|","-|","-|"],
      ["|-|","-|","-|","-|","-|"],
      ["|x|","-|","-|","-|","-|"]]


if __name__ == "__main__":
    main()
