import os

# Lists
menu = ["Add Student", "Add Subjects", "Add Grades", "View Report", "Exit"]
report = ["View Students", "View Subjects", "View Grades", "View Ranked Grades", "Return to Main Menu"]
students = []
subjects = []
grades = []

# Declared Variables
student_size = 0
subject_size = 0
student_index = 0
grade = 0.0
running = True # Program running state

# Prompts
invalid_input_prompt = "Invalid input. Please enter a valid input."
return_prompt = "Please press Enter to return..."

while running:
    os.system('cls')
    print("Menu\n")
    for i in range(5):
        print(f"{i +1}. {menu[i]}")
    try:
        choice = int(input("\nEnter number: "))
    except ValueError:
        print(invalid_input_prompt)
        input(f"\n{return_prompt}")
        continue
    if choice <= 0 or choice > 5:
        print(invalid_input_prompt)
        input(f"\n{return_prompt}")
        continue
    if choice == 1:
        os.system('cls')
        print(f"{menu[choice - 1]}\n")
        try:
            student_size = int(input("How many students do you want to add?: "))
            if student_size <= 0:
                print("\nNo student/s were added.")
                input(f"\n{return_prompt}")
                continue
        except ValueError:
            print(invalid_input_prompt)
            input(f"\n{return_prompt}")
            continue
        try:
            os.system('cls')
            print(f"{menu[choice - 1]}\n")
            for i in range(student_size):
                student_name = input(f"Enter name of student {i + 1}: ")
                students.append(student_name)
        except ValueError:
            print(invalid_input_prompt)
            input(f"\n{return_prompt}")
            continue
        print("\nStudent/s added successfully.")
        input("\nPress enter to view listed students...")
        os.system('cls')
        print("Listed Students:\n")
        for i in range(student_size):
            print(f"{i + 1}. {students[i]}")
        input(f"\n{return_prompt}")
    elif choice == 2:
        os.system('cls')
        print(f"{menu[choice - 1]}\n")
        try:
            subject_size = int(input("How many subjects do you want to add?: "))
            if subject_size <= 0:
                print("\nNo subjects/s were added.")
                input(f"\n{return_prompt}")
                continue
        except ValueError:
            print(invalid_input_prompt)
            input(f"\n{return_prompt}")
            continue
        try:
            os.system('cls')
            print(f"{menu[choice - 1]}\n")
            for i in range(subject_size):
                subject_name = input("Enter subject/s: ")
                subjects.append(subject_name)
        except ValueError:
            print(invalid_input_prompt)
            input(f"\n{return_prompt}")
            continue
        print("\nSubject/s added successfully.")
        input("\nPress enter to view listed subjects...")
        os.system('cls')
        print("Listed Subjects:\n")
        for i in range(subject_size):
            print(f"{i + 1}. {subjects[i]}")
        input(f"\n{return_prompt}")
    elif choice == 3:
        os.system('cls')
        print(f"{menu[choice - 1]}\n")
        if len(students) == 0:
            print("No students added yet. Please add students first.")
            input(f"\n{return_prompt}")
            continue
        while running:
            try:
                os.system('cls')
                print(f"{menu[choice - 1]}\n")
                for i, name in enumerate(students, start=1):
                    print(f"{i}. {name}")
                student_index = int(input("\nEnter the number of the student to add grades for: ")) - 1
                if student_index < 0 or student_index >= len(students):
                    print(invalid_input_prompt)
                    input(f"\n{return_prompt}")
                    break
                elif any(entry['Student'] == students[student_index] for entry in grades):
                    print(f"\n{students[student_index]} already has a grade.")
                    change_grade = input("Do you want to change the grade? (y/n): ")
                    if change_grade.lower() == 'y':
                        for entry in grades:
                            if entry['Student'] == students[student_index]:
                                grade = float(input(f"\nEnter new grade for {students[student_index]}: "))
                                if grade < 0.0 or grade > 100.0:
                                    print("\nGrade must be between 0 and 100")
                                    input(f"\n{return_prompt}")
                                    break
                                entry['Grade'] = grade
                                print(f"\nGrade updated to {grade}% for {students[student_index]}.")
                                break
                    else:
                        print("\nGrade not changed.")
                        input(f"\n{return_prompt}")
                        continue
                else:
                    grade = float(input(f"\nEnter grade for {students[student_index]}: "))
                    if grade < 0.0 or grade > 100.0:
                        print("\nGrade must be between 0 and 100")
                        input(f"\n{return_prompt}")
                        continue
                    print(f"\nGrade of {grade}% added for {students[student_index]}.")
                grades.append({"Student": students[student_index], "Grade": grade})
                repeat = input("\nDo you want to repeat (y/n)? ")
                if repeat.lower() != 'y':
                    break
            except ValueError:
                print(invalid_input_prompt)
                input(f"\n{return_prompt}")
    elif choice == 4:
        while running:
            os.system('cls')
            print("Report Menu\n")
            for i in range(5):
                print(f"{i +1}. {report[i]}")
            try:
                choice = int(input("\nEnter number: "))
            except ValueError:
                print(invalid_input_prompt)
                input(f"\n{return_prompt}")
                continue
            if choice <= 0 or choice > 5:
                print(invalid_input_prompt)
                input(f"\n{return_prompt}")
                continue
            if choice == 1:
                os.system('cls')
                print(f"{report[choice - 1]}\n")
                if len(students) == 0:
                    print("No students added yet.")
                    input(f"\n{return_prompt}")
                    continue
                students.sort() # Sort students alphabetically
                for i, name in enumerate(students, start=1):
                    print(f"{i}. {name}")
                input(f"\n{return_prompt}")
            elif choice == 2:
                os.system('cls')
                print(f"{report[choice - 1]}\n")
                if len(subjects) == 0:
                    print("No subjects added yet.")
                    input(f"\n{return_prompt}")
                    continue
                print("Subjects:\n")
                for i, name in enumerate(subjects, start=1):
                    print(f"{i}. {name}")
                input(f"\n{return_prompt}")
            elif choice == 3:
                os.system('cls')
                print(f"{report[choice - 1]}\n")
                if len(grades) == 0:
                    print("No grades added yet.")
                    input(f"\n{return_prompt}")
                    continue
                print("Grades:\n")
                for entry in grades:
                    print(f"Student: {entry['Student']}, Grade: {entry['Grade']}%")
                input(f"\n{return_prompt}")
            elif choice == 4:
                while running:
                    os.system('cls')
                    print(f"{report[choice - 1]}\n")
                    if len(grades) == 0:
                        print("No grades added yet.")
                        input(f"\n{return_prompt}")
                        continue
                    print("Grades:\n")
                    for entry in grades:
                        print(f"Student: {entry['Student']}, Grade: {entry['Grade']}%")
                    print("\nRanked Grades:\n")
                    sorted_grades = sorted(grades, key=lambda x: x['Grade'], reverse=True)
                    for i, entry in enumerate(sorted_grades, start=1):
                        print(f"{i}. Grade: {entry['Grade']}%, Student: {entry['Student']}")
                    repeat = input("\nDo you want to exit (y/n)? ")
                    if repeat.lower() == 'y':
                        input("\nPress enter to return...")
                        break
                    input(f"\n{return_prompt}")
            elif choice == 5:
                break
    elif choice == 5:
        running = False
        print("Exiting program...")