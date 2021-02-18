from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas

# Function to return sentiment files for every set of Google Play comment data
def sentiment(pathName, outputFileName, statisticFile):

    # Read file i
    filePath = pandas.read_csv(pathName)

    # Create and name sentiment analysis file
    outputFile = open('/Users/jaime/Documents/York_University/Winter_2021/Data_Vizualization/Project/Sentiment/'+'Sentiment_Score_for_'+outputFileName+".csv", 'w', encoding='utf8')

    # Create an empty array
    sentences = []

    # Create an empty array
    author = []
    date = []
    appName = []
    appPath = []

    # Loop through the csv file to find all comments written in English
    for i in range(len(filePath)):
        if filePath['Language'][i] == 'English' and len(str(filePath['Author'][i]))>2 and 'google' not in str(filePath['Author'][i]).lower() and 'nan' != str(filePath['Author'][i]).lower():
            sentences.append(filePath['Body'][i])
            author.append(filePath['Author'][i])
            date.append(filePath['Date'][i])

    # Get app info
    appName.append(filePath['App'][1])
    appPath.append(filePath['App ID'][1])


    # Add column names
    outputFile.write('Author, date, neg,neu,pos,compound, sentiment\n')

    # Initialize VADER and write the relevant scores to the output file in csv form
    analyzer = SentimentIntensityAnalyzer()
    negProportion = 0
    posProportion = 0
    nReviews = len(sentences)
    for i, sentence in enumerate(sentences):

        # neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
        sentiment_classification = 'neutral'

        sentiment_dict = analyzer.polarity_scores(str(sentence))

        # sentiment compound score classification
        if (sentiment_dict['compound'] >= 0.05):
            sentiment_classification = 'positive'
            posProportion += 1
        elif(sentiment_dict['compound'] <= -0.05):
            sentiment_classification = 'negative'
            negProportion += 1

        outputFile.write(str(author[i])+",")
        outputFile.write(str(date[i])+",")
        outputFile.write(str(sentiment_dict['neg'])+",")
        outputFile.write(str(sentiment_dict['neu'])+",")
        outputFile.write(str(sentiment_dict['pos'])+",")
        outputFile.write(str(sentiment_dict['compound'])+",")
        outputFile.write(str(sentiment_classification)+ ",\n")

        nReviews += 1

    # stats for the app
    statisticFile.write(str(appName)+",")
    statisticFile.write(str(appPath)+",")
    statisticFile.write(str(nReviews)+",")
    statisticFile.write(str(division(negProportion, nReviews))+",")
    statisticFile.write(str(division((nReviews-negProportion-posProportion), nReviews))+",")
    statisticFile.write(str(division(posProportion, nReviews))+",")
    statisticFile.write(str(getSentiment(division(posProportion, nReviews), division(negProportion, nReviews), division((nReviews-negProportion-posProportion), nReviews))))
    statisticFile.write(",\n")


# Division avoiding zero denominator
def division(n, d):
    return n / d if d else 0


def getSentiment(pos, neg, neu):
    if pos > neg and pos > neu:
        return 'positive'
    elif neg > pos and neg > neu:
        return 'negative'
    else:
        return 'neutral'
