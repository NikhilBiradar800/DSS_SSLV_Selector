# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:36 2023

@author: Evangelia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Excel file into a DataFrame
launchers_df = pd.read_excel('launchers.xlsx')

# Convert relevant columns to numeric type
launchers_df['LEO Capacity (kg)'] = pd.to_numeric(launchers_df['LEO Capacity (kg)'], errors='coerce')
launchers_df['SSO Capacity (kg)'] = pd.to_numeric(launchers_df['SSO Capacity (kg)'], errors='coerce')

# Valid countries list
valid_countries = ["JAPAN", "CHINA", "USA", "INDIA", "NEW ZEALAND", "RUSSIA", "EUROPE", ""]

while True:
    # Prompt the user for input
    total_mass = float(input("Enter the total mass of the satellite(s) in kg: "))
    
    # Prompt the user for country preference with error handling
    while True:
        country_preference = input("Enter the country of preference (Japan, China, USA, India, New Zealand, Russia, Europe or blank for any): ").strip().upper()
        if country_preference in valid_countries:
            break
        else:
            print("Invalid country. Try again.")

    orbit_type = input("Enter the type of orbit (LEO/SSO): ").strip().upper()

    # Check if orbit type is valid
    if orbit_type not in ['LEO', 'SSO']:
        print("Invalid orbit type. Please enter LEO or SSO.")
        continue

    # Filter the launchers based on user input criteria
    filtered_launchers = launchers_df.copy()
    if country_preference:
        filtered_launchers = filtered_launchers[filtered_launchers['Country'].str.upper() == country_preference]

    if orbit_type == 'LEO':
        filtered_launchers = filtered_launchers[filtered_launchers['LEO Capacity (kg)'] >= total_mass]
    elif orbit_type == 'SSO':
        filtered_launchers = filtered_launchers[filtered_launchers['SSO Capacity (kg)'] >= total_mass]

    # Check if the combination of country and orbit type is available
    if not filtered_launchers.empty:
        break
    else:
        print("Try again, this combination of country and orbit type is not possible.")

# Calculate the cost and reliability for each launcher
filtered_launchers['Cost ($)'] = (
    total_mass * filtered_launchers[f'{orbit_type} Price ($K/kg)'] * 1000
)
filtered_launchers['Reliability (%)'] = (
    filtered_launchers['Reliability (%)'] 
)

# Sort the launchers by cost and reliability
sorted_launchers = filtered_launchers.sort_values(by=['Cost ($)', 'Reliability (%)'], ascending=[True, False])

# Display the available launchers
print("\nAvailable Launchers:")
print(sorted_launchers[['Vehicle', 'Country', f'{orbit_type} Capacity (kg)', 'Cost ($)', 'Reliability (%)']])

# Define the worst and best values for each attribute
worst_values = {
    'LEO Capacity (kg)': 300,
    'SSO Capacity (kg)': 161,
    'GTO Capacity (kg)': 5200,
    'LEO Price ($K)': 1.41,
    'SSO Price ($K)': 2.8,
    'GTO Price ($K)': 2.35,
    'Total Launches': 3,
    'Reliability (%)': 33.33,
    'Frequency': 24
}

best_values = {
    'LEO Capacity (kg)': 63800,
    'SSO Capacity (kg)': 7960,
    'GTO Capacity (kg)': 26700,
    'LEO Price ($K)': 43.1,
    'SSO Price ($K)': 100.4,
    'GTO Price ($K)': 25.7,
    'Total Launches': 289,
    'Reliability (%)': 100,
    'Frequency': 1270
}

# Define the swings from worst to best
swings = {attr: best_values[attr] - worst_values[attr] for attr in worst_values}

# Let's assume we have performed swing weight elicitation and obtained the following swings
swing_weights = {
    'LEO Capacity (kg)': 30,
    'SSO Capacity (kg)': 30,
    'GTO Capacity (kg)': 30,
    'LEO Price ($K)': 20,
    'SSO Price ($K)': 20,
    'GTO Price ($K)': 20,
    'Total Launches': 15,
    'Reliability (%)': 25,
    'Frequency': 10
}

