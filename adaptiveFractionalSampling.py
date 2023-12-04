import numpy as np
import matplotlib.pyplot as plt

def adaptive_fractional_sampling(n, initial_fraction):
    cumulative_success_rate = []
    current_fraction = initial_fraction
    max_number = 0

    for i in range(n):
        # Ensure that the sample size is at least 1
        sample_size = max(1, int(current_fraction * n))
        sample = np.random.randint(1, n+1, sample_size)

        # Update maximum number observed
        max_in_sample = np.max(sample)
        max_number = max(max_number, max_in_sample)

        # Check if current paper has the highest number
        if max_in_sample == n:
            cumulative_success_rate.append(1.0)
            break
        else:
            cumulative_success_rate.append(0.0)

        # Adjust fraction based on maximum number observed
        if max_in_sample < max_number / 2:
            current_fraction *= 2
        else:
            current_fraction /= 2

    return cumulative_success_rate

# Example parameters
num_papers = 100
initial_sampling_fraction = 0.1
num_experiments = 5

# Run the strategy multiple times
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
for _ in range(num_experiments):
    cumulative_success = adaptive_fractional_sampling(num_papers, initial_sampling_fraction)
    plt.plot(range(1, len(cumulative_success) + 1), np.cumsum(cumulative_success) / np.arange(1, len(cumulative_success) + 1), label=f'Experiment {_ + 1}')

# Plotting
plt.xlabel('Number of Papers Observed')
plt.ylabel('Cumulative Success Rate')
plt.title('Adaptive Fractional Sampling Strategy - Multiple Experiments')
plt.legend()
plt.show()
