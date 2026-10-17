"""
Oefening 2: Sliding Puzzle (8-puzzle)
======================================
Implementeer de sliding puzzle en los hem op met BFS/DFS.
"""
import numpy as np
from collections import deque 

class SlidingPuzzle:
    GRIDSIZE = 3
    EMPTY = 0

    GOAL = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    def __init__(self, game):
        self.Game = np.array(game)

    def possible_new_configurations(self):
        # TODO: geef alle nieuwe configuraties door het lege vakje te verschuiven
        row, col = self.locate_empty()

        moves =  [[-1, 0], [1, 0], [0, 1], [0, -1]] # links, rechts, boven, onder
        configurations = []
        for col_move, row_move in moves:
            new_col_pos = col - col_move
            new_row_pos = row - row_move

            if (new_col_pos or new_row_pos) >= 0 and (new_col_pos or new_row_pos) <= 2:
                new_state = self.duplicate()

                new_state.Game[row][col], new_state.Game[new_row_pos][new_col_pos] = new_state.Game[new_row_pos][new_col_pos], new_state.Game[row][col]

                configurations.append(new_state)

        return configurations

    def locate_empty(self):
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return (row, col)
        raise Exception("Geen leeg vakje!")

    def manhattan_distance(self):
        # TODO: bereken de Manhattan-afstand tot de goal-configuratie
        row_goal, col_goal = 2, 2
        row_game, col_game = self.locate_empty()

        return abs(row_goal - row_game) + abs(col_goal - col_game)
 

    def is_goal(self):
        return np.array_equal(self.Game, self.GOAL)

    def duplicate(self):
        return SlidingPuzzle([[self.Game[r][c] for c in range(self.GRIDSIZE)] for r in range(self.GRIDSIZE)])

    def log(self):
        print("---")
        for row in self.Game:
            print(", ".join(str(int(x)) for x in row))
        print("---")


def solve_puzzle(start_puzzle: SlidingPuzzle):
    # TODO: los de puzzel op met BFS
    queu = deque([start_puzzle])
    visited = set()

    while queu:
        puzzle = queu.popleft()

        if puzzle.is_goal():
            return puzzle

        config = str(puzzle.Game)
        if config in visited:
            continue

        visited.add(config)
        new_configurations = puzzle.possible_new_configurations()
        for new_puzzle in new_configurations:
            queu.append(new_puzzle)

    return None


       


if __name__ == "__main__":
    game = [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
    ]
    puzzle = SlidingPuzzle(game)
    print("Startconfiguratie:")
    puzzle.log()

    oplossing = solve_puzzle(puzzle)
    print("Oplossing:")
    oplossing.log()