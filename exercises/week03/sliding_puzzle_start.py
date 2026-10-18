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
        configs = []

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)] # rechts, links, boven, onder

        current_row, current_col = self.locate_empty()

        for row_move, col_move in moves:
            new_row = current_row + row_move
            new_col = current_col + col_move

            if 0 <= new_row <= 2 and 0 <= new_col <= 2:
                new_config = self.duplicate()
                new_config.Game[current_row][current_col], new_config.Game[new_row][new_col] = new_config.Game[new_row][new_col], new_config.Game[current_row][current_col]

                configs.append(new_config)

        return configs

    def locate_empty(self):
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return (row, col)
        raise Exception("Geen leeg vakje!")

    def manhattan_distance(self):
        # TODO: bereken de Manhattan-afstand tot de goal-configuratie
        return 0

    def is_goal(self):
        return np.array_equal(self.Game, self.GOAL)

    def duplicate(self):
        return SlidingPuzzle([[self.Game[r][c] for c in range(self.GRIDSIZE)] for r in range(self.GRIDSIZE)])

    def log(self):
        print("---")
        for row in self.Game:
            print(", ".join(str(int(x)) for x in row))
        print("---")


def solve_puzzle(start_puzzle : SlidingPuzzle):
    # TODO: los de puzzel op met BFS
    frontier = deque([start_puzzle])
    used = []

    while frontier:
        current_config = frontier.popleft()

        if current_config.is_goal():
            return current_config.Game

        used.append(current_config.Game)

        for config in current_config.possible_new_configurations():
            if not any(np.array_equal(config.Game, board) for board in used):
                frontier.append(config)


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
    print("Oplossing:\n", oplossing)