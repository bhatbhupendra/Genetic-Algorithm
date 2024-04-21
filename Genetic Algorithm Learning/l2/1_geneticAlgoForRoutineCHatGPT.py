import random

# Define the number of time slots and subjects
num_time_slots = 4
num_subjects = 6

# Generate initial population
def generate_population(population_size):
    population = []
    for _ in range(population_size):
        chromosome = random.sample(range(num_subjects) , num_time_slots)
        population.append(chromosome)
    return population # [["","","","","",""],["","","","","",""]]

# Evaluate fitness of a chromosome
def fitness(chromosome):
    conflicts = 1
    for slot in range(num_time_slots):
        #calculate conflict
        subjects_in_slot = [i for i, x in enumerate(chromosome) if x == slot]
        conflicts += len(subjects_in_slot) - len(set(subjects_in_slot))
    return conflicts

# Genetic Algorithm
population_size = 10
population = generate_population(population_size)
generations = 100

for _ in range(generations):
    # Select parents
    parents = random.choices(population, k=2, weights=[1/fitness(chromosome) for chromosome in population])

    # Crossover
    crossover_point = random.randint(1, num_subjects - 1)
    offspring = parents[0][:crossover_point] + parents[1][crossover_point:]

    # Mutation
    if random.random() < 0.1:
        mutation_point = random.randint(0, num_subjects - 1)
        offspring[mutation_point] = random.randint(0, num_time_slots - 1)

    # Replace worst chromosome in population with offspring
    population.remove(max(population, key=fitness))
    population.append(offspring)

# Output the best chromosome
best_chromosome = min(population, key=fitness)
print("Best Class Routine:", best_chromosome)
