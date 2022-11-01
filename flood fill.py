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

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    def dfs(a: int, b: int):
        if (
            a >= 0 
            and a < len(input_board)
            and b >= 0
            and b < len(input_board[0])
            and input_board[a][b] == old
        ):
        
            input_board[a][b] == new
            dfs(a + 1, b)
            dfs(a - 1, b)
            dfs(a, b + 1)
            dfs(a, b - 1)
     

    dfs(x, y)
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
