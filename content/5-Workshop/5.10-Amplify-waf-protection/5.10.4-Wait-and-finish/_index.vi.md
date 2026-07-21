---
title : "Bước 4: Chờ hệ thống liên kết và hoàn tất"
date: 2026-07-12
weight : 4
chapter : false
pre : " <b> 5.10.4. </b> "
---

#### Mục tiêu

Trong bước này, bạn sẽ chờ AWS hoàn tất việc liên kết WAF với ứng dụng Amplify và kiểm tra trạng thái sau khi kích hoạt.

#### Hướng dẫn

![alt text](image.png)

1. Sau khi nhấn `Add firewall`, hệ thống sẽ quay về trang quản lý Firewall.
2. Ở mục `Web Application Firewall`, trạng thái ban đầu có thể là `Associating`.
3. Quá trình này mất vài phút để AWS khởi tạo và áp dụng quy tắc bảo mật.
4. Khi hoàn tất, bạn có thể chọn `View WAF logs` để xem lưu lượng truy cập được cho phép hoặc bị chặn.

#### Kết quả mong đợi

Sau khi hoàn tất, ứng dụng của bạn sẽ được bảo vệ bởi AWS WAF và sẵn sàng theo dõi các hoạt động truy cập một cách hiệu quả.
