# from sklearn.neural_network import MLPRegressor
# from sklearn.metrics import mean_absolute_error
# regressor = MLPRegressor()
# regressor.fit(scaled, targets)
# outputs = regressor.predict(scaled)
# print(mean_absolute_error(targets, outputs))


import numpy as np

def random_binary_solution(D):
    return np.random.randint(0,2,D)