# Normalize the swing weights
total_swing = sum(swing_weights.values())
normalized_weights = {k: v / total_swing for k, v in swing_weights.items()}

print("Normalized Swing Weights:")
for k, v in normalized_weights.items():
    print(f"{k}: {v}")

# Define the function to calculate MAU
def calculate_mau(capacity, price, launches, reliability, frequency, weights):
    # Normalize attributes using linear transformations
    normalized_capacity = (capacity - worst_values['LEO Capacity (kg)']) / swings['LEO Capacity (kg)']
    normalized_price = (price - worst_values['LEO Price ($K)']) / swings['LEO Price ($K)']
    normalized_launches = (launches - worst_values['Total Launches']) / swings['Total Launches']
    normalized_reliability = (reliability - worst_values['Reliability (%)']) / swings['Reliability (%)']
    normalized_frequency = (frequency - worst_values['Frequency']) / swings['Frequency']

    # Calculate MAU
    mau = (weights['LEO Capacity (kg)'] * normalized_capacity +
           weights['LEO Price ($K)'] * normalized_price +
           weights['Total Launches'] * normalized_launches +
           weights['Reliability (%)'] * normalized_reliability +
           weights['Frequency'] * normalized_frequency)
    return mau

# Define the weights obtained from the swing weight process
weights = {
    'LEO Capacity (kg)': normalized_weights['LEO Capacity (kg)'],
    'LEO Price ($K)': normalized_weights['LEO Price ($K)'],
    'Total Launches': normalized_weights['Total Launches'],
    'Reliability (%)': normalized_weights['Reliability (%)'],
    'Frequency': normalized_weights['Frequency']
}

# Attributes for each launcher alternative
import pandas as pd

# Read the Excel file into a DataFrame
launchers_df = pd.read_excel('launchers.xlsx')

# Define the launcher attributes based on the provided table

# Define the launcher attributes based on the provided table

