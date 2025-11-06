import time
import random
from influxdb_client import InfluxDBClient, Point

# Thông tin kết nối
token = "dtTP_TinBc0Hq1I5_ysTD7BhFW--I8BcYfa9MipYMn1h0-pn2BDXc11iw-l6VOqVuHnSDfLRkg2Uz0bz7J_hjw=="
org = "myorg"
bucket = "iotdb"

# Kết nối InfluxDB
client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
write_api = client.write_api()

# Gửi dữ liệu mô phỏng mỗi 5 giây
while True:
    temperature = round(random.uniform(25.0, 35.0), 2)
    humidity = round(random.uniform(50.0, 90.0), 2)
    power = random.choice([0, 1])  # 1 = đang bật, 0 = tắt

    point = (
        Point("room_sensor")
        .field("temperature", temperature)
        .field("humidity", humidity)
        .field("power", power)
    )

    write_api.write(bucket=bucket, org=org, record=point)
    print(f"📡 Sent: temp={temperature}°C | hum={humidity}% | power={power}")
    time.sleep(5)
