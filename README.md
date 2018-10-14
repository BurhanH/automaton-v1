# Automaton-v1
Automation framework (UI) - an example. Based on Python, Selenium, and Behave

[![Build Status](https://travis-ci.org/BurhanH/automaton-v1.svg?branch=master)](https://travis-ci.org/BurhanH/automaton-v1)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7f7d510da5284321bfcdc5c290e25bdb)](https://www.codacy.com/app/BurhanH/automaton-v1?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BurhanH/automaton-v1&amp;utm_campaign=Badge_Grade)

## Requirements
Python 3.6.\*, Selenium 3.14.0, Behave 1.2.6, <br>
virtualenv (virtual environment manager), <br>
Firefox 62.\*, geckodriver 0.22, <br>
Chrome 69.\*, chromedriver 2.42 <br> 

## Project structure
```text
-- automaton-v1
   |-- .gitattributes
   |-- .gitignore
   |-- .travis.yml
   |-- LICENSE
   |-- README.md
   |-- requirements.txt
   `-- features
       |-- environment.py
       |-- browser.feature
       |-- google.feature
       |-- tutorial.feature
       `-- steps
           |-- browser.py
           |-- google.py
           |-- tutorial.py
```

## How to prepare environment
1) Install [Python](https://www.python.org/downloads/)
2) Install and configure [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3) Clone or copy (download) the repository into your virtual environment
4) Activate virtual environment, move to `automaton-v1` folder, and execute command `pip install -r requirements.txt`
5) Install Firefox / Chrome web browser
6) Download, extract and move geckodriver / chromedriver into `bin` folder for Mac/Linux, `Scripts` folder for Windows on virtual environment

## How to run tests
1) Open terminal window
2) Move to virtual environment folder
3) Activate virtual environment
4) Move to `automaton-v1` folder
5) Execute `behave`

## How to run particular file / scenario
1) `behave features/google.feature` for Mac / Linux or `behave features\google.feature` for Windows, will executes all scenarios in `google.feature` file  
2) `behave features/google.feature:4` for Mac / Linux or `behave features\google.feature:4` for Windows, will executes the first scenario in `google.feature` file 
3) `behave features/google.feature:17` for Mac / Linux or `behave features\google.feature:17` for Windows, will executes the second scenario with first parameter from Example table in `google.feature` file

To be continue ...
