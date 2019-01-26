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
        randNo = randint(1, 194)
        while randNo in chro:
            randNo = randint(1, 194)
        chro.insert(i,randNo)
    return(chro)

def getFitnessOfChromo(chromo, data):
    total = getDistFromCity(chromo[0], chromo[1], data)
    for i in range (2, 194):
        total = total + getDistFromCity(chromo[i-1],chromo[i], data)
    return(total)

def generateRandomPopulation(size): # generates Population size: 30
    population = []
    for i in range (0,size):
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

def fitnessProportionalSelection(fitness, nSelect):
    fitnessSum = 0
    fitnessProportions = []
    parentsIndices = []
    for i in fitness:
        fitnessSum = fitnessSum + i
    for i in fitness:
        fitnessProportions.append(i/fitnessSum)
    #choosing 1st parent
    findParentLoop = True
    for n in range (nSelect):
        findParentLoop = True
        while(findParentLoop == True):
            randNo = random()
            lower = 0
            for i in range (len(fitness)):
                if ((randNo>lower) and (randNo<lower + fitnessProportions[i])):
                    if(i not in parentsIndices):
                        parentsIndices.append(i)
                        print("-----",n,"th parent index------",i)
                        findParentLoop = False
                lower = lower + fitnessProportions[i]
    return parentsIndices

def nth_largest(n, iter):
    return heapq.nlargest(n, iter)[-1]

def rankbasedSelection(fitness):
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
    for i in range (len(fitness)):
        if ((randNo>lower) and (randNo<lower + ranksProportion[i])):
            parentsIndices.append(i)
            print("-----1st parent index------",i)
        lower = lower + ranksProportion[i]
    #choosing 2nd parent
    randNo = random()
    lower = 0
    findParentLoop = True
    while(findParentLoop == True):
        for i in range (len(fitness)):
            if ((randNo>lower) and (randNo<lower + ranksProportion[i])):
                if(i!=parentsIndices[0]): #not same as previous parent
                    parentsIndices.append(i)
                    findParentLoop = False
                    print("-----2nd parent index------",i)                    
            lower = lower + ranksProportion[i]
    return parentsIndices

def binaryTournament(fitness):
    parentsIndices = []
    pool1 = []
    pool2 = []
    pool1Loop = True
    pool2Loop = True
    pool1Best = 0
    pool2Best = 0

    #players for pool1
    while (pool1Loop):
        for i in range (2):
            randNo = randint(0, len(fitness)-1)
            if(len(pool1)==1):
                if (pool1[0] != randNo):
                    pool1.append(randNo)
                    pool1Loop = False
            if(len(pool1)==0):
                pool1.append(randNo)
    #best from pool 1
    if(fitness[pool1[0]]>fitness[pool1[1]]):
        pool1Best = pool1[0];
    if(fitness[pool1[0]]<fitness[pool1[1]]):
        pool1Best = pool1[1];
    parentsIndices.append(pool1Best)
    
    #players for pool2
    while (pool2Loop):
        for i in range (2):
            randNo = randint(0, len(fitness)-1)
            if(len(pool2)==1):
                if (pool2[0] != randNo) and (pool1Best != randNo):
                    pool2.append(randNo)
                    pool2Loop = False
            if(len(pool2)==0):
                pool2.append(randNo)
    #best from pool 2
    if(fitness[pool2[0]]>fitness[pool2[1]]):
        pool2Best = pool2[0];
    if(fitness[pool2[0]]<fitness[pool2[1]]):
        pool2Best = pool2[1];
    parentsIndices.append(pool2Best)
    return(parentsIndices)
    
def crossOver(parentsIndex, population, nChildren):
    parent1 = population[parentsIndex[0]]
    parent2 = population[parentsIndex[1]]
    #print("parent 1: ", (parent1))
    #print("parent 2: ", parent2)
    
    producedChildren = []
    nPortions = int(194/nChildren)
    
    child1 = []
    child2 = []
    #generating template
    for i in range(194):
        child1.append(-222)
        child2.append(-222)

    #generating child 
    for i in range (0,int(nChildren/2)):
        # child 1    
        start = nPortions*i
        child1[start:start+ nPortions] = parent1[start:start+ nPortions]
        isChildComplete = False;
        childIndex = start+ nPortions
        ParentIndex = start+ nPortions
        while(isChildComplete==False):
            if(parent2[ParentIndex] not in child1[start:start+ nPortions]):
                child1[childIndex] = parent2[ParentIndex];
                childIndex+= 1
                ParentIndex+= 1
            elif (parent2[ParentIndex] in child1[start:start+ nPortions]):
                ParentIndex+= 1
            if (ParentIndex==len(child1)):
                ParentIndex = 0
            if (childIndex==len(child1)):
                childIndex = 0
            if(childIndex == start):
                isChildComplete = True
        # child 2
        start = nPortions*i
        child2[start:start+ nPortions] = parent2[start:start+ nPortions]
        isChildComplete = False;
        childIndex = start+ nPortions
        ParentIndex = start+ nPortions
        while(isChildComplete==False):
            if(parent1[ParentIndex] not in child2[start:start+ nPortions]):
                child2[childIndex] = parent1[ParentIndex];
                childIndex+= 1
                ParentIndex+= 1
            elif (parent1[ParentIndex] in child2[start:start+ nPortions]):
                ParentIndex+= 1
            if (ParentIndex==len(child2)):
                ParentIndex = 0
            if (childIndex==len(child2)):
                childIndex = 0
            if(childIndex == start):
                isChildComplete = True
        #adding child
        producedChildren.append(child1)
        producedChildren.append(child2)
    return(producedChildren)        

def mutation(children, rate):
    mutatedChildren = children
    for i in range (len(mutatedChildren)):
        randNo = random()
        if (randNo<rate):
            # switching calues
            switchPos1 = randint(0, int(194/2))
            switchPos2 = randint(int(194/2), 193)
            temp = mutatedChildren[i][switchPos1]
            mutatedChildren[i][switchPos1] = mutatedChildren[i][switchPos2]
            mutatedChildren[i][switchPos2] = temp
    return mutatedChildren
        
#main

def main():
    data = readData()
    # generate initial population
    population = generateRandomPopulation(30)
    fitness = []
    # compute fitness
    for i in population:
        fitness.append(getFitnessOfChromo(i, data))
    #print("fitness:",fitness)
    # Population[3] has the fitness[3]
    
    # choosing parents 
    parents = fitnessProportionalSelection(fitness, 2)
    #parents = rankbasedSelection(fitness)
    parentsIndex = binaryTournament(fitness)
    #crossover
    children = crossOver(parentsIndex, population, 10);
    children = mutation(children, 0.5) #mutated children
    #compute fitness of children
    for i in range (len(children)):
        population.append(children[i])
        fitness.append(getFitnessOfChromo(children[i], data))
    
    
main();
