# Custom Flexible Student Grade & Statistics Calculator
# Function 1: Calculate statistics using variable-length positional arguments
def calculate_statistics(*args):
    if not args:
        return 0, 0, 0.0

    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)

    # Return multiple values as a tuple
    return minimum, maximum, average

# Function 2: Calculate letter-grade distribution
def calculate_grade_distribution(*args):
    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for mark in args:
        if mark >= 90:
            distribution["A"] += 1
        elif mark >= 80:
            distribution["B"] += 1
        elif mark >= 70:
            distribution["C"] += 1
        elif mark >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return distribution

# Function 3: Display assessment details using keyword arguments
def display_assessments(**kwargs):
    print("\nAssessment Details:")

    for assessment, mark in kwargs.items():
        print(f"{assessment}: {mark}")

# Function 4: Calculate and display student performance
def calculate_performance(student_name, *args, **kwargs):
    print("\n" + "=" * 40)
    print("STUDENT GRADE & STATISTICS REPORT")
    print("=" * 40)

    print(f"Student Name: {student_name}")

    # Display named assessments if provided
    if kwargs:
        display_assessments(**kwargs)

    if not args:
        print("\nNo grades provided.")
        return

    # Tuple unpacking: store returned values in separate variables
    minimum, maximum, average = calculate_statistics(*args)

    print("\nStatistical Results:")
    print(f"Minimum Marks: {minimum}")
    print(f"Maximum Marks: {maximum}")
    print(f"Average Marks: {average:.2f}")

    # Calculate letter-grade distribution
    distribution = calculate_grade_distribution(*args)

    print("\nLetter Grade Distribution:")
    for grade, count in distribution.items():
        print(f"Grade {grade}: {count} student(s)/assessment(s)")

    print("=" * 40)

if __name__ == "__main__":
    grades1 = [85, 92, 76, 88, 95]
    calculate_performance(
        "Student 1",
        *grades1
    )
    assessments = {
        "Assignment": 85,
        "Midterm": 92,
        "Practical": 78,
        "Final_Exam": 88
    }
    display_assessments(**assessments)
    named_grades = list(assessments.values())
    calculate_performance(
        "Student 2",
        *named_grades,
        **assessments
    )