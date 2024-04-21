import random

num_time_slots = 4
num_subjects = 6

def generate_population(population_size):
    population = []
    for _ in range(population_size):
        chromosome = random.sample(range(6), 4)
        # chromosome = random.sample([1,2,3,4,5,6], 4)
        # chromosome = random.sample(["NP","TEL","MUL","BUSS","ICT","ELEX"], 4)
        population.append(chromosome)
    return population

def fitness(chromosome):
    conflicts = 1
    conflict = 0
    for sub in range(num_subjects):
        #calculate conflict
        for i, x in enumerate(chromosome):
            if x == sub:
                conflict+=1
        if conflict >=2:
            conflicts+=1
            conflict=0
        else:
            conflict=0
    return conflicts

# Genetic Algorithm
population_size = 5#10
population = generate_population(population_size)
# population = [[4, 4, 3, 2], [0, 4, 3, 2],[1, 4, 5, 2],[1,2,3,4],[5,6,1,2]]
generations = 2#100


for _ in range(generations):
    # Select parents
    print(population)
    parents = random.choices(population, k=2, weights=[1/fitness(chromosome) for chromosome in population])
    print(parents)

    # Crossover
    crossover_point = random.randint(1, num_time_slots - 1)
    print(crossover_point)
    offspring = parents[0][:crossover_point] + parents[1][crossover_point:]
    print("offspring",offspring)

    # Mutation
    if random.random() < 0.1:
        mutation_point = random.randint(0, num_subjects - 1)
        print(mutation_point)
        offspring[mutation_point] = random.randint(0, num_subjects - 1)
    print("mutated offspring",offspring)

    # Replace worst chromosome in population with offspring
    population.remove(max(population, key=fitness))
    population.append(offspring)
    print("new pop after removing",population)


# Output the best chromosome after N Generation
best_chromosome = min(population, key=fitness)
print("Best Class Routine:", best_chromosome)





    