def main():
    N = int(input("Enter a positive integer N: "))

    # Number has to be positive
    while N <= 0:
        N = int(input("Please enter a positive integer N: "))

    # Read the N numbers from the user
    numbers = []
    for i in range(N):
        num = int(input(f"Number {i + 1}: "))
        numbers.append(num)

    X = int(input("Please enter an integer X: "))

    # Get all indices for the input number
    indices = [i + 1 for i, num in enumerate(numbers) if num == X]

    if len(indices) > 0:
        print(indices)
    else:
        print("-1")

if __name__ == "__main__":
    main()
