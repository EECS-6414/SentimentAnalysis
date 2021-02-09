from os import listdir

# Function to return all file pathways and their corresponding file names
def files(mainPath):

    # List all folder names in the main pathway
    folderPath = [f for f in listdir(mainPath)]

    # Create a blank array
    fileName = []

    # Save the individual file names
    for i in range(len(folderPath)):
        fileName.append(folderPath[i])

    # Create the requisite file pathways
    for i in range(len(folderPath)):
        folderPath[i] = mainPath+"/"+folderPath[i]+"/"+folderPath[i]+".csv"

    # Return the file pathway and the file name itself
    return folderPath, fileName