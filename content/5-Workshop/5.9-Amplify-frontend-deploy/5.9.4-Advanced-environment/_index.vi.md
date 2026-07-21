---
title : "Bước 4: Thiết lập Nâng cao và Biến Môi trường"
date: 2026-07-12
weight : 4
chapter : false
pre : " <b> 5.9.4. </b> "
---

#### Mục tiêu

Trong bước này, bạn sẽ mở các tùy chọn nâng cao của Amplify và thêm các biến môi trường cần thiết cho quá trình build frontend.

#### Hướng dẫn

![alt text](image.png)

1. Cuộn xuống và mở rộng mục `Advanced settings`.
2. Các tùy chọn như `Build instance type`, `Build image` hoặc `Cache key` là tùy chọn, bạn có thể giữ mặc định hoặc chỉnh phù hợp.
3. Trong phần `Environment variables`, nhấn `Add new` để thêm các biến môi trường cần thiết.
4. Đảm bảo các biến như `COGNITO_REGION`, `COGNITO_USER_POOL_ID`, `API_GATEWAY_HTTP_URL` và các biến tương tự đã được thêm đầy đủ.

#### Lưu ý

Các biến môi trường này phải khớp với những biến được gọi trong file `amplify.yml` để build thành công.
