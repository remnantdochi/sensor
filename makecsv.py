import serial
import pandas as pd
from datetime import datetime

# 시리얼 포트 설정 - macOS에서 보드 포트로 변경
ser = serial.Serial('/dev/tty.usbmodem55F5F3B72', 115200, timeout=1)

gyro_data = []
accel_data = []

try:
    while True:
        # 시리얼 포트에서 데이터 읽기
        line = ser.readline().decode('utf-8').strip()
        # 유효한 데이터 형식인지 확인
        if line.startswith("Gyroscope (°/s) - "):
            try:
                # 자이로스코프 데이터 분리
                _, gyro_values = line.split("Gyroscope (°/s) - ")
                gyro_x, gyro_y, gyro_z = [float(val.split(": ")[1]) for val in gyro_values.split(", ")]
                gyro_data.append([gyro_x, gyro_y, gyro_z])
                print(f"Gyroscope Data - X: {gyro_x}, Y: {gyro_y}, Z: {gyro_z}")

            except (ValueError, IndexError):
                # 데이터 파싱 오류가 발생하면 건너뜀
                continue

        elif line.startswith("Acceleration (m/s²) - "):
            try:
                # 가속도 데이터 분리
                _, accel_values = line.split("Acceleration (m/s²) - ")
                accel_x, accel_y, accel_z = [float(val.split(": ")[1]) for val in accel_values.split(", ")]
                accel_data.append([accel_x, accel_y, accel_z])
                print(f"Acceleration Data - X: {accel_x}, Y: {accel_y}, Z: {accel_z}")

            except (ValueError, IndexError):
                # 데이터 파싱 오류가 발생하면 건너뜀
                continue

except KeyboardInterrupt:
    # Ctrl+C로 중지 시 데이터를 CSV로 저장
    df_gyro = pd.DataFrame(gyro_data, columns=['Gyro_X', 'Gyro_Y', 'Gyro_Z'])
    df_accel = pd.DataFrame(accel_data, columns=['Accel_X', 'Accel_Y', 'Accel_Z'])

    # 두 데이터프레임을 하나의 CSV로 저장
    with pd.ExcelWriter("sensor_data.xlsx") as writer:
        df_gyro.to_excel(writer, sheet_name="Gyroscope", index=False)
        df_accel.to_excel(writer, sheet_name="Acceleration", index=False)

    print("Data saved to sensor_data.xlsx")