# Attributes for all alternatives
launcher_attributes = {
    "Epsilon 6": {"Country": "Japan", "LEO Capacity (kg)": 1200, "SSO Capacity (kg)": 450,
                  "LEO Price ($K)": 31.7, "SSO Price ($K)": 84.4, "Total Launches": 4,
                  "Reliability (%)": 100, "Frequency": 651},
    "Kuaizhou": {"Country": "China", "LEO Capacity (kg)": 1500, "SSO Capacity (kg)": 1000,
                 "LEO Price ($K)": 10, "SSO Price ($K)": 13.1, "Total Launches": 23,
                 "Reliability (%)": 88, "Frequency": 610},
    "Minotaur I": {"Country": "USA", "LEO Capacity (kg)": 580, "SSO Capacity (kg)": 317,
                   "LEO Price ($K)": 35.9, "SSO Price ($K)": 68.7, "Total Launches": 12,
                   "Reliability (%)": 100, "Frequency": 505},
    "Minotaur IV": {"Country": "USA", "LEO Capacity (kg)": 1650, "SSO Capacity (kg)": 1000,
                    "LEO Price ($K)": 13.3, "SSO Price ($K)": 22, "Total Launches": 6,
                    "Reliability (%)": 100, "Frequency": 447},
    "Pegasus": {"Country": "USA", "LEO Capacity (kg)": 375, "SSO Capacity (kg)": 161,
                "LEO Price ($K)": 43.1, "SSO Price ($K)": 100.4, "Total Launches": 45,
                "Reliability (%)": 89, "Frequency": 232},
    "Taurus XL": {"Country": "USA", "LEO Capacity (kg)": 1590, "SSO Capacity (kg)": 860,
                  "LEO Price ($K)": 28.5, "SSO Price ($K)": 52.6, "Total Launches": 3,
                  "Reliability (%)": 33.33, "Frequency": 1270},
    "Taurus": {"Country": "USA", "LEO Capacity (kg)": 1380, "SSO Capacity (kg)": 720,
               "LEO Price ($K)": 18.8, "SSO Price ($K)": 35.9, "Total Launches": 10,
               "Reliability (%)": 70, "Frequency": 956},
    "Vega": {"Country": "Europe", "LEO Capacity (kg)": 2500, "SSO Capacity (kg)": 1395,
             "LEO Price ($K)": 1.5, "SSO Price ($K)": 25.1, "Total Launches": 13,
             "Reliability (%)": 100, "Frequency": 206},
    "Delta 2": {"Country": "USA", "LEO Capacity (kg)": 5144, "SSO Capacity (kg)": 3123,
                "LEO Price ($K)": 14.6, "SSO Price ($K)": 24, "Total Launches": 155,
                "Reliability (%)": 97.44, "Frequency": 92},
    "Delta 2M": {"Country": "USA", "LEO Capacity (kg)": 3158, "SSO Capacity (kg)": 1998,
                 "LEO Price ($K)": 19.3, "SSO Price ($K)": 30.8, "Total Launches": 34,
                 "Reliability (%)": 100, "Frequency": 228},
    "GSLV": {"Country": "India", "LEO Capacity (kg)": 5000, "SSO Capacity (kg)": None,
             "LEO Price ($K)": 8.8, "SSO Price ($K)": None, "Total Launches": 13,
             "Reliability (%)": 60, "Frequency": 538},
    "CZ 2C": {"Country": "China", "LEO Capacity (kg)": 3200, "SSO Capacity (kg)": 2000,
              "LEO Price ($K)": 9.5, "SSO Price ($K)": 15.3, "Total Launches": 73,
              "Reliability (%)": 99, "Frequency": 269},
    "CZ 2D": {"Country": "China", "LEO Capacity (kg)": 3500, "SSO Capacity (kg)": 1300,
              "LEO Price ($K)": 5.9, "SSO Price ($K)": 15.8, "Total Launches": 43,
              "Reliability (%)": 97.67, "Frequency": 229},
    "CZ 4C": {"Country": "China", "LEO Capacity (kg)": 4200, "SSO Capacity (kg)": 1700,
              "LEO Price ($K)": 11.4, "SSO Price ($K)": 28.1, "Total Launches": 25,
              "Reliability (%)": 96, "Frequency": 184},
    "PSLV-CA": {"Country": "India", "LEO Capacity (kg)": 2800, "SSO Capacity (kg)": 1100,
                "LEO Price ($K)": 7.2, "SSO Price ($K)": 18.3, "Total Launches": 13,
                "Reliability (%)": 100, "Frequency": 353},
    "PSLV-G": {"Country": "India", "LEO Capacity (kg)": 3700, "SSO Capacity (kg)": 1050,
               "LEO Price ($K)": 5.4, "SSO Price ($K)": 19.2, "Total Launches": 12,
               "Reliability (%)": 83.33, "Frequency": 764},
    "PSLV-XL": {"Country": "India", "LEO Capacity (kg)": 3800, "SSO Capacity (kg)": 1750,
                "LEO Price ($K)": 5.3, "SSO Price ($K)": 11.5, "Total Launches": 20,
                "Reliability (%)": 95, "Frequency": 182},
    "Delta 4M": {"Country": "USA", "LEO Capacity (kg)": 9144, "SSO Capacity (kg)": None, "GTO": 6222,
                 "LEO Price ($K)": 9.7, "SSO Price ($K)": None, "Total Launches": 3,
                 "Reliability (%)": 100, "Frequency": 667},
    "CZ 3A": {"Country": "China", "LEO Capacity (kg)": 6000, "SSO Capacity (kg)": 5000, "GTO": None,
              "LEO Price ($K)": 9.8, "SSO Price ($K)": 11.8, "Total Launches": 27,
              "Reliability (%)": 100, "Frequency": 343},
    "CZ 3C": {"Country": "China", "LEO Capacity (kg)": 9100, "SSO Capacity (kg)": 6500, "GTO": None,
              "LEO Price ($K)": 11.3, "SSO Price ($K)": 15.8, "Total Launches": 16,
              "Reliability (%)": 100, "Frequency": 260},
    "Soyuz 2": {"Country": "Russia", "LEO Capacity (kg)": 7900, "SSO Capacity (kg)": 4850, "GTO": None,
                "LEO Price ($K)": 6.9, "SSO Price ($K)": 11.3, "Total Launches": 167,
                "Reliability (%)": 95.8, "Frequency": 64},
    "Falcon 9": {"Country": "USA", "LEO Capacity (kg)": 22800, "SSO Capacity (kg)": 7960, "GTO": 8300,
                 "LEO Price ($K)": 2.8, "SSO Price ($K)": 2.8, "Total Launches": 289,
                 "Reliability (%)": 99.3, "Frequency": 24},
    "Falcon Heavy": {"Country": "USA", "LEO Capacity (kg)": 63800, "SSO Capacity (kg)": None, "GTO": 26700,
                     "LEO Price ($K)": 1.41, "SSO Price ($K)": None, "Total Launches": 100,
                     "Reliability (%)": 90, "Frequency": 24},
    "H-2A": {"Country": "Japan", "LEO Capacity (kg)": 11730, "SSO Capacity (kg)": None, "GTO": 5800,
             "LEO Price ($K)": 7.7, "SSO Price ($K)": None, "Total Launches": 45,
             "Reliability (%)": 86, "Frequency": 157},
    "Delta 4 Heavy": {"Country": "USA", "LEO Capacity (kg)": 28370, "SSO Capacity (kg)": None, "GTO": 13130,
                      "LEO Price ($K)": 9.5, "SSO Price ($K)": None, "Total Launches": 11,
                      "Reliability (%)": 93, "Frequency": 467},
    "CZ 3B/E": {"Country": "China", "LEO Capacity (kg)": 11500, "SSO Capacity (kg)": None, "GTO": 5200,
                "LEO Price ($K)": 6, "SSO Price ($K)": None, "Total Launches": 55,
                "Reliability (%)": 94.55, "Frequency": 153},
    "Proton M": {"Country": "Russia", "LEO Capacity (kg)": 21000, "SSO Capacity (kg)": None, "GTO": 5500,
                 "LEO Price ($K)": 6.7, "SSO Price ($K)": None, "Total Launches": 102,
                 "Reliability (%)": 90, "Frequency": 63},
    "Electron": {"Country": "New Zealand", "LEO Capacity (kg)": 300, "SSO Capacity (kg)": 200, "GTO": None,
                 "LEO Price ($K)": 23.33, "SSO Price ($K)": 23.33, "Total Launches": 20,
                 "Reliability (%)": 80, "Frequency": None},
}

