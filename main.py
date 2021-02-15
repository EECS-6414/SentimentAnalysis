import threading
from collections import OrderedDict
from concurrent.futures import thread
from time import sleep

import pandas

from authors.appWithAuthorsAnalysis import analyzeAuthors
from authors.authorsExtractor import extractAuthors
from authors.frequency import frequencyAuthors
from authors.structure import Structure
from fileNames import files

# A program to produce sentiment analysis output data on Google Play Store reviews using VADER Sentiment Analysis
def main():
    # Give main path name for data
    mainPath = '/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/gitlab/datasets/Google'

    # Call file name function to get all file names and pathways
    readFile = files(mainPath)

    # Create statistic file
    # statisticFile = open('/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/sentiment_statistics.csv', 'w', encoding='utf8')

    # Create name file
    # authorsFile = open('/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/Names/names.csv', 'w', encoding='utf8')

    # Create name file
    authorsFileReading = open('/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/Names/names.csv', 'r', encoding='utf8')

    # Create name file
    authorsFinalAnalysis= open('/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/Names/finalAuthors.csv', 'w', encoding='utf8')

    # Add columns
    # statisticFile.write('App,App ID,Reviews,neg,neu,pos\n')

    # Add columns
    # authorsAppFile.write('Author,Frequency\n')
    # for a in authorsFileReading:
    #     authorsAppFile.write(str(a))


    # Call sentiment function to get csv output files for all of the applications with English reviews
    # for i in range(len(readFile[0])):
    #     sentiment(readFile[0][i], readFile[1][i], statisticFile)

    # Extract the name of authors to create network
    # for i in range(len(readFile[0])):
    #     extractAuthors(readFile[0][i], authorsFile)

    # for generating csv with apps and authors
    authorListAux = []

    for i in authorsFileReading:
        authorListAux.append(i[0: len(i)-1])

    authorListAux.sort()

    # adds the common apps
    analyzeAuthors(authorListAux)

    sleep(4)
    # to count the frequency
    frequencyAuthors()


# Run Main
if __name__ == "__main__":
    main()