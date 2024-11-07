import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read acceleration data from Excel file
df = pd.read_excel("sensor_data.xlsx", sheet_name="Acceleration")

# Create an array of acceleration data
accel_data = df[['Accel_X', 'Accel_Y', 'Accel_Z']].to_numpy()

# Set expected values
expected_values = np.array([0.0, 0.0, 9.81])  # X, Y are 0, Z is 9.81

# Calculate mean values
mean_accel = np.mean(accel_data, axis=0)

# Calculate offset: subtract mean values from expected values
offset_values = mean_accel - expected_values

# Print offset values
print(f"X-axis Offset: {offset_values[0]:.4f} m/s²")
print(f"Y-axis Offset: {offset_values[1]:.4f} m/s²")
print(f"Z-axis Offset: {offset_values[2]:.4f} m/s²")

# Plot graphs
labels = ['X-axis', 'Y-axis', 'Z-axis']

# Graph to visualize mean values, expected values, and offsets
plt.figure(figsize=(12, 6))

# First graph: mean values and expected values
plt.subplot(2, 1, 1)
plt.bar(labels, mean_accel, color='lightblue', label='Mean Value')
plt.axhline(0, color='red', linestyle='--', label='Expected Value')
plt.axhline(expected_values[2], color='green', linestyle='--', label='Expected Z Value (9.81)')
plt.title('Mean and Expected Values of Acceleration')
plt.xlabel('Axis')
plt.ylabel('Acceleration (m/s²)')
plt.xticks(rotation=0)
plt.legend()
plt.grid(axis='y')

# Second graph: offsets
plt.subplot(2, 1, 2)
plt.bar(labels, offset_values, color='orange', label='Offset')
plt.axhline(0, color='red', linestyle='--', label='Zero Line')
plt.title('Offset Values of Acceleration')
plt.xlabel('Axis')
plt.ylabel('Offset (m/s²)')
plt.xticks(rotation=0)
plt.legend()
plt.grid(axis='y')

# Show graphs
plt.tight_layout()
plt.show()