#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main module

Contains the class TextAnalyser to handle a text

NLP3O is a word game between NLP (Natural Language Processing) and C3PO

Created on Tue Apr 25 15:10:58 2017

@author: Mashimo
"""
from .inputhandler import readStopwords


class TextAnalyser:
    'Text object, with analysis methods' 
    def __init__(self, inputText, language = "EN"):
        self.text = inputText
        self.tokens = []
        self.language = language
        self.stopWords = set(readStopwords(language))
        
    def length(self):
        """ return length of text in chars """
        return len(self.text)
        
    def tokenise(self):
        """ split the text into tokens, store and returns them """
        self.tokens = self.text.split() # split by space; return a list
        return self.tokens
    
    def getTokens(self):
        """ returns the tokens (need to be previously tokenised) """
        return len(self.tokens)
    
    def removePunctuation(self):
        """ remove punctuation from text"""
        import re

        self.text = re.sub(r'([^\s\w_]|_)+', '', self.text.strip()) # remove punctuation

    def removeStopWords(self):
        """ remove stop words from text.
        Stopwords are defined at initialisation based on language.
        Only one set of stopwords is possible (no language mix)"""
        self.tokens = [token for token in self.tokens if token not in self.stopWords]
    


    def preprocessText(self, lowercase=True, removeStopWords=False):
        """ pre-process the text:
            1. lower case 
            2. remove punctuation
            3. tokenise the text
            4. remove stop words"""
        if lowercase:
            self.text = self.text.lower()
    
        self.removePunctuation()

        self.tokenise()  
        
        if removeStopWords:
            self.removeStopWords()
        
    def uniqueTokens(self):
        """ returns the unique tokens"""
        return (len(set(self.tokens)))
    
    def getMostCommonWords(self, n=10):
        """ get the n most common words in the text;
        n is the optional paramenter"""
        from collections import Counter

        wordsCount = Counter(self.tokens) # count the occurrences
    
        return wordsCount.most_common()[:n]
    
