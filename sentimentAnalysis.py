from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas

# Function to return sentiment files for every set of Google Play comment data
def sentiment(pathName, outputFileName):

    # Read file i
    filePath = pandas.read_csv(pathName)

    # Create and name sentiment analysis file
    outputFile = open('/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/Sentiment/'+'Sentiment_Score_for_'+outputFileName+".csv", 'w', encoding='utf8')

    # Create an empty array
    sentences = []

    # Create an empty array
    reviewId = []

    # Loop through the csv file to find all comments written in English
    for i in range(len(filePath)):
        if filePath['Language'][i] == 'English':
            sentences.append(filePath['Body'][i])
            reviewId.append(filePath['Review ID'][i])


    # Add column names
    outputFile.write('Review ID,neg,neu,pos,compound, sentiment\n')

    # Initialize VADER and write the relevant scores to the output file in csv form
    analyzer = SentimentIntensityAnalyzer()
    for i, sentence in enumerate(sentences):

        # neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
        sentiment_classification = 'neutral'

        sentiment_dict = analyzer.polarity_scores(str(sentence))

        # sentiment compound score classification
        if (sentiment_dict['compound'] >= 0.05):
            sentiment_classification = 'positive'
        elif(sentiment_dict['compound'] <= -0.05):
            sentiment_classification = 'negative'

        outputFile.write(str(reviewId[i])+",")
        outputFile.write(str(sentiment_dict['neg'])+",")
        outputFile.write(str(sentiment_dict['neu'])+",")
        outputFile.write(str(sentiment_dict['pos'])+",")
        outputFile.write(str(sentiment_dict['compound'])+",")
        outputFile.write(str(sentiment_classification)+ ",\n")