import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Set seed for reproducibility

def optimal_stopping_simulation(n, fraction_observed):
    numbers = np.random.rand(n)
    observed_numbers = sorted(numbers[:int(fraction_observed * n)])
    threshold = max(observed_numbers)
    selected_number = max(numbers)

    return selected_number == threshold

def run_optimal_stopping_simulation(n, num_simulations, fraction_observed):
    success_rates = []

    for _ in range(num_simulations):
        numbers = np.random.rand(n)
        observed_numbers = sorted(numbers[:int(fraction_observed * n)])
        threshold = max(observed_numbers)
        selected_number = max(numbers)

        success = selected_number == threshold
        success_rates.append(success)

    cumulative_success_rates = np.cumsum(success_rates) / np.arange(1, num_simulations + 1)

    return cumulative_success_rates

# Simulation parameters
n = 100  # Number of Papers
fraction_observed = 0.37  # Fraction observed for the optimal stopping rule
num_simulations = 1000  # Number of simulations

# Run optimal stopping simulation
cumulative_success_rates = run_optimal_stopping_simulation(n, num_simulations, fraction_observed)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, num_simulations + 1), cumulative_success_rates, label='Optimal Stopping Rule')
plt.xlabel('Number of Trials')
plt.ylabel('Cumulative Success Rate')
plt.title('Optimal Stopping Rule: Cumulative Success Rate over Trials')
plt.legend()
plt.show()