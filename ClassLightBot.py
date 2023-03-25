class LightBot:
    def __init__(self, meno_suboru, pozicia_robota):
        # read the file
        file = open(meno_suboru).readlines()

        # info 'bout the bot
        self.pozY = pozicia_robota[0]
        self.pozX = pozicia_robota[1]
        self.rot = pozicia_robota[2]  # 0 1 2 3 --> Left Down Right Up

        # map details
        mapWH = file[0].split()
        self.height = int(mapWH[0])
        self.width = int(mapWH[1])
        self.lights = [0, 0]  # off, on

        # make the map
        # every block is a list of type [type, visited] , height, on/off -->
        # type = g(ground), w(wall), l(lamp)
        # visited = bool
        # height = int --> this is added when the block is wall/ light
        # on/off = bool --> this is added only when it is a light
        self.map = []
        for h in range(self.height):  # height
            self.map.append([])
            for w in range(self.width):  # width
                self.map[h].append(["g", False, 0])  # type, visited, height
                for i in range(1, len(file)):  # info about the blocks
                    line = file[i].split()
                    if int(line[0]) == h and int(line[1]) == w:
                        if len(line) == 3:
                            self.map[h][w] = ["w", False, int(line[2])]  # type, visited, height
                        else:
                            self.map[h][w] = ["l", False, int(line[2]), False]  # type, visited, height, on/off
                            self.lights[0] += 1
        self.map[self.pozY][self.pozX][1] = True

    # done
    def robot(self):
        return self.pozY, self.pozX, self.rot

    # done
    def __str__(self):
        self.layout = ""  # num=. ,+=+, [] = o/O
        botRot = [">", "v", "<", "^"]
        for h in range(self.height):
            for w in range(self.width):
                if h == self.pozY and w == self.pozX:
                    self.layout += botRot[self.rot]
                elif self.map[h][w][0] == "l":
                    if self.map[h][w][3]:
                        self.layout += "O"
                    else:
                        self.layout += "o"
                elif self.map[h][w][1]:
                    self.layout += "+"

                else:
                    self.layout += "."
            if h < self.height - 1:
                self.layout += "\n"

        return self.layout

    def rob(self, prikazy):
        dir = [0, 0]
        for i in prikazy:
            if self.rot == 0:
                dir = [0, 1]
            elif self.rot == 1:
                dir = [1, 0]
            elif self.rot == 2:
                dir = [0, -1]
            else:
                dir = [-1, 0]

            if i == "l":
                self.rot = (self.rot - 1) % 4
            elif i == "p":
                self.rot = (self.rot + 1) % 4
            elif i == "k":
                if (self.pozY + dir[0]) not in [-1, self.height + 1] and (self.pozX + dir[1]) not in [-1, self.width + 1]:
                    if self.map[self.pozY][self.pozX][2] == self.map[self.pozY + dir[0]][self.pozX + dir[1]][2]:

                        self.pozY, self.pozX = self.pozY + dir[0], self.pozX + dir[1]
                        self.map[self.pozY][self.pozX][1] = True
            elif i == "s":
                if (self.pozY + dir[0]) not in [-1, self.height + 1] and (self.pozX + dir[1]) not in [-1, self.width + 1]:
                    if self.map[self.pozY][self.pozX][2] > self.map[self.pozY + dir[0]][self.pozX + dir[1]][2] \
                            or (self.map[self.pozY][self.pozX][2] + 1) == self.map[self.pozY + dir[0]][self.pozX + dir[1]][2]:
                        self.pozY, self.pozX = self.pozY + dir[0], self.pozX + dir[1]
                        self.map[self.pozY][self.pozX][1] = True
            elif i == "z":
                if self.map[self.pozY][self.pozX][0] == "l":
                    self.map[self.pozY][self.pozX][3] = not self.map[self.pozY][self.pozX][3]
                    if self.map[self.pozY][self.pozX][3]:
                        self.lights[0] -= 1
                        self.lights[1] += 1
                    else:
                        self.lights[0] += 1
                        self.lights[1] -= 1

    # done
    def kolko(self):
        return self.lights[0], self.lights[1]
