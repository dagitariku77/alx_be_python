
# daily_reminder.py

def get_task_details():
    # Prompt the user to input task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def create_reminder(task, priority, time_bound):
    reminder = f"Reminder: '{task}' is a "

    match priority:
        case 'high':
            reminder += "high priority task"
            if time_bound == 'yes':
                reminder += " that requires immediate attention today!"
            else:
                reminder += "."

        case 'medium':
            reminder += "medium priority task"
            if time_bound == 'yes':
                reminder += " that should be done soon."
            else:
                reminder += "."

        case 'low':
            reminder += "low priority task"
            if time_bound == 'yes':
                reminder += " that should be done when possible."
            else:
                reminder += " Consider completing it when you have free time."

        case _:
            reminder += "task with an unknown priority level."
    
    return reminder

def main():
    task, priority, time_bound = get_task_details()
    reminder = create_reminder(task, priority, time_bound)
    print(reminder)

if __name__ == "__main__":
    main()
