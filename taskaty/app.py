from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Simple ClI Task Manager")
    subparsers = parser.add_subparsers()

    add_task = subparsers.add_parser("add", help="Add Task.")
    add_task.add_argument("title", help="Title of the task.", type=str)
    add_task.add_argument("-d", "--description", help="The description of the task.", type=str, default=None)
    add_task.add_argument("-s", "--start_date", help="Date to begin the task.", type=str, default=None)
    add_task.add_argument("-e", "--end_date", help="Date to end the task.", type=str, default=None)
    add_task.add_argument("--done", help="The task is done or not!", default=False)

    list_task = subparsers.add_parser("list", help="List the tasks.")
    list_task.add_argument("-a", "--all", help="List all tasks.", )

    check_task = subparsers.add_parser("check", help="Check the task.")
    check_task.add_argument("-t", "-task", help="Number of the task to be done.", type=int)

    remove_task = subparsers.add_parser("remove", help="Remove the task.")
    remove_task.add_argument("-t", "-task", help="Number of the task to remove.", type=int)

    reset_tasks = subparsers.add_parser("reset", help="Remove all tasks")

    args = parser.parse_args()

if __name__ == "__main__":
    main()