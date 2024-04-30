import random

num_time_slots = 4
num_subjects = 6

subjects=["NP","TEL","MUL","BUSS","ICT","ELEX"]
teachers={
    "TM":["NP",1,1,1,1],
    "PG":["TEL",1,1,0,0],
    "SP":["MUL",1,1,1,1],
    "SA":["BUSS",1,1,1,1],
    "SK":["ICT",1,1,1,1],
    "ELET":["ELEX",1,1,0,0],
}


#Fitness section
def fitness(chromosome):
    print(chromosome)
    return 1

def generate_population(population_size):
    population = []
    chromosome =[]
    for _ in range(population_size):
        for _ in range(6):
            num_cols = random.randint(2, 4)  # Randomly choose number of columns (2, 3, or 4)
            row = [random.choice(subjects) for _ in range(num_cols)]
            for _ in range(4-num_cols):#for empty data
                row.append("")         #for empty data
            chromosome.append(row)
        population.append(chromosome)
    return population

# Genetic Algorithm
population_size = 1
population = generate_population(population_size)
generations = 2
print('The Generated Population',population)


for _ in range(generations):
    # Select parents
    parents = random.choices(population, k=2, weights=[1/fitness(chromosome) for chromosome in population])
    print("Selected Parents",parents)

