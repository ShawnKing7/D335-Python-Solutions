# Employee A: 15.62 miles
# Employee B: 41.85 miles
# Employee C: 32.67 miles
# solution accepts three integer inputs representing the number of times an employee travels to the job site
# solution outputs "Distance: " followed by the total value to two decimal places
miles_per_employee = {
    'A': 15.62,
    'B': 41.85,
    'C': 32.67
}
employee_A = int(input())
employee_B = int(input())
employee_C = int(input())
total_miles_traveled = (employee_A * miles_per_employee['A'] +
                        employee_B * miles_per_employee['B'] +
                        employee_C * miles_per_employee['C'])
print(f"Distance: {total_miles_traveled:.2f} miles")
