
# Bài tập 3   : môn Phát triển ứng dụng trên nền web
Giảng viên  : Đỗ Duy Cốp
Lớp học phần: 58KTPM
Ngày giao   : 2025-10-24 13:50
Hạn nộp     : 2025-11-06 23:59
--------------------------------------------------
-- Yêu cầu     : LẬP TRÌNH ỨNG DỤNG WEB trên nền linux
# 1 : CÀI ĐẶT MÔI TRƯỜNG (Em sử dụng Docker Desktop trên máy để thực hiện đề tài)
Sử dụng 1 file docker-compose.yml để cài đặt các docker container sau: mariadb (3306), phpmyadmin (8080), nodered/node-red (1880), influxdb (8086), grafana/grafana (3000), nginx (80,443)
b1: Tạo thư mục dự án

<img width="1155" height="525" alt="image" src="https://github.com/user-attachments/assets/bf734e08-700e-4ea9-81b9-4d75109e28c9" />

-> Vào powershell gõ các câu lệnh khởi tạo thư mục

b2: Tạo file docker compose.yml tại thư mục dự án

<img width="540" height="324" alt="image" src="https://github.com/user-attachments/assets/e76aba9c-6c7e-4ef3-9736-00f7ed2845eb" />

b3: Tạo file Nginx.conf

<img width="941" height="486" alt="image" src="https://github.com/user-attachments/assets/5664bf6a-093f-4c16-a169-a0dae3b669e2" />

b4: Khởi tạo thư mục để chứa các file để lập trình web

<img width="1412" height="341" alt="image" src="https://github.com/user-attachments/assets/30b72202-fd88-4fc2-ac79-5c17b1bdcfdc" />

b5: Mở Docker Desktop trên máy, bật ứng dụng chạy nền . Vào PowerShell với quyền admin và khởi chạy lệnh: docker-compose up -d

<img width="1911" height="907" alt="image" src="https://github.com/user-attachments/assets/556750d0-25e4-45a8-a51f-e5042d0eae20" />

b6: Em tạo domain riêng cho mình web3iot.com 
1. cấu hình lại file hosts, vào đường dẫn C:\Windows\System32\drivers\etc\hosts
 thêm dòng 127.0.0.1   web3iot.com vào file

<img width="1266" height="724" alt="image" src="https://github.com/user-attachments/assets/da0b9061-9aea-487c-91b3-ad3f7608d151" />

 Vào trình duyệt http://web3iot.com thấy chạy được thì domain đã trỏ thành công 

 <img width="1267" height="365" alt="image" src="https://github.com/user-attachments/assets/c6678a1a-9556-4c60-9dc1-aa36d1230052" />

Khởi động lại file Nginx.conf bằng câu lệnh chạy trên powershell admin

<img width="1112" height="211" alt="image" src="https://github.com/user-attachments/assets/d759fb82-4ba0-4c77-952b-943819ca4bc4" />

Truy cập được các trình duyệt nodered và grafana (đăng nhập grafana bằng tài khoản mặc định admin/admin rồi đổi mật khẩu cho cá nhân)

<img width="1911" height="1065" alt="image" src="https://github.com/user-attachments/assets/b6cd1608-045d-472c-81ec-23a6695d790e" />

<img width="1904" height="1029" alt="image" src="https://github.com/user-attachments/assets/16ea1cf1-d52e-4bb0-8e1a-d7e8b736cbaf" />

2. Vào nodered
- cài đặt node-red-contrib-influxdb bằng cách vào Manager Pallet trong nodered ở thanh menu , ài node kết nối InfluxDB

<img width="999" height="538" alt="image" src="https://github.com/user-attachments/assets/206af169-b012-4d7c-9eb7-64fce77940fa" />

- Tạo flow mô phỏng cảm biến

<img width="925" height="257" alt="image" src="https://github.com/user-attachments/assets/54b6dd48-e3ee-4d07-834a-8a9b3e7be990" />

- Thêm dữ liệu cho fuction

<img width="810" height="586" alt="image" src="https://github.com/user-attachments/assets/d2c1166d-20cc-4cb3-b54f-96b031bc26a4" />

- Cấu hình node InfluxDB Out:

<img width="683" height="663" alt="image" src="https://github.com/user-attachments/assets/9dd2cc40-420a-411c-9af3-efe2330d89af" />

