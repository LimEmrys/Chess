letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
red_pieces = []
green_pieces = []

class Pieces:
    def __init__ (self, posX, posY, piece, code, state):
        self.posX = posX
        self.posY = posY
        self.piece = piece
        self.code = code
        self.state = state

red_pieces.append(Pieces ("a", 4, "Red Soldier", "RS", "Alive"))
red_pieces.append(Pieces ("c", 4, "Red Soldier", "RS", "Alive"))
red_pieces.append(Pieces ("e", 4, "Red Soldier", "RS", "Alive"))
red_pieces.append(Pieces ("g", 4, "Red Soldier", "RS", "Alive"))
red_pieces.append(Pieces ("i", 4, "Red Soldier", "RS", "Alive"))
red_pieces.append(Pieces ("b", 3, "Red Cannon", "RC", "Alive"))
red_pieces.append(Pieces ("h", 3, "Red Cannon", "RC", "Alive"))
red_pieces.append(Pieces ("a", 1, "Red Chariot", "RR", "Alive"))
red_pieces.append(Pieces ("b", 1, "Red Horse", "RH", "Alive"))
red_pieces.append(Pieces ("c", 1, "Red Elephant", "RE", "Alive"))
red_pieces.append(Pieces ("d", 1, "Red Advisor", "RA", "Alive"))
red_pieces.append(Pieces ("e", 1, "Red General", "RG", "Safe"))
red_pieces.append(Pieces ("f", 1, "Red Advisor", "RA", "Alive"))
red_pieces.append(Pieces ("g", 1, "Red Elephant", "RE", "Alive"))
red_pieces.append(Pieces ("h", 1, "Red Horse", "RH", "Alive"))
red_pieces.append(Pieces ("i", 1, "Red Chariot", "RC", "Alive"))

green_pieces.append(Pieces ("a", 7, "Green Soldier", "GS", "Alive"))
green_pieces.append(Pieces ("c", 7, "Green Soldier", "GS", "Alive"))
green_pieces.append(Pieces ("e", 7, "Green Soldier", "GS", "Alive"))
green_pieces.append(Pieces ("g", 7, "Green Soldier", "GS", "Alive"))
green_pieces.append(Pieces ("i", 7, "Green Soldier", "GS", "Alive"))
green_pieces.append(Pieces ("b", 8, "Green Cannon", "GC", "Alive"))
green_pieces.append(Pieces ("h", 8, "Green Cannon", "GC", "Alive"))
green_pieces.append(Pieces ("a", 10, "Green Chariot", "GR", "Alive"))
green_pieces.append(Pieces ("b", 10, "Green Horse", "GH", "Alive"))
green_pieces.append(Pieces ("c", 10, "Green Elephant", "GE", "Alive"))
green_pieces.append(Pieces ("d", 10, "Green Advisor", "GA", "Alive"))
green_pieces.append(Pieces ("e", 10, "Green General", "GG", "Safe"))
green_pieces.append(Pieces ("f", 10, "Green Advisor", "GA", "Alive"))
green_pieces.append(Pieces ("g", 10, "Green Elephant", "GE", "Alive"))
green_pieces.append(Pieces ("h", 10, "Green Horse", "GH", "Alive"))
green_pieces.append(Pieces ("i", 10, "Green Chariot", "GR", "Alive"))

def render():
    print ("____________________________")
    for i in range(10):
        row = "|"
        for idx in range(9):
            skip = 0
            for ind in range(16):
                if red_pieces[ind].posY == i + 1 and red_pieces[ind].posX == letters[idx]:
                    row = row + red_pieces[ind].code
                    row = row + "|"
                    skip = 1
            
            if skip == 0:
                for ind in range(16):
                    if green_pieces[ind].posY == i + 1 and green_pieces[ind].posX == letters[idx]:
                        row = row + green_pieces[ind].code
                        row = row + "|"
                        skip = 1
                        
            if skip == 0:
                row = row + "  |"
                
        print (row)
        print ("____________________________")

render()
