---
title : "Kết nối GitHub với AWS CodePipeline"
date: 2026-07-12
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Mục tiêu

Phần này hướng dẫn bạn thiết lập kết nối giữa AWS CodePipeline và GitHub thông qua AWS CodeConnections, để pipeline có thể tự động lấy mã nguồn từ repository và tiến hành deployment.

#### Bước 5: Kết nối AWS CodePipeline với GitHub (AWS CodeConnections)

Để pipeline có thể tự động lấy code từ GitHub về deploy, bạn cần tạo một kết nối bảo mật giữa AWS và tài khoản GitHub của mình.

##### 5.1. Khởi tạo kết nối trên AWS

![Ảnh 1](/images/5-Workshop/5.7-CodeConnections/anh1.png)

1. Trên thanh điều hướng bên trái của AWS Console, truy cập vào `Developer Tools` → `Settings` → `Connections`.
2. Tại giao diện chính, nhấn nút `Create connection`.

##### 5.2. Thiết lập thông tin nhà cung cấp

![Ảnh 2](/images/5-Workshop/5.7-CodeConnections/anh2.png)

1. `Select a provider`: chọn `GitHub`.
2. `Connection name`: nhập tên cho kết nối này, ví dụ `GameHub`.
3. Nhấn nút `Connect to GitHub`.

##### 5.3. Xác thực và cấp quyền trên GitHub

![Ảnh 3](/images/5-Workshop/5.7-CodeConnections/anh3.png)

1. Trình duyệt sẽ tự động chuyển hướng sang trang xác thực của GitHub.
2. Kiểm tra kỹ tài khoản GitHub đang đăng nhập.
3. Nhập mật khẩu hoặc xác thực nếu GitHub yêu cầu.
4. Nhấn `Confirm` để cho phép AWS truy cập repository của bạn.

##### 5.4. Kiểm tra trạng thái hoàn tất

![Ảnh 4](/images/5-Workshop/5.7-CodeConnections/anh4.png)

1. Sau khi xác thực thành công, bạn sẽ được quay trở lại giao diện AWS và thấy thông báo màu xanh: `Connection GameHub created successfully`.
2. Hãy kiểm tra mục `Status`. Nếu hiển thị màu xanh lá và là `Available`, nghĩa là kết nối đã sẵn sàng hoạt động.

#### Kết quả mong đợi

Sau khi hoàn tất bước này, bạn đã có một kết nối an toàn giữa AWS và GitHub, đủ điều kiện để CodePipeline tự động lấy source code và triển khai ứng dụng.

#### Lưu ý quan trọng

- Nên đặt tên kết nối ngắn gọn và dễ nhận diện, ví dụ `GameHub`.
- Nếu trạng thái kết nối chưa chuyển sang `Available`, hãy chờ vài phút rồi kiểm tra lại.

