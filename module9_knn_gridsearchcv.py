import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

class DataPairs:
    def __init__(self):
        self.X = np.array([])
        self.Y = np.array([])
        self.N = 0
        self._init_len_from_stdin()
        self.read_pairs_from_user()

    def _init_len_from_stdin(self):
        N = int(input("Enter a positive integer N: "))
        while N <= 0:
            N = int(input("Please enter a positive integer N: "))
        self.N = N

    def read_pairs_from_user(self):
        for i in range(self.N):
            x = float(input("Please enter the feature x for data pair %d: " % (i + 1)))
            y = int(input("Please enter the label y for data pair %d: " % (i + 1)))
            while y < 0:
                y = int(input("y should be non-negative"))

            self.X = np.append(self.X, x)
            self.Y = np.append(self.Y, y)

    def get_data_pairs(self):
        return (self.X, self.Y)    

class BestKNeighbors:
    def __init__(self):
        self.train_pairs = DataPairs()
        self.test_pairs = DataPairs()

    def compute_best_k_and_its_accuracy(self):
        (train_x, train_y) = self.train_pairs.get_data_pairs()
        (test_x, test_y) = self.test_pairs.get_data_pairs()
        
        knn = KNeighborsClassifier()
        parameters = {'n_neighbors': range(1, 11)}

        clf = GridSearchCV(knn, parameters, cv=2)
        clf.fit(np.reshape(train_x, (-1, 1)), train_y)

        k = clf.best_params_['n_neighbors']
        best_knn = KNeighborsClassifier(n_neighbors=k)
        best_knn.fit(np.reshape(train_x, (-1, 1)), train_y)
        accuracy = best_knn.score(np.reshape(test_x, (-1, 1)), test_y)

        return (k, accuracy)

def main():
    best_k = BestKNeighbors()
    k, accuracy = best_k.compute_best_k_and_its_accuracy()
    print(f"Best K and its accuracy: {k}, {accuracy:.4f}")

if __name__ == "__main__":
    main()
