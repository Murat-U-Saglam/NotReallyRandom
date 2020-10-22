import csv
import hashlib
import random
import datetime
import base64
from getpass import getpass
import time
import os

firstname = []
surname = []
hashOfFirst = []
hashOfSecond = []
averageHashArray = []

#Organising the array
with open('names.csv', "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        firstname.append(row[1])
        surname.append(row[0])


def getRandomPerson():
    loadingScren()
    random.seed(None)
    randomIndex = random.randint(0,len(firstname)-1)
    print(firstname[randomIndex], surname[randomIndex])


#Hash the first and second name
for x in range(len(firstname)-1):
    hashedFirstName = hashlib.sha256(firstname[x].encode('utf-8')).hexdigest()
    hashOfFirst.append(hashedFirstName)
    hashedSecondName = hashlib.sha256(surname[x].encode('utf-8')).hexdigest()
    hashOfSecond.append(hashedSecondName)


def randomlyrandom():
    loadingScren()
    currentTime= str(datetime.datetime.now())
    hashOfCurrentTime = hashlib.sha256(currentTime.encode('utf-8')).hexdigest()
    averageHash()
    hashOfCurrentTimeAsInt = int(hashOfCurrentTime, 16)
    Difference=99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    savedIndex=0
    for x in range(len(averageHashArray)):
        temp = averageHashArray[x] - hashOfCurrentTimeAsInt
        if temp <=0:
            temp = temp * -1
        if temp < Difference:
            Difference = temp
            savedIndex = x
    print(firstname[savedIndex], surname[savedIndex])


def averageHash():
    for x in range(len(hashOfFirst)):
        a = int(hashOfFirst[x], 16)
        b = int(hashOfSecond[x], 16)
        averageHashArray.append(a+b//2)

def loadingScren():
    for x in range(20):
        print(".")
        time.sleep(0.01)
        print(". o")
        time.sleep(0.01)
        print(". o O")
        time.sleep(0.01)
        print(". o O @")
        time.sleep(0.01)
        print(". o O @ * \a")
        time.sleep(0.01)

def notSoRandom():
    chosenOne = getpass("")
    chosenOne=chosenOne.upper()
    for x in range(len(firstname)-1):
        if firstname[x] == chosenOne:
            desiredIndex = x
    loadingScren()
    print(firstname[desiredIndex], surname[desiredIndex])


def cwdPick():
    loadingScren()
    currentDirectory = os.getcwd()
    hashOfcurrentDirectory = hashlib.sha256(currentDirectory.encode('utf-8')).hexdigest()
    averageHash()
    hashOfcurrentDirectory = int(hashOfcurrentDirectory, 16)
    Difference=99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    savedIndex=0
    for x in range(len(averageHashArray)):
        temp = averageHashArray[x] - hashOfcurrentDirectory
        if temp <=0:
            temp = temp * -1
        if temp < Difference:
            Difference = temp
            savedIndex = x
    print(firstname[savedIndex], surname[savedIndex])


def main():
    print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*****,,,,...%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*//((#(#((%///*,,,,,.@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,*//(/%#//%%*&@@@*&#(##/(/,@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,,,,*//(((//####***/&&&&&@(#%*@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,/#&##*#%%&&&&&&&&#@&&(((@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,**(#%##%%/#%%%&%%&@&@@#&%#%@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,**,**//((///###%%%%%%%%%@@@@@@&(@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,,..,.,*/(((((##%#%%%%%%%@@@@@@@(%@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...........*((((((###%%#%%%%%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.........,,,... */(###(#######@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@........,,,*,,,,,,.(/(#((/(///((@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@,...,,,,,,****,,*,,,,#####(((/((/(@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@*,,***************/***#(#(#####(((#@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@/*,******/*////////#//.((####((((((/@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%*,*****///(((((((/(&(&,##((((((((##(%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@/**/////(((((####((#@#%,%###(///(/(#(@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#///(/((((###(%&&%##%@#/%%%%####(/((#(&@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@(((&/((##%@#&%#@@%%%#&@%%%%%%#((((((#(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@%(/@/((##%@@%%##%&%%#&%%%%%%%%%%####(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@&//%(#%##%%&%%%%##%##%%%%%%%%%%%%%(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&&((#%&%%%%%%%&&%%&&%&&%%%%%&&%%%%##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&&@&@@&@@@@@&%&@@@&&%%%%#%#&&&&%@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%@@@@@@@@@@@@%%&@@@&&&&%%%####%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@##@@@@@@@@@&&&%%&&&@@@@&&&&%##(%(/(**/%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&
@@@@@@%&@@@&&@&&&&&&@&@@@@@@@@@&@&&@/#@(#*#(#%(/&//%@@@@@@@@@@@@@@@@@@@@@@@&&&&&
@@@@@@@&&&&&@@%%%%%%&&@@@@@@@@@@##*@/((%/**.#/(,,/.@@@@@@@@@@@@@@@@@@@@@@@@@&&&&
@@@@@@&&&&&@@%&&&&&&&@@@@@@@@@@@@%%%#/(*/(*.,..,.   @@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@(/@@@@@@&&%#%@&&&&&@@@@@@@&&@@&%&(#,,&/*.. ** /@@@@@@@@@@@@@@@@@@@@@@@@@@@@
&&&&(/(@@@@@@&%%%@@&&&&&&&&@@&%&@&@&&%%%&(%%%(%##/@@@@@@@@@@&&&&&&&@@@@@@@@@@@@@
&&&#*#&@@@@@&&%%&@&&&&&%%%%@@@&&%@@@&%%&@&#%###((@@@@@@@@&&&&&&&&&&&&@@@@@@@@@@@                                                                   
""")
    while True:
        Flag=input("r:     For Random User\nt:     For watch your Time\nd:     For watch your Directory\nInput:\t")
        if Flag == "r":
            getRandomPerson()
            break
        elif Flag == "t":
            randomlyrandom()
            break
        elif Flag == "rr":
            notSoRandom()
        elif Flag == "d":
            cwdPick()
        else:
            print("Error Input, Double check your Input")


main()