# Loop through launcher_attributes and use .loc to assign values to the DataFrame
for launcher, attributes in launcher_attributes.items():
    launchers_df.loc[launchers_df['Vehicle'] == launcher, 'Country'] = attributes['Country']
    launchers_df.loc[launchers_df['Vehicle'] == launcher, 'LEO Capacity (kg)'] = attributes['LEO Capacity (kg)']
    launchers_df.loc[launchers_df['Vehicle'] == launcher, 'SSO Capacity (kg)'] = attributes['SSO Capacity (kg)']
    launchers_df.loc[launchers_df['Vehicle'] == launcher, 'LEO Price ($K)'] = attributes['LEO Price ($K)']
    launchers_df.loc[launchers_df['Vehicle'] == launcher, 'SSO Price ($K)'] = attributes['SSO Price ($K)']
    launchers_df.loc[launchers_df['Vehicle'] == launcher, 'Total Launches'] = attributes['Total Launches']
    launchers_df.loc[launchers_df['Vehicle'] == launcher, 'Reliability (%)'] = attributes['Reliability (%)']
    launchers_df.loc[launchers_df['Vehicle'] == launcher, 'Frequency'] = attributes['Frequency']

# Display the updated DataFrame with the added attributes
print(launchers_df)


# Calculate MAU for each launcher alternative
# Calculate MAU for each launcher alternative
mau_values = {}
for launcher, attr_values in launcher_attributes.items():
    mau_values[launcher] = calculate_mau(attr_values['LEO Capacity (kg)'],
                                         attr_values['LEO Price ($K)'],
                                         attr_values['Total Launches'],
                                         attr_values['Reliability (%)'],
                                         attr_values['Frequency'],
                                         weights)

