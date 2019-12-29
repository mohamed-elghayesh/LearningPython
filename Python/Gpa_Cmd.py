# GPA calculator using loops

# validates that the number of terms is between 1 - 8
def read_terms():
    while True:
        terms_no = validate_input("Terms")
        if  (terms_no > 0 and terms_no <= 8):
            return terms_no
        else:
            print("There is a maximum of 8 Terms!, Try again!")
            continue

# validate that the input is an integer
def validate_input(entity):
    while True:
        try:
            userInput = int(input("Enter number of %s: "%entity))       
        except ValueError:
            print("Only integers are allowed! Try again.")
            continue
        return userInput

# reades and validates course number per term
# also sums up term gpa by calling get_marks()
def term_courses(term_id):
    print("Courses in Term", term_id)
    while True:
        courses = validate_input("Courses")
        if  (courses > 0 and courses <= 6):
            return get_marks(courses)
        else:
            print("There is a maximum of 6 Courses per Term!, Try again!")
            continue

def get_marks(courses):
    term_gpa = 0
    for course in range(1,courses+1):
        # TODO write code to evaluate mark are in the forms of A+ to F
        mark = input("Enter the Mark of Course %d (A+, A-, B, ...): " %course)
        chrs = int(input("Enter the course credite houres: "))

        # TODO extract a method to map mark to gpa
        if (mark == 'A+'): mark_value = 12/chrs
        elif (mark == 'A'): mark_value = 11.5/chrs
        elif (mark == 'A-'): mark_value = 11/chrs
        elif (mark == 'B+'): mark_value = 10/chrs
        elif (mark == 'B'): mark_value = 9/chrs
        elif (mark == 'B-'): mark_value = 8/chrs
        elif (mark == 'C+'): mark_value = 7/chrs
        elif (mark == 'C'): mark_value = 6/chrs
        elif (mark == 'C-'): mark_value = 5/chrs
        elif (mark == 'D+'): mark_value = 4/chrs
        elif (mark == 'D'): mark_value = 3/chrs
        elif (mark == 'F'): mark_value = 0

        term_gpa += mark_value
    
    print("Term GPA: %2.3f" %(term_gpa/courses))
    return term_gpa/courses

# main body
print("Welcome to the GPA calculator")
print("=============================")

terms_no = read_terms()
# TODO use term_gpa to as a list and append to it while looping
total_gpa = 0
for term in range(1,terms_no+1):
    total_gpa += term_courses(term)
print("Overall GPA: %2.3f" %(total_gpa/terms_no))
# TODO write a method to print (Excellent, VGood, Good, ...)
    
