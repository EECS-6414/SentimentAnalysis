from _csv import reader

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas

# Function to return sentiment files for every set of Google Play comment data
from authors.structure import Structure


def analyzeAuthors(authorList):

    # Read file i
    print("Processing...")

    outputFile = open('/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/final_group.csv', 'w', encoding='utf8')

    newList = []
    i = 0
    hasDuplicated = False
    while i < len(authorList) - 1:
        currentAuthor = authorList[i].split(",")[0]
        nextAuthor = authorList[i+1].split(",")[0]
        if currentAuthor == nextAuthor:
            currentData = authorList[i].split(",")
            nextData = authorList[i+1].split(",")
            currentDataApp = currentData[1]
            currentDataAppId = currentData[len(currentData)-1]
            nextDataApp = nextData[1]
            nextDataAppId = nextData[len(nextData)-1]
            futureData = currentAuthor + "," + currentDataApp +";"+ nextDataApp + ","+ currentDataAppId +";"+ nextDataAppId
            authorList[i] = futureData
            # combine
            i += 2
            hasDuplicated = True
        elif hasDuplicated:
            newList.append(authorList[i-2])
            hasDuplicated = False
        else:
            i += 1



    print("Printing in csv...")

    for a in newList:
        parts = a.split(",")
        outputFile.write(str(a)+"\n")
