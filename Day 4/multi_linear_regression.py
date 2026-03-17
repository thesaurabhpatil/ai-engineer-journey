import numpy as np

# Generate synthetic data
np.random.seed(0)

# 100 samples, 3 features
X = np.random.rand(100, 3)

true_W = np.array([[2], [3], [4]])
Y = X @ true_W

# Initialize weights
W = np.zeros((3, 1))

learning_rate = 0.1
epochs = 100

for epoch in range(epochs):
    Y_pred = X @ W
    
    loss = np.mean((Y - Y_pred) ** 2)
    
    gradient = -(2 / len(X)) * X.T @ (Y - Y_pred)
    
    W = W - learning_rate * gradient
    
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss {loss:.4f}")

print("Final Weights:")
print(W)
