'''
Notes:
Sample Chromosome = [1,2,4,65,12,51,42,....32] // length = 194
'''
from random import *
import math
import heapq #finding nth largest

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
    parentsIndices = []
    for i in fitness:
        fitnessSum = fitnessSum + i
    for i in fitness:
        fitnessProportions.append(i/fitnessSum)
    #choosing 1st parent
    randNo = random()
    lower = 0
    for i in range (0,30):
        if ((randNo>lower) and (randNo<lower + fitnessProportions[i])):
            parentsIndices.append(i)
            print("-----1st parent index------",i)
        lower = lower + fitnessProportions[i]
    #choosing 2nd parent
    randNo = random()
    lower = 0
    findParentLoop = True
    while(findParentLoop == True):
        for i in range (0,30):
            if ((randNo>lower) and (randNo<lower + fitnessProportions[i])):
                if(i!=parentsIndices[0]): #not same as previous parent
                    parentsIndices.append(i)
                    findParentLoop = False
                    print("-----2nd parent index------",i)                    
            lower = lower + fitnessProportions[i]
    return parentsIndices

def nth_largest(n, iter):
    return heapq.nlargest(n, iter)[-1]

def rankbasedSelection(population, fitness):
    rankSum = 0
    ranksProportion = []
    parentsIndices = []
    #creating array for storing ranks
    ranks = []
    for i in range (len(fitness)):
        ranks.append(0)
    #finding ranks
    for i in range (1,len(fitness)+1):
        nthLargestElement = nth_largest(i, fitness)
        for j in range (len(fitness)):
            if (nthLargestElement == fitness[j]):
                ranks[j] = i;
    # rank sum for calculation proportions
    for i in ranks:
        rankSum = rankSum + i
    for i in ranks:
        ranksProportion.append(i/rankSum)
    #choosing 1st parent
    randNo = random()
    lower = 0
    for i in range (0,30):
        if ((randNo>lower) and (randNo<lower + ranksProportion[i])):
            parentsIndices.append(i)
            print("-----1st parent index------",i)
        lower = lower + ranksProportion[i]
    #choosing 2nd parent
    randNo = random()
    lower = 0
    findParentLoop = True
    while(findParentLoop == True):
        for i in range (0,30):
            if ((randNo>lower) and (randNo<lower + ranksProportion[i])):
                if(i!=parentsIndices[0]): #not same as previous parent
                    parentsIndices.append(i)
                    findParentLoop = False
                    print("-----2nd parent index------",i)                    
            lower = lower + ranksProportion[i]
    return parentsIndices


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
    rankbasedSelection(population, fitness)
    
main();
