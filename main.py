import stack
import random as r

col: int = 4
row: int = 4
TOTAL: int = col*row
iteractions: int = 0
occupate = []
matrix = [[column for column in range(col)] for row in range(row)]

def main():
    global iteractions, occupate, col, row

    possibleCoords = [[-1,0], [0,1], [1,0], [0,-1]]

    coords = [0,0]
    occupate.append(coords)
    stack.push(coords)
    matrix[coords[0]][coords[1]] = iteractions
    print(coords)
    startMaze()

    for i in range(TOTAL-1):
        newcorods = coords
        pC = r.choice(possibleCoords)
        while newcorods[0] + pC[0] < 0 or newcorods[1] + pC[1] < 0:
            pC = r.choice(possibleCoords)
        newcorods[0] += pC[0]
        newcorods[1] += pC[1]

        coords = newcorods
        occupate.append(coords)
        stack.push(coords)
        print(coords)

def startMaze():
    pass

if __name__ == "__main__":
    main()
