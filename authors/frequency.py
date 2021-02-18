from _csv import reader
from collections import Counter

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas

# Function to return sentiment files for every set of Google Play comment data
from authors.structure import Structure


def frequencyAuthors():
    # Read file i
    print("Frequency...")

    authorsFileReading = open(
        '/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/final_group.csv', 'r',
        encoding='utf8')
    outputFile = open(
        '/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/Names/frequency.csv', 'w',
        encoding='utf8')

    outputFile.write('Author,App,App ID,Total\n')

    for a in authorsFileReading:
        count = a.split(';')
        frequency = "," + str((len(count)-1)/2 + 1)
        outputFile.write(a[0: len(a) - 1] + frequency + "\n")
