#!/usr/bin/Python3
import ujson

# Function that calculates each readers total readtime and prints it
# Read time is identified from the event_type
# pagereadtime is totalled for each user uuid
def reader_profile(file_name):
    data = {}
    lst = {}

    # iterate through json lines file and process data line by line
    for line in open(file_name, 'r', encoding='utf-8'):
        s = ujson.loads(line)
        data = s  
        et = data.get('event_type')        
        user = data.get('visitor_uuid')

        # if the event type is pagereadtime
        if('pagereadtime' in et):
            time = int(data.get('event_readtime'))
            # if event type already exists in new list, update with incremented count value
            if(str(user) in lst):            
                n = lst.get(user) + time
                lst[user] = n
            # if event type does not exist; add it to the list with default count value 1
            if(str(user) not in lst):
                lst[user] = time
    
    # Sorts the list based on highest value, takes the top 10 and places into temp variable
    # original dictionary is preserved
    temp = (sorted(lst.items(), key=lambda x: x[1], reverse=True)[:10]) 
    
    # Prints each of the 10 users and their read times in descending order
    # Adds the top 10 to a new dictionary which is returned from the function
    sorted_dict = {}
    for k, v in temp:
        print("User: " + k + ", time spend reading: " + str(v) + " ms")
        sorted_dict[k] = v

    return sorted_dict

# Used to test the task from the IDE
if __name__ == "__main__":
    reader_profile('100.json')
    

