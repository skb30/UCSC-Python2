"""

Scott Barth
Assignment 3 Part 2


Write a program that will read the file, 'red-headed-league.txt', count the frequency of the words and
 store it as a csv file.

Create a class called WordCounter with the following methods.

def __init__(self,filename) where filename is the name of the text file, 'red-headed-league.txt'. This
 function should read the text file

def removepunctuation(self) must remove all the punctuations and leave only alphabets and numbers
 in each word

def findcount(self) must count the frequency of each word and store it in a instance variable
 called countdict

def writecountfile(self,csvfilename) writes the content of the countdict variable to a csv file with
 two columns. The first column is the word and second column is the count.

Create an instance of the class and call appropriate method and store the result in a csv file.
 Printout the five most popular words.


NOTE: DO NOT USE THE COUNTER DATA STRUCTURE IN COLLECTIONS MODULE.

"""


import csv
import operator

class WordCounter():
    def __init__(self, filename):
        self.words = ""
        self.clean = []
        self.countdict = {}


        # open the file for read using the pythonic way.
        with open(filename, 'r') as fo:
           self.words = fo.read().split()

    def removepunctuation(self):
        temp = []
        clist = []


        # clean the data for processing



        # some words have hyphens so we need to split those too
        for word in self.words:
            temp = word.split('-')
            if len(temp) > 1:
                for item in temp:
                    clist.append(item)
            else:
                clist.append(word)
        # empty list because we're going to use it again
        temp = []

        # now we can clean
        for word in clist:

            # for each word, strip out unwanted characters
            for c in word.rstrip():
                if c.isalnum():
                    temp.append(c)
            # convert the list to a string and append it to the clean list
            self.clean.append(''.join(temp))

            temp = []

    def findcount(self):
        count = 0
        usedwords = []

        # process each word in the list counting the occurences
        for word in self.clean:

            # let's speed it up. If we've already seen this word, no need to count it again.
            if usedwords.count(word) > 0:
                continue
            # eliminate duplicate searches
            usedwords.append(word)

            count = self.clean.count(word)

            self.countdict[word] = count
            # print("The word '{}' occurs {} times in the file.".format(word, count))

        # sort and print
        sorted_list = sorted(self.countdict.items(), key=operator.itemgetter(1), reverse=True)
        i = 0
        print("List the five most popular words:\n")

        while True:
            if i > 5:
                break

            print("'{}' was used {} times.".format(sorted_list[i][0],sorted_list[i][1]))
            i+= 1



    def writecountfile(self, csvfilename):
        # open the file
        temp = []
        with open(csvfilename, 'w') as fo:
            wo = csv.writer(fo)
            for key,value in self.countdict.items():
                temp.append([key, value])


            wo.writerows(temp)





word = WordCounter('red-headed-league.txt')
word.removepunctuation()
word.findcount()
word.writecountfile('mycsv.csv')

