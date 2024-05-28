# https://github.com/dekilhaden/03230050_BIA101_CAP3.git
# Deki Lhadon
# BBIA
# 03230050
################################
# REFERENCES
# Links that you referred while solving
# the problem
# https://www.w3schools.com/python/python_files.asp
# https://www.tutorialspoint.com/python/python_files_io.htm
################################
# SOLUTION
# Your Solution Score: <242740>

# Read the input.txt file 
def read_input(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)
    return lines

def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        first_digit = int(line[0]) if line[0].isdigit() else 0
        last_digit = int(line[-1]) if line[-1].isdigit() else 0
        two_digit_number = first_digit * 10 + last_digit
        total_sum += two_digit_number
    return total_sum

def print_solution(file_path, total_sum):
# implement the task 1 solution here
# print the solution to output as:
# "The total sum from the given input file <file name> is the <answer>"
 print(f"The total sum from the given input file {file_path} is {total_sum}")

# Main code
file_path = '03230050_BIA101_CAP3\\050.txt'  
lines = read_input(file_path)
total_sum = calculate_sum(lines)
print_solution(file_path, total_sum)