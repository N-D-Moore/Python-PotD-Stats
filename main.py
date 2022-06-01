import csv

stats = {
    #job, race, food, total
    "STR": [0,0,0,0],
    "DEX": [0,0,0,0],
    "VIT": [0,0,0,0],
    "INT": [0,0,0,0],
    "MND": [0,0,0,0],
    "PIE": [0,0,0,0],
    "AP": [0,0,0,0],
    "DH": [0,0,0,0],
    "CH": [0,0,0,0],
    "AMP": [0,0,0,0],
    "HMP": [0,0,0,0],
    "DET": [0,0,0,0],
    "SKS": [0,0,0,0],
    "SPS": [0,0,0,0],
    "TEN": [0,0,0,0]
}

def updateRaceStats(data=[]):
    stats["STR"][1] = data[1]
    stats["AP"][1] = data[1]
    stats["DEX"][1] = data[2]
    stats["VIT"][1] = data[3]
    stats["INT"][1] = data[4]
    stats["AMP"][1] = data[4]
    stats["MND"][1] = data[5]
    stats["HMP"][1] = data[5]

def updateJobStats(data=[]):
    for i, x in enumerate(stats):
        stats[x][0] = data[i+1]

def updateFoodStats(data=[]):
    temp = int(stats[data[1]][3])*0.10
    if temp < int(data[2]):
        stats[data[1]][2] = int(temp)
    else:
        stats[data[1]][2] = data[2]
    
    temp = int(stats[data[3]][3])*0.10
    if temp < int(data[4]):
        stats[data[3]][2] = int(temp)
    else:
        stats[data[3]][2] = data[4]

    temp = int(stats[data[5]][3])*0.10
    if temp < int(data[6]):
        stats[data[5]][2] = int(temp)
    else:
        stats[data[5]][2] = data[6]

def updataTotalStats():
    for x in stats:
        stats[x][3] = int(stats[x][0])+int(stats[x][1])+int(stats[x][2])

#get user input and parse respective csv files
with open("RacialStats.csv") as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)
print("Select race")
for i in range(len(data)):
    if i>0:
        print("[" + str(i) + "]", data[i][0])
race = input()
race = data[int(race)]
updateRaceStats(race)
data.clear()

with open("JobStats.csv") as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)
print("Select Job")
for i in range(len(data)):
    if i>0:
        print("[" + str(i) + "]", data[i][0])
job = input()
job = data[int(job)]
updateJobStats(job)
data.clear()

with open("FoodStats.csv") as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)
print("Select Food")
for i in range(len(data)):
    if i>0:
        print("[" + str(i) + "]", data[i][0])
food = input()
food = data[int(food)]
updataTotalStats()
updateFoodStats(food)
updataTotalStats()
data.clear()

#print table
for i in range(44):
    print("-", end="")
    if i==43:
        print("")
print ("|{:^6} | {:^6} | {:^6} | {:^6} | {:^6}|".format("STAT", "JOB", "RACE", "FOOD", "TOTAL"))
for i in range(42):
    if i==0:
        print("|", end="")
    print("-", end="")
    if i==41:
        print("|")
for i, x in stats.items():
    print ("|{:^6} | {:^6} | {:^6} | {:^6} | {:^6}|".format(i, x[0], x[1], x[2], x[3]))
for i in range(44):
    print("-", end="")
    if i==43:
        print("")
        
#print out stat meanings
print(int((150*(stats["PIE"][3]-218))/600), "additional Mana Points per server tick for Healers")
print(str(int((550*(stats["DH"][3]-354))/600)/10) + "% chance to Direct Hit increasing damage by 25%")
print(str(int((200*(stats["CH"][3]-354))/600+50)/10) + "% chance to Critical Hit increasing damage by " + str((400+int((200*(stats["CH"][3]-354))/600))/10) + "%")
print(str(int((140*(stats["DET"][3]-218))/600+1000)/1000))
print((1000+int((130*(stats["SKS"][3]-354))/600))/1000, "increased Auto Attack, Damage over Time, and Healing over Time from Skills")
print("Cast time of skills reduced from 2.5 seconds to " + str(int(2500*(1000+round(130*(354-stats["SKS"][3])/600))/10000)/100) + " seconds")
print((1000+int((130*(stats["SPS"][3]-354))/600))/1000, "increased Auto Attack, Damage over Time, and Healing over Time from Spells")
print("Cast time of spells reduced from 2.5 seconds to " + str(int(2500*(1000+round(130*(354-stats["SPS"][3])/600))/10000)/100) + " seconds")
print("Outgoing damage and healing multiplied by", (1000+int((100*(stats["TEN"][3]-354))/600))/1000)
print("Incoming damage and healing multiplied by", (1000-int((100*(stats["TEN"][3]-354))/600))/1000)
