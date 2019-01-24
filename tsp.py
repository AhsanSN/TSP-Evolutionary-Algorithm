'''
Notes:
Sample Chromosome = [1,2,4,65,12,51,42,....32] // length = 194
'''
from random import *
import math

def generateRadomChromosome(): 
    chro = []
    for i in range (0,194):
        #generate random number
        randNo = randint(0, 194)
        while randNo in chro:
            randNo = randint(0, 194)
        chro.insert(i,randNo)
    return(chro)

def generateRandomPopulation(): # generates Population size: 30
    population = []
    for i in range (0,30):
        population.insert(i,generateRadomChromosome())
    print(len(population))
    
#generateRandomPopulation();

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

def getCoodsFromCity(cityNumber):
    data = readData()
    return [data[cityNumber-1][1],data[cityNumber-1][2]]

def getDistFromCity(cityNumber1, cityNumber2):
    cityCoods1 = getCoodsFromCity(cityNumber1)
    cityCoods2 = getCoodsFromCity(cityNumber2)
    return (math.sqrt((float(cityCoods1[0])-float(cityCoods2[0]))**2 + (float(cityCoods1[1])-float(cityCoods2[1]))**2))
    #+ (int(cityNumber1[1])-int(cityNumber2[1]))**2 

print(getDistFromCity(3,4))

