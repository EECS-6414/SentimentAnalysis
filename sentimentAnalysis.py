from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas

# Function to return sentiment files for every set of Google Play comment data
def sentiment(pathName, outputFileName):

    # Read file in
    filePath = pandas.read_csv(pathName)

    # Create and name sentiment analysis file
    outputFile = open('Data/outputFiles/'+'Sentiment_Score_for_'+outputFileName+".csv", 'w', encoding='utf8')

    # Create an empty array
    sentences = []

    # Loop through the csv file to find all comments written in English
    for i in range(len(filePath)):
        if filePath['Language'][i] == 'English':
            sentences.append(filePath['Body'][i])

    # Add column names
    outputFile.write('neg,neu,pos,compound\n')

    # Initialize VADER and write the relevant scores to the output file in csv form
    analyzer = SentimentIntensityAnalyzer()
    for sentence in sentences:
        sentiment_dict = analyzer.polarity_scores(str(sentence))
        outputFile.write(str(sentiment_dict['neg'])+",")
        outputFile.write(str(sentiment_dict['neu'])+",")
        outputFile.write(str(sentiment_dict['pos'])+",")
        outputFile.write(str(sentiment_dict['compound']) + ",\n")