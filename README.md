# Rules engine to calculate supplemental benefits

This repository contains the code for my submission.

## Description

This program acts as a rules engine and assesses whether a client qualifies for a supplement in December. If the client qualifies for the supplement, this program will calculate the appropriate amount based on their specific assistance program 
and any additional eligibility criteria.

## Getting Started

### Dependencies

To get started, you must have git and python installed on your computer. To install python you can refer to https://www.python.org/downloads/ and to install git you can refer to https://github.com/git-guides/install-git

### Installing the program

To install the program you must use git to clone it onto your computer. You can do this by running the following in terminal:

```
git clone https://github.com/azingzap/winterRulesEngine.git

```
Then `cd` into the project directory where you will install the requirements file by running:

```
cd winterRulesEngine
pip install -r requirements.txt
```
After installing the requirements file you will have all the proper packages needed to run the program.

### Executing the program

To begin running the program you must first ensure you are in the `RulesEngine directory`. You can get there by running:

```
cd RulesEngine 
```
In that directory open the `config.py` file and declare the topic id by changing <addTopicID>:
```
topicID = "<addTopicID>"
```

After that, run the `client.py` file. You can run this file in any terminal by running:

```
python client.py
```

This file ensures that the client created subscribes to the Winter Application. You can then switch over and enter the desired values into the winter application and watch the message from the Winter Application get published to the client. From there you 
will be able to watch the client publish the new message to the output topic all in the terminal. 

**Please ensure that the topic ID matches the ID in the Winter Application**

## If Winter Application does not work

If the winter application does not work for you like it did not work for me you can run a winter Application imitator in `app_Imitation.py` I created.

### How to execute the Winter Application imitator

While the `client.py` file is running, open another terminal or console and run the `app_Imitation.py` file that is in the same directory as the `client.py` file. You can run this file in any python idle or terminal by running:
```
python app_Imitation.py
```
Then switch back to the terminal running "client.py" and watch the output. In `app_Imitation.py`, it is hard coded to use an 
example input for a couple with 8 children that require benefits.

## How to run unit tests
To run the unit tests you must be somewhere in the project directory. from there you can run the unit tests by typing the following in the terminal:
```
pytest
```
