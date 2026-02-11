# To-Do List Application

A simple command-line to-do list application to manage your daily tasks.

## How to Run
```bash
python to_do_list.py
```

## Features
✅ **Add Tasks** - Add new tasks to your to-do list
✅ **View Tasks** - See all your tasks numbered
✅ **Remove Tasks** - Delete tasks you've completed
✅ **Menu-Driven** - Easy-to-use menu interface
✅ **Input Validation** - Handles invalid inputs gracefully

## How It Works

### Main Menu
```
To-Do List Menu:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
```

### Example Usage
```
To-Do List Menu:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice (1-4): 1
Enter a new task: Buy groceries
Task added successfully.

Enter your choice (1-4): 1
Enter a new task: Finish Python project
Task added successfully.

Enter your choice (1-4): 2
To-Do List:
1. Buy groceries
2. Finish Python project

Enter your choice (1-4): 3
To-Do List:
1. Buy groceries
2. Finish Python project
Enter the number of the task that you want to remove: 1
Task 'Buy groceries' removed successfully.

Enter your choice (1-4): 4
Exiting the To-Do List application. Goodbye!
```

## Technical Details
- Uses a Python list to store tasks
- Menu-driven interface with while loop
- Input validation for task numbers
- Error handling for invalid inputs

## Learning Concepts
- Lists and list operations (append, pop)
- Loops (while, for)
- Conditional statements (if-elif-else)
- Functions
- String formatting (f-strings)
- Try-except blocks