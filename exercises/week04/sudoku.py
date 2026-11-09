import numpy as np

class SudokuSolver:
    def __init__(self, puzzle, initial_temperature=1000, cooling_rate=0.995, num_iterations=10000):
        self.puzzle = puzzle
        self.indexes = self.get_indexes()
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.num_iterations = num_iterations

    def get_indexes(self):
        indexes = []

        for i in self.puzzle:
            for j in i :
                if j == 0:
                    indexes.append((i, j))

        return indexes

    def calculate_cost(self):
        cost = 0

        for i in self.indexes:
            row, col = i

            for value in self.puzzle[row]:
                if value > 0:
                    cost +=1

            for row_in_puzzle in self.puzzle:
                if row_in_puzzle[col] > 0:
                    cost +=1




        

        

if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    puzzle = np.array(puzzle)

    # print(puzzle[(0, 1)])

    sudoku_solver = SudokuSolver(puzzle)
    best_grid, best_cost = sudoku_solver.simulated_annealing()

    print("Best Grid:")
    print(best_grid)
    print("Best Cost:", best_cost)