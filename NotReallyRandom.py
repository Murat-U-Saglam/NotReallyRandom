import csv
import hashlib
import random
import os

firstname = []
surname = []
hashOfFirst = []
hashOfSecond = []

#Organising the array
with open('names.csv', "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        firstname.append(row[0])
        surname.append(row[1])


#Use maybe for later
for x in range(len(firstname)-1):
    hashedFirstName = hashlib.sha256(firstname[x].encode('utf-8')).hexdigest()
    hashOfFirst.append(hashedFirstName)
    hashedSecondName = hashlib.sha256(surname[x].encode('utf-8')).hexdigest()
    hashOfSecond.append(hashedSecondName)

def getRandomPerson():
    random.seed(None)
    randomIndex = random.randint(0,len(firstname)-1)
    print(firstname[randomIndex], surname[randomIndex])

def randomlyrandom():
    print("Being Created")

def main():
    while True:
        Flag=input("r:     For Random User\nrr:    For Randomly Random\nInput:\t")
        if Flag == "r":
            getRandomPerson()
            break
        elif Flag == "rr":
            randomlyrandom()
            break
        else:
            print("Print Error Input, Double check your Input")

main()





