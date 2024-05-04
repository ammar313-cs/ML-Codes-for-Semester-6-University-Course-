from random import randint

MAX = 9000
nodes = 5
GENES = "ABCDEFG"
START = 0
population = 100
mutation_rate = 3

pos = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6}

graph = [[0, 90, MAX, 300, 140, MAX, 220],
         [100, 0, 80, MAX, MAX, 300, 150],
         [MAX, 340, 0, 40, 250, MAX, MAX],
         [360, MAX, 240, 0, 80, 170, MAX],
         [450, 40, MAX, MAX, 0, MAX, 100],
         [70, MAX, 330, 160, MAX, 0, 110],
         [MAX, 320, 140, 90, 280, 190, 0]]


class chromo:
    def __init__(self, _path, _fitness):
        self.path = _path
        self.fitness = _fitness

def fitness(chromo):
    fitness = 0
    
    for r in range(len(chromo)-1):
        g = chromo[r]
        k = chromo[r+1]
        row = pos[g]
        col = pos[k]
        if graph[row][col] == MAX:
            return MAX
        else:
            fitness += graph[row][col]

    return fitness

def apartheid(population, number):
    new = []

    while (len(new) < number):
        index = randint(0, len(population)-1)

        if population[index] not in new:
            new.append(population[index])

    return new




# function to select fittest population
def tournament_selection(population, tournament_size):
    """
    Selects the fittest individuals from the population using tournament selection
    """
    fittest = []
    for i in range(len(population)):
        tournament = random.sample(population, tournament_size)
        fittest_individual = max(tournament, key=lambda x: x.fitness)
        fittest.append(fittest_individual)
    return fittest


# function to create offsprings
import random

def order_crossover(parent1, parent2):
    """
    Applies order crossover (OX) to two parent individuals and returns two offspring individuals
    """
    n = len(parent1)
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)
    if a > b:
        a, b = b, a
    mask = [False] * n
    for i in range(a, b+1):
        mask[i] = True
    offspring1 = [-1] * n
    offspring2 = [-1] * n
    for i in range(a, b+1):
        offspring1[i] = parent1[i]
        offspring2[i] = parent2[i]
    j1 = 0
    j2 = 0
    for i in range(n):
        if not mask[parent2[i]]:
            while offspring1[j1] != -1:
                j1 = (j1 + 1) % n
            offspring1[j1] = parent2[i]
        if not mask[parent1[i]]:
            while offspring2[j2] != -1:
                j2 = (j2 + 1) % n
            offspring2[j2] = parent1[i]
    return offspring1, offspring2

def mutation(individual):
    """
    Applies mutation to an individual by swapping two cities with a certain probability (mutation_rate)
    """
    positions = []
    mutated = individual
    n = len(individual)

    for i in range(n):
        positions.append(i)

    for i in range(mutation_rate):
        pos1, pos2 = random.sample(positions, 2)
        mutated[pos1], mutated[pos2] = mutated[pos2], mutated[pos1]
    
    return mutated

def generate_path(genes):
    start = random.choice(genes)

    remaining = [i for i in genes if i != start]
    random.shuffle(remaining)
    end = start
    path = [start]

    for i in range(len(remaining)):
        if i == 7:
            break
        ver = remaining[i]
        if ver != end:
            path.append(ver)
    
    path.append(end)

    return ''.join(path)

def make_pop(population, genes):
    
    first_pop = []

    for i in range(population):
        path = generate_path(GENES)
        chromosom = chromo(path, fitness(path))
        first_pop.append(chromosom)
    
    return first_pop

def pop_score(population):

    score = 0

    for i in population:
        score =+ i.fitness
    return score


def create_offspring(selected_individuals, crossover_rate):
    """
    Creates new offspring by applying crossover and mutation to the selected individuals
    """
    offspring = []
    for i in range(0, len(selected_individuals), 2):
        parent1 = selected_individuals[i]
        if i+1 < len(selected_individuals):
            parent2 = selected_individuals[i+1]
        else:
            parent2 = selected_individuals[0]
        if random.random() < crossover_rate:
            offspring1, offspring2 = order_crossover(parent1.genes, parent2.genes)
        else:
            offspring1, offspring2 = parent1.genes[:], parent2.genes[:]
        mutation(offspring1)
        mutation(offspring2)
        offspring.append(Individual(offspring1))
        offspring.append(Individual(offspring2))
    return offspring

# to call the function
selected_individuals = tournament_selection(population, tournament_size)
