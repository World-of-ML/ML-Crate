import pandas as pd
import numpy as np

# Generate synthetic data 
np.random.seed(42)

n_samples = 1000
data = {
    "Payment History": np.random.randint(50, 101, size=n_samples),  # Scores between 50 and 100
    "Credit Utilization Ratio": np.random.uniform(0, 100, size=n_samples),  # Percentage
    "Number of Credit Accounts": np.random.randint(1, 15, size=n_samples),  # Random number of accounts
    "Education Level": np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], size=n_samples),
    "Employment Status": np.random.choice(['Employed', 'Unemployed', 'Self-Employed'], size=n_samples)
}

# Convert to DataFrame
synthetic_data = pd.DataFrame(data)

synthetic_data.to_csv("synthetic_credit_data.csv", index=False)

print("Synthetic dataset saved as 'synthetic_credit_data.csv'.")
