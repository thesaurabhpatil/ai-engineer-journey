import numpy as np

# Generate data
x = np.array([1, 2, 3, 4, 5])
y = 5 * x  # true relationship

# Initialize weight
w = 0.0

learning_rate = 0.1
epochs = 100

for epoch in range(epochs):
    y_pred = w * x
    
    # Compute loss
    loss = np.mean((y - y_pred) ** 2)
    
    # Compute gradient
    gradient = -2 * np.mean(x * (y - y_pred))
    
    # Update weight
    w = w - learning_rate * gradient
    
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss {loss:.4f}, Weight {w:.4f}")

print("Final weight:", w)
