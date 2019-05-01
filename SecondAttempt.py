import numpy as np
crudeNames = ["MSW", "MSB", "MPR"]

crudes =[ [36.1, 82.2, 129.6, 178, 234.4, 290.5, 346.2, 410.2, 485.5, 604.4],
          [36.1,78.1,123.5,175.5,231.4,292.6,353.0,420.6,502.1,638.3],
          [95.9, 165.2, 237.2, 316.6, 396.9, 496.0,596.5, 707.4, 833.4, 1008.5, 1169.1]]
y = [5,10,20,30,40,50,60,70,80,90, 95, 99]

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

crude1idx = crudes[crudeNames.index(crude1)]
crude2idx = crudes[crudeNames.index(crude2)]
crude1y = y[:len(crude1idx)]
crude2y = y[:len(crude2idx)]

maxTemp = max(crude1idx + crude2idx)
minTemp = min(crude1idx + crude2idx)

temps = np.linspace(minTemp, maxTemp, (int(maxTemp + 1) - int(minTemp)) * 10 - (10 - round((maxTemp - float(int(maxTemp)))*10)) -(round((minTemp - float(int(minTemp)))*10)))
for x in range(len(temps)):
    if temps[x] is not None:
        temps[x] = round(temps[x], 1)
total = float(volume1) + float(volume2)
percentage1 = float(volume1) / total
percentage2 = float(volume2) / total
newDistillationVols = []
for i in range(len(temps)):
    newDistillationVols.append(round(percentage1 *(np.interp(temps[i], crude1idx, crude1y)) + percentage2*(np.interp(temps[i], crude2idx, crude2y))))
for i in y:
    if i in newDistillationVols:
        print(str(i) + ":" + str(temps[newDistillationVols.index(i)]))
    else:
        print(str(i) + ":" + str(None))
