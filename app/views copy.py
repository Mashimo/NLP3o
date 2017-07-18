#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:48:15 2017

@author: Mashimo
"""

from app import app
from flask import render_template, flash, request
from .forms import InputTextForm
from .c3po import TextAnalyser
from .inputhandler import getSampleText



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='NL3PO')
    
@app.route('/mytext', methods=['GET', 'POST'])
def analyseThis():
    theInputForm = InputTextForm()
    userText = "and not leave this empty!"
    typeText = "You should write something ..."

    
    if request.method == 'POST':

        if 'D1' in request.form.values():
            userText, typeText = getSampleText(1) #"Call me Ishmael ..."

    
        elif 'GO' in request.form.values():
        #flash('GO  button!')
  
            if theInputForm.validate_on_submit():
                userText = theInputForm.inputText.data
                typeText = "Your text:"

        # start analysing the text
                
        myText = TextAnalyser(userText) # new object

        myText.preprocessText(lowercase = theInputForm.ignoreCase.data,
                              removeStopWords = theInputForm.ignoreStopWords.data)
          # display all user text if short otherwise the first fragment of it
        if len(userText) > 90:
            fragment = userText[:90] + " ..."
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
                           theData = myText.getMostCommonWords(10),
                           inputTypeText = typeText,
                           originalText = fragment,
                           numChars = myText.length(),
                           numTokens = myText.getTokens(),
                           uniqueTokens = uniqueTokensText,
                           commonWords = myText.getMostCommonWords(10))
    
    elif request.method == 'GET':
        return render_template('mytext.html', 
                           title = 'Your input',
                           form = theInputForm)
        

                
@app.route('/results')
def results():
    return render_template('index.html',
                           title='C3PO',
                           user="you should not be here")
    
    