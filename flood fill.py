from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

#wow seems like a new method

def flood_fill(input_board: list[str], old: str, new: str, x: int, y: int) -> list[str]:
    for row in input_board:
        col = list(row)
        for i in col:
            i = new
            row = ''.join(col)
        if x > 0 and x <= len(input_board) and y > 0 and y <= len(input_board[x]) and input_board[x][y] == old:
        return input_board
                
 
modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)


# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....
