# First three rows are input features, the last row is event label.
dataset =[[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

# Assuming no inhibitory input
def MCP(row):
     activation = 0
     for i in range(len(row) - 1):
         activation += row[i]
     return 1.0 if activation > 0.0 else 0.0

for row in dataset:
    prediction = MCP(row)
    print("True Information=%d, Model Prediction=%d" % (row[-1], prediction))

#dataset = [[0.50, 0.27, 4, 0], [0.32, 0.33, 3, 0], [0.21, 0.65, 5, 0], [0.01, 0.91, 5, 0], [0.001, 1.10, 5, 0],
#           [0.45, 0.11, 4, 1], [0.67, 0.09, 2, 1], [0.91, 0.05, 1, 1], [0.87, 0.01, 1, 1], [0.720, 0.03, 2, 1]]
