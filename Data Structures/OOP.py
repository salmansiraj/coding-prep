# Chess Board Example
class Board:
    def __init__(self) -> None:
        self.board[['-' for i in range(8)] for j in range(8)]


class Piece:
    def __init__(self, name) -> None:
        self.name = name

    def move(self, from, to):
        pass

    def capture(self, from, to):
        pass


# Pass base clasee in class parenthesis
class Pawn(Piece):
    # Will need to construct Piece object init in base object
    def __init__(self, name) -> None:
        Piece.__init__(self, name)

    def move(self, from, to):
        # If starting block, move up two else move one
        pass

    def capture(self, from, to):
        # captures diagonally
        pass
