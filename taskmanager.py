from datetime import datetime

tasks = []

def add_task(task_name, priority, due_date):
    try:
        datetime.strptime(due_date, "%m-%d-%Y")
    except ValueError:
        print("Invalid date format. Please use mm-dd-yyyy.")
        return
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
    if not tasks:
        print("No tasks available.")
        return
    sorted_tasks = sorted(tasks, key=lambda x: ({"high": 0, "medium": 1, "low": 2}[x['priority']], x['due_date']))
    print("\nTo-Do List:")
    for task in sorted_tasks:
        status = "Completed" if task['status'] else "Pending"
        print(f"Task: {task['task_name']} | Priority: {task['priority']} | Status: {status} | Due Date: {task['due_date']}")
    print("\n")

def view_overdue_tasks():
    today = datetime.now().strftime("%m-%d-%Y")
    overdue_tasks = [task for task in tasks if task['due_date'] < today and not task['status']]
    if overdue_tasks:
        print("\nOverdue Tasks:")
        for task in overdue_tasks:
            print(f"Task: {task['task_name']} | Due Date: {task['due_date']}")
    else:
        print("No overdue tasks.")

def check_progress():
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("No tasks available to calculate progress.")
        return
    completed_tasks = sum(1 for task in tasks if task['status'])
    progress = (completed_tasks / total_tasks) * 100
    print(f"\nTask Completion Progress: {completed_tasks}/{total_tasks} tasks completed ({progress:.2f}% complete).")

def main():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Mark a Task as Complete")
        print("4. View Tasks")
        print("5. View Overdue Tasks")
        print("6. Check Task Completion Progress")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            task_name = input("Enter task name: ")
    
            while True:
                priority = input("Enter task priority (high, medium, low): ").lower()
                if priority in ['high', 'medium', 'low']:
                    break
                else:
                    print('Please enter a valid priority level (high, medium, low).')

            while True:
                due_date = input("Enter task due date (mm-dd-yyyy): ")
                try:
                    valid_date = datetime.strptime(due_date, "%m-%d-%Y")
                    break  
                except ValueError:
                    print("Invalid date format. Please enter the date in mm-dd-yyyy format.")
    
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
            check_progress()
        
        elif choice == "7":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
