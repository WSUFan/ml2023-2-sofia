def main():
    # Ask the user for the number of inputs they wish to enter
    N = int(input("Enter a positive integer N: "))

    # Ensure that the number entered is positive
    while N <= 0:
        N = int(input("Please enter a positive integer N: "))

    # Read the N numbers from the user
    numbers = []
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Ask the user for the number X to search for
    X = int(input("Enter an integer X: "))

    # Check if X is in the list of numbers and print the result
    if X in numbers:
        print(f"The index of {X} is {numbers.index(X) + 1}")
    else:
        print("-1")

if __name__ == "__main__":
    main()
