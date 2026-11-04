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
            index_printable = random.randint(0, len(string.printable) - 1)
            phrase = phrase + string.printable[index_printable]

        return phrase


    def calculate_fitness(self, phrase):
        characters_at_cor_pos = 0

        for i, j in zip(phrase, self.target_phrase):
            if i == j :
                characters_at_cor_pos += 1 

        return characters_at_cor_pos / len(phrase)

    def generate_population(self, size, phrase_length):
        population = []

        for _ in range(size):
            population.append(self.generate_phrase(phrase_length))

        return population

    def crossover(self, phrase1, phrase2):
        crossover_point = random.randint(0, len(phrase1))

        return phrase1[:crossover_point] + phrase2[crossover_point:]

    def mutate(self, phrase, rate):
        for i in range(len(phrase)):
            if random.random() <= rate:
                new_char = random.choice(string.printable)
                phrase = phrase[:i] + new_char + phrase[i + 1:]

        return phrase

    def select_best(self, population):
        return max(population, key=self.calculate_fitness)



    def select_parent(self, population):
        tournament_size = 5

        tournament = random.sample(
            population,
            min(tournament_size, len(population))
        )

        return self.select_best(tournament)

    def genetic_algorithm(self):
        population = self.generate_population(
            self.population_size,
            len(self.target_phrase)
        )

        best_phrase = self.select_best(population)

        for generation in range(self.num_generations):

            new_population = []

            # Elitism: behoud de beste zin
            new_population.append(best_phrase)

            while len(new_population) < self.population_size:

                # Selecteer twee ouders
                parent1 = self.select_parent(population)
                parent2 = self.select_parent(population)

                # Maak een kind
                child = self.crossover(parent1, parent2)

                # Mutatie
                child = self.mutate(child, self.mutation_rate)

                # Voeg het kind toe aan de nieuwe populatie
                new_population.append(child)

            # Vervang de oude populatie
            population = new_population

            # Zoek de beste zin van deze generatie
            current_best = self.select_best(population)

            if self.calculate_fitness(current_best) > self.calculate_fitness(best_phrase):
                best_phrase = current_best

            # Controleer of de doelzin gevonden is
            if best_phrase == self.target_phrase:
                print(f"Doelzin gevonden in generatie {generation + 1}")
                return best_phrase

        return best_phrase

def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    puzzle = WordPuzzle(target_phrase)
    best_phrase = puzzle.genetic_algorithm()
    print(f"Beste zin: {best_phrase}")


if __name__ == "__main__":
    main()



    # ORIGINELE genetic_algorithm
    # def genetic_algorithm(self):
    #     start_population = self.generate_population(self.population_size, len(self.target_phrase))

    #     population = start_population.copy()

    #     for _ in range(self.num_generations):
            
    #         best_phrase1, best_phrase2 = self.select_best(population)
    #         new_population = [best_phrase1, best_phrase2]

    #         new_phrase = self.crossover(best_phrase1, best_phrase2)

    #         new_population.append(self.mutate(new_phrase, self.mutation_rate))
    #         population = new_population

    #     return self.select_best(population)[0]