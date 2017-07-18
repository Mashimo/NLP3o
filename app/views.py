#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Routing module for NLP3O app

Created on Tue Apr 18 17:48:15 2017

@author: Mashimo
"""

from app import app
from flask import render_template, flash, request
from .forms import InputTextForm
from .nlp3o import TextAnalyser
from .inputhandler import getSampleText

    # Submit button in web for pressed
@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def manageRequest():
    
      # some useful initialisation
    theInputForm = InputTextForm()
    userText = "and not leave this empty!"
    typeText = "You should write something ..."
    language = "EN"
    
      # POST - retrieve all user submitted data
        
    inputFromBook = request.form['book'] # which text?
        
    # DEBUG flash('the book selected is: %s' % inputFromBook)

    if inputFromBook == "mobydick":
        userText, typeText = getSampleText(1) 
        language = "EN"
            
    elif inputFromBook == "marinetti":
        userText, typeText = getSampleText(2)
        language = "IT"

    elif inputFromBook == "urteil":
        userText, typeText = getSampleText(3)
        language = "DE"

    else:
        if theInputForm.validate_on_submit():
            userText = theInputForm.inputText.data
            typeText = "Your own text"
            language = request.form['lang'] # which language?
                
    # DEBUG flash('read:  %s' % typeText)
     
          # Which kind of user action ?
    if 'TA'  in request.form.values(): 
            # GO Text Analysis 

               # start analysing the text   
        myText = TextAnalyser(userText, language) # new object

        myText.preprocessText(lowercase = theInputForm.ignoreCase.data,
                              removeStopWords = theInputForm.ignoreStopWords.data)
            
               # display all user text if short otherwise the first fragment of it
        if len(userText) > 99:
            fragment = userText[:99] + " ..."
        else:
            fragment = userText
            
              # check that there is at least one unique token to avoid division by 0
        if myText.uniqueTokens() == 0:
            uniqueTokensText = 1
        else:
            uniqueTokensText = myText.uniqueTokens()
            
              # render the html page
        return render_template('results.html',
                           title='Text Analysis',
                           inputTypeText = typeText,
                           originalText = fragment,
                           numChars = myText.length(),
                           numTokens = myText.getTokens(),
                           uniqueTokens = uniqueTokensText,
                           commonWords = myText.getMostCommonWords(10))
        
    else:                
        return render_template('future.html',
                           title='Not yet implemented')


       
  # render web form page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def initial():
      # render the initial main page            
    return render_template('index.html', 
                           title = 'NLP3o - Your input',
                           form = InputTextForm())
  
@app.route('/results')
def results():
    return render_template('index.html',
                           title='NLP3o - Text Analysis')
    
  # render about page
@app.route('/about')
def about():
    return render_template('about.html',
                           title='About NLP3o') 