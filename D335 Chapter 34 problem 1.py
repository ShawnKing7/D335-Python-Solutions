#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

print(f"Distance: {sum([int(input()) * x for x in [15.62, 41.85, 32.67]]):.2f} miles")