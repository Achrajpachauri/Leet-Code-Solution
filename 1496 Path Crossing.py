
def d():
    
    path = "NES"

    moves = {

    "N": (0, 1),
    "S": (0, -1),
    "W": (-1, 0),
    "E": (1, 0)
    }

    visited = {(0, 0)}
    x = 0
    y = 0

    for c in path:
        # print("Move")
        dx, dy = moves[c]
        #print(moves[c])
        x += dx
        y += dy
        #print("visited")
        if (x, y) in visited:
            #print(visited)
            return True
        

    visited.add((x, y))

    return False

s=d()
print(s)