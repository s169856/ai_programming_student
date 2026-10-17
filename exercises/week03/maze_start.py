"""
Oefening 3: Maze met DFS
=========================
Implementeer DFS om een weg door het maze te vinden.
"""
import numpy as np


class Maze:
    def __init__(self, size, start, end, walls):
        self.size = size
        self.start = start
        self.end = end
        self.maze = np.zeros(size, dtype=str)
        self.maze[:, :] = '.'
        self.maze[start] = 'S'
        self.maze[end] = 'E'
        for wall in walls:
            self.maze[wall] = '#'

    def valid_moves(self, current):
        # TODO: geef lijst van (rij,kolom)-coördinaten die geldig zijn
        
        col, row = current

        moves =  [[-1, 0], [1, 0], [0, 1], [0, -1]] # links, rechts, boven, onder
        geldige_moves = []
        
        for col_move, row_move in moves:
            new_col_pos = col - col_move
            new_row_pos = row - row_move

            if 0 <= new_col_pos <= 9 and 0 <= new_row_pos <= 9 and self.maze[new_row_pos, new_col_pos] != "#":
                geldige_moves.append((new_row_pos, new_col_pos))

        return geldige_moves

    def extract_path(self, stack):
        # TODO: haal het pad uit de stack van start tot end
        pad = []

        for pos in stack:
            pad.append(pos)
            if pos == self.end:
                break

        return pad

    def print_maze(self):
        for row in self.maze:
            print(' '.join(row))

def find_path(maze):
    # TODO: implementeer DFS met een stack
    stack = [maze.start]
    parent = {maze.start: None}
    visited = {maze.start}

    while stack:
        current = stack.pop()
        if current == maze.end:
            pad = []
            stap = current

            while stap is not None:
                pad.append(stap)
                stap = parent[stap]

            pad.reverse()
            return (pad, len(pad) - 1)

        for buur in maze.valid_moves(current):
            if buur not in visited:
                visited.add(buur)
                parent[buur] = current
                stack.append(buur)

    return (None, 0)


if __name__ == "__main__":
    maze_size = (10, 10)
    start_point = (0, 0)
    end_point = (9, 9)
    walls = [(2, 1), (2, 2), (2, 3), (4, 6), (6, 6), (7, 6), (8, 6),
             (4, 7), (4, 8), (2, 2), (5, 2), (6, 2), (4, 2), (3, 2),
             (8, 0), (9, 6), (1, 8), (2, 8), (6, 9), (7, 9),
             (3, 6), (3, 7), (4, 1), (5, 1)]

    my_maze = Maze(maze_size, start_point, end_point, walls)
    pad, stappen = find_path(my_maze)

    my_maze.print_maze()
    print("Pad:", pad)
    print("Stappen:", stappen)