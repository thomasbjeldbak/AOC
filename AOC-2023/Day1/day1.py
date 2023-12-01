import re


def sum_first_last_digits(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_sum = 0

    for line in lines:
        # Find the first digit in the line
        first_digit = next((char for char in line if char.isdigit()), None)

        # Find the last digit in the line
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        # Check if both first and last digits are found
        if first_digit is not None and last_digit is not None:
            value = int(first_digit + last_digit)
            total_sum += value

    return total_sum


with open("input.txt") as f:
    data = f.read().strip()


def calibration(data):
    ls = data.split("\n")
    ns = [re.findall("\d", x) for x in ls]
    return sum(int(n[0] + n[-1]) for n in ns)


# Part 2
data = (
    data.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)

filename = "input.txt"
calibration_values = sum_first_last_digits(filename)
print(f"Part 1: {calibration_values}")
print(f"Part 2: {calibration(data)}")
