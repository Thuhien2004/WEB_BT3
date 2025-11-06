from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

# Cấu hình InfluxDB
token = "dtTP_TinBc0Hq1I5_ysTD7BhFW--I8BcYfa9MipYMn1h0-pn2BDXc11iw-l6VOqVuHnSDfLRkg2Uz0bz7J_hjw=="
org = "myorg"
bucket = "iotdb"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Vòng lặp mô phỏng dữ liệu cảm biến
while True:
    temperature = round(random.uniform(25, 35), 2)
    humidity = round(random.uniform(40, 70), 2)
    light = round(random.uniform(200, 800), 2)

    point = Point("room_sensors") \
        .tag("location", "lab101") \
        .field("temperature", temperature) \
        .field("humidity", humidity) \
        .field("light", light)

    write_api.write(bucket=bucket, org=org, record=point)
    print(f"Gửi dữ liệu: Nhiệt độ={temperature}°C, Ẩm={humidity}%, Ánh sáng={light} lux")

    time.sleep(5)  # Gửi 5 giây/lần