- Cấu hình node inject

<img width="727" height="862" alt="image" src="https://github.com/user-attachments/assets/d061f779-4035-4231-aa37-74da4cff0a1e" />

3. Mô phỏng cảm biến gửi dữ liệu vào influxdb
- Tạo file sensor.py tại thư mục dự án
  
<img width="1642" height="950" alt="image" src="https://github.com/user-attachments/assets/77adc2f4-99d2-4482-a383-6c6d65d98e27" />

- cài đặt thư viện "influxdb-client"

<img width="1441" height="672" alt="image" src="https://github.com/user-attachments/assets/6d14801a-7b6f-46dd-a5de-e5d55906de56" />
 
- Tạo file mô phỏng cảm biến sensor_simulator.py

<img width="1421" height="899" alt="image" src="https://github.com/user-attachments/assets/bfea571b-ffaf-4456-bb7d-d610ed41c79e" />

- Chạy mô phỏng cảm biến của file sensor_simulator.py bằng powershell

<img width="896" height="408" alt="image" src="https://github.com/user-attachments/assets/72c7369b-ccdb-4419-aa90-f02181cbe03e" />

* TỔNG QUAN MỤC TIÊU:

Cảm biến (hoặc API) → Node-RED → InfluxDB (lưu lịch sử)
                          ↓
                       MariaDB (lưu giá trị mới nhất)
                          ↓
                     Web SPA (index.html)
                          ↓
                     Grafana (xem biểu đồ)
                          ↓
                       Nginx (chạy web + proxy)

B1: Tạo cơ sở dữ liệu cho MariaDB + phpMyAdmin
1. chạy MariaDB và phpMyAdmin bằng Docker:

<img width="1518" height="360" alt="image" src="https://github.com/user-attachments/assets/ff247e58-2622-4def-9fe4-0a9e8740b18f" />

- Truy cập lại vào http:/localhost:8081 thì ra giao diện phpmyadmin sau đó đăng nhập vào

<img width="815" height="664" alt="image" src="https://github.com/user-attachments/assets/512a61de-6cc5-4499-b750-46a71525d850" />

- Đăng nhập thành công thì vào giao diện như sau:

 <img width="1916" height="983" alt="image" src="https://github.com/user-attachments/assets/c1c69ee5-4803-48c1-b1d4-2fafa7f461db" />

2. Tạo database và bảng trong phpMyAdmin

<img width="1006" height="344" alt="image" src="https://github.com/user-attachments/assets/d8d55f71-34b5-45d4-b0bb-b98f2d9787eb" />

Với tên db là iotdb , ta đến các bước tạo bảng lưu dữ liệu cảm biến trong tab SQL của iotdb

<img width="1447" height="715" alt="image" src="https://github.com/user-attachments/assets/27153512-9deb-4a4c-a091-1b1b752c40ed" />

- Sau đó iotdb sẽ xuất hiện 2 bảng ensors và users

<img width="1743" height="243" alt="image" src="https://github.com/user-attachments/assets/8bd60696-721e-4614-8538-9828e5673407" />

B2: Kết nối nodered với MariaDB để lưu dữ liệu cảm biến 
1. Vào node red và cài đặt thư viện node-red-node-mysql

<img width="949" height="467" alt="image" src="https://github.com/user-attachments/assets/619dd191-8dec-4337-afa6-65b44591a53e" />

2. Tạo các flow lưu dữ liệu

<img width="766" height="234" alt="image" src="https://github.com/user-attachments/assets/b0a30386-30ba-4486-8317-870e73f13d5d" />

- Cấu hình từng node

<img width="744" height="897" alt="image" src="https://github.com/user-attachments/assets/50a09120-d25d-4341-b8ea-444bb6d6721f" />
<img width="833" height="450" alt="image" src="https://github.com/user-attachments/assets/94c9b0dc-9abf-4db5-bd45-d5be5f0c9a1d" />
<img width="659" height="871" alt="image" src="https://github.com/user-attachments/assets/96523481-8bdc-4558-8296-5e09d662559c" />

- Deploy thì thấy hiện not yet conected , có nghĩa là nodered chưa được chung mạng với mariadb và phpmyadmin, chạy lệnh "docker network connect iot-net nodered" sau đó deploy lại
  
<img width="955" height="282" alt="image" src="https://github.com/user-attachments/assets/c77f6953-ea2f-4297-bc87-a621b502bd95" />

