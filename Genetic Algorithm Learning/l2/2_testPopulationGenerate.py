import random

num_time_slots = 4
num_subjects = 6

population = []
for _ in range(10):
    chromosome = random.sample(range(6), 4)
    # chromosome = random.sample([1,2,3,4,5,6], 4)
    # chromosome = random.sample(["NP","TEL","MUL","BUSS","ICT","ELEX"], 4)
    population.append(chromosome)

print(population)