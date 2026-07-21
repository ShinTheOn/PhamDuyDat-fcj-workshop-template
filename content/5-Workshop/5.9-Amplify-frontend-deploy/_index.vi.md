---
title : "Triển khai Frontend trên AWS Amplify"
date: 2026-07-12
weight : 9
chapter : false
pre : " <b> 5.9. </b> "
---

#### Mục tiêu

Trong phần này, bạn sẽ triển khai frontend của ứng dụng GameHub lên AWS Amplify bằng cách kết nối repository GitHub, cấu hình build cho Flutter Web và thiết lập biến môi trường cần thiết.

#### Tổng quan

AWS Amplify là dịch vụ phù hợp để host ứng dụng frontend tĩnh hoặc SPA như Flutter Web. Sau khi hoàn tất các bước dưới đây, frontend sẽ được tự động build và deploy mỗi khi có thay đổi trên nhánh Git được chọn.

#### Cấu trúc nội dung

- Bước 1: Khởi tạo ứng dụng trên AWS Amplify
- Bước 2: Liên kết repository và nhánh
- Bước 3: Cấu hình app settings và file amplify.yml
- Bước 4: Thiết lập nâng cao và biến môi trường
- Bước 5: Kiểm tra và triển khai

