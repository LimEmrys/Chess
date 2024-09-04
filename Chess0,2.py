letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
white_pieces = []
black_pieces = []

class Pieces:
    def __init__ (self, posX, posY, piece, code, state):
        self.posX = posX
        self.posY = posY
        self.piece = piece
        self.code = code
        self.state = state

white_pieces.append(Pieces ("a", 2, "White Pawn", "WP", "Alive"))
white_pieces.append(Pieces ("b", 2, "White Pawn", "WP", "Alive"))
white_pieces.append(Pieces ("c", 2, "White Pawn", "WP", "Alive"))
white_pieces.append(Pieces ("d", 2, "White Pawn", "WP", "Alive"))
white_pieces.append(Pieces ("e", 2, "White Pawn", "WP", "Alive"))
white_pieces.append(Pieces ("f", 2, "White Pawn", "WP", "Alive"))
white_pieces.append(Pieces ("g", 2, "White Pawn", "WP", "Alive"))
white_pieces.append(Pieces ("h", 2, "White Pawn", "WP", "Alive"))
white_pieces.append(Pieces ("a", 1, "White Rook", "WR", "Alive"))
white_pieces.append(Pieces ("b", 1, "White Horse", "WH", "Alive"))
white_pieces.append(Pieces ("c", 1, "White Bishop", "WB", "Alive"))
white_pieces.append(Pieces ("d", 1, "White King", "WK", "Safe"))
white_pieces.append(Pieces ("e", 1, "White Queen", "WQ", "Alive"))
white_pieces.append(Pieces ("f", 1, "White Bishop", "WB", "Alive"))
white_pieces.append(Pieces ("g", 1, "White Horse", "WH", "Alive"))
white_pieces.append(Pieces ("h", 1, "White Rook", "WR", "Alive"))

black_pieces.append(Pieces ("a", 7, "Black Pawn", "BP", "Alive"))
black_pieces.append(Pieces ("b", 7, "Black Pawn", "BP", "Alive"))
black_pieces.append(Pieces ("c", 7, "Black Pawn", "BP", "Alive"))
black_pieces.append(Pieces ("d", 7, "Black Pawn", "BP", "Alive"))
black_pieces.append(Pieces ("e", 7, "Black Pawn", "BP", "Alive"))
black_pieces.append(Pieces ("f", 7, "Black Pawn", "BP", "Alive"))
black_pieces.append(Pieces ("g", 7, "Black Pawn", "BP", "Alive"))
black_pieces.append(Pieces ("h", 7, "Black Pawn", "BP", "Alive"))
black_pieces.append(Pieces ("a", 8, "Black Rook", "BR", "Alive"))
black_pieces.append(Pieces ("b", 8, "Black Horse", "BH", "Alive"))
black_pieces.append(Pieces ("c", 8, "Black Bishop", "BB", "Alive"))
black_pieces.append(Pieces ("d", 8, "Black Queen", "BQ", "Alive"))
black_pieces.append(Pieces ("e", 8, "Black King", "BK", "Safe"))
black_pieces.append(Pieces ("f", 8, "Black Bishop", "BB", "Alive"))
black_pieces.append(Pieces ("g", 8, "Black Horse", "BH", "Alive"))
black_pieces.append(Pieces ("h", 8, "Black Rook", "BR", "Alive"))

def render():
    print ("_________________________")
    for i in range(8):
        row = "|"
        for idx in range(8):
            skip = 0
            for ind in range(16):
                if white_pieces[ind].posY == i + 1 and white_pieces[ind].posX == letters[idx]:
                    row = row + white_pieces[ind].code
                    row = row + "|"
                    skip = 1
            
            if skip == 0:
                for ind in range(16):
                    if black_pieces[ind].posY == i + 1 and black_pieces[ind].posX == letters[idx]:
                        row = row + black_pieces[ind].code
                        row = row + "|"
                        skip = 1
                        
            if skip == 0:
                row = row + "  |"
                
        print (row)
        print ("_________________________")

render()
