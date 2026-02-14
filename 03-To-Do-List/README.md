# To-Do List Application

A command-line to-do list application with persistent file storage. Your tasks are automatically saved and loaded!

## How to Run
```bash
python to_do_list.py
```

## Features
✅ **Add Tasks** - Add new tasks to your to-do list
✅ **View Tasks** - See all your tasks numbered
✅ **Remove Tasks** - Delete tasks you've completed
✅ **Persistent Storage** - Tasks are saved to `tasks.txt` file
✅ **Auto-Load** - Tasks load automatically when you restart
✅ **Menu-Driven** - Easy-to-use menu interface
✅ **Input Validation** - Handles invalid inputs gracefully

## What's New in This Version
🆕 **File Persistence** - Your tasks are saved to `tasks.txt`
🆕 **Auto-Load Tasks** - Tasks load automatically when program starts
🆕 **Better Error Handling** - Graceful keyboard interrupt handling

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

#### First Run (Creating New Task List)
```
No existing task file found. Starting with an empty to-do list.

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

Enter your choice (1-4): 4
Exiting the To-Do List application. Goodbye!
```

#### Second Run (Loading Previous Tasks)
```
To-Do List Menu:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice (1-4): 2
To-Do List:
1. Buy groceries
2. Finish Python project

(Tasks loaded automatically from tasks.txt!)
```

## File Structure
```
03-To-Do-List/
├── to_do_list.py       # Main application
├── tasks.txt           # Auto-created - stores your tasks
└── README.md          # This file
```

## Technical Details

### Data Persistence
- Tasks are stored in `tasks.txt` file
- One task per line
- File is created automatically on first save
- File loads automatically on startup

### Key Functions
- `load_tasks()` - Reads tasks from `tasks.txt` on startup
- `save_tasks()` - Writes current tasks to `tasks.txt`
- `add_task()` - Adds new task and saves to file
- `view_tasks()` - Displays all tasks
- `remove_task()` - Deletes task and saves to file
- `main()` - Main menu loop with error handling

### Features
- Automatic file loading on startup
- Tasks saved after each add/remove operation
- Graceful handling of missing file (first run)
- Keyboard interrupt handling (CTRL+C)

## Learning Concepts
- File I/O operations (reading and writing)
- Exception handling (FileNotFoundError, KeyboardInterrupt)
- Data persistence
- Try-except blocks
- Lists and list operations
- String formatting (f-strings)
- Menu-driven application design

## How Your Tasks Are Saved
Each task is stored on a separate line in `tasks.txt`:
```
Buy groceries
Finish Python project
Clean the house
Study Python
```

When you restart the app, these tasks are automatically loaded back!