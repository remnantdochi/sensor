import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Excel 파일에서 가속도 데이터를 읽기
df = pd.read_excel("sensor_data.xlsx", sheet_name="Acceleration")

# 가속도 데이터 배열 생성
accel_data = df[['Accel_X', 'Accel_Y', 'Accel_Z']].to_numpy()

# 예상되는 값 설정
expected_values = np.array([0.0, 0.0, 9.81])  # X, Y는 0, Z는 9.81

# 평균값 계산
mean_accel = np.mean(accel_data, axis=0)

# 오프셋 계산: 예상되는 값에서 평균값을 뺌
offset_values = mean_accel - expected_values

# 오프셋 출력
print(f"X-axis Offset: {offset_values[0]:.4f} m/s²")
print(f"Y-axis Offset: {offset_values[1]:.4f} m/s²")
print(f"Z-axis Offset: {offset_values[2]:.4f} m/s²")

# 그래프 그리기
labels = ['X-axis', 'Y-axis', 'Z-axis']

# 평균값, 예상값 및 오프셋을 시각화할 그래프
plt.figure(figsize=(12, 6))

# 첫 번째 그래프: 평균값 및 예상값
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

# 두 번째 그래프: 오프셋
plt.subplot(2, 1, 2)
plt.bar(labels, offset_values, color='orange', label='Offset')
plt.axhline(0, color='red', linestyle='--', label='Zero Line')
plt.title('Offset Values of Acceleration')
plt.xlabel('Axis')
plt.ylabel('Offset (m/s²)')
plt.xticks(rotation=0)
plt.legend()
plt.grid(axis='y')

# 그래프 출력
plt.tight_layout()
plt.show()