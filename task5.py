#!/usr/bin/Python3
import sys, json
import tasks4 as t4
import subprocess
import re

# Main function to be called from the main file
def main_call(file_name, doc_id, user_id):
    generate_graph(file_name, doc_id, user_id)
    systems_call("also_likes.dot")

# Function to invert the key value pairs in a dictionary to a new dictionary
# from [k : v]      doc > user
# to [v : k]        user > doc
def invert_dict(dict_name):
    new_dict = {}
    pattern = r'(\w+)'
    for k,v in dict_name:
        for x in v:
            match = re.search(pattern, str(x))
            if match:
                value = match.group(0)
                new_dict.setdefault(value,[]).append(k)
    temp = list(new_dict.items())
    return temp

# Function to generate the dot file "also_likes.dot" that contains the graph
# This is called from the main file/command line to view the graph
def generate_graph(file_name, doc_id, user_id):
    
    # Generate dictionary from running task 4d
    # Invert the graph to user -> doc
    graph_dict = t4.also_likes(file_name, doc_id, user_id)   
    user_dict = invert_dict(graph_dict)

    # Writes out the dot file in acceptable format with appropriate values from dictionaries
    with open('also_likes.dot','w') as out:
        for line in ('digraph G {',' ranksep=.75; ratio=compress; size = "15,22"; orientation=landscape; rotate=180;',' {', '   node [shape=plaintext, fontsize=16];','','   Readers -> Documents','[label="Size: 1m"];',):
            out.write('{}\n'.format(line))
        # Writes out the highlighted doc id and user id(if exists)

        if(user_id is not None):
            out.write(' "{}" [label="{}", shape="box", style=filled,color=".3 .6 .7"];\n'.format(user_id[-4:], user_id[-4:]))
        out.write(' "{}" [label="{}", shape="circle", style=filled,color=".3 .6 .7"];\n'.format(doc_id[-4:], doc_id[-4:]))
        
        # Writes out the document and user id's
        # uses a set to prevent duplicate entries
        for k, v in user_dict:
            has_done=set([])
            text = k[-4:]
            if text not in has_done:
                out.write(' "{}" [label="{}", shape="box"];\n'.format(text, text))
                has_done.add(text)
                
        for k, v in graph_dict:
            has_done=set([])
            text = k[-4:]
            if text not in has_done:
                out.write(' "{}" [label="{}", shape="circle"];\n'.format(text, text))
                has_done.add(text)
        
        # Writes out the Readers, using sets to prevent duplicate entries
        out.write('\n{  rank = same; "Readers";\n')
        for k, v in user_dict:
            has_done=set([])
            text = k[-4:]
            if text not in has_done:
                out.write('  "{}";\n'.format(text))
                has_done.add(text)
        out.write('};{ rank = same; "Documents";\n')

        # Writes out the Documents, using sets to prevent duplicate entries
        for k, v in graph_dict:
            has_done=set([])
            text = k[-4:]
            if text not in has_done:
                out.write('  "{}";\n'.format(text))
                has_done.add(text)
        out.write('}; ')

        # Writes out the connections between user id's and document id's from user dictionary
        if(user_id is not None):
            out.write(' "{}" -> "{}";\n'.format(user_id[-4:], doc_id[-4:]))
        for k, v in user_dict:
            for x in v:
                out.write(' "{}" -> "{}";\n'.format(k[-4:],x[-4:]))
        out.write(' };\n}')

# Function to make a systems call to the commmand line
# Converts the input dot file to .ps file then runs with evince
def systems_call(dot_file):
    subprocess.Popen([r"dot","-Tps", "-o", "also_likes.ps", dot_file]).wait()
    subprocess.Popen([r"evince", "also_likes.ps"])


 # Run from main file (command line) or GUI
 # Running file alone does not execute anything       
if __name__ == '__main__':
    pass