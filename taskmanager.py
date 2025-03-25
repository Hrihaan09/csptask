tasks = []

def add_task(task_name, priority, due_date):
    task = {
        "task_name": task_name,
        "priority": priority,
        "status": False,  
        "due_date": due_date
    }
    tasks.append(task)

def remove_task(task_name):
    global tasks
    tasks = [task for task in tasks if task['task_name'] != task_name]

def mark_task_complete(task_name):
    for task in tasks:
        if task['task_name'] == task_name:
            task['status'] = True 

def view_tasks():
    sorted_tasks = sorted(tasks, key=lambda x: (x['priority'], x['due_date']), reverse=True)
    if len(sorted_tasks) == 0:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for task in sorted_tasks:
            status = "Completed" if task['status'] else "Pending"
            print(f"Task: {task['task_name']} | Priority: {task['priority']} | Status: {status} | Due Date: {task['due_date']}")
        print("\n")

def check_progress(goal_tasks):
    completed_tasks = sum(1 for task in tasks if task['status'] == True)
    progress = (completed_tasks / goal_tasks) * 100
    print(f"Task Completion Progress: {completed_tasks}/{goal_tasks} tasks completed ({progress:.2f}% complete).")

from datetime import datetime

def view_overdue_tasks():
    today = datetime.now().strftime("%m-%d-%Y")
    overdue_tasks = [task for task in tasks if task['due_date'] < today and not task['status']]
    if overdue_tasks:
        print("\nOverdue Tasks:")
        for task in overdue_tasks:
            print(f"Task: {task['task_name']} | Due Date: {task['due_date']}")
    else:
        print("No overdue tasks.")

def set_task_goal_and_check(goal):
    print("\nSetting Goal and Checking Progress...")
    check_progress(goal)

def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Mark a Task as Complete")
        print("4. View Tasks")
        print("5. View Overdue Tasks")
        print("6. Set Task Goal and Check Progress")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            task_name = input("Enter task name: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter task due date (mm-dd-yyyy): ")
            add_task(task_name, priority, due_date)
        
        elif choice == "2":
            task_name = input("Enter task name to remove: ")
            remove_task(task_name)
        
        elif choice == "3":
            task_name = input("Enter task name to mark as complete: ")
            mark_task_complete(task_name)
        
        elif choice == "4":
            view_tasks()
        
        elif choice == "5":
            view_overdue_tasks()
        
        elif choice == "6":
            goal = (input("Enter the task completion goal: "))
            set_task_goal_and_check(goal)
        
        elif choice == "7":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

main()

