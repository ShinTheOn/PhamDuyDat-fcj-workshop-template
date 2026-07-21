---
title : "Cấu hình Stage Dev"
date: 2026-07-12
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

#### Mục tiêu

Phần này hướng dẫn bạn thiết lập chi tiết môi trường Development cho pipeline SAM, bao gồm tên stage, nguồn xác thực, vùng AWS và các giá trị mặc định mà AWS SAM có thể tự tạo.

#### Bước 1: Nhập thông tin cho Stage Dev

Khi hệ thống hỏi về môi trường Development, hãy thực hiện theo các lựa chọn sau:

1. `Stage configuration name`: nhập `dev`
2. `Select a credential source`: chọn `2` (default named profile)
3. `Enter the region`: nhập mã vùng AWS của bạn, ví dụ `ap-southeast-1`
4. Nếu được hỏi về profile, hãy nhập `gamehub` nếu bạn đã cấu hình trước đó
5. Khi hệ thống yêu cầu điền các giá trị như ARN, IAM user, execution role, artifact bucket, hãy nhấn `Enter` để bỏ qua. AWS SAM sẽ tự tạo các tài nguyên này cho bạn
6. `Does your application contain any IMAGE type Lambda functions?`: nhập `n` (No)

> Note: Đây là bước rất quan trọng vì stage Dev là môi trường đầu tiên để kiểm thử và triển khai nhanh trước khi chuyển sang môi trường Prod.

#### Bước 2: Ý nghĩa của các lựa chọn

- `Stage configuration name = dev`: giúp phân biệt môi trường phát triển với môi trường production.
- `default named profile`: cho phép SAM sử dụng profile AWS đã cấu hình trước đó trên máy của bạn.
- `Enter the region`: cần khớp với vùng AWS bạn đang dùng để tránh lỗi khi tạo stack hoặc bucket.
- Nhấn `Enter` cho các thông tin ARN/role/bucket: giúp SAM tự khởi tạo các tài nguyên bootstrap một cách thuận tiện.
- Chọn `n` cho IMAGE type Lambda: phù hợp với hầu hết các ứng dụng không dùng container image Lambda.

#### Bước 3: Kiểm tra lại trước khi tiếp tục

Sau khi hoàn tất nhập thông tin, hãy kiểm tra lại các mục sau:
- Tên stage đã là `dev`
- Region đã đúng với môi trường AWS của bạn
- Profile AWS đã được xác nhận hoạt động
- Không có lỗi về quyền truy cập hoặc cấu hình IAM

#### Kết quả mong đợi

Sau khi thiết lập xong, bạn đã sẵn sàng cho bước tiếp theo trong quy trình pipeline, trong đó stage Dev sẽ được dùng làm môi trường triển khai ban đầu.

![Ảnh 1](/images/5-Workshop/5.4-Stage-setup/anh1.png)

