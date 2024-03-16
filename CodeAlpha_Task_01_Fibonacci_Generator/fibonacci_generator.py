# Start generating fibonacci numbers
print('Starting Fibonacci Generator....')

# Calculate fibonacci numbers
f_num: int = 2

# Get user input
max_num: int = int(input('How much fibanacci numbers do you need?\n'))

# Calculate
while (f_num < (max_num + 2)):
    fibonacci: int = ((f_num - 2) + (f_num - 1))
    # Print fibonacci number
    print(f'F{f_num - 1} : {fibonacci}')
    # Increse f_num by 1
    f_num += 1