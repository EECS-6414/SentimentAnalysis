from _csv import reader
from string import printable, ascii_letters, digits


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
        if currentAuthor == '':
            authorList[i] = authorList[i][1: len(authorList)]
            currentAuthor = authorList[i].split(",")[0]
        # remove the authors with special char at first position
        if set(authorList[i][0:1]).difference(ascii_letters):
            i += 1
            continue
        nextAuthor = authorList[i+1].split(",")[0]
        repeatName = False
        if currentAuthor == nextAuthor and len(currentAuthor) > 2: # only names bigger than 3 chart
            cont = 0
            for j in range(i, len(authorList)-1):
                nextAuthor = authorList[j+1].split(",")[0]
                if currentAuthor == nextAuthor:
                    currentData = authorList[i].split(",")
                    nextData = authorList[j+1].split(",")
                    currentDataApp = currentData[1]
                    currentDataAppId = currentData[len(currentData)-1]
                    nextDataApp = nextData[1]
                    nextDataAppId = nextData[len(nextData)-1]
                    if currentDataApp == nextDataApp:
                        repeatName = True
                    futureData = currentAuthor + "," + currentDataApp +";"+ nextDataApp + ","+ currentDataAppId +";"+ nextDataAppId
                    authorList[i] = futureData
                    cont += 1
                else:
                    # add to new list
                    if repeatName:
                        i += cont
                        repeatName = False
                    else:
                        newList.append(authorList[i])
                        i += cont
                    break
        else:
            i += 1



    print("Printing in csv...")

    for a in newList:
        parts = a.split(",")
        outputFile.write(str(a)+"\n")
