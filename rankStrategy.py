import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Set seed for reproducibility

def rank_based_simulation(n):
    numbers = np.random.rand(n)
    ranks = np.argsort(numbers)
    rank_probabilities = {rank: (rank + 1) / (n + 1) for rank in range(n)}

    selected_number = max(numbers)
    selected_rank = ranks[-1]

    estimated_probability = rank_probabilities[selected_rank]

    return selected_number == max(numbers), estimated_probability

def run_rank_based_simulation(n, num_simulations):
    success_rates = []
    estimated_probabilities = []

    for _ in range(num_simulations):
        success, estimated_probability = rank_based_simulation(n)
        success_rates.append(success)
        estimated_probabilities.append(estimated_probability)

    cumulative_success_rates = np.cumsum(success_rates) / np.arange(1, num_simulations + 1)

    return cumulative_success_rates, estimated_probabilities

# Simulation parameters
n = 100  # Number of Papers
num_simulations = 1000  # Number of simulations

# Run rank-based simulation
cumulative_success_rates, estimated_probabilities = run_rank_based_simulation(n, num_simulations)

# Plotting the results
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Number of Trials')
ax1.set_ylabel('Cumulative Success Rate', color='tab:blue')
ax1.plot(np.arange(1, num_simulations + 1), cumulative_success_rates, color='tab:blue', label='Cumulative Success Rate')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.set_ylabel('Estimated Probability', color='tab:red')
ax2.plot(np.arange(1, num_simulations + 1), estimated_probabilities, color='tab:red', label='Estimated Probability')
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.legend(loc='upper right')

plt.title('Rank-Based Probability Estimation: Cumulative Success Rate and Estimated Probability over Trials')
plt.show()
