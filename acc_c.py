import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Excel 파일에서 가속도 데이터를 읽기
df = pd.read_excel("sensor_data.xlsx", sheet_name="Acceleration")

# 가속도 데이터 배열 생성
accel_data = df[['Accel_X', 'Accel_Y', 'Accel_Z']].to_numpy()

# 평균값 계산
mean_accel = np.mean(accel_data, axis=0)

# 각 축의 평균값을 빼서 조정된 데이터 계산
adjusted_data = accel_data - mean_accel

# 히스토그램 그리기
plt.figure(figsize=(12, 6))

# X축 히스토그램
plt.subplot(3, 1, 1)
plt.hist(adjusted_data[:, 0], bins=30, color='blue', alpha=0.7)
plt.axvline(0, color='red', linestyle='--', label='Mean Value')
plt.title('X-axis Adjusted Data Histogram')
plt.xlabel('Adjusted Value (m/s²)')
plt.ylabel('Frequency')
plt.legend()
plt.grid()

# Y축 히스토그램
plt.subplot(3, 1, 2)
plt.hist(adjusted_data[:, 1], bins=30, color='orange', alpha=0.7)
plt.axvline(0, color='red', linestyle='--', label='Mean Value')
plt.title('Y-axis Adjusted Data Histogram')
plt.xlabel('Adjusted Value (m/s²)')
plt.ylabel('Frequency')
plt.legend()
plt.grid()

# Z축 히스토그램
plt.subplot(3, 1, 3)
plt.hist(adjusted_data[:, 2], bins=30, color='green', alpha=0.7)
plt.axvline(0, color='red', linestyle='--', label='Mean Value')
plt.title('Z-axis Adjusted Data Histogram')
plt.xlabel('Adjusted Value (m/s²)')
plt.ylabel('Frequency')
plt.legend()
plt.grid()

# 그래프 출력
plt.tight_layout()
plt.show()