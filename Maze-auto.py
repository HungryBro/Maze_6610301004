import os
import keyboard
import time

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def auto_move(self):
        while True:
            if self.ply.y == self.end.y and self.ply.x == self.end.x:
                self.printEND()
                break

            # Calculate distances based on only empty cells
            dist_up = self.calculate_distance(self.ply.y - 1, self.ply.x)
            dist_down = self.calculate_distance(self.ply.y + 1, self.ply.x)
            dist_left = self.calculate_distance(self.ply.y, self.ply.x - 1)
            dist_right = self.calculate_distance(self.ply.y, self.ply.x + 1)

            # Check if moving left or right is possible and has a shorter distance
            if self.isInBound(self.ply.y, self.ply.x - 1) and self.maze[self.ply.y][self.ply.x - 1] == " " and dist_left < dist_up and dist_left < dist_down:
                self.move_left()
            elif self.isInBound(self.ply.y, self.ply.x + 1) and self.maze[self.ply.y][self.ply.x + 1] == " " and dist_right < dist_up and dist_right < dist_down:
                self.move_right()
            # If not possible or not shorter distance, move in the direction of the shortest distance
            elif dist_up <= dist_down and dist_up <= dist_left and dist_up <= dist_right:
                self.move_up()
            elif dist_down <= dist_left and dist_down <= dist_right:
                self.move_down()
            elif dist_left <= dist_right:
                self.move_left()
            else:
                self.move_right()

            self.print()
            time.sleep(0.25)

        def calculate_distance(self, y, x):
            if not self.isInBound(y, x) or self.maze[y][x] == "X":
                return float('inf')  # If out of bounds or a wall, return infinity
            return abs(y - self.end.y) + abs(x - self.end.x)

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None

    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x


if __name__ == '__main__':
    m = maze()
    m.print()

    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        if keyboard.is_pressed("w"):
            if m.move_up():
                m.print()
            else:
                break
        if keyboard.is_pressed("s"):
            if m.move_down():
                m.print()
            else:
                break
        if keyboard.is_pressed("a"):
            if m.move_left():
                m.print()
            else:
                break
        if keyboard.is_pressed("d"):
            if m.move_right():
                m.print()
            else:
                break
        if keyboard.is_pressed("o"):
            m.auto_move()