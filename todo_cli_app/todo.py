import json
import os
from datetime import datetime

# keep the list of all tasks
DATA_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open (DATA_FILE , "r") as f:
        return json.load(f) # change it to python list

def save_tasks(tasks):
    with open (DATA_FILE ,"w") as f:
        return json.dump(tasks , f , indent = 2)


def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("nothing to do")
        return
    for i ,task in enumerate(tasks ,1): #start index from 1 instead of zero
        print (f"{i}, {task['title']} - {task['date']}")
   
def add_tasks(title):
    tasks = load_tasks()
    new_task = {
        "title" : title,
        "date" : datetime.now().strftime("%Y-%m-%d  %H:%M:%S")  
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print ("successfully added")
   
def delete_tasks(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print (f" task {removed['title']} is deleted")
    else:
        print ("invalid number")

def main():
    while True:
        print ("""
        1. show tasks
        2. add task
        3. delete task
        4. exit """)
        choice = input ("please enter your choice:")
        if choice =='1':
            show_tasks()
        elif choice =='2' :
            title = input("title:")
            add_tasks(title)
        elif choice =='3':
            show_tasks()
            try:
                index = int(input("please enter the number of the task which you want to delete:"))
                delete_tasks(index)
            except ValueError:
                print("invalid number")
        elif choice == '4':
            print("finish")
            break
        else:
            print("invalid choice")


if __name__=="__main__":
    main()
