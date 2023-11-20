import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

class KNN:
    def __init__(self):
        self.X = np.array([])
        self.Y = np.array([])
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
            self.X = np.append(self.X, x)
            self.Y = np.append(self.Y, y)
    
    def predict_y(self, x):
        if self.k > len(self.X):
            raise ValueError("k cannot be greater than the total number of nodes.")
        knn = KNeighborsRegressor(n_neighbors=self.k)
        knn.fit(np.reshape(self.X, (-1, 1)), self.Y)

        return knn.predict([[x]])
    
    def calcullate_cod(self, x):
        knn = KNeighborsRegressor(n_neighbors=self.k)
        knn.fit(np.reshape(self.X, (-1, 1)), self.Y)
        Y_pred = knn.predict(np.reshape(self.X, (-1, 1)))
        r2 = r2_score(self.Y, Y_pred)
        return r2

def main():
    knn = KNN()
    
    knn.init_from_stdin()
    
    x = int(input("Please enter x for predict: "))

    y = knn.predict_y(x)
    print("The predicted y is: %f" % y)

    r2 = knn.calcullate_cod(x)
    print("The coefficient of determination (R square) is: %f " % r2)

if __name__ == "__main__":
    main()
