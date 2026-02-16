def get_student_name():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please try again.")

def get_student_marks():
    marks = [ ]
    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return marks

def calculate_average(marks):
    return sum(marks) / len(marks)

def check_pass_fail(marks):
    return all(mark >= 40 for mark in marks)
    
    # def check_pass_fail(average):
    # return average >= 40

def delete_result(name):
    with open("student_results.txt", "r") as file:
        lines = file.readlines()
    
    deleted_count = 0
    with open("student_results.txt", "w") as file:
        for line in lines:
            if name.lower() not in line.lower():
                file.write(line)
            else:
                deleted_count += 1
    
    if deleted_count > 0:
        print(f"Result for {name} deleted successfully. ({deleted_count} record(s) removed)")
    else:
        print(f"No results found for {name}")

def display_result(name, marks, average, results):
    print(f"Student Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Result: {'Pass' if results else 'Fail'}")

def save_to_file(name, marks, average, results):
    with open("student_results.txt", "a") as file:
        file.write(f"{name}, {marks}, {average:.2f}, {'Pass' if results else 'Fail'}\n")

def view_all_results():
    try:
        with open("student_results.txt", "r") as file:
            results = file.readlines()
            if not results:
                print("No results saved yet.")
                return
            
            print("\n" + "="*60)
            print("ALL STUDENT RESULTS")
            print("="*60)
            for result in results:
                print(result.strip())
            print("="*60 + "\n")
    except FileNotFoundError:
        print("No results file found. Please save some results first.")

def main():
    try:
        while True:
            print("\n1. Add new student")
            print("2. View all results")
            print("3. Delete a student's result")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ").strip()
            
            if choice == "1":
                name = get_student_name()
                marks = get_student_marks()
                average = calculate_average(marks)
                results = check_pass_fail(marks)
                display_result(name, marks, average, results)
                save_to_file(name, marks, average, results)
            
            elif choice == "2":
                view_all_results()
            
            elif choice == "3":
                name = input("Enter the name of the student whose result you want to delete: ").strip()
                delete_result(name)
            
            elif choice == "4":
                print("Exiting. Goodbye!")
                return
            
            else:
                print("Invalid choice. Please try again.")
    except (KeyboardInterrupt, EOFError):
        print("\nKeyboard interrupt received. Exiting gracefully.")

if __name__ == "__main__":
    main()


