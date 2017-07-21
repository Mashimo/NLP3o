# NLP3o

NLP3o is a set of tools for Natural Language Processing, and a web app for educational purpose.

The goal is to understand how the main NLP algorithms work.
No efficiency nor speed.

The name NLP3o is a word game between NLP and the protocol robot C3PO.<br>


## Key Features

* Tokenise a text
* Remove stop words (English, German, Italian dictionaries)
* Pre-process text (remove punctuation, lower case)
* Extract top words

### Prerequisites

Everything you need is detailed in the requirements text file (req.txt).  
This app is built using **Python 3**


### Installing

To clone and run this application, you'll need Git.

    # Clone this repository
    $ git clone https://github.com/Mashimo/NLP3o

    # Install dependencies
    # Please refer to Python and Flask documentation

## Run the app
To start the app you just run this script.  
On OS X, Linux and Cygwin you have to indicate that this is an executable file before you can run it:

    $ chmod a+x run.py
Then the script can simply be executed as follows:

    ./run.py


On Windows you have to run the script as an argument to the Python interpreter from the virtual environment, e.g.

    $ flask\Scripts\python run.py
After the server initializes it will listen on port 5000 waiting for connections.  
Now open up your web browser and enter one of the following URLs in the address field:

    http://localhost:5000

    http://localhost:5000/index

### Screenshots
Home page

![User-entered text](/READMEimages/text.png)

Settings

![Settings](/READMEimages/Settings.png)

Results page

![Results](/READMEimages/Results.png)
## Use Heroku app

The app can be tested on a Heroku dyno too. (soon)


## Credits - built with:

* [Python 3](https://www.python.org/downloads/) - the language
* [Flask](http://flask.pocoo.org/) - the web micro-framework
* [d3](https://d3js.org/) - the interactive graphics library


## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

* Hat tip to [dataBASIC.io](https://www.databasic.io/) for the inspiration
* the Stanford NLP course
