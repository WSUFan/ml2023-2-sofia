import numpy as np
from sklearn.metrics import precision_score, recall_score

class QualityMetrics:
    def __init__(self):
        self.X = np.array([])
        self.Y = np.array([])
        self.N = 0
    
    def init_from_stdin(self):
        self._init_len_from_stdin()
        self._init_xy_from_stdin()

    def _init_len_from_stdin(self):
        N = int(input("Enter a positive integer N: "))
        while N <= 0:
            N = int(input("Please enter a positive integer N: "))
        self.N = N
    
    def _init_xy_from_stdin(self):
        for i in range(self.N):
            x = int(input("Please enter the ground truth x for num %d: " % (i + 1)))
            while x != 1 and x != 0:
                x = int(input("x should be either 0 or 1"))

            y = int(input("Please enter predicted class y for num %d: " % (i + 1)))
            while y != 1 and y != 0:
                y = int(input("y should be either 0 or 1"))

            self.X = np.append(self.X, x)
            self.Y = np.append(self.Y, y)

    def calculate(self):
        precision = precision_score(self.X, self.Y)
        recall = recall_score(self.X, self.Y)
        return precision, recall

def main():
    q = QualityMetrics()
    
    q.init_from_stdin()
    p, r = q.calculate()
    print(f"Precision: {p:.2f}")
    print(f"Recall: {r:.2f}")

if __name__ == "__main__":
    main()
