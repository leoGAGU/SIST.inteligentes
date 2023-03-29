import numpy as np

class Perceptron:
    def __init__(self, lr=0.1, epochs=100):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        self.weights = np.random.randn(X.shape[1])
        self.bias = np.random.randn()
        
        for epoch in range(self.epochs):
            for i in range(X.shape[0]):
                pred = self.predict(X[i])
                error = y[i] - pred
                self.weights += self.lr * error * X[i]
                self.bias += self.lr * error
    
    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        return np.where(z > 0, 1, 0)

# Compuerta AND
X_and = np.array([[0,0], [0,1], [1,0], [1,1]])
y_and = np.array([0, 0, 0, 1])
and_perceptron = Perceptron()
and_perceptron.fit(X_and, y_and)

# Compuerta OR
X_or = np.array([[0,0], [0,1], [1,0], [1,1]])
y_or = np.array([0, 1, 1, 1])
or_perceptron = Perceptron()
or_perceptron.fit(X_or, y_or)

# Compuerta NOT
X_not = np.array([[0], [1]])
y_not = np.array([1, 0])
not_perceptron = Perceptron()
not_perceptron.fit(X_not, y_not)

# Prueba del perceptrón
print(f"AND: {and_perceptron.predict(X_and)}")
print(f"OR: {or_perceptron.predict(X_or)}")
print(f"NOT: {not_perceptron.predict(X_not)}")
