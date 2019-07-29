from itertools import combinations

with open("data.txt", "r") as f:
    raw_data = f.read().split("\n")

n = int(raw_data[0])

data = [list(map(int, x.split())) for x in raw_data[1:1 + n]], [list(map(int, x.split())) for x in
                                                                raw_data[1 + n:1 + 2 * n]]

screen = [[0] * n for _ in range(n)]


def getRow(isHorizontal, row):
    if isHorizontal == 0:
        return [screen[x][row] for x in range(n)]
    else:
        return [screen[row][x] for x in range(n)]


def isValid(origin, new):
    return not any([origin[x] * new[x] == -1 for x in range(n)])


def dtorow(dt, bl):
    _ret = []
    bl[0] -= 1
    bl[-1] -= 1
    while (dt or bl):
        if bl:
            _ret += [-1] * bl[0]
            bl = bl[1:]
        if dt:
            _ret += [1] * dt[0]
            dt = dt[1:]
    return _ret


def getPs(d):
    def getDelta(x):
        for i in range(len(x) - 1):
            yield x[i + 1] - x[i]

    l = n - (sum(d) + len(d) - 1)
    return list(map(lambda x: dtorow(d, list(getDelta([-1] + list(x) + [len(d) + l]))),
                    combinations(range(len(d) + l), len(d))))


def getValidPs(d, o):
    return [x for x in getPs(d) if isValid(x, o)]


def updateRow(isHorizontal, r):
    row = getRow(isHorizontal, r)
    tdata = data[1 - isHorizontal][r]
    vps = getValidPs(tdata, row)
    isY = [True] * n
    isN = [True] * n
    for ps in vps:
        for i in range(n):
            isY[i] = isY[i] and ps[i] == 1
            isN[i] = isN[i] and ps[i] == -1
    _ret = row
    for i in range(n):
        if isY[i]: _ret[i] = 1
        if isN[i]: _ret[i] = -1

    if isHorizontal == 0:
        for x in range(n):
            screen[x][r] = _ret[x]
    else:
        for x in range(n):
            screen[r][x] = _ret[x]


def updateScr():
    for i in range(n):
        updateRow(0, i)
    for i in range(n):
        updateRow(1, i)
    drawScr()


def drawScr(strlist="■□x"):
    for y in range(n):
        for x in range(n):
            if screen[x][y] == 1:
                print(strlist[0] + " ", end="")
            elif screen[x][y] == 0:
                print(strlist[1] + " ", end="")
            elif screen[x][y] == -1:
                print(strlist[2] + " ", end="")
        print("")
    print("=" * 10)


def solve():
    while any([0 in x for x in screen]):
        updateScr()
    drawScr("■  ")

solve()