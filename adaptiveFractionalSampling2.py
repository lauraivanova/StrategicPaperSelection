import matplotlib.pyplot as plt
import numpy as np

def adaptive_fractional_sampling_strategy(num_papers, initial_fraction, true_highest_number):
    cumulative_success_rate = []
    dynamic_thresholds = []
    
    current_max_number = 0
    threshold = initial_fraction * true_highest_number
    
    for i in range(1, num_papers + 1):
        observed_number = np.random.uniform(0, true_highest_number)
        current_max_number = max(current_max_number, observed_number)
        threshold = initial_fraction * current_max_number
        
        if observed_number >= threshold:
            cumulative_success_rate.append(1)
        else:
            cumulative_success_rate.append(0)
        
        dynamic_thresholds.append(threshold)
    
    return np.cumsum(cumulative_success_rate) / np.arange(1, num_papers + 1)

def plot_strategy_analysis(num_simulations, num_papers, initial_fraction, true_highest_number):
    cumulative_success_rates = np.zeros((num_simulations, num_papers))
    
    for i in range(num_simulations):
        cumulative_success_rates[i, :] = adaptive_fractional_sampling_strategy(
            num_papers, initial_fraction, true_highest_number
        )
    
    mean_success_rate = np.mean(cumulative_success_rates, axis=0)
    
    plt.figure(figsize=(12, 8))
    plt.plot(range(1, num_papers + 1), mean_success_rate, label='Mean Success Rate', color='blue')
    plt.title('Adaptive Fractional Sampling Strategy Analysis (10,000 Simulations)')
    plt.xlabel('Number of Papers Selected')
    plt.ylabel('Cumulative Success Rate')
    plt.legend()
    plt.show()

# Example usage
plot_strategy_analysis(num_simulations=10000, num_papers=100, initial_fraction=0.1, true_highest_number=1000)
