from taskaty.Task import Task
from datetime import date
from tabulate import tabulate

class TaskController:

    def __init__(self, file_name):
        self.file_name = file_name