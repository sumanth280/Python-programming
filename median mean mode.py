from statistics import mode

# Ask user for input
nums = input("Enter some numbers, separated by spaces: ")

# Convert input string into a list of integers
num_list = list(map(int, nums.split()))

# Calculate mean
mean = sum(num_list) / len(num_list)

# Calculate median
num_list.sort()
mid = len(num_list) // 2
if len(num_list) % 2 == 0:
    median = (num_list[mid - 1] + num_list[mid]) / 2
else:
    median = num_list[mid]

# Calculate mode
try:
    mode_value = mode(num_list)
except:
    mode_value = "No mode"

# Print results
print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode_value)
