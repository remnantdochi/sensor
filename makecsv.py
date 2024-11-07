import serial
import pandas as pd
from datetime import datetime

# Set up the serial port - change to the board port on macOS
ser = serial.Serial('/dev/tty.usbmodem55F5F3B72', 115200, timeout=1)

gyro_data = []
accel_data = []

try:
    while True:
        # Read data from the serial port
        line = ser.readline().decode('utf-8').strip()
        # Check if the data format is valid
        if line.startswith("Gyroscope (°/s) - "):
            try:
                # Separate gyroscope data
                _, gyro_values = line.split("Gyroscope (°/s) - ")
                gyro_x, gyro_y, gyro_z = [float(val.split(": ")[1]) for val in gyro_values.split(", ")]
                gyro_data.append([gyro_x, gyro_y, gyro_z])
                print(f"Gyroscope Data - X: {gyro_x}, Y: {gyro_y}, Z: {gyro_z}")

            except (ValueError, IndexError):
                # Skip if there is a data parsing error
                continue

        elif line.startswith("Acceleration (m/s²) - "):
            try:
                # Separate acceleration data
                _, accel_values = line.split("Acceleration (m/s²) - ")
                accel_x, accel_y, accel_z = [float(val.split(": ")[1]) for val in accel_values.split(", ")]
                accel_data.append([accel_x, accel_y, accel_z])
                print(f"Acceleration Data - X: {accel_x}, Y: {accel_y}, Z: {accel_z}")

            except (ValueError, IndexError):
                # Skip if there is a data parsing error
                continue

except KeyboardInterrupt:
    # Save data to CSV when stopped with Ctrl+C
    df_gyro = pd.DataFrame(gyro_data, columns=['Gyro_X', 'Gyro_Y', 'Gyro_Z'])
    df_accel = pd.DataFrame(accel_data, columns=['Accel_X', 'Accel_Y', 'Accel_Z'])

    # Save both dataframes to a single CSV
    with pd.ExcelWriter("sensor_data.xlsx") as writer:
        df_gyro.to_excel(writer, sheet_name="Gyroscope", index=False)
        df_accel.to_excel(writer, sheet_name="Acceleration", index=False)

    print("Data saved to sensor_data.xlsx")