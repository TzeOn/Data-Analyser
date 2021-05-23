#!/usr/bin/Python3
import sys, ujson
import matplotlib.pyplot as plt
import re

# Function to generate a histogram of reads by useragent
def by_ua(file_name):
    data = {}
    lst = {}

    # iterate through json lines file and process data line by line
    for line in open(file_name, 'r', encoding='utf-8'):
        s = ujson.loads(line)
        data = s  
        ua = data.get('visitor_useragent')
        
        # if user agent already exists in new list, update with incremented count value
        if(str(ua) in lst):            
            n = lst.get(ua) + 1
            lst[ua] = n
        # if user agent does not exist; add it to the list with default count value 1
        if(str(ua) not in lst):
            lst[ua] = 1

    # Assign title, labels, and colours for histogram then display it
    # Visitor useragents on X-Axis
    # Views on Y-Axis 
    plt.title('Browser identifiers for file: ' + file_name)
    plt.xlabel('Browser identifiers')
    plt.ylabel('Views')
    plt.bar(lst.keys(), lst.values(), color='b')
    plt.show()

    return lst

# Refines the function of 2a by isolating the browser name from the user agent
# Refined using RegEx
def by_browser(dict_input):
    lst = {}
    # RegEx from start of the string to the first '/' character
    pattern = r'[a-z | A-Z]+?(?=\/)'

    # Iterating through the dictionary generated from the first task
    # Attempts to find browser name using RegEx pattern above
    # Adds browser to dictionary, or updates existing values
    for key in dict_input.items():
        match = re.search(pattern, str(key))
        if match:
            browser = match.group(0)            
        
        if(str(browser) in lst):
            n = lst.get(browser) + 1
            lst[browser] = n
        if(str(browser) not in lst):
            lst[browser] = 1

    # Assign title, labels, and colours for histogram then display it
    # Browser names on X-Axis
    # Views on Y-Axis 
    plt.title('Browser views for file')
    plt.xlabel('Browsers')
    plt.ylabel('Views')
    plt.bar(lst.keys(), lst.values(), color='b')
    plt.show()

    return lst

# Used to run the tasks on the IDE
if __name__ == "__main__":
    ua_list = by_ua('test.json')
    by_browser(ua_list)