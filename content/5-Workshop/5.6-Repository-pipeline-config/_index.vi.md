---
title : "Kết nối GitHub với AWS CodePipeline"
date: 2026-07-12
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Mục tiêu

Phần này hướng dẫn bạn thiết lập kết nối giữa AWS CodePipeline và GitHub thông qua AWS CodeConnections, để pipeline có thể tự động lấy source code từ repository và tiến hành deployment.

#### Bước 5: Kết nối AWS CodePipeline với GitHub (AWS CodeConnections)

Để pipeline có thể tự động lấy code từ GitHub về deploy, bạn cần tạo một kết nối bảo mật giữa AWS và tài khoản GitHub của mình.

##### 5.1. Khởi tạo kết nối trên AWS

1. Trên thanh điều hướng bên trái của AWS Console, truy cập vào `Developer Tools` → `Settings` → `Connections`.
2. Tại giao diện chính, nhấn nút `Create connection`.
3. Hệ thống sẽ hiển thị một số lựa chọn nhà cung cấp. Bạn cần chọn `GitHub` làm nền tảng kết nối.

> Note: Bước này rất quan trọng vì nếu kết nối chưa được tạo đúng, CodePipeline sẽ không thể truy cập repository GitHub để lấy source code.

##### 5.2. Thiết lập thông tin nhà cung cấp

1. `Select a provider`: chọn `GitHub`.
2. `Connection name`: nhập tên cho kết nối, ví dụ `GameHub`.
3. Nhấn nút `Connect to GitHub` để bắt đầu quá trình xác thực.

> Note: Nên dùng tên ngắn gọn và dễ nhận diện như `GameHub`, `GameHub-Conn` hoặc tên dự án của bạn để dễ quản lý sau này.

##### 5.3. Xác thực và cấp quyền trên GitHub

1. Trình duyệt sẽ tự động chuyển hướng sang trang xác thực của GitHub.
2. Hãy kiểm tra kỹ tài khoản GitHub đang đăng nhập trước khi tiếp tục.
3. Nhập mật khẩu hoặc xác thực 2 bước nếu GitHub yêu cầu.
4. Nhấn `Confirm` để cho phép AWS truy cập repository của bạn.

> Note: Nếu bạn có nhiều tài khoản GitHub hoặc tổ chức, hãy đảm bảo chọn đúng tài khoản và tổ chức có quyền truy cập repository cần deploy.

##### 5.4. Kiểm tra trạng thái hoàn tất

1. Sau khi xác thực thành công, bạn sẽ được quay trở lại AWS Console và thấy thông báo màu xanh: `Connection GameHub created successfully`.
2. Truy cập lại mục `Connections` để kiểm tra trạng thái.
3. Nếu mục `Status` hiển thị màu xanh lá và là `Available`, nghĩa là kết nối đã sẵn sàng để sử dụng trong pipeline.

#### Kết quả mong đợi

Sau khi hoàn tất bước này, bạn đã có một kết nối an toàn giữa AWS và GitHub, đủ điều kiện để CodePipeline tự động lấy code từ repository về triển khai.

#### Lưu ý quan trọng

- Hãy lưu lại tên kết nối và ARN nếu cần dùng lại cho các bước cấu hình pipeline tiếp theo.
- Nếu trạng thái kết nối chưa chuyển sang `Available`, hãy chờ một vài phút rồi kiểm tra lại.





