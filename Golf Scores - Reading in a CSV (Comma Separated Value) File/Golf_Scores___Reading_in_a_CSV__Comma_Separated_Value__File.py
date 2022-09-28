#Golf Program  

# added a comma separated file into the project folder and named it "scores.txt" which consists of three lists (arrays). The lists are forenameList, surnameList and scoreList.

# wrote the golfer's name and lowest score and saved it to a file in the project folder and named it "winner.txt"

# wrote the golfer's name and highest score and saved it to a file in the project folder and named it "loser.txt"

#libraries 
import csv

#list defintions
forenameList = []
surnameList  = []
scoreList    = []


#methods
def fillLists():
    with open("scores.txt", "r") as csvFile:
        csvReader = csv.reader(csvFile) # created a variable called csvReader which will use the csv library and read the text file, returning the data.
        for row in csvReader:
            surnameList.append(row[0])
            forenameList.append(row[1])
            scoreList.append(int(row[2]))
        #end for
    #end with
    print(surnameList)  # delete after running
    print(forenameList) # delete after running
    print(scoreList)    # delete after running
    return surnameList, forenameList, scoreList
#end fillLists

def findMaximum(scoreList):
    maxScore = None
    maxPosition = None
    if len(scoreList)>0:
        maxScore = scoreList[0]
        for index in range (len(scoreList)):
            if scoreList[index] > maxScore:
                maxScore = scoreList[index]
                maxPosition = index
            #end if
        #end for
    #end if
    print (maxScore, "at position ", maxPosition)  # delete after running
    return maxScore, maxPosition
#end findMaximum

def findMinimum(scoreList):
    minScore = None
    minPosition = None
    if len(scoreList)>0:
        minScore = scoreList[0]
        for index in range (len(scoreList)):
            if scoreList[index] < minScore:
                minScore = scoreList[index]
                minPosition = index
            #end if
        #end for
    #end if
    print (minScore, "at position ", minPosition)  # delete after running
    return minScore, minPosition
#end findMaximum

def writeToFile(maxScore,maxPosition, minScore,minPosition):
    #write to file Winner
    winnerName = forenameList[minPosition] + " " + surnameList[minPosition]
    print (winnerName + " had the Lowest score of " + str(minScore))
    with open ("winner.txt","w") as f:
        f.write(winnerName + " had the Lowest score of " + str(minScore))
    #end with

    #write to File loser
    winnerName = forenameList[maxPosition] + " " + surnameList[maxPosition]
    print (winnerName + " had the highest score of " + str(maxScore))
    with open ("loser.txt","w") as f:
        f.write(winnerName + " had the highest score of " + str(maxScore))
    #end with
#end writeToFile


#main program
surnameList, forenameList, scoreList = fillLists()
maxScore, maxPosition = findMaximum(scoreList)
minScore, minPosition  = findMinimum(scoreList)
writeToFile(maxScore,maxPosition, minScore,minPosition)

