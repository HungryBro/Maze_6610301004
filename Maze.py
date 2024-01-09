import os
import keyboard
import time
from collections import deque

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
    
    def find_path_to_end(self):
        visited = set()
        queue = deque([(self.ply.y, self.ply.x, [])])

        while queue:
            y, x, path = queue.popleft()
            if (y, x) in visited:
                continue

            visited.add((y, x))

            if (y, x) == (self.end.y, self.end.x):
                return path

            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_y, next_x = y + dy, x + dx

                if not self.isInBound(next_y, next_x):
                    continue

                if self.maze[next_y][next_x] in ['X', 'P']:
                    continue

                new_path = path + [(next_y, next_x)]
                queue.append((next_y, next_x, new_path))

        return None
    
    def auto_move_to_end(self):
        path = self.find_path_to_end()
        if path:
            for y, x in path:
                self.maze[self.ply.y][self.ply.x] = " "
                self.ply = pos(y, x)
                self.maze[y][x] = "P"
                time.sleep(0.25)
                self.print()
                if (y, x) == (self.end.y, self.end.x):
                    self.printEND()
                    break

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
        if keyboard.is_pressed("q"): # click q to exit program
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

        if keyboard.is_pressed("p"): # click p to auto walk
            m.auto_move_to_end()
            break