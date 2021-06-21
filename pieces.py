class Piece():
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Pawn(Piece):
    def __init__(self, row, col):
        super().__init__(row, col)

class wPawn(Pawn):
    def __init__(self, row, col):
        super().__init__(row, col)
    
class bPawn(Pawn):
    def __init__(self, row, col):
        super().__init__(row, col)

class Bishop(Piece):
    def __init__(self, row, col):
        super().__init__(row, col)

class wBishop(Bishop):
    def __init__(self, row, col):
        super().init(row, col)
    
class bBishop(Bishop):
    def __init__(self, row, col):
        super().__init__(row, col)

class Knight(Piece):
    def __init__(self, row, col):
        super().__init__(row, col)

class wKnight(Knight):
    def __init__(self, row, col):
        super().__init__(row, col)

class bKnight(Knight):
    def __init__(self, row, col):
        super().__init__(row, col)

class Queen(Piece):
    def __init__(self, row, col):
        super().__init__(row, col)

class wQueen(Queen):
    def __init__(self, row, col):
        super().__init__(row, col)

class bQueen(Queen):
    def __init__(self, row, col):
        super().__init__(row, col)
    
class King(Piece):
    def __init__(self, row, col):
        super().__init__(row, col)

class wKing(King):
    def __init__(self, row, col):
        super().__init__(row, col)

class bKing(King):
    def __init__(self, row, col):
        super().__init__(row, col)

