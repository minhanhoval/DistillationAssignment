percentages = [5,10,20,30,40,50,60,70,80,90, 95, 99]
crudeNames = ["MSW", "MSB"]
crudes = [{
    5: 36.1,
    10: 82.2,
    20: 129.6,
    30: 178,
    40: 234.4,
    50: 290.5,
    60: 346.2,
    70: 410.2,
    80: 485.5,
    90: 604.4,
    95: None,
    99: None
},

    {
    5: 36.1,
    10: 78.1,
    20: 123.5,
    30: 175.5,
    40: 231.4,
    50: 292.6,
    60: 353.0,
    70: 420.6,
    80: 502.1,
    90: 638.3,
    95: None,
    99: None
},]
newDistillation = {}

#Getting input
crude1 = input("Enter First Crude")
while crude1 not in crudeNames:
    crude1 = input("INCORRECT: Enter First Crude")
volume1 = input("Enter First Crude Volume")
while not volume1.isdigit():
    volume1 = input("INCORRECT: Enter First Crude Volume")
crude2 = input("Enter Second Crude")
while crude2 not in crudeNames:
    crude2 = input("INCORRECT: Enter Second Crude")
volume2 = input("Enter Second Crude Volume")
while not volume2.isdigit():
    volume2 = input("INCORRECT: Enter Second Crude Volume")

#Calculating ratio of total volume
total = int(volume1) + int(volume2)
percentage1 = int(volume1) / total
percentage2 = int(volume2) / total

for i in percentages:
    if (crudes[crudeNames.index(crude1)][i] != None) and (crudes[crudeNames.index(crude2)][i] != None):
        newDistillation[i] = crudes[crudeNames.index(crude1)][i] * percentage1
        newDistillation[i] += crudes[crudeNames.index(crude2)][i] * percentage2
    elif (crudes[crudeNames.index(crude1)][i] == None) and (crudes[crudeNames.index(crude2)][i] == None):
        newDistillation[i] = None
    elif (crudes[crudeNames.index(crude1)][i] == None):
        newDistillation[i] = crudes[crudeNames.index(crude2)][i] * percentage2
    elif (crudes[crudeNames.index(crude2)][i] == None):
        newDistillation[i] = crudes[crudeNames.index(crude1)][i] * percentage1

    print(str(i) + ":" + str(newDistillation[i]))
