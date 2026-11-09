"""
Oefening 1: Word Generator (Genetisch Algoritme)
==================================================
Evolueer een populatie van willekeurige zinnen naar een doelzin.
"""
import random
import string


class WordPuzzle:
    def __init__(self, target_phrase, population_size=100, mutation_rate=0.01, num_generations=10000):
        self.target_phrase = target_phrase
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations

    def generate_phrase(self, length):
        phrase = ""

        for _ in range(length):
            char_index = random.randint(0, len(string.printable) - 1)
            phrase = phrase + string.printable[char_index]

        return phrase

    def calculate_fitness(self, phrase):
        char_cor_pos = 0

        for i  in range(len(self.target_phrase)):
            if phrase[i] == self.target_phrase[i]:
                char_cor_pos += 1

        return char_cor_pos / len(self.target_phrase)
 
    def generate_population(self, size, phrase_length):
        population = []

        for _ in range(size):
            population.append(self.generate_phrase(phrase_length))

        return population

    def crossover(self, phrase1, phrase2):
        index = random.randint(0, len(self.target_phrase)-1)

        part1 = phrase1[0:index]
        part2 = phrase2[index:]

        return part1 + part2

    def mutate(self, phrase, rate):
        
        for i in range(len(phrase)):
            chance = random.random()
            if chance < rate:
                new_char_index = random.randint(0, len(string.printable) - 1)
                phrase = phrase[:i] + string.printable[new_char_index] + phrase[i+1:]

        return phrase
            

    def select_best(self, population):
        return max(population, key=self.calculate_fitness)


    def genetic_algorithm(self):
        start_population = self.generate_population(self.population_size, len(self.target_phrase))
        prev_best_phrase = self.select_best(start_population)

        population = self.generate_population(self.population_size, len(self.target_phrase))

        for _ in range(self.num_generations):
            best_phrase = self.select_best(population)

            new_population = []
            while len(new_population) < self.population_size:
                new_phrase = self.crossover(prev_best_phrase, best_phrase)
                new_phrase = self.mutate(new_phrase, self.mutation_rate)

                new_population.append(new_phrase)

            prev_best_phrase = best_phrase
            population = new_population

        return best_phrase
            

def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    puzzle = WordPuzzle(target_phrase)
    best_phrase = puzzle.genetic_algorithm()
    print(f"Beste zin: {best_phrase}")


if __name__ == "__main__":
    main()