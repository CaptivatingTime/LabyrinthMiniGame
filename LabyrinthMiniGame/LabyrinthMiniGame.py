
step = 1
def choice2d(dir1, dir2):
    decision = input ("You have two choses - " + dir1 + " or " + dir2 + "." + " Chose!\n ")
    return decision

def choice3d(dir1, dir2, dir3):
    decision = input ("You have two choses - " + dir1 + ", " + dir2 + " or " + dir3 + "." + " Chose!\n ")
    return decision

def mapUpdate (steps):
    
    
    if steps == 1:
        print("\nGood you live.....for now\n")
        print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
|-|-|-|-|-|\n\
|-|-|-|-|-|\n\
|*|-|-|-|-|\n\
|x|-|-|-|-|\n")
    elif steps == 2:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
|-|-|-|-|-|\n\
|*|-|-|-|-|\n\
| |-|-|-|-|\n\
|x|-|-|-|-|\n")
    elif steps == 3:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
|*|-|-|-|-|\n\
| |-|-|-|-|\n\
| |-|-|-|-|\n\
|x|-|-|-|-|\n")
    elif steps == 4:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
| |*|-|-|-|\n\
| |-|-|-|-|\n\
| |-|-|-|-|\n\
|x|-|-|-|-|\n")
    elif steps == 5:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
| | |*|-|-|\n\
| |-|-|-|-|\n\
| |-|-|-|-|\n\
|x|-|-|-|-|\n")
    elif steps == 6:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
| | | |-|-|\n\
| |-|*|-|-|\n\
| |-|-|-|-|\n\
|x|-|-|-|-|\n")
    elif steps == 7:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
| | | |-|-|\n\
| |-| |*|-|\n\
| |-|-|-|-|\n\
|x|-|-|-|-|\n")
    elif steps == 8:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
| | | |-|-|\n\
| |-| | |-|\n\
| |-|-|*|-|\n\
|x|-|-|-|-|\n")
    elif steps == 9:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
| | | |-|-|\n\
| |-| | |-|\n\
| |-|-| |*|\n\
|x|-|-|-|-|\n")
    elif steps == 10:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
| | | |-|-|\n\
| |-| | |*|\n\
| |-|-| | |\n\
|x|-|-|-|-|\n")
    elif steps == 11:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
| | | |-|*|\n\
| |-| | | |\n\
| |-|-| | |\n\
|x|-|-|-|-|\n")
    elif steps == 12:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|-|*|\n\
| | | |-| |\n\
| |-| | | |\n\
| |-|-| | |\n\
|x|-|-|-|-|\n")
    elif steps == 13:
          print("\nGood you live.....for now\n")
          print("|-|-|-|-|F|\n\
|-|-|-|*| |\n\
| | | |-| |\n\
| |-| | | |\n\
| |-|-| | |\n\
|x|-|-|-|-|\n")
    elif steps == 14:
          print("\nGood you live.....for now\n")
          print("|-|-|-|*|F|\n\
|-|-|-| | |\n\
| | | |-| |\n\
| |-| | | |\n\
| |-|-| | |\n\
|x|-|-|-|-|\n")
    elif steps == 15:
          print("\nYou actualy did it!\n")
          print("|-|-|-|$|$|\n\
|-|-|-|$|$|\n\
|$|$|$|-|$|\n\
|$|-|$|$|$|\n\
|$|-|-|$|$|\n\
|x|-|-|-|-|\n")


def isCorrect(decision, correct):
    if decision == correct:
        mapUpdate(step)
        


print(" You woke up in mysterious place.\n Everything around you seems familiar yet unknown.\n All you know is that you take one step at a time,\n if it is right one - good, if not - you are no more\n")

print("|-|-|-|-|F|\n\
|-|-|-|-|-|\n\
|-|-|-|-|-|\n\
|-|-|-|-|-|\n\
|-|-|-|-|-|\n\
|x|-|-|-|-|\n")

step = 1


choice = choice2d("up","right")
isCorrect(choice, "up")
step = step + 1

choice = choice2d("up","right")
isCorrect(choice, "up")
step = step + 1

choice = choice2d("up","right")
isCorrect(choice, "up")
step = step + 1

choice = choice2d("up","right")
isCorrect(choice, "right")
step = step + 1

choice = choice3d("up","right", "down")
isCorrect(choice, "right")
step = step + 1

choice = choice3d("up","right", "down")
isCorrect(choice, "down")
step = step + 1

choice = choice3d("left","right", "down")
isCorrect(choice, "right")
step = step + 1

choice = choice2d("up","down")
isCorrect(choice, "down")
step = step + 1

choice = choice3d("left","right", "down")
isCorrect(choice, "right")
step = step + 1

choice = choice3d("up","right", "down")
isCorrect(choice, "up")
step = step + 1

choice = choice2d("up","up")
isCorrect(choice, "up")
step = step + 1

choice = choice2d("up","left")
isCorrect(choice, "up")
step = step + 1

choice = choice2d("left","left")
isCorrect(choice, "left")
step = step + 1       

choice = choice3d("left","up", "down")
isCorrect(choice, "up")
step = step + 1

choice = choice2d("left","right")
isCorrect(choice, "right")
step = step + 1 

