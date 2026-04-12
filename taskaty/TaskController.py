from taskaty.Task import Task
from datetime import date
from tabulate import tabulate

class TaskController:

    def __init__(self, file_name):
        self.file_name = file_name

    def add_task(self, args):
        if not args.start_date:
            now = date.today().isoformat()
            args.start_date = now

        task = Task(args.title, args.description, args.start_date, args.end_date, 
                    args.done)

        with open(self.file_name, 'a') as file:
            file.write(str(task) + '\n')
        print(f"Task '{task.title}' added successfully!")

    def list_tasks(self):
        unfinished_tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.split(', ')

                end_date = None if end_date == 'None' else end_date
                done = False if done.strip('\n') == 'False' else True
                
                if done:
                    continue
                unfinished_tasks.append({'title': title, 'description': description, 
                                        'start_date': start_date, 'end_date': end_date})
        return unfinished_tasks
    
    def list_all_tasks(self):
        all_tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.split(', ')

                end_date = None if end_date == 'None' else end_date
                done = False if done.strip('\n') == 'False' else True

                all_tasks.append({'title': title, 'description': description, 
                                  'start_date': start_date, 'end_date': end_date,
                                  'done': done})
        return all_tasks