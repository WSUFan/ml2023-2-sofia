import sys
import numpy as np

class KNN:
    def __init__(self):
        self.nodes = []
        self.N = 0
        self.k = 0
    
    def init_from_stdin(self):
        self._init_len_from_stdin()
        self._init_k_from_stdin()
        self._init_xy_from_stdin()

    def _init_len_from_stdin(self):
        N = int(input("Enter a positive integer N: "))
        while N <= 0:
            N = int(input("Please enter a positive integer N: "))
        self.N = N

    def _init_k_from_stdin(self):
        k = int(input("Enter a positive integer k: "))
        while k <= 0:
            k = int(input("Please enter a positive integer k: "))
        self.k = k
    
    def _init_xy_from_stdin(self):
        for i in range(self.N):
            x = int(input("Please enter x for num %d: " % (i + 1)))
            y = int(input("Please enter y for num %d: " % (i + 1)))
            self.nodes.append((x, y))
    
    def predict_y(self, x):
        if self.k > len(self.nodes):
            raise ValueError("k cannot be greater than the total number of nodes.")
        
        distances = np.array([np.sqrt((node[0] - x) ** 2) for node in self.nodes])

        # get k shortest index
        k_indices = np.argsort(distances)[:self.k]

        y_values = np.array([self.nodes[i][1] for i in k_indices])
        return np.mean(y_values)

def main():
    knn = KNN()
    
    knn.init_from_stdin()
    
    x = int(input("Please enter x for predict: "))

    y = knn.predict_y(x)
    
    print("The predicted y is: %f" % y)

if __name__ == "__main__":
    main()
