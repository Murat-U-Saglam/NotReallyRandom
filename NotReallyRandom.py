import csv
import hashlib
import random
import datetime
import base64

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
        firstname.append(row[0])
        surname.append(row[1])


def getRandomPerson():
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


def notSoRandom():
    while True:
        print(". o O @ * \a")


def main():
    while True:
        Flag=input("r:     For Random User\nrr:    For Randomly Random\nInput:\t")
        if Flag == "r":
            getRandomPerson()
            break
        elif Flag == "rr":
            randomlyrandom()
            break
        elif Flag == "rrr":
            notSoRandom()
        else:
            print("Print Error Input, Double check your Input")

main()
