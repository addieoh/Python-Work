rules = 'RL'
size = 1

class Turn: L, R = False, True

def run_langton(rules, size):
    x = size // 2
    y = size // 2
    dir = 0
    
    Colors = list(rules)
    ruleList = []
    for i in Colors:
        ruleList.append([i])
    for i in range(len(ruleList)):
        ruleList[i].append(i)

    grid = [[0] * size for i in range(size)]

    i = 0
    while (x < size) and (x >= 0) and (y < size) and (y >= 0):

        z = grid[y][x]
        z += 1
        z = z % len(Colors)
        grid[y][x] = z
        
        if dir == 0:
            y -= 1
        elif dir == 1:
            x += 1
        elif dir == 2:
            y += 1
        elif dir == 3:
            x -= 1
        else:
            assert False

        i += 1

        if (x >= size) or (x < 0) or (y >= size) or (y < 0):
            break

        z2 = grid[y][x]
        if ruleList[z2][0] == 'L':
            if dir == 0:
                dir = 3
            else:
                dir = dir - 1
        else:
            if dir == 3:
                dir = 0
            else:
                dir = dir + 1


    count = i
    return (count, grid)
