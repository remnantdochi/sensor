import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# Set board size (unit: m) - Cube (width 2cm, height 2cm, depth 2cm)
board_size = np.array([0.02, 0.02, 0.02])

# Test position and rotation data (linear movement and simple rotation)
positions = [np.array([i * 0.01, i * 0.01, i * 0.01]) for i in range(100)]
angles_list = [np.array([i * 0.05, i * 0.03, i * 0.04]) for i in range(100)]

# 3D animation setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to create board cube vertices
def create_board_vertices(center, size):
    dx, dy, dz = size / 2
    cx, cy, cz = center
    vertices = np.array([
        [cx - dx, cy - dy, cz - dz],
        [cx + dx, cy - dy, cz - dz],
        [cx + dx, cy + dy, cz - dz],
        [cx - dx, cy + dy, cz - dz],
        [cx - dx, cy - dy, cz + dz],
        [cx + dx, cy - dy, cz + dz],
        [cx + dx, cy + dy, cz + dz],
        [cx - dx, cy + dy, cz + dz]
    ])
    return vertices

# Initial board setup
vertices = create_board_vertices([0, 0, 0], board_size)
faces = [[vertices[j] for j in [0, 1, 2, 3]],
         [vertices[j] for j in [4, 5, 6, 7]],
         [vertices[j] for j in [0, 1, 5, 4]],
         [vertices[j] for j in [2, 3, 7, 6]],
         [vertices[j] for j in [1, 2, 6, 5]],
         [vertices[j] for j in [4, 7, 3, 0]]]

board = Poly3DCollection(faces, color='cyan', alpha=0.5)
ax.add_collection3d(board)

# Set axis range and add axis labels
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_zlim(-0.5, 0.5)
ax.set_xlabel('Position X (m)')
ax.set_ylabel('Position Y (m)')
ax.set_zlabel('Position Z (m)')

# Function to apply simple rotation and translation
def apply_simple_rotation(vertices, angle):
    cos_theta, sin_theta = np.cos(angle), np.sin(angle)
    rotation_matrix = np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])
    return vertices @ rotation_matrix.T

# Update function
def update(num):
    # Simple position and rotation change
    pos = positions[num]
    angle = num * 0.05  # Simple rotation around z-axis
    rotated_vertices = apply_simple_rotation(vertices - np.mean(vertices, axis=0), angle) + pos

    # Update each face
    for idx, face in enumerate(faces):
        for j in range(4):
            face[j][:] = rotated_vertices[idx * 4 + j]
    board.set_verts(faces)

# Run animation
ani = FuncAnimation(fig, update, frames=len(positions), interval=200)

plt.show()