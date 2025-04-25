'''
Problem: Task Scheduling Problem (Optimization)

Description:
Develop an algorithm to schedule tasks efficiently based on their deadlines and durations.
The goal is to maximize the number of tasks that can be completed before their respective deadlines.

Each task has:
- A name
- A deadline (time units)
- A duration (time units required to complete the task)

The algorithm should determine which tasks can be completed within their deadlines
and return a list of completed tasks.

Approach:
- Sort tasks by their deadlines (earliest first)
- Track current time as tasks are scheduled
- For each task, check if it can be completed before its deadline
- If a task can be completed, add it to the completed tasks list and update current time
'''

def schedule_tasks(tasks):
    # Sort tasks by their deadline
    tasks.sort(key=lambda x: x["deadline"])
    
    current_time = 0  # Track the time spent on tasks
    completed_tasks = []  # List of completed tasks
    
    for task in tasks:
        # Check if we can complete the task within its deadline
        if current_time + task["duration"] <= task["deadline"]:
            completed_tasks.append(task["name"])
            current_time += task["duration"]  # Add task duration to current time
    
    return completed_tasks

# Example usage
if __name__ == "__main__":
    # Example input
    tasks = [
        {"name": "Task 1", "deadline": 4, "duration": 2},
        {"name": "Task 2", "deadline": 3, "duration": 1},
        {"name": "Task 3", "deadline": 2, "duration": 1},
        {"name": "Task 4", "deadline": 1, "duration": 2},
    ]

    # Get the tasks that can be completed
    completed = schedule_tasks(tasks)

    # Output the result
    print("Tasks that can be completed:", completed)