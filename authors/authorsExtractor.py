from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas

# Function to return sentiment files for every set of Google Play comment data
def extractAuthors(pathName, authorsFile):

    # Read file i
    filePath = pandas.read_csv(pathName)

    # Create an empty array
    authors = []

    # Loop through the csv file to find all authors in English
    for i in range(len(filePath)):
        if filePath['Language'][i] == 'English':
            # don't add these authors
            if ('google' not in str(filePath['Author'][i]).lower()) and ('nan' != str(filePath['Author'][i]).lower()):
                text = str(filePath['Author'][i])+","+str(filePath['App'][i])+","+str(filePath['App ID'][i])
                authors.append(text)

    for author in authors:
        authorsFile.write(str(author) + "\n")