- Tiếp tục tạo thêm các bảng trong iotdb

<img width="1292" height="206" alt="image" src="https://github.com/user-attachments/assets/ff3fb488-7d68-4ab7-a059-df5a8fd667c2" />

- Tạo flow chính: Nodes: http in (POST /sensor), json, function (build influx payload + sql), influxdb out, mysql (execute msg.topic)

<img width="673" height="658" alt="image" src="https://github.com/user-attachments/assets/e32cee6e-839f-4186-b1de-91d3fd238482" />
<img width="813" height="860" alt="image" src="https://github.com/user-attachments/assets/86ede8ab-2d1b-476f-befb-f88b0df75346" />
<img width="671" height="902" alt="image" src="https://github.com/user-attachments/assets/4ffcf5b5-f90c-40b6-9644-9898acc1a569" />
<img width="663" height="919" alt="image" src="https://github.com/user-attachments/assets/c36b5818-28a4-4ddb-845c-c27aa1c2c18b" />
+ Cấu hình InfluxDB trong Docker:
<img width="1919" height="481" alt="image" src="https://github.com/user-attachments/assets/c0403b56-ff35-4c9b-8b44-e548ed82f22d" />

- Tạo Flow: Login API (/api/login): Nodes: http in POST /api/login → json → mysql SELECT → function compare → mysql insert session → function set cookie → http response.
  
<img width="1080" height="239" alt="image" src="https://github.com/user-attachments/assets/b3686fa2-79ba-43dd-bceb-e71a2a3c52be" />

+ Cấu hình từng node của flow
<img width="660" height="490" alt="image" src="https://github.com/user-attachments/assets/0a9dec58-94fa-4002-9267-7fa88bba2dad" />
<img width="826" height="692" alt="image" src="https://github.com/user-attachments/assets/b0628b9a-905a-4e2c-b30a-7cce7c0ba5b8" />
<img width="652" height="719" alt="image" src="https://github.com/user-attachments/assets/b54275ac-56a0-4a09-8e12-c60a3231c772" />
<img width="670" height="494" alt="image" src="https://github.com/user-attachments/assets/acd6cf5a-ecbd-4756-af75-9086f17a3677" />

- Tạo Flow 3 — /api/data (GET dữ liệu cảm biến) ,Frontend gọi API này để hiển thị bảng giá trị mới nhất.
<img width="636" height="431" alt="image" src="https://github.com/user-attachments/assets/fdc209af-139a-4372-8e76-796518d89702" />
<img width="826" height="547" alt="image" src="https://github.com/user-attachments/assets/91bae170-5db9-4ad4-a548-4dd23a79cff2" />
<img width="652" height="799" alt="image" src="https://github.com/user-attachments/assets/59819aa1-941a-49d3-bc23-ee1b93dff12d" />
 
 - Tạo flow 4( /api/logout)

<img width="941" height="146" alt="image" src="https://github.com/user-attachments/assets/905a9a3a-26ff-4b80-bcbb-2f7c1c754806" />

# :))))) Em xin lỗi thầy rất nhiều nhưng em mãi không chữa được lỗi 

5. Nginx làm web-server
 - Cấu hình nginx để chạy được website qua url http://fullname.com  (thay fullname bằng chuỗi ko dấu viết liền tên của bạn)
 - Cấu hình nginx để http://fullname.com/nodered truy cập vào nodered qua cổng 80, (dù nodered đang chạy ở port 1880)
 - Cấu hình nginx để http://fullname.com/grafana truy cập vào grafana qua cổng 80, (dù grafana đang chạy ở port 3000)
-----> 
<img width="810" height="437" alt="image" src="https://github.com/user-attachments/assets/d282d208-1f75-4a6b-ab35-7c84db61f394" />
Truy cập được bằng domain nguyenthithuhien.com
<img width="1429" height="593" alt="image" src="https://github.com/user-attachments/assets/f7ed6eac-d575-4afa-a7cd-84616a675664" />
- Thiết kế giao diện web tại file index.html trong thư mục www
<img width="1855" height="1029" alt="image" src="https://github.com/user-attachments/assets/faeed963-72d8-491c-892b-19d080834966" />

# em làm đến đây là không đăng nhập được vì em mắc ở nodered, em xin lỗi thầy , em đã cố hết sức :(((






