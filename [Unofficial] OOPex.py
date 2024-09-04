letters = ["a","b","c","d","e","f","g","h"]

class Pieces:
    def __init__ (self, posX, posY, piece):
        self.posX = posX
        self.posY = posY
        self.piece = piece

    def __str__ (self):
        return f"{self.piece}: {self.posY}{self.posX}"

    def move(self):
        if self.piece == "Black Pawn" or "White Pawn":
            self.posX += 1

    def kill(self):
        if self.piece == "Black Pawn" or "White Pawn":
            self.posX += 1
            self.posY = letters[letters.index(self.posY) + 1]

    def upgrade(self):
        if self.piece == "Black Pawn":
            self.piece = "Black Queen"
        elif self.piece == "White Pawn":
            self.piece = "White Queen"
        
p1 = Pieces (2,"a","Black Pawn")

print(p1)
p1.move()
print(p1)
p1.kill()
print(p1)
p1.upgrade()
print(p1)
