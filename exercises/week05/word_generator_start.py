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
            index_printable = random.randint(0, len(string.printable))
            phrase = phrase + string.printable[index_printable]

        return phrase


    def calculate_fitness(self, phrase):
        characters_at_cor_pos = 0

        for i, j in phrase, self.target_phrase:
            if i == j :
                characters_at_cor_pos += 1 

        return characters_at_cor_pos / len(phrase)

    def generate_population(self, size, phrase_length):
        population = []

        for _ in size:
            population.append(self.generate_phrase(phrase_length))

        return population

    def crossover(self, phrase1, phrase2):
        part_phrase1 = phrase1[0:random.randint(0, len(phrase1))]
        part_phrase2 = phrase2[0:random.randint(0, len(phrase2))]

        return part_phrase1 + part_phrase2

    def mutate(self, phrase, rate):
        for i in range(len(phrase)):
            if random.random() <= rate:
                phrase[i] = string.printable[random.randint(0, len(string.printable))]

        return phrase

    def select_best(self, population):
        population.sort(key=self.calculate_fitness, reverse = True)
        return population[0]

    def genetic_algorithm(self):
        start_populatie = self.generate_population(self.population_size, len(self.target_phrase))





def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    puzzle = WordPuzzle(target_phrase)
    best_phrase = puzzle.genetic_algorithm()
    print(f"Beste zin: {best_phrase}")


if __name__ == "__main__":
    main()