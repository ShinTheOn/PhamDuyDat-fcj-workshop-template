---
title : "Cấu hình AWS SAM Pipeline"
date : 2026-07-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Tổng quan luồng tự động hóa AWS SAM CI/CD Pipeline

Trong phần này, chúng ta sẽ thực hiện xây dựng một hệ thống phân phối và triển khai tự động (Continuous Integration / Continuous Deployment - CI/CD) hoàn chỉnh cho ứng dụng Serverless sử dụng AWS SAM CLI Pipeline. Quy trình này giúp tự động hóa toàn bộ các công đoạn từ kiểm thử mã nguồn, đóng gói tài nguyên hạ tầng cho đến khi phân phối ứng dụng đến người dùng cuối.

Luồng kiến trúc hoạt động của CI/CD:
* Bước 1: Kho lưu trữ GitHub nhận sự kiện Git Push.
* Bước 2: AWS CodePipeline tự động kích hoạt giai đoạn Source để kéo code về.
* Bước 3: AWS CodePipeline chuyển sang giai đoạn UpdatePipeline để cập nhật cấu hình luồng.
* Bước 4: AWS CodeBuild kích hoạt công đoạn UnitTest thực thi kịch bản kiểm thử tự động.
* Bước 5: AWS CodeBuild tiến hành công đoạn BuildAndPackage để biên dịch gói dữ liệu backend.
* Bước 6: AWS CloudFormation tự động cập nhật các tài nguyên Serverless ngầm.

---

#### Các bước triển khai chi tiết

##### Bước 1: Khởi tạo và lưu trữ cấu hình môi trường bảo mật
1. Truy cập vào bảng điều khiển AWS Systems Manager > Chọn mục Parameter Store ở danh sách menu bên trái.
2. Bấm chọn Create parameter và tiến hành thiết lập thông số /prod/super-admin-email với kiểu dữ liệu là SecureString.
3. Bấm Create parameter để hoàn tất.

![Parameter Store thành công]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cb30346a-c85c-469b-848a-c12f1d74650f" />


##### Bước 2: Khởi tạo hạ tầng Pipeline cho môi trường Testing
1. Mở Terminal tại thư mục gốc chứa dự án mã nguồn của bạn trên máy tính.
2. Thực hiện chạy lệnh khởi tạo môi trường Testing bằng lệnh: sam pipeline bootstrap
3. Tiến hành thiết lập các thông số: Tên cấu hình là Testing, Region ap-southeast-1, chọn nhà cung cấp quyền mặc định IAM (default) và xác nhận tạo tài nguyên hạ tầng.

![Hoàn thành tạo tài nguyên Testing]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cc8d0aed-53e5-4494-bfbf-f2fd86c13d2c" />


##### Bước 3: Khởi tạo hạ tầng Pipeline cho môi trường Production (Prod)
1. Tại giao diện Terminal, tiếp tục thực hiện lệnh bootstrap lần thứ hai cho môi trường Prod bằng lệnh: sam pipeline bootstrap
2. Nhập tên cấu hình môi trường là Prod, chọn khu vực ap-southeast-1 và liên kết với thông tin Pipeline User đã tạo để hoàn tất.

![Hoàn thành tạo tài nguyên Prod]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ff65f777-b8a0-493c-856f-48c29c5d7786" />


##### Bước 4: Thiết lập kết nối mã nguồn an toàn CodeStar Connection
1. Điều hiểu đến bảng điều khiển AWS CodePipeline > Developer Tools > Chọn Connections.
2. Xác minh trạng thái hiển thị của cổng kết nối GitHub (Ví dụ: GameHub) phải báo trạng thái màu xanh lá cây Available.

![Cấu hình CodeStar Connection thành công]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/534c08d0-47c5-4b42-a89d-4b0f92a5d40c" />


##### Bước 5: Kiểm tra quá trình vận hành luồng tự động hóa Pipeline
1. Thực hiện lệnh Git đẩy mã nguồn từ máy local của bạn lên nhánh chính trên GitHub để kích hoạt chuỗi tiến trình tự động hóa bằng 3 lệnh liên tiếp:
git add .
git commit -m "deploy: trigger serverless sam pipeline workflow"
git push origin main
2. Truy cập vào giao diện quản lý của dịch vụ AWS CodePipeline, chọn luồng pipeline mang tên Gamehub-Pipeline để giám sát luồng thực thi tự động chạy qua đủ 4 giai đoạn: Source, UpdatePipeline, UnitTest, và BuildAndPackage.

![Luồng Gamehub-Pipeline chạy thành công]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/094c24c4-4f57-410b-8e22-cef2eaf8a5bf" />


##### Bước 6: Xác minh kết quả thực thi các công việc trong AWS CodeBuild
1. Di chuyển sang giao diện quản trị dịch vụ AWS CodeBuild > Chọn mục Build projects.
2. Giám sát trạng thái chi tiết của danh sách 4 dự án build thành phần. Tất cả các cột trạng thái chạy gần nhất (Latest build status) đều phải báo tích xanh hiển thị chữ Succeeded.

![Các project CodeBuild chạy thành công]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/04a3332a-4a5f-4f76-8dad-4897940ab8e2" />