# Display the MAU for each launcher alternative
for launcher, mau in mau_values.items():
    print(f"The MAU for {launcher} is: {mau:.4f}")


# Define the number of samples for the Monte Carlo simulation
num_samples = 1000

# Define the distributions for each attribute
def generate_samples(distribution, mean, std_dev, size):
    return distribution(mean, std_dev, size=size)

# Define the distributions for each attribute, parameterized to use in the simulation
mean_capacity = launchers_df['SSO Capacity (kg)'].mean()
std_dev_capacity = launchers_df['SSO Capacity (kg)'].std()

mean_leo_price = launchers_df['LEO Price ($K/kg)'].mean()
std_dev_leo_price = launchers_df['LEO Price ($K/kg)'].std()

mean_sso_price = launchers_df['SSO Price ($K/kg)'].mean()
std_dev_sso_price = launchers_df['SSO Price ($K/kg)'].std()

mean_total_launches = launchers_df['Total Launches'].mean()
std_dev_total_launches = launchers_df['Total Launches'].std()

mean_reliability = launchers_df['Reliability (%)'].mean()
std_dev_reliability = launchers_df['Reliability (%)'].std()

mean_frequency = launchers_df['Frequency'].mean()
std_dev_frequency = launchers_df['Frequency'].std()

# Create an empty dictionary to store simulation results
simulation_results = {}

# Perform the Monte Carlo simulation for each launcher
for launcher, attr_values in launcher_attributes.items():
    # Generate random samples for each attribute
    sso_capacity = generate_samples(np.random.normal, mean_capacity, std_dev_capacity, num_samples)
    leo_price = generate_samples(np.random.normal, mean_leo_price, std_dev_leo_price, num_samples)
    sso_price = generate_samples(np.random.normal, mean_sso_price, std_dev_sso_price, num_samples)
    total_launches = generate_samples(np.random.normal, mean_total_launches, std_dev_total_launches, num_samples)
    reliability = generate_samples(np.random.normal, mean_reliability, std_dev_reliability, num_samples)
    frequency = generate_samples(np.random.normal, mean_frequency, std_dev_frequency, num_samples)
    
    # Calculate the utility for each sample and store it in a list
    utilities = []
    for i in range(num_samples):
        utility = calculate_total_utility(sso_capacity[i], leo_price[i], sso_price[i], total_launches[i], reliability[i], frequency[i], weights)
        utilities.append(utility)
    
    # Store the list of utilities in the simulation_results dictionary
    simulation_results[launcher] = utilities

# Plot histograms for utility distributions
plt.figure(figsize=(14, 7))
for launcher, utilities in simulation_results.items():
    plt.hist(utilities, bins=30, alpha=0.5, label=launcher)
plt.title('Utility Distributions for Each Launcher')
plt.xlabel('Simulated Utility')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Perform sensitivity analysis for cost variations
# Define a range of cost variation factors
cost_variation_range = np.linspace(0.8, 1.2, num=21)

# Create an empty dictionary to store sensitivity analysis results
cost_sensitivity_results = {}

# Perform sensitivity analysis for cost variations
for launcher, attr_values in launcher_attributes.items():
    sensitivity_utilities = []
    for cost_variation in cost_variation_range:
        # Adjust the cost attributes based on the variation
        adjusted_attr_values = attr_values.copy()
        adjusted_attr_values['LEO Price ($K/kg)'] *= cost_variation
        adjusted_attr_values['SSO Price ($K/kg)'] *= cost_variation
        
        # Calculate the utility with adjusted cost attributes
        sensitivity_utility = calculate_total_utility(adjusted_attr_values['SSO Capacity (kg)'], adjusted_attr_values['LEO Price ($K/kg)'], adjusted_attr_values['SSO Price ($K/kg)'], attr_values['Total Launches'], attr_values['Reliability (%)'], attr_values['Frequency'], weights)
        
        sensitivity_utilities.append(sensitivity_utility)
    
    # Store the sensitivity analysis results in the dictionary
    cost_sensitivity_results[launcher] = sensitivity_utilities


