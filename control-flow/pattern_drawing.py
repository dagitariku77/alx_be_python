# pattern_drawing.py

def draw_pattern(size):
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after completing a row
        row += 1

def main():
    # Prompt the user to enter a positive integer
    size = int(input("Enter the size of the pattern: "))

    # Check if the input is a positive integer
    if size > 0:
        draw_pattern(size)
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()
