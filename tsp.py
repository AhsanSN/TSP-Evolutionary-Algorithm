'''
Notes:
Sample Chromosome = [1,2,4,65,12,51,42,....32] // length = 194
'''
from random import *
import math

# helper functions
def generateRandomChromosome(): 
    chro = []
    for i in range (0,194):
        #generate random number
        randNo = randint(0, 194)
        while randNo in chro:
            randNo = randint(0, 194)
        chro.insert(i,randNo)
    return(chro)

def getFitnessOfChromo(chromo, data):
    total = getDistFromCity(chromo[0], chromo[1], data)
    for i in range (2, 194):
        total = total + getDistFromCity(chromo[i-1],chromo[i], data)
    return(total)

def generateRandomPopulation(): # generates Population size: 30
    population = []
    for i in range (0,30):
        population.insert(i,generateRandomChromosome())
    return(population)

def readData():
    f = open("data.txt", "r")
    coods = []
    i=0
    for x in f:
        #extract parts
        parts= []
        temp = ""
        for j in x:
            if((j==' ')or(j=='\n')):
                parts.append(temp)
                temp = ""
            else:
                temp = temp + str(j);
        coods.insert(i,parts)
        i=i+1
    return(coods)

def getCoodsFromCity(cityNumber, data):
    return [data[cityNumber-1][1],data[cityNumber-1][2]]

def getDistFromCity(cityNumber1, cityNumber2, data):
    cityCoods1 = getCoodsFromCity(cityNumber1, data)
    cityCoods2 = getCoodsFromCity(cityNumber2, data)
    return (math.sqrt((float(cityCoods1[0])-float(cityCoods2[0]))**2 + (float(cityCoods1[1])-float(cityCoods2[1]))**2))

#parent selection procedures

def fitnessProportionalSelection(population, fitness):
    fitnessSum = 0
    fitnessProportions = []
    for i in fitness:
        fitnessSum = fitnessSum + i
    for i in fitness:
        fitnessProportions.append(i/fitnessSum)
    randNo = random()
    print("rand: ",randNo)
    for i in range (0,29):
        print(fitnessProportions[i])
        if ((randNo>fitnessProportions[i]) and (randNo<fitnessProportions[i+1])):
            print(fitnessProportions[i])
            print(fitnessProportions[i+1])


#main
def main():
    data = readData()
    # generate initial population
    population = generateRandomPopulation()
    fitness = []
    # compute fitness
    for i in population:
        fitness.append(getFitnessOfChromo(i, data))
    #print("fitness:",fitness)
    # Population[3] has the fitness[3]
    # choosing parents
    fitnessProportionalSelection(population, fitness)
    
main();
