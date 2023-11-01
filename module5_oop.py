class DataProcessor:
    def __init__(self):
        self.numbers = []
        self.N = 0
    
    def init_from_stdin(self):
        self._init_len_from_stdin()
        self._init_data_from_stdin()

    def _init_len_from_stdin(self):
        N = int(input("Enter a positive integer N: "))
        while N <= 0:
            N = int(input("Please enter a positive integer N: "))
        self.N = N
    
    def _init_data_from_stdin(self):
        for _ in range(self.N):
            num = int(input("Please enter a number: "))
            self.numbers.append(num)
    
    def search_data(self, X):
        indices = [i + 1 for i, num in enumerate(self.numbers) if num == X]
        return indices

def main():
    data_processor = DataProcessor()
    
    data_processor.init_from_stdin()
    
    # Search for a number in the list
    X = int(input("Please enter an integer X for search: "))
    indices = data_processor.search_data(X)
    
    if len(indices) > 0:
        print(indices)
    else:
        print("-1")

if __name__ == "__main__":
    main()
