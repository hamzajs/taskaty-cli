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