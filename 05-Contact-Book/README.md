# Contact Book Application

A comprehensive command-line contact book application to manage your contacts and phone numbers efficiently.

## How to Run
```bash
python contact_book.py
```

## Features
✅ **Add Contacts** - Add new contacts with multiple phone numbers
✅ **View All Contacts** - Display all contacts in sorted order
✅ **Search Contacts** - Search by name or phone number
✅ **Delete Contact** - Remove entire contact or specific numbers
✅ **Duplicate Detection** - Prevents duplicate numbers and handles duplicates intelligently
✅ **Phone Number Normalization** - Handles various phone formats
✅ **Multiple Numbers Per Contact** - Store multiple phone numbers for one person

## How It Works

### Main Menu
```
Contact Book Menu:
1. Add Contact
2. View Contacts
3. Delete Contact / Delete Number
4. Search Contact
5. Exit
```

### Features Explained

#### 1. Add Contact
- Enter contact name and phone number
- Option to add multiple numbers to the same contact
- Detects if number already exists under another contact
- Option to move number between contacts or keep it shared

#### 2. View Contacts
- Shows all contacts in alphabetical order
- Displays all phone numbers for each contact
- Format: `Name: phone1 | phone2 | phone3`

#### 3. Delete Contact / Delete Number
- Search for contact by name
- Choose to delete entire contact OR specific number
- Contact auto-deleted if last number is removed

#### 4. Search Contact
- Search by partial name (case-insensitive)
- Search by phone number (partial or full)
- Shows matching contacts with all their numbers

#### 5. Exit
- Safely exit the application

## Example Usage

### Adding a Contact
```
Enter your choice (1-5): 1
Enter contact name: John Doe
Enter phone number: +1-234-567-8900
Contact 'John Doe' added successfully.
Add another number to this contact? (y/n): y
Enter phone number: 234-567-8901
Number 234-567-8901 added to John Doe.
Add another number to this contact? (y/n): n
```

### Viewing Contacts
```
Enter your choice (1-5): 2
Contact List:
Alice Smith: +1-555-1234 | +1-555-5678
John Doe: +1-234-567-8900 | 234-567-8901
Bob Johnson: 555-9999
```

### Searching Contacts
```
Enter your choice (1-5): 4
Enter contact name (or part of it) or phone number to search: john
John Doe: +1-234-567-8900 | 234-567-8901
```

### Deleting a Contact
```
Enter your choice (1-5): 3
Enter contact name (or part of it) to delete contact/number: john
Selected: John Doe
1. Delete entire contact
2. Delete a specific number
Choose (1/2): 1
Contact deleted.
```

## Technical Details

### Data Structure
- **contacts**: Dictionary storing contact information with normalized names as keys
- **phone_index**: Reverse index mapping normalized phone numbers to contact names

### Key Functions
- `normalize_name()` - Converts names to lowercase and standardized format
- `normalize_phone()` - Removes formatting from phone numbers
- `add_contact()` - Adds new contact with duplicate detection
- `view_contacts()` - Displays all contacts sorted alphabetically
- `search_contacts()` - Searches by name or phone number
- `delete_contact_or_number()` - Deletes contacts or specific numbers

## Learning Concepts
- Dictionaries and nested data structures
- Sets for efficient lookups
- String normalization and formatting
- User input validation
- Error handling with try-except
- Menu-driven application design
- Duplicate detection and handling
- Search functionality (by name and phone)

## Phone Number Formats Supported
- `+1-234-567-8900` (with country code)
- `234-567-8900` (with dashes)
- `2345678900` (digits only)
- `(234) 567-8900` (with parentheses)

All formats are normalized internally for accurate duplicate detection!