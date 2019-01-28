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

def getFitnessOfChromo(chromo, data): #doesnt show distance
    total = getDistFromCity(chromo[0], chromo[1], data)
    for i in range (2, 194):
        total = total + getDistFromCity(chromo[i-1],chromo[i], data)
    total = 1000000000/total
    return(total) #the less the total the greater the fitness

def getFitnessAsDistance(chromo, data): #doesnt show distance
    total = getDistFromCity(chromo[0], chromo[1], data)
    for i in range (2, 194):
        total = total + getDistFromCity(chromo[i-1],chromo[i], data)
    return(total) #the less the total the greater the fitness

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
    appendValue = 0
    for i in fitness:
        fitnessSum = fitnessSum + i
    for i in fitness:
        fitnessProportions.append(i/fitnessSum)
    #choosing parents
    for n in range (nSelect):
        findParentLoop = True
        if(len(parentsIndices)==len(fitness)):
            findParentLoop = False;
        while(findParentLoop == True):
            randNo = random()
            lower = 0
            for i in range (len(fitness)):
                if ((randNo>lower) and (randNo<lower + fitnessProportions[i])):
                    if(i not in parentsIndices):
                        parentsIndices.append(i)
                        findParentLoop = False
                lower = lower + fitnessProportions[i]
    return parentsIndices

def nth_largest(n, iter):
    return heapq.nlargest(n, iter)[-1]

def rankbasedSelection(fitness, nSelect):
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
    #choosing parents
    for n in range (nSelect):
        findParentLoop = True
        if(len(parentsIndices)==len(fitness)):
            findParentLoop = False;
        while(findParentLoop == True):
            randNo = random()
            lower = 0
            for i in range (len(fitness)):
                if ((randNo>lower) and (randNo<lower + ranksProportion[i])):
                    if(i not in parentsIndices):
                        parentsIndices.append(i)
                        findParentLoop = False
                lower = lower + ranksProportion[i]
    return parentsIndices

def binaryTournament(fitness, nSelect, parentSelect=1):
    parentsIndices = []
    pool = []
    poolLoop = True
    poolBest = 0
    #players for pool1
    for n in range (nSelect):
        while (poolLoop):
            for i in range (2):
                randNo = randint(0, len(fitness)-1)
                if(len(parentsIndices)==len(fitness)-1):
                    poolLoop = False;
                if ((randNo not in parentsIndices) and (len(parentsIndices)<len(fitness)+1)):
                    if(len(pool)==1):
                        if (pool[0] != randNo):
                            pool.append(randNo)
                            poolLoop = False
                    if(len(pool)==0):
                        pool.append(randNo)
        #best from pool 1            
        if (len(pool)==2):
            # for parent select
            if(parentSelect == 1):
                if(fitness[pool[0]]>fitness[pool[1]]):
                    poolBest = pool[0];
                if(fitness[pool[0]]<fitness[pool[1]]):
                    poolBest = pool[1];
                parentsIndices.append(poolBest)
                
        if (len(parentsIndices)<nSelect):
            poolLoop = True
            pool = []
            poolBest = 0
    return(parentsIndices)
    
    
def crossOver(parentsIndex, population):
    startCopyIndex = randint(1, 190)
    finishCopyIndex = randint(startCopyIndex, 193)
    
    
    parent1 = population[parentsIndex[0]]
    parent2 = population[parentsIndex[1]]
    producedChildren = []
    child1 = []
    child2 = []
    #generating template
    for i in range(194):
        child1.append(-222)
        child2.append(-222)
    #generating child
        
    # child 1
    child1[startCopyIndex:finishCopyIndex] = parent1[startCopyIndex:finishCopyIndex]
    isChildComplete = False;
    childIndex = finishCopyIndex
    ParentIndex = finishCopyIndex
    while(isChildComplete==False):
        if(parent2[ParentIndex] not in child1[startCopyIndex:finishCopyIndex]):
            child1[childIndex] = parent2[ParentIndex];
            childIndex+= 1
            ParentIndex+= 1
        elif (parent2[ParentIndex] in child1[startCopyIndex:finishCopyIndex]):
            ParentIndex+= 1
        if (ParentIndex==len(child1)):
            ParentIndex = 0
        if (childIndex==len(child1)):
            childIndex = 0
        if(childIndex == startCopyIndex):
            isChildComplete = True
    # child 2
    child2[startCopyIndex:finishCopyIndex] = parent2[startCopyIndex:finishCopyIndex]
    isChildComplete = False;
    childIndex = finishCopyIndex
    ParentIndex = finishCopyIndex
    while(isChildComplete==False):
        if(parent1[ParentIndex] not in child2[startCopyIndex:finishCopyIndex]):
            child2[childIndex] = parent1[ParentIndex];
            childIndex+= 1
            ParentIndex+= 1
        elif (parent1[ParentIndex] in child2[startCopyIndex:finishCopyIndex]):
            ParentIndex+= 1
        if (ParentIndex==len(child2)):
            ParentIndex = 0
        if (childIndex==len(child2)):
            childIndex = 0
        if(childIndex == startCopyIndex):
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
    # setting some variables
    nPopulation = 100
    mutationRate = 0.2
    nChildren = 10 #must be even
    nGenerations = 1000
    # generate initial population
    population = generateRandomPopulation(nPopulation)
    fitness = []
    fitnessDistance = []
    # compute fitness
    for i in population:
        fitness.append(getFitnessOfChromo(i, data))
        fitnessDistance.append(getFitnessAsDistance(i, data))
    #print("fitness:",fitness)
    # Population[3] has the fitness[3]

    #begin loop
    for generation in range (nGenerations):
        if(generation%10==0):            
            print("generation:",generation)

            #fitness statistics
            print("avg distance: ", sum(fitnessDistance) / float(len(fitnessDistance)))
            print("min distance: ", min(fitnessDistance))
        for childGeneration in range (nChildren//2):
            # choosing parents 
            parentsIndex = fitnessProportionalSelection(fitness, 2)
            #parentsIndex = rankbasedSelection(fitness, 2 )
            #parentsIndex = binaryTournament(fitness, 2)
            
            children = crossOver(parentsIndex, population);
            children = mutation(children, mutationRate) #mutated children
        
            #compute fitness of children
            for i in range (len(children)):
                population.append(children[i])
                fitness.append(getFitnessOfChromo(children[i], data))
                fitnessDistance.append(getFitnessAsDistance(children[i], data))
                
            # select new population        
            #populationIndices = fitnessProportionalSelection(fitness, nPopulation)
            populationIndices = rankbasedSelection(fitness, nPopulation)
            #populationIndices = binaryTournament(fitness, nPopulation)

            tempPopulation = []
            tempFitness = []
            tempFitnessDistance = []
            for i in (populationIndices):
                tempFitness.append(fitness[i])
                tempFitnessDistance.append(fitnessDistance[i])
                tempPopulation.append(population[i])
                
            population = tempPopulation
            fitness = tempFitness
            fitnessDistance = tempFitnessDistance
    
main();
