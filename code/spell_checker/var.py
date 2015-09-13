#!/usr/bin/env python

from textblob import TextBlob

def main() : 
	sent = TextBlob("my name pras tean is")

	var = sent.correct()
	print var

if __name__ == '__main__' : 
	main()