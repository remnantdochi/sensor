import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Load acceleration data from sensor_data.xlsx
df_accel = pd.read_excel("sensor_data.xlsx", sheet_name="Acceleration")

# Set initial position and velocity
position = np.array([0.0, 0.0, 0.0])
velocity = np.array([0.0, 0.0, 0.0])
dt = 0.1  # Time interval (seconds)

# Initialize list to store position data
positions = [position.copy()]

# Calculate velocity and position using acceleration data
for i in range(len(df_accel)):
    # Extract acceleration data
    acc_x, acc_y, acc_z = df_accel['Accel_X'][i], df_accel['Accel_Y'][i], df_accel['Accel_Z'][i]
    acceleration = np.array([acc_x, acc_y, acc_z])

    # Calculate velocity and position (integration)
    velocity += acceleration * dt
    position += velocity * dt

    # Save current position
    positions.append(position.copy())

# Convert position results to a DataFrame
df_position = pd.DataFrame(positions, columns=['Pos_X', 'Pos_Y', 'Pos_Z'])

# Set up 3D animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize trajectory line
trajectory_line, = ax.plot([], [], [], 'b-', linewidth=1, label='Trajectory')  # Line representing the trajectory
cube = ax.plot([], [], [], 'ro', markersize=5, label='Current Position')[0]  # Point representing the current position

# Set axis limits and labels
ax.set_xlim(df_position['Pos_X'].min()-1, df_position['Pos_X'].max()+1)
ax.set_ylim(df_position['Pos_Y'].min()-1, df_position['Pos_Y'].max()+1)
ax.set_zlim(df_position['Pos_Z'].min()-1, df_position['Pos_Z'].max()+1)
ax.set_xlabel('Position X (m)')
ax.set_ylabel('Position Y (m)')
ax.set_zlabel('Position Z (m)')
ax.legend()

def update(num):
    # Trajectory up to the current position
    pos = df_position.iloc[:num+1]
    x, y, z = pos['Pos_X'], pos['Pos_Y'], pos['Pos_Z']
    
    # Update trajectory and current position
    trajectory_line.set_data(x, y)
    trajectory_line.set_3d_properties(z)
    cube.set_data([x.iloc[-1]], [y.iloc[-1]])
    cube.set_3d_properties([z.iloc[-1]])
    
    # Display elapsed time
    elapsed_time = num * dt
    ax.set_title(f"3D Position and Trajectory of Cube - Elapsed Time: {elapsed_time:.1f} s")

# Run animation
ani = FuncAnimation(fig, update, frames=len(df_position), interval=200)

plt.show()