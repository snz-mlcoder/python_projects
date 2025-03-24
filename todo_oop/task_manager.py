import os
import json
from task import Task

class TaskManager:
    def __init__(self, data_file = "todo.json"):
        self.data_file = data_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file , "r") as f :
            data = json.load(f)
            return [Task.from_dict(item) for item in data]

    def save_tasks(self):
        with open (self.data_file , "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent = 2)

    def show_tasks(self):
        if not self.tasks:
            print ("nothing to do")
        for i , task in enumerate(self.tasks , 1):
            print (f"{i}: {task.title } - {task.date}")



    def add_tasks(self , title):
        task = Task(title)

        self.tasks.append(task)
        self.save_tasks()
        print("successfully added")


    def delete_tasks(self , index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f" task {removed.title} is deleted")
        else:
            print("invalid number")

    def edit_tasks(self , index, new_title):

        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].title= new_title
            self.save_tasks()
            print('edited successfully')
        else:
            print("invalid number")


