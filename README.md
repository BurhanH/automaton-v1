# Automaton-v1
Automation framework (UI) - an example. Based on Python, Selenium, and Behave

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/BurhanH/automaton-v1/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/BurhanH/automaton-v1.svg?branch=master)](https://travis-ci.org/BurhanH/automaton-v1)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7f7d510da5284321bfcdc5c290e25bdb)](https://www.codacy.com/app/BurhanH/automaton-v1?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BurhanH/automaton-v1&amp;utm_campaign=Badge_Grade)

## Requirements
Python 3.6.\*, Selenium 3.141.0, Behave 1.2.6, <br>
virtualenv (virtual environment manager), <br>
Firefox 64.\*, geckodriver 0.23, <br>
Chrome 71.\*, chromedriver 2.45 <br> 

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

## How to run particular file or scenario
1) `behave features/google.feature` for Mac / Linux or `behave features\google.feature` for Windows, will execute all scenarios in `google.feature` file  
2) `behave features/google.feature:4` for Mac / Linux or `behave features\google.feature:4` for Windows, will execute the first scenario in `google.feature` file 
3) `behave features/google.feature:17` for Mac / Linux or `behave features\google.feature:17` for Windows, will execute the second scenario with the first parameter from Examples table in `google.feature` file

## How to run test/s in Chrome browser
1) Go to any UI scenario and change the tag from `@firefox` to `@chrome`. Note! Before execution read steps 5-6 from [How to prepare environment](https://github.com/BurhanH/automaton-v1#how-to-prepare-environment) section

To be continue ...
