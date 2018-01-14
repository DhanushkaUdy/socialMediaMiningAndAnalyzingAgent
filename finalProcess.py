import tweetsRetriever as twitter
import wordPreProcessing as wordprocess
import nltk
import os
import csv

Splitted = wordprocess.Splitter()
Tagger = wordprocess.POSTagger()
DictionaryTagger = wordprocess.DictionaryTagger([
    'E:\\SocialMediaMinner\\Dictionaries\\products.yml',
    'E:\\SocialMediaMinner\\Dictionaries\\feelings.yml',
    'E:\\SocialMediaMinner\\Dictionaries\\auxiliary.yml'])

productName = []
feelings = []
auxiliary = []

loguserFilepath = 'E:\\SocialMediaMinner\\logged' # current logged users file path
retreivedTweetsFiles = 'E:\\SocialMediaMinner\\RetrievedTweets' # retrieved tweets save file path
finalOutput = 'E:\\SocialMediaMinner\\FinalOutput' # Final Output Save path

for filename in os.listdir(loguserFilepath):
    fName = filename.split('.')[0]
    inputFileStr = 'E:\\SocialMediaMinner\\logged\\' + fName + '.csv'
    twitterId = open(inputFileStr,"r").read()
    custweets = twitter.getTweets()
    reTweets = custweets.get_all_tweets(twitterId)
    # os.remove('E:\\SocialMediaMinner\\logged\\' + fName + '.csv')  #Remove logged file

    if os.path.isfile('E:\\SocialMediaMinner\\RetrievedTweets\\'+ fName + '.txt'):
        os.remove('E:\\SocialMediaMinner\\RetrievedTweets\\'+ fName + '.txt')
        tweetsDataFile = open(os.path.join(retreivedTweetsFiles,'%s.txt' % fName),"w")
        writer = csv.writer(tweetsDataFile)
        writer.writerows(reTweets)
        tweetsDataFile.close()
    else:
        tweetsDataFile = open(os.path.join(retreivedTweetsFiles, '%s.txt' % fName), "w")
        writer = csv.writer(tweetsDataFile)
        writer.writerows(reTweets)
        tweetsDataFile.close()


for filename in os.listdir(retreivedTweetsFiles):
    # print(filename)
    tweetsData = open('E:\\SocialMediaMinner\\RetrievedTweets\\'+ filename,"r").read().split("b'")
    for i in range(1,len(tweetsData)):
        splites_words = Splitted.split(tweetsData[i])
        tags_words = Tagger.pos_tag(splites_words)
        DictTagged = DictionaryTagger.tag(tags_words)
        print (DictTagged)
        print(" ======================================= ")

        lOFArray = len(DictTagged)
        for x in range(0,lOFArray):
            lOfInstance = len(DictTagged[x])
            boolean = False

            for y in range(0, lOfInstance):
                listOfOpinions = str(DictTagged[x][y]).split(',')
                string = listOfOpinions[2]
                opinion = string[3:11]

                if (opinion == "products"):
                    productName.append(listOfOpinions[1])
                    print(listOfOpinions[1])
                elif (opinion == "feelings"):
                    feelings.append(listOfOpinions[1])
                    print(listOfOpinions[1])

            #this is for extract auxiliary
            for z in range(0, lOfInstance):
                listOfOpinions = str(DictTagged[x][z]).split(',')
                string = listOfOpinions[2]
                opinion = string[3:11]

                if (opinion == "auxiliar"):
                    auxiliary.append(listOfOpinions[1].replace("'", ""))
                    print(listOfOpinions[1])
                    boolean = True
                    break

            if(boolean == False):
                auxiliary.append(" noanyadjective")

                # else:
                #     print(isAvailableAuxiliary)
                #     if(isAvailableAuxiliary == False):
                #         auxiliary.append("noanyadjective")

    finalData = open(os.path.join(finalOutput, filename), "w")
    for i in range(0, len(productName)):
        finalData.write(productName[i].replace("'", "").lstrip()+ "" +feelings[i].replace("'", "")+ "" +auxiliary[i]+ "\n")
    finalData.close()





















