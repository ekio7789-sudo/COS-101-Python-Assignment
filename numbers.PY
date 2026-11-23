print("The program is designed to solve for the Sum, Mean, Median, Mode, and Average of numbers")
print('Type "exit" at any point to quit.')

def calculate_sum(numbers):
    return sum(numbers)

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    midpoint = n // 2
    if n % 2 == 0:
        return (numbers[midpoint - 1] + numbers[midpoint]) / 2
    else:
        return numbers[midpoint]

def calculate_mode(numbers):
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    if len(modes) == len(set(numbers)):
        return "No mode"
    else:
        return modes

def calculate_average(numbers):
    return calculate_mean(numbers)  # Average is same as mean

while True:
    choice = input("Input S for Sum, Me for Mean, Med for Median, Mo for Mode, and A for Average (or type 'exit' to quit): ")
    if choice.lower() == "exit":
        print("Program terminated.")
        break
    
    numbers_input = input("Enter numbers separated by space (or type 'exit' to quit): ")
    if numbers_input.lower() == "exit":
        print("Program terminated.")
        break
    
    
    try:
        numbers = list(map(float, numbers_input.split()))
    except ValueError:
        print("Invalid input. Please enter numbers separated by space.")
        continue
    
    if choice == "S":
        print("Sum:", calculate_sum(numbers))
    elif choice == "Me":
        print("Mean:", calculate_mean(numbers))
    elif choice == "Med":
        print("Median:", calculate_median(numbers))
    elif choice == "Mo":
        print("Mode:", calculate_mode(numbers))
    elif choice == "A":
        print("Average:", calculate_average(numbers))
    else:
        print("Invalid choice")
