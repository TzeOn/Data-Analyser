#!/usr/bin/Python3
from tkinter import *
import tasks1 as t1
import tasks2 as t2
import task3 as t3
import tasks4 as t4
import task5 as t5

def launch():
    # Instantiate window
    window = Tk()
    window.title("Data Analysis")
    window.configure(background="#FFF6BF")
    window.geometry("800x600")

    # Click function
    def click():
        user_id = textbox_user.get() 
        doc_id = textbox_doc.get() 
        task_id = textbox_task.get() 
        file_name = textbox_file.get()
        sorting = textbox_sort.get()

        # If no user id was entered then set to None
        # Prevents error of displaying empty green box in graph for task 5
        # as otherwise user id would be an empty string "" instead of None
        if(user_id == ""):
            user_id = None

        # Declare dictionary to store result data, clears any existing data in textbox
        result_dict = {} 
        results.delete(0.0, END)

        # Runs task depending on input else error message
        try:
            # Input task1a
            if('1a' in task_id):
                print('Running Task 1a')
                result_dict = t1.by_country(file_name, doc_id)

            # Input task1b
            if('1b' in task_id):
                print('Running Tasks 1a and 1b')
                country = t1.by_country(file_name, doc_id)
                result_dict = t1.to_continent(country)

            # Input task2a
            if('2a' in task_id):
                print('Running Task 2a')
                result_dict = t2.by_ua(file_name)

            # Input task2b
            if('2b' in task_id):
                print('Running Task 2a and 2b')
                user_agents = t2.by_ua(file_name)
                temp = t2.by_browser(user_agents)
                result_dict.update(temp)

            # Input task3
            if('3' in task_id):
                print('Running Task 3')
                result_dict = t3.reader_profile(file_name)

            # Input task4d
            if('4d' in task_id):
                result_dict = t4.also_likes(file_name, doc_id, user_id, sorting)

            # Input task5
            if('5' in task_id):
                t5.main_call(file_name, doc_id, user_id)    

            # Check whether the variable is Dict or List, 
            # then prints output to GUI appropriately for each data structure
            if(isinstance(result_dict, dict)):
                for k, v in result_dict.items():
                    output = k + "  " + str(v) + " \n"
                    results.insert(END, output)
            if(isinstance(result_dict, list)):
                for k, v in result_dict:
                    output = k + ", " + str(len(v)) + " readers\n"
                    results.insert(END, output)

            # Clear the dict       
            result_dict.clear()
        except:
            output = "Error with input values"
            results.insert(END, output)

    # Labels in the GUI prompting user for input
    Label (window, text="Enter User ID: ", bg='#FFF6BF', fg='black', font="none 12 bold") .grid(row=0, column=0, sticky=E + N)
    Label (window, text="Enter Doc ID: ", bg='#FFF6BF', fg='black', font="none 12 bold") .grid(row=1, column=0, sticky=E + N)
    Label (window, text="Enter Task ID: ", bg='#FFF6BF', fg='black', font="none 12 bold") .grid(row=2, column=0, sticky=E + N)
    Label (window, text="Enter File name: ", bg='#FFF6BF', fg='black', font="none 12 bold") .grid(row=3, column=0, sticky=E + N)
    Label (window, text="Sorting for 4d: a - ascending: ", bg='#FFF6BF', fg='black', font="none 12 bold") .grid(row=4, column=0, sticky=E + N)
    

    # Textboxes to allow user to input data 
    textbox_user = Entry(window, width=20, bg='white')
    textbox_user.grid(row=0, column=1, sticky=E + N)

    textbox_doc = Entry(window, width=20, bg='white')
    textbox_doc.grid(row=1, column=1, sticky=E + N)

    textbox_task = Entry(window, width=20, bg='white')
    textbox_task.grid(row=2, column=1, sticky=E + N)

    textbox_file = Entry(window, width=20, bg='white')
    textbox_file.grid(row=3, column=1, sticky=E + N)

    textbox_sort = Entry(window, width=20, bg='white')
    textbox_sort.grid(row=4, column=1, sticky=E + N)

    # Submit button that runs the task. If no task is entered then will present error
    Button(window, text="Run Task", width=8, command=click) .grid(row=5, column=1, sticky=E + N + S + W)

    # Textbox output to display the output of the tasks run
    # Note: task 5 will not display output in the textbox, but launches the graph
    results = Text(window, wrap=WORD, background='#eee')
    results.grid(row=6, column=0, columnspan=8, sticky=N + S + W + E)
    window.grid_columnconfigure(5, weight=1)
    window.grid_rowconfigure(6, weight=1)

    # Starts the GUI window
    window.mainloop()

# Runs the GUI from the IDE for testing
if __name__ == '__main__':
    print('Launching GUI')
    launch()