'''
NODE_COORD_SECTION
1 24748.3333 50840.0000
2 24758.8889 51211.9444
3 24827.2222 51394.7222
4 24904.4444 51175.0000
5 24996.1111 51548.8889
6 25010.0000 51039.4444
7 25030.8333 51275.2778
8 25067.7778 51077.5000
9 25100.0000 51516.6667
10 25103.3333 51521.6667
11 25121.9444 51218.3333
12 25150.8333 51537.7778
13 25158.3333 51163.6111
14 25162.2222 51220.8333
15 25167.7778 51606.9444
16 25168.8889 51086.3889
17 25173.8889 51269.4444
18 25210.8333 51394.1667
19 25211.3889 51619.1667
20 25214.1667 50807.2222
21 25214.4444 51378.8889
22 25223.3333 51451.6667
23 25224.1667 51174.4444
24 25233.3333 51333.3333
25 25234.1667 51203.0556
26 25235.5556 51330.0000
27 25235.5556 51495.5556
28 25242.7778 51428.8889
29 25243.0556 51452.5000
30 25252.5000 51559.1667
31 25253.8889 51535.2778
32 25253.8889 51549.7222
33 25256.9444 51398.8889
34 25263.6111 51516.3889
35 25265.8333 51545.2778
36 25266.6667 50969.1667
37 25266.6667 51483.3333
38 25270.5556 51532.7778
39 25270.8333 51505.8333
40 25270.8333 51523.0556
41 25275.8333 51533.6111
42 25277.2222 51547.7778
43 25278.3333 51525.5556
44 25278.3333 51541.3889
45 25279.1667 51445.5556
46 25281.1111 51535.0000
47 25281.3889 51512.5000
48 25283.3333 51533.3333
49 25283.6111 51546.6667
50 25284.7222 51555.2778
51 25286.1111 51504.1667
52 25286.1111 51534.1667
53 25286.6667 51533.3333
54 25287.5000 51537.7778
55 25288.0556 51546.6667
56 25290.8333 51528.3333
57 25291.9444 51424.4444
58 25292.5000 51520.8333
59 25298.6111 51001.6667
60 25300.8333 51394.4444
61 25306.9444 51507.7778
62 25311.9444 51003.0556
63 25313.8889 50883.3333
64 25315.2778 51438.6111
65 25316.6667 50766.6667
66 25320.5556 51495.5556
67 25322.5000 51507.7778
68 25325.2778 51470.0000
69 25326.6667 51350.2778
70 25337.5000 51425.0000
71 25339.1667 51173.3333
72 25340.5556 51293.6111
73 25341.9444 51507.5000
74 25358.8889 51333.6111
75 25363.6111 51281.1111
76 25368.6111 51226.3889
77 25374.4444 51436.6667
78 25377.7778 51294.7222
79 25396.9444 51422.5000
80 25400.0000 51183.3333
81 25400.0000 51425.0000
82 25404.7222 51073.0556
83 25416.9444 51403.8889
84 25416.9444 51457.7778
85 25419.4444 50793.6111
86 25429.7222 50785.8333
87 25433.3333 51220.0000
88 25440.8333 51378.0556
89 25444.4444 50958.3333
90 25451.3889 50925.0000
91 25459.1667 51316.6667
92 25469.7222 51397.5000
93 25478.0556 51362.5000
94 25480.5556 50938.8889
95 25483.3333 51383.3333
96 25490.5556 51373.6111
97 25492.2222 51400.2778
98 25495.0000 50846.6667
99 25495.0000 50965.2778
100 25497.5000 51485.2778
101 25500.8333 50980.5556
102 25510.5556 51242.2222
103 25531.9444 51304.4444
104 25533.3333 50977.2222
105 25538.8889 51408.3333
106 25545.8333 51387.5000
107 25549.7222 51431.9444
108 25550.0000 51433.3333
109 25560.2778 51158.6111
110 25566.9444 51484.7222
111 25567.5000 50958.8889
112 25574.7222 51486.3889
113 25585.5556 51151.3889
114 25609.4444 51092.2222
115 25610.2778 51475.2778
116 25622.5000 51454.4444
117 25645.8333 51450.0000
118 25650.0000 51372.2222
119 25666.9444 51174.4444
120 25683.8889 51505.8333
121 25686.3889 51468.8889
122 25696.1111 51260.8333
123 25700.8333 51584.7222
124 25708.3333 51591.6667
125 25716.6667 51050.0000
126 25717.5000 51057.7778
127 25723.0556 51004.1667
128 25734.7222 51547.5000
129 25751.1111 51449.1667
130 25751.9444 50920.8333
131 25758.3333 51395.8333
132 25765.2778 51019.7222
133 25772.2222 51483.3333
134 25775.8333 51023.0556
135 25779.1667 51449.7222
136 25793.3333 51409.4444
137 25808.3333 51060.5556
138 25816.6667 51133.3333
139 25823.6111 51152.5000
140 25826.6667 51043.8889
141 25829.7222 51245.2778
142 25833.3333 51072.2222
143 25839.1667 51465.2778
144 25847.7778 51205.8333
145 25850.0000 51033.3333
146 25856.6667 51083.3333
147 25857.5000 51298.8889
148 25857.5000 51441.3889
149 25866.6667 51066.6667
150 25867.7778 51205.5556
151 25871.9444 51354.7222
152 25872.5000 51258.3333
153 25880.8333 51221.3889
154 25883.0556 51185.2778
155 25888.0556 51386.3889
156 25900.0000 51000.0000
157 25904.1667 51201.6667
158 25928.3333 51337.5000
159 25937.5000 51313.3333
160 25944.7222 51456.3889
161 25950.0000 51066.6667
162 25951.6667 51349.7222
163 25957.7778 51075.2778
164 25958.3333 51099.4444
165 25966.6667 51283.3333
166 25983.3333 51400.0000
167 25983.6111 51328.0556
168 26000.2778 51294.4444
169 26008.6111 51083.6111
170 26016.6667 51333.3333
171 26021.6667 51366.9444
172 26033.3333 51116.6667
173 26033.3333 51166.6667
174 26033.6111 51163.8889
175 26033.6111 51200.2778
176 26048.8889 51056.9444
177 26050.0000 51250.0000
178 26050.2778 51297.5000
179 26050.5556 51135.8333
180 26055.0000 51316.1111
181 26067.2222 51258.6111
182 26074.7222 51083.6111
183 26076.6667 51166.9444
184 26077.2222 51222.2222
185 26078.0556 51361.6667
186 26083.6111 51147.2222
187 26099.7222 51161.1111
188 26108.0556 51244.7222
189 26116.6667 51216.6667
190 26123.6111 51169.1667
191 26123.6111 51222.7778
192 26133.3333 51216.6667
193 26133.3333 51300.0000
194 26150.2778 51108.0556
'''

