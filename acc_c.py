import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read acceleration data from Excel file
df = pd.read_excel("sensor_data.xlsx", sheet_name="Acceleration")

# Create an array of acceleration data
accel_data = df[['Accel_X', 'Accel_Y', 'Accel_Z']].to_numpy()

# Calculate mean values
mean_accel = np.mean(accel_data, axis=0)

# Calculate adjusted data by subtracting the mean value from each axis
adjusted_data = accel_data - mean_accel

# Plot histograms
plt.figure(figsize=(12, 6))

# X-axis histogram
plt.subplot(3, 1, 1)
plt.hist(adjusted_data[:, 0], bins=30, color='blue', alpha=0.7)
plt.axvline(0, color='red', linestyle='--', label='Mean Value')
plt.title('X-axis Adjusted Data Histogram')
plt.xlabel('Adjusted Value (m/s²)')
plt.ylabel('Frequency')
plt.legend()
plt.grid()

# Y-axis histogram
plt.subplot(3, 1, 2)
plt.hist(adjusted_data[:, 1], bins=30, color='orange', alpha=0.7)
plt.axvline(0, color='red', linestyle='--', label='Mean Value')
plt.title('Y-axis Adjusted Data Histogram')
plt.xlabel('Adjusted Value (m/s²)')
plt.ylabel('Frequency')
plt.legend()
plt.grid()

# Z-axis histogram
plt.subplot(3, 1, 3)
plt.hist(adjusted_data[:, 2], bins=30, color='green', alpha=0.7)
plt.axvline(0, color='red', linestyle='--', label='Mean Value')
plt.title('Z-axis Adjusted Data Histogram')
plt.xlabel('Adjusted Value (m/s²)')
plt.ylabel('Frequency')
plt.legend()
plt.grid()

# Display the plot
plt.tight_layout()
plt.show()