#!/usr/bin/Python3
import ujson
import re

# Finds the readers of a given document uuid
# If a user uuid is specified then will ignore that user uuid
# If no user uuid specified, it is set to None and still functions 
def find_readers(file_name, doc_id, user_id=0):
    data = {}
    lst = {}

     # iterate through json lines file and process data line by line
    print('Finding other readers...')
    for line in open(file_name, 'r', encoding='utf-8'):
        s = ujson.loads(line)
        data = s  
        doc = data.get('subject_doc_id')               

        # if Doc uuid matched input uuid, get necessary data from line
        if(str(doc) == str(doc_id)):
            user = data.get('visitor_uuid')
            event = data.get('event_type')
            if(str(event) == 'read'):
                # Only add/update when the event_type = read to prevent multiple entries for each user
                if(str(user) in lst):            
                    n = lst.get(user) + 1
                    lst[user] = n
                # Only add if not the input user uuid
                if(str(user) not in lst and str(user) != str(user_id)):
                    lst[user] = 1

    # Message for how many other readers were found
    print(len(lst), "other readers found")

    # Return to be used in the 'also_likes' function
    return lst

# Finds the document uuids read by the given user uuid(s)
# *args used to allow for multiple user uuid's to be fed into the function
# Allows for all user uuid's to be searched while only processing the file once
def find_docs(file_name, *user_id):
    data = {}
    lst = {}

     # iterate through json lines file and process data line by line
    print('Finding liked documents from reader... ')
    for line in open(file_name, 'r', encoding='utf-8'):
        s = ujson.loads(line)
        data = s  
        user = data.get('visitor_uuid')               
        event = data.get('event_type')
        list_users = [] # list of users to be used as dictionary values
        
        # Iterates through the multiple user uuids where x: list
        # Iterates through x to find each user uuid
        # Performs processing on each individual user uuid where event is read, for each json line
        for x in user_id:
            for reader in x:
                if(str(user) == str(reader) and str(event) == 'read'):
                    doc = data.get('subject_doc_id')

                    # if Doc uuid already exists in dictionary; fill list with existing [doc] values, 
                    # then add new user to the list
                    # Then set the newly updated list as the value 
                    # for dictionary entry at that doc uuid
                    if(str(doc) in lst): 
                        for k, v in lst.items():
                            if(k == str(doc)):
                                for x in v:
                                    list_users.append(x)
                                    # If user already exists in list, remove to prevent errors
                                    if(x == str(user)):
                                        list_users.remove(x)
                        list_users.append(str(user))
                        lst[doc] = list_users

                    # if Doc uuid does not exist in dictionary, add new user to list
                    # Then set the newly created list as the value 
                    # for the dictionary entry at that doc uuid
                    if(str(doc) not in lst and str(doc) != "None"):
                        list_users.append(str(user))
                        lst[doc] = list_users

    # Return to be used in the 'also_likes' function
    # Returned dictionary contains document uuid as key, with a list of user uuid as values
    return lst

# Sorting function. Sorts in ascending order, returns sorted list
def ascending(dict_name):
    temp = (sorted(dict_name.items(), key=lambda v: len(v[1])))
    return temp

# Sorting function. Sorts in descending order, returns sorted list
def descending(dict_name):
    temp = (sorted(dict_name.items(), key=lambda v: len(v[1]), reverse=True))
    return temp

# Main task that is called from the main file for the also likes functionality.
# Calls find_readers on the input document uuid to return a list of readers
# Calls find_docs with the list of readers
# Calls sorting function based on input parameter
# By default sorts in descending order if not otherwise specified
def also_likes(file_name, doc_id, user_id, sort_function ="d"):
    readers = find_readers(file_name, doc_id, user_id)

    # Fill a list with the keys from readers dictionary
    # Generates list of readers
    list_users = list(readers.keys())

    # Call function to find document uuids read by each user from the list, stored in temp dict
    # Sorting function is called on the temp dictionary to generate the top 10, then prints out
    # the document views/reads are calculated via length of the value (user list)
    temp = find_docs(file_name, list_users)
    if(sort_function == 'a'):
        sorted_docs = ascending(temp)
    else:
        sorted_docs = descending(temp)
    print('--------------------------------------------------------------')
    print('Top 10 list of liked documents \n')
    count=0
    for k, v in sorted_docs:
        if(count < 10):
            print("Document: " + k + ", viewed by " + str(len(v)) + " readers")
            count+=1

    return sorted_docs

# Used to test the tasks from the IDE
if __name__ == "__main__":
    #find_readers('100.json', '100806162735-00000000115598650cb8b514246272b5')
    #find_docs('100.json', '00000000deadbeef')
    #likes('100.json', 'aaaaaaaaaaaa-00000000df1ad06a86c40000000feadbe', '00000000deadbeef')
    also_likes('100.json', 'aaaaaaaaaaaa-00000000df1ad06a86c40000000feadbe', '00000000deadbeef')
    
