user_input = input("Please enter your name: ")
student_grade = input("Enter student's grade: ")
if student_grade.isdigit():
        grade = int(student_grade)
        
        if grade < 40 or grade > 100:
            print("Error. Grade must be in the range of 40-100 only.")
        else:
            if 99 <= grade <= 100:
                print("Excellent! Your Final Grade is 1.0")
            elif 96 <= grade <= 98:
                print("Outstanding! Your Final Grade is 1.25")
            elif 93 <= grade <= 95:
                print("Superior! Your Final Grade is 1.50")
            elif 90 <= grade <= 92:
                print("Very Good! Your Final Grade is 1.75")
            elif 87 <= grade <= 89:
                print("You did Good! Your Final Grade is 2.0")
            elif 84 <= grade <= 86:
                print("You got a Satisfactory grade. Your Final Grade is 2.25") 
            elif 81 <= grade <= 83:
                print("You got a Fairly Satisfactory grade. Your Final Grade is 2.50")
            elif 78 <= grade <= 80:
                print("You got a fair grade! Your Final Grade is: 2.75")
            elif 75 <= grade <= 77:
                print("You passed. Your Final Grade is: 3.0")
            elif 40 <= grade <= 74:
                print("Sorry, you failed. Your Final Grade is: 5.0")                   
else:
    print("Error. Please enter a valid number.")    
                   