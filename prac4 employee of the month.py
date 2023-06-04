def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def determine_employee_of_the_month(employees):
    max_average_score = -1
    employee_of_the_month = ""

    for employee, scores in employees.items():
        attendance_score = scores['attendance']
        behavior_score = scores['behavior']
        performance_score = scores['performance']

        average_score = calculate_average([attendance_score, behavior_score, performance_score])

        if average_score > max_average_score:
            max_average_score = average_score
            employee_of_the_month = employee

    return employee_of_the_month

# Example data
employees_data = {
    "John": {"attendance": 90, "behavior": 8, "performance": 9},
    "Alice": {"attendance": 95, "behavior": 9, "performance": 7},
    "Bob": {"attendance": 85, "behavior": 7, "performance": 9}
}

employee_of_the_month = determine_employee_of_the_month(employees_data)
print("Employee of the Month:", employee_of_the_month)
