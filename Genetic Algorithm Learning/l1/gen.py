import random

def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z-25

def fitness (x,y,z):
    ans = foo(x,y,z)
    if ans == 0:
        return 99999
    else:
        return abs (1/ans)
    
# generate solutions
solutions = [ ]
for s in range(1000):
    solutions.append((
        random.uniform(0,1000),
        random.uniform(0,1000),
        random.uniform (0,1000)
        ))
    
# print(solutions[:5])


for i in range(10000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0],s[1],s[2]),s))
    rankedsolutions.sort()
    rankedsolutions.reverse()
    print (f"=== Gen {i} best solutions ")
    print (rankedsolutions[0])

    if rankedsolutions[0][0] >999:
        break

    bestsolutins = rankedsolutions[:100]

    elements=[]
    for s in bestsolutins:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])
    print(elements)
    newGen =[]
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99,1.01)
        e2 = random.choice(elements) * random.uniform(0.99,1.01)
        e3 = random.choice(elements) * random.uniform(0.99,1.01)

        newGen.append((e1,e2,e3))

    solutions =newGen
