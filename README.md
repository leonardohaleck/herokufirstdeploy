### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The libraries used in these notebooks are: Pandas, Flask, Plotly and GUnicorn.
The code was written using Python 3.

## Project Motivation<a name="motivation"></a>

The main objective of this project was to learn to use Plotly, Flask and Heroku to Deploy a Web Application.
I used the Stackoverflow Survey 2019 dataset to answer the following questions:

1. What were the most used Languages by Data Scientists and Machine Learning Specialists in 2019?
2. What are the most desired Languages by Data Scientists and Machine Learning Specialists for 2020?

## File Descriptions <a name="files"></a>

• wrangling.py: does the data wrangling
• functions.py: contains some functions to ranking data, sort data and create charts
• app.py: creates the charts and initialize the application in Flask

• survey_results_public_2019.csv: Stackoverflow Survey 2019 dataset

• home.html: contains the HTML code
• Procfile: indicates to Heroku what app Flask to run
• runtime.txt: indicates to Heroku what Python version to use
• requirements.txt: indicates to Heroku what libraries to install

## Results<a name="results"></a>

The Web Appliction can be accessed [here](https://lh-herokufirstdeploy.herokuapp.com/).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Stack Overflow for the data.  You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://www.kaggle.com/mchirico/stack-overflow-developer-survey-results-2019).  Otherwise, feel free to use the code here as you would like! 
