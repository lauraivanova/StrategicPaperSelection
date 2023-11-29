import numpy as np

np.random.seed(42)

# Simulating the optimal stopping rule
n = 100
fraction_observed = 0.37

numbers = np.random.rand(n)
observed_numbers = sorted(numbers[:int(fraction_observed * n)])
threshold = max(observed_numbers)
selected_number = max(numbers)

success = selected_number == threshold
print(f"Did we succeed? {success}")