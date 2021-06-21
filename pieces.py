class Piece():
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour

class Pawn(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)

class Bishop(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)

class Knight(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)

class Queen(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
    
class King(Piece):
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
