import csv as csv
import more_itertools as mit
import random
import math

random.seed(10)

N = 128
T = 10000

def path_cost(path, N, dist):

    c = 0

    for i in range(0, N-1):
        x1 = path[i]
        x2 = path[i+1]
        
        c = c + dist[x1][x2]
    
    return c

def neighbor(path):
    
    pick_1 = random.randint(0, N-1)
    pick_2 = random.randint(0, N-1)
    
    temp = path[pick_1]
    path[pick_1] = path[pick_2]
    path[pick_2] = temp

    return path




def read_csv(file_name):
    file = open(file_name)
    csvreader = csv.reader(file)
    matrix_2d = []

    for row in csvreader:
        current = []
        for element in row:
            current.append(int(element))
        
        matrix_2d.append(current)
        current = []

    return matrix_2d


    
if __name__ == '__main__':
    print("TEST")
    distances = read_csv("cities_128.csv")
    # print(readpandas("cities_128.csv"))
    # READ CSV

    iterable = range(N) 
    current = list(mit.random_permutation(iterable))
    
    current_cost = path_cost(current, N, distances)
    print('Cost of starting path: ', current_cost)

    for i in range(10):
        new = neighbor(current)
        new_cost = path_cost (new, N, distances)
        
        if(new_cost < current_cost):
            current = new
            current_cost = new_cost
        else:
            # Compute the delta in energy
            delta = new_cost - current_cost 
            
            if(math.exp(-delta / T) > random.random()):
                current = new
                current_cost = new_cost
        print(i, current_cost, new_cost, delta, T, math.exp(-delta /  T))
        T = T*0.99

    print('Cost of final path: ', current_cost)
    
    
    