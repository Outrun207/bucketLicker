import sys
import argparse
import requests

def doRequest(line):
    bucket = "http://" + line + ".s3.amazonaws.com"
    r = requests.get(bucket)
    statusCode = r.status_code
    if statusCode == 404:
        print(bucket + " does not exist. 404 returned.")
    elif statusCode == 403:
        print(bucket +  " exists. 403 returned.")
    elif statusCode == 200:
        print(bucket +  " exists and is open. 200 returned")
    else:
        print(line + " " + str(statusCode))  

def readTheWordList(wordlist):
    with open(wordlist) as infile:
        for line in infile:
            doRequest(line.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    Bucket Licker! A Python implementation of Bucket Kicker. 
    """)
    parser.add_argument("wordlist", help="Wordlist containing names of bucket's you'd like to check the existance of")
    args = parser.parse_args()
    readTheWordList(args.wordlist)




