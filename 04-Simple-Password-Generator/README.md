# Simple Password Generator

A command-line tool to generate secure random passwords with customizable options.

## How to Run
```bash
python simple_password_generator.py
```

## Features
✅ **Custom Length** - Choose password length
✅ **Lowercase Letters** - Include a-z
✅ **Uppercase Letters** - Include A-Z
✅ **Numbers** - Include 0-9
✅ **Symbols** - Include special characters (!@#$%^&*)
✅ **Random Shuffling** - Ensures unpredictable order
✅ **Error Handling** - Validates all inputs

## How It Works

The program asks you:
1. **Password length** - How long should the password be?
2. **Include lowercase?** - Do you want a-z? (y/n)
3. **Include uppercase?** - Do you want A-Z? (y/n)
4. **Include numbers?** - Do you want 0-9? (y/n)
5. **Include symbols?** - Do you want special characters? (y/n)

Then it generates a random password with all selected character types!

## Example Usage
```
Enter the desired password length: 12
Include lowercase? (y/n): y
Include uppercase? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y
Generated Password: K7@mPx#qR2$L
```

## Another Example
```
Enter the desired password length: 8
Include lowercase? (y/n): y
Include uppercase? (y/n): n
Include numbers? (y/n): y
Include symbols? (y/n): n
Generated Password: a3b5c2d9
```

## Technical Details
- Uses `string` module for character sets
- Uses `random` module for shuffling
- Ensures at least one character from each selected type
- Validates that password length is sufficient

## Learning Concepts
- String manipulation
- Random selection and shuffling
- Function parameters with default values
- Error handling (try-except)
- User input validation
- List comprehensions