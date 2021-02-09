from sentimentAnalysis import sentiment
from fileNames import files

# A program to produce sentiment analysis output data on Google Play Store reviews using VADER Sentiment Analysis
def main():
    # Give main path name for data
    mainPath = 'Data/Cleaned_reviews_set_2'

    # Call file name function to get all file names and pathways
    readFile = files(mainPath)

    # Call sentiment function to get csv output files for all of the applications with English reviews
    for i in range(len(readFile[0])):
        sentiment(readFile[0][i], readFile[1][i])

# Run Main
if __name__ == "__main__":
    main()