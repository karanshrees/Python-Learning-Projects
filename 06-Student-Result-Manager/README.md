# Student Result Manager

A command-line application to manage student marks, calculate averages, determine pass/fail status, and maintain a persistent record of results with delete functionality.

## How to Run
```bash
python student_result_manager.py
```

## Features
✅ **Add Student Results** - Enter student name and marks for 3 subjects
✅ **Calculate Average** - Automatically calculates average marks
✅ **Pass/Fail Determination** - Checks if student passes (all subjects >= 40)
✅ **Display Results** - Shows individual student results with formatting
✅ **Save to File** - Results are saved to `student_results.txt` for persistence
✅ **View All Results** - Display all saved student results
✅ **Delete Results** - Delete student results by name
✅ **Input Validation** - Validates marks (0-100) and student names
✅ **Error Handling** - Graceful handling of errors and interrupts

## What's New in This Version
🆕 **Delete Student Results** - Remove student records from file by name
🆕 **Delete Confirmation** - Shows how many records were deleted
🆕 **Case-Insensitive Search** - Delete works with any case variation

## How It Works

### Main Menu
```
1. Add new student
2. View all results
3. Delete a student's result
4. Exit
```

### Features Explained

#### 1. Add New Student
- Enter student name (non-empty validation)
- Enter marks for 3 subjects
- Each mark must be between 0-100
- Automatic average calculation
- Pass/Fail determination (pass if all subjects >= 40)
- Results displayed immediately
- Results saved to file automatically

#### 2. View All Results
- Shows all previously saved student results
- Displays in a formatted table
- Shows name, marks, average, and pass/fail status
- Sorted by order of entry

#### 3. Delete a Student's Result
- Search for student by name
- **Case-insensitive** search (works with "John", "john", "JOHN")
- Deletes all records matching that name
- Shows confirmation with number of records deleted
- If no match found, displays "No results found"

#### 4. Exit
- Safely exit the application

## Example Usage

### Adding a Student
```
Enter your choice (1/2/3/4): 1
Enter student name: John Doe
Enter marks for subject 1: 85
Enter marks for subject 2: 90
Enter marks for subject 3: 78
Student Name: John Doe
Marks: [85.0, 90.0, 78.0]
Average: 84.33
Result: Pass
```

### Viewing All Results
```
Enter your choice (1/2/3/4): 2

============================================================
ALL STUDENT RESULTS
============================================================
John Doe, [85.0, 90.0, 78.0], 84.33, Pass
Alice Smith, [35.0, 50.0, 45.0], 43.33, Fail
Bob Johnson, [92.0, 88.0, 95.0], 91.67, Pass
============================================================
```

### Deleting a Student's Result
```
Enter your choice (1/2/3/4): 3
Enter the name of the student whose result you want to delete: John Doe
Result for John Doe deleted successfully. (1 record(s) removed)
```

**After deletion:**
```
Enter your choice (1/2/3/4): 2

============================================================
ALL STUDENT RESULTS
============================================================
Alice Smith, [35.0, 50.0, 45.0], 43.33, Fail
Bob Johnson, [92.0, 88.0, 95.0], 91.67, Pass
============================================================
```

### Case-Insensitive Delete
```
Enter your choice (1/2/3/4): 3
Enter the name of the student whose result you want to delete: alice smith
Result for alice smith deleted successfully. (1 record(s) removed)
```

Works with "Alice Smith", "alice smith", "ALICE SMITH", etc.

## File Structure
```
06-Student-Result-Manager/
├── student_result_manager.py    # Main application
├── student_results.txt          # Auto-created - stores results
└── README.md                    # This file
```

## Pass/Fail Criteria
**Student PASSES if:**
- ALL three subjects have marks >= 40

**Student FAILS if:**
- ANY subject has marks < 40

## Input Validation

### Student Name
- Cannot be empty
- Must contain at least one character

### Marks
- Must be a valid number (integer or decimal)
- Must be between 0 and 100 (inclusive)
- Automatically rejects invalid values

## Data Format in student_results.txt
```
John Doe, [85.0, 90.0, 78.0], 84.33, Pass
Alice Smith, [35.0, 50.0, 45.0], 43.33, Fail
```

Each line contains:
- Student Name
- Marks as list
- Average (2 decimal places)
- Result (Pass or Fail)

## Technical Details

### Key Functions
- `get_student_name()` - Gets and validates student name
- `get_student_marks()` - Gets and validates marks for 3 subjects
- `calculate_average(marks)` - Calculates average of marks
- `check_pass_fail(marks)` - Determines pass/fail (all marks >= 40)
- `delete_result(name)` - Deletes student results by name (case-insensitive)
- `display_result()` - Displays individual student result
- `save_to_file()` - Saves result to `student_results.txt`
- `view_all_results()` - Displays all saved results
- `main()` - Main menu loop

### Data Persistence
- Results are stored in `student_results.txt`
- File is created automatically on first save
- File is appended to for each new student
- File is rewritten when deleting records

### Delete Functionality
- Case-insensitive matching
- Searches for student name in each line
- Deletes all matching records
- Rewrites file without matching lines
- Shows count of deleted records

## Learning Concepts
- Input validation and error handling
- File I/O operations (reading and writing)
- File manipulation (deleting lines)
- List operations and calculations
- Exception handling (ValueError, FileNotFoundError, KeyboardInterrupt)
- String manipulation (case conversion)
- String formatting (f-strings)
- Conditional statements (if-elif-else)
- Loops (while, for)
- Menu-driven application design
- Data persistence

## Example Workflow
```
1. Run program
2. Add multiple students with their results
3. View all results to verify
4. Delete a student's result if needed
5. View all results again to confirm deletion
6. Exit when done
```

## Notes
- Delete is case-insensitive for easier searching
- If multiple records exist for same student, all are deleted
- To start fresh, delete `student_results.txt` manually
- Application handles both integer and decimal marks
- Deletion immediately updates the file