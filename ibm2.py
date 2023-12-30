import numpy as np
from sklearn.model_selection import train_test_split

# Load the data
data = np.loadtxt('PLTR_stock_data.csv', delimiter=',')
# Drop the 'Date' column
data = data.drop(['Date'], axis=1)
# Split the data into features and labels
features = data[:, :-1]
labels = data[:, -1].reshape(-1, 1)

# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.3, random_state=42)

# Define the activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the activation function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the number of hidden nodes
num_hidden_nodes = 5

# Initialize the weights and biases for the input layer
input_weights = np.random.randn(train_features.shape[1], num_hidden_nodes)
input_bias = np.random.randn(1, num_hidden_nodes)

# Initialize the weights and biases for the hidden layer
hidden_weights = np.random.randn(num_hidden_nodes, 1)
hidden_bias = np.random.randn(1, 1)

# Set the learning rate and number of epochs
learning_rate = 0.1
num_epochs = 10000

# Train the neural network
for epoch in range(num_epochs):
    # Forward propagation
    hidden_layer_input = np.dot(train_features, input_weights) + input_bias
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, hidden_weights) + hidden_bias
    predicted_output = sigmoid(output_layer_input)

    # Calculate the error
    error = train_labels - predicted_output

    # Backward propagation
    output_delta = error * sigmoid_derivative(predicted_output)
    hidden_error = np.dot(output_delta, hidden_weights.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)

    # Update the weights and biases
    hidden_weights += learning_rate * np.dot(hidden_layer_output.T, output_delta)
    hidden_bias += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
    input_weights += learning_rate * np.dot(train_features.T, hidden_delta)
    input_bias += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

# Test the neural network
hidden_layer_input = np.dot(test_features, input_weights) + input_bias
hidden_layer_output = sigmoid(hidden_layer_input)
output_layer_input = np.dot(hidden_layer_output, hidden_weights) + hidden_bias
predicted_output = sigmoid(output_layer_input)

# Print the mean squared error
mse = np.mean((predicted_output - test_labels) ** 2)
print(f'Mean Squared Error: {mse}')