# Perform sensitivity analysis for weight variations
for launcher, attr_values in launcher_attributes.items():
    sensitivity_utilities = []
    for weight_variation in weight_variation_range:
        # Adjust the weights based on the variation
        adjusted_weights = {
            "LEO Capacity (kg)": weights['LEO Capacity (kg)'] * weight_variation,
            "LEO Price ($K/kg)": weights['LEO Price ($K/kg)'] * weight_variation,
            "Total Launches": weights['Total Launches'] * weight_variation,
            "Reliability (%)": weights['Reliability (%)'] * weight_variation,
            "Frequency": weights['Frequency'] * weight_variation
        }
        
        # Calculate the utility with adjusted weights
        sensitivity_utility = calculate_total_utility(attr_values['SSO Capacity (kg)'], attr_values['LEO Price ($K/kg)'], attr_values['SSO Price ($K/kg)'], attr_values['Total Launches'], attr_values['Reliability (%)'], attr_values['Frequency'], adjusted_weights)
        
        sensitivity_utilities.append(sensitivity_utility)
    
    # Store the sensitivity analysis results in the dictionary
    weight_sensitivity_results[launcher] = sensitivity_utilities

# Plot Weight Sensitivity Analysis
plt.figure(figsize=(14, 7))
for launcher, utilities in weight_sensitivity_results.items():
    plt.plot(weight_variation_range, utilities, label=launcher)
plt.title('Sensitivity Analysis of Utility to Weight Variations')
plt.xlabel('Weight Variation Factor')
plt.ylabel('Total Utility')
plt.legend()
plt.grid(True)
plt.show()

# Perform sensitivity analysis for cost variations
# Define a range of cost variation factors
cost_variation_range = np.linspace(0.8, 1.2, num=21)

# Create an empty dictionary to store sensitivity analysis results
cost_sensitivity_results = {}

# Perform sensitivity analysis for cost variations
for launcher, attr_values in launcher_attributes.items():
    sensitivity_utilities = []
    for cost_variation in cost_variation_range:
        # Adjust the cost attributes based on the variation
        adjusted_attr_values = attr_values.copy()
        adjusted_attr_values['LEO Price ($K/kg)'] *= cost_variation
        adjusted_attr_values['SSO Price ($K/kg)'] *= cost_variation
        
        # Calculate the utility with adjusted cost attributes
        sensitivity_utility = calculate_total_utility(adjusted_attr_values['SSO Capacity (kg)'], adjusted_attr_values['LEO Price ($K/kg)'], adjusted_attr_values['SSO Price ($K/kg)'], attr_values['Total Launches'], attr_values['Reliability (%)'], attr_values['Frequency'], weights)
        
        sensitivity_utilities.append(sensitivity_utility)
    
    # Store the sensitivity analysis results in the dictionary
    cost_sensitivity_results[launcher] = sensitivity_utilities

# Plot Cost Sensitivity Analysis
plt.figure(figsize=(14, 7))
for launcher, utilities in cost_sensitivity_results.items():
    plt.plot(cost_variation_range, utilities, label=launcher)
plt.title('Sensitivity Analysis of Utility to Cost Variations')
plt.xlabel('Cost Variation Factor')
plt.ylabel('Total Utility')
plt.legend()
plt.grid(True)
plt.show()

# Recommend the launcher with the highest expected utility
expected_utilities = {launcher: np.mean(utilities) for launcher, utilities in simulation_results.items()}
best_launcher = max(expected_utilities, key=expected_utilities.get)
print(f"The recommended launcher is: {best_launcher}")

