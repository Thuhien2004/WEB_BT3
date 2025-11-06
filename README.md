
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

b6: Em tạo domain riêng cho mình web3iot.com bằng các bước nhỏ:
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



























