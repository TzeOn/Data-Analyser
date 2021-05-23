#!/usr/bin/Python3
import sys, ujson
import matplotlib.pyplot as plt
import pycountry_convert as pc 

# Task 1a function taking file name and doc_id as parameters. 
# Analyses file to return a dictionary and graph of views by country on given doc_id
def by_country(file_name, doc_id):
    data = {}
    lst = {}

    # iterate through json lines file and process necessary data line by line
    # only visitor_country and subject_doc_id required for processing
    for line in open(file_name, 'r'):
        s = ujson.loads(line)
        data = s  
        c = data.get('visitor_country')
        i = data.get('subject_doc_id')
        
        # Identifies entries for the given doc_id and adds the country to dictionary, updating values of views
        if(str(i) == str(doc_id)):
            # if country already exists in new list, update with incremented count value
            if(str(c) in lst):            
                n = lst.get(c) + 1
                lst[c] = n
            # if country does not exist; add it to the list with default count value 1
            if(str(c) not in lst):
                lst[c] = 1

    # Assign title, labels, and colours for histogram then display it
    # Countries on X-Axis
    # Views on Y-Axis
    plt.title('Views by country on document '+ doc_id)
    plt.xlabel('Countries')
    plt.ylabel('Views')
    plt.bar(lst.keys(), lst.values(), color='b')
    plt.show()
    
    # Created dictionary is returned to be used for task 2b
    return lst


# Function calls the task1a function then converts the country codes to continent codes using 
# pycountry-convert library.
# returns dictionary of continents and views from each
def to_continent(d):
    lst={}
    
    # Iterate through dictionary passed in as parameter (from by_country function)
    # Uses library to convert each country code into continent code
    for key, value in d.items():       
        continent = pc.country_alpha2_to_continent_code(key)

        # Adds new continent to dictionary or updates existing continent with added value
        if(str(continent) in lst):            
            n = lst.get(continent) + value
            lst[continent] = n            
        if(str(continent) not in lst):
            lst[continent] = value
                
    # Assign title, labels, and colours for histogram then display it
    # Continents on X-Axis
    # Views on Y-Axis       
    plt.title('Views by continent on document ')
    plt.xlabel('Continents')
    plt.ylabel('Views')
    plt.bar(lst.keys(), lst.values(), color='b')
    plt.show()

    return lst

# Used to run the tasks from IDE
if __name__ == "__main__":
    pass
