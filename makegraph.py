import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# sensor_data.xlsx에서 가속도 데이터 로드
df_accel = pd.read_excel("sensor_data.xlsx", sheet_name="Acceleration")

# 초기 위치와 속도 설정
position = np.array([0.0, 0.0, 0.0])
velocity = np.array([0.0, 0.0, 0.0])
dt = 0.1  # 시간 간격 (초)

# 위치 데이터를 저장할 리스트 초기화
positions = [position.copy()]

# 가속도 데이터를 이용해 속도와 위치 계산
for i in range(len(df_accel)):
    # 가속도 데이터 추출
    acc_x, acc_y, acc_z = df_accel['Accel_X'][i], df_accel['Accel_Y'][i], df_accel['Accel_Z'][i]
    acceleration = np.array([acc_x, acc_y, acc_z])

    # 속도 및 위치 계산 (적분)
    velocity += acceleration * dt
    position += velocity * dt

    # 현재 위치 저장
    positions.append(position.copy())

# 위치 결과를 데이터프레임으로 변환
df_position = pd.DataFrame(positions, columns=['Pos_X', 'Pos_Y', 'Pos_Z'])

# 3D 애니메이션 설정
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 궤적 라인 초기화
trajectory_line, = ax.plot([], [], [], 'b-', linewidth=1, label='Trajectory')  # 궤적을 나타내는 라인
cube = ax.plot([], [], [], 'ro', markersize=5, label='Current Position')[0]  # 현재 위치를 나타내는 점

# 축 범위 설정 및 축 이름 추가
ax.set_xlim(df_position['Pos_X'].min()-1, df_position['Pos_X'].max()+1)
ax.set_ylim(df_position['Pos_Y'].min()-1, df_position['Pos_Y'].max()+1)
ax.set_zlim(df_position['Pos_Z'].min()-1, df_position['Pos_Z'].max()+1)
ax.set_xlabel('Position X (m)')
ax.set_ylabel('Position Y (m)')
ax.set_zlabel('Position Z (m)')
ax.legend()

def update(num):
    # 현재 위치까지의 궤적
    pos = df_position.iloc[:num+1]
    x, y, z = pos['Pos_X'], pos['Pos_Y'], pos['Pos_Z']
    
    # 궤적과 현재 위치 갱신
    trajectory_line.set_data(x, y)
    trajectory_line.set_3d_properties(z)
    cube.set_data([x.iloc[-1]], [y.iloc[-1]])
    cube.set_3d_properties([z.iloc[-1]])
    
    # 경과 시간 표시
    elapsed_time = num * dt
    ax.set_title(f"3D Position and Trajectory of Cube - Elapsed Time: {elapsed_time:.1f} s")

# 애니메이션 실행
ani = FuncAnimation(fig, update, frames=len(df_position), interval=200)

plt.show()