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
num_simulations = 1000  # Number of simulations
observation_thresholds = np.arange(0.1, 1.0, 0.1)  # Different observation thresholds

# Run simulations for different observation thresholds
results = []
for threshold in observation_thresholds:
    cumulative_success_rates = run_optimal_stopping_simulation(n, num_simulations, threshold)
    results.append(cumulative_success_rates)

# Plotting the results
plt.figure(figsize=(10, 6))
for i, threshold in enumerate(observation_thresholds):
    plt.plot(np.arange(1, num_simulations + 1), results[i], label=f'Threshold = {threshold}')

plt.xlabel('Number of Trials')
plt.ylabel('Cumulative Success Rate')
plt.title('Optimal Stopping Rule: Cumulative Success Rate for Different Observation Thresholds')
plt.legend(title='Observation Threshold')
plt.show()