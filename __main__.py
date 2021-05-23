#!/usr/bin/Python3
import tasks1 as t1
import tasks2 as t2
import task3 as t3
import tasks4 as t4
import task5 as t5

import gui as gui
import sys
import getopt
from datetime import datetime

# Author: Vincent Chung
# All code was written by the author

# Main entry point for the program
# Run from outside the folder with:
# python3 cw2 -u user_id -d doc_id -t task_id -f file_name -s sorting
# Note: implementation expects the input file to be in the same directory as cw2
# NOT inside cw2

# Declare variables to null by default
user_id = None
doc_id = None
task_id = None
file_name = None
sorting = "d"

# Stores input in array of arguments for getopt
argv = sys.argv[1:]

# Try/Except to get arguments from command line with given tags to prevent GetoptErrors
try:
    opts, arg = getopt.getopt(argv, "u:d:t:f:s:")
except getopt.GetoptError as e:
    print(e)
    opts = []

# Loop through all arguments to find user id, doc id, task id, and file name
# '-s' is used to input desired sorting for task 4d (a:ascending or d:descending)
# Runs without sort input - default descending order
for opt, arg in opts:
    if opt in ['-u']:
        user_id = arg
    elif opt in ['-d']:
        doc_id = arg
    elif opt in ['-t']:
        task_id = arg
    elif opt in ['-f']:
        file_name = arg
    elif opt in ['-s']:
        sorting = arg


# Input task = task1a
if('1a' in task_id):
    print('Running Task 1a')
    tstart = datetime.now()
    country = t1.by_country(file_name, doc_id)
    tfinish = datetime.now()
    ms = tfinish - tstart
    print(ms)

# Input task = task1b
if('1b' in task_id):
    print('Running Tasks 1a and 1b')
    tstart = datetime.now()
    country = t1.by_country(file_name, doc_id)
    t1.to_continent(country)
    tfinish = datetime.now()
    ms = tfinish - tstart
    print(ms)

# Input task = task2a
if('2a' in task_id):
    print('Running Task 2a')
    tstart = datetime.now()
    t2.by_ua(file_name)
    tfinish = datetime.now()
    ms = tfinish - tstart
    print(ms)

# Input task = task2b
if('2b' in task_id):
    print('Running Task 2a and 2b')
    tstart = datetime.now()
    user_agents = t2.by_ua(file_name)
    t2.by_browser(user_agents)
    tfinish = datetime.now()
    ms = tfinish - tstart
    print(ms)

# Input task = task 3
if('3' in task_id):
    print('Running Task 3')
    tstart = datetime.now()
    t3.reader_profile(file_name)
    tfinish = datetime.now()
    ms = tfinish - tstart
    print(ms)

# Input task = task 4d
if('4d' in task_id):
    print('Running task 4d')
    tstart = datetime.now()
    t4.also_likes(file_name, doc_id, user_id, sorting)
    tfinish = datetime.now()
    ms = tfinish - tstart
    print(ms)

# Input task = task 5
if('5' in task_id):
    print("Running task 5")
    tstart = datetime.now()
    t5.main_call(file_name, doc_id, user_id)
    tfinish = datetime.now()
    ms = tfinish - tstart
    print(ms)

# Input task = task 6
# Launches the GUI
if('6' in task_id):
    print('Launching GUI')
    gui.ACTIVE   
    gui.launch() 
