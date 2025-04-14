from datetime import datetime

tasks = []

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m-%d-%Y")
        if date_obj.date() < datetime.now().date():
            return False, "Due date cannot be in the past."
        return True, date_obj
    except ValueError:
        return False, "Invalid date format. Please use mm-dd-yyyy."

def add_task(task_name, priority, due_date):
    if not task_name.strip():
        print("Task name cannot be empty.")
        return False
    
    if any(task['task_name'].lower() == task_name.lower() for task in tasks):
        print("A task with this name already exists.")
        return False

    is_valid_date, result = validate_date(due_date)
    if not is_valid_date:
        print(result)
        return False

    task = {
        "task_name": task_name.strip(),
        "priority": priority.lower(),
        "status": False, 
        "due_date": due_date
    }
    tasks.append(task)
    print(f"Task '{task_name}' added successfully.")
    return True

def remove_task(task_name):
    global tasks
    original_length = len(tasks)
    tasks = [task for task in tasks if task['task_name'].lower() != task_name.lower()]
    if len(tasks) == original_length:
        print(f"Task '{task_name}' not found.")
        return False
    print(f"Task '{task_name}' removed successfully.")
    return True

def mark_task_complete(task_name):
    for task in tasks:
        if task['task_name'].lower() == task_name.lower():
            if task['status']:
                print(f"Task '{task_name}' is already marked as complete.")
            else:
                task['status'] = True
                print(f"Task '{task_name}' marked as complete.")
            return True
    print(f"Task '{task_name}' not found.")
    return False

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    try:
        sorted_tasks = sorted(tasks, key=lambda x: (
            {"high": 0, "medium": 1, "low": 2}[x['priority']], 
            datetime.strptime(x['due_date'], "%m-%d-%Y")
        ))
        print("\nTo-Do List:")
        for task in sorted_tasks:
            status = "Completed" if task['status'] else "Pending"
            print(f"Task: {task['task_name']} | Priority: {task['priority']} | "
                  f"Status: {status} | Due Date: {task['due_date']}")
        print()
    except Exception as e:
        print("Error occurred while displaying tasks:", str(e))

def view_overdue_tasks():
    try:
        today = datetime.now()
        overdue_tasks = [
            task for task in tasks 
            if datetime.strptime(task['due_date'], "%m-%d-%Y") < today 
            and not task['status']
        ]
        if overdue_tasks:
            print("\nOverdue Tasks:")
            for task in overdue_tasks:
                print(f"Task: {task['task_name']} | Due Date: {task['due_date']}")
        else:
            print("No overdue tasks.")
    except Exception as e:
        print("Error occurred while checking overdue tasks:", str(e))

def check_progress():
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("No tasks available to calculate progress.")
        return
    completed_tasks = sum(1 for task in tasks if task['status'])
    progress = (completed_tasks / total_tasks) * 100
    print(f"\nTask Completion Progress: {completed_tasks}/{total_tasks} "
          f"tasks completed ({progress:.2f}% complete).")

def main():
    while True:
        try:
            print("\n--- To-Do List Manager ---")
            print("1. Add a Task")
            print("2. Remove a Task")
            print("3. Mark a Task as Complete")
            print("4. View Tasks")
            print("5. View Overdue Tasks")
            print("6. Check Task Completion Progress")
            print("7. Exit")
            
            choice = input("Choose an option (1-7): ").strip()
            
            if choice == "1":
                while True:
                    task_name = input("Enter task name: ").strip()
                    if task_name:
                        break
                    print("Task name cannot be empty.")
        
                while True:
                    priority = input("Enter task priority (high, medium, low): ").lower().strip()
                    if priority in ['high', 'medium', 'low']:
                        break
                    print('Please enter a valid priority level (high, medium, low).')

                while True:
                    due_date = input("Enter task due date (mm-dd-yyyy): ").strip()
                    is_valid, message = validate_date(due_date)
                    if is_valid:
                        break
                    print(message)
        
                add_task(task_name, priority, due_date)
            
            elif choice == "2":
                task_name = input("Enter task name to remove: ").strip()
                remove_task(task_name)
            
            elif choice == "3":
                task_name = input("Enter task name to mark as complete: ").strip()
                mark_task_complete(task_name)
            
            elif choice == "4":
                view_tasks()
            
            elif choice == "5":
                view_overdue_tasks()
            
            elif choice == "6":
                check_progress()
            
            elif choice == "7":
                print("Thank you for using the To-Do List Manager. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
                
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main()
