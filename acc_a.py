import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Excel 파일에서 가속도 데이터를 읽기
df = pd.read_excel("sensor_data.xlsx", sheet_name="Acceleration")

# 가속도 데이터 배열 생성
accel_data = df[['Accel_X', 'Accel_Y', 'Accel_Z']].to_numpy()

# 평균값 계산
mean_accel = np.mean(accel_data, axis=0)

# 드리프트 계산
drift_values = accel_data - mean_accel

# 드리프트의 평균과 표준편차 계산
drift_mean = np.mean(drift_values, axis=0)
drift_std = np.std(drift_values, axis=0)

# 드리프트 값 시각화
plt.figure(figsize=(12, 6))

# X축 드리프트
plt.subplot(3, 1, 1)
plt.plot(drift_values[:, 0], label='X-axis Drift', color='blue')
plt.axhline(y=drift_mean[0], color='red', linestyle='--', label='Mean Drift')
plt.axhline(y=drift_mean[0] + drift_std[0], color='green', linestyle='--', label='Std Dev Upper')
plt.axhline(y=drift_mean[0] - drift_std[0], color='green', linestyle='--', label='Std Dev Lower')
plt.title('X-axis Drift')
plt.xlabel('Sample Index')
plt.ylabel('Drift (m/s²)')
plt.legend()
plt.grid()

# Y축 드리프트
plt.subplot(3, 1, 2)
plt.plot(drift_values[:, 1], label='Y-axis Drift', color='orange')
plt.axhline(y=drift_mean[1], color='red', linestyle='--', label='Mean Drift')
plt.axhline(y=drift_mean[1] + drift_std[1], color='green', linestyle='--', label='Std Dev Upper')
plt.axhline(y=drift_mean[1] - drift_std[1], color='green', linestyle='--', label='Std Dev Lower')
plt.title('Y-axis Drift')
plt.xlabel('Sample Index')
plt.ylabel('Drift (m/s²)')
plt.legend()
plt.grid()

# Z축 드리프트
plt.subplot(3, 1, 3)
plt.plot(drift_values[:, 2], label='Z-axis Drift', color='purple')
plt.axhline(y=drift_mean[2], color='red', linestyle='--', label='Mean Drift')
plt.axhline(y=drift_mean[2] + drift_std[2], color='green', linestyle='--', label='Std Dev Upper')
plt.axhline(y=drift_mean[2] - drift_std[2], color='green', linestyle='--', label='Std Dev Lower')
plt.title('Z-axis Drift')
plt.xlabel('Sample Index')
plt.ylabel('Drift (m/s²)')
plt.legend()
plt.grid()

# 그래프 출력
plt.tight_layout()
plt.show()

# 드리프트 값 출력
print(f"X-axis Drift Mean: {drift_mean[0]:.8f} m/s², Std Dev: {drift_std[0]:.8f} m/s²")
print(f"Y-axis Drift Mean: {drift_mean[1]:.8f} m/s², Std Dev: {drift_std[1]:.8f} m/s²")
print(f"Z-axis Drift Mean: {drift_mean[2]:.8f} m/s², Std Dev: {drift_std[2]:.8f} m/s²")