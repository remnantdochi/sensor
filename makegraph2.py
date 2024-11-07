import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# 보드 크기 설정 (단위: m) - 정육면체 (가로 2cm, 세로 2cm, 높이 2cm)
board_size = np.array([0.02, 0.02, 0.02])

# 테스트용 위치와 회전 데이터 (직선 이동 및 단순 회전)
positions = [np.array([i * 0.01, i * 0.01, i * 0.01]) for i in range(100)]
angles_list = [np.array([i * 0.05, i * 0.03, i * 0.04]) for i in range(100)]

# 3D 애니메이션 설정
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 보드 정육면체 생성 함수
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

# 초기 보드 설정
vertices = create_board_vertices([0, 0, 0], board_size)
faces = [[vertices[j] for j in [0, 1, 2, 3]],
         [vertices[j] for j in [4, 5, 6, 7]],
         [vertices[j] for j in [0, 1, 5, 4]],
         [vertices[j] for j in [2, 3, 7, 6]],
         [vertices[j] for j in [1, 2, 6, 5]],
         [vertices[j] for j in [4, 7, 3, 0]]]

board = Poly3DCollection(faces, color='cyan', alpha=0.5)
ax.add_collection3d(board)

# 축 범위 설정 및 축 이름 추가
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_zlim(-0.5, 0.5)
ax.set_xlabel('Position X (m)')
ax.set_ylabel('Position Y (m)')
ax.set_zlabel('Position Z (m)')

# 회전 및 이동을 단순히 적용하는 함수
def apply_simple_rotation(vertices, angle):
    cos_theta, sin_theta = np.cos(angle), np.sin(angle)
    rotation_matrix = np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])
    return vertices @ rotation_matrix.T

# 업데이트 함수
def update(num):
    # 간단한 위치 및 회전 변화
    pos = positions[num]
    angle = num * 0.05  # 간단히 z축을 기준으로 회전
    rotated_vertices = apply_simple_rotation(vertices - np.mean(vertices, axis=0), angle) + pos

    # 각 면 업데이트
    for idx, face in enumerate(faces):
        for j in range(4):
            face[j][:] = rotated_vertices[idx * 4 + j]
    board.set_verts(faces)

# 애니메이션 실행
ani = FuncAnimation(fig, update, frames=len(positions), interval=200)

plt.show()