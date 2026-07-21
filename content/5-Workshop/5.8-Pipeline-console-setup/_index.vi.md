---
title : "Khởi tạo Pipeline trên AWS Console"
date: 2026-07-12
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

#### Mục tiêu

Trong phần này, bạn sẽ tiếp tục thiết lập quy trình triển khai bằng cách tạo một pipeline mới trên AWS Console, sử dụng template CloudFormation và kết nối với repository GitHub đã thiết lập trước đó.

#### Bước 6: Khởi tạo và cấu hình CodePipeline trên AWS Console

Sau khi kết nối GitHub đã sẵn sàng, bạn có thể tạo pipeline trực tiếp từ giao diện AWS Console để tự động hóa quy trình build và deploy.

![Ảnh 1](/images/5-Workshop/5.8-Pipeline-console-setup/anh1.png)

##### 1. Chọn loại hình và template deployment

![Ảnh 2](/images/5-Workshop/5.8-Pipeline-console-setup/anh2.png)

1. Trên thanh điều hướng bên trái, truy cập vào `Developer Tools` → `CodePipeline` → `Pipelines`.
2. Nhấn nút `Create pipeline`.
3. Tại trang cấu hình ban đầu:
   - `Category`: chọn `Deployment`.
   - `Template`: chọn thẻ `Deploy to CloudFormation (Deploy your cloud formation template)`.
4. Nhấn `Next` để tiếp tục.

##### 2. Thiết lập nguồn cấp code (Source)

![Ảnh 3](/images/5-Workshop/5.8-Pipeline-console-setup/anh3.png)

Tiến hành liên kết repository GitHub mà bạn đã kết nối trước đó:

1. `Source provider`: chọn `GitHub (via GitHub App)`.
2. `Connection`: chọn đúng kết nối GitHub đã tạo ở bước trước.
3. `Repository name`: chọn repository phù hợp của dự án, ví dụ `DTDuc04/DoAnMiniGame`.
4. `Default branch`: nhập tên nhánh dùng để kích hoạt deploy tự động, ví dụ `V1`.
5. `Output artifact format`: giữ mặc định là `CodePipeline default`.
6. Nhấn `Next`.

##### 3. Cấu hình chi tiết thông số template

![Ảnh 4](/images/5-Workshop/5.8-Pipeline-console-setup/anh4.png)

Điền các thông tin nhận diện cho pipeline và stack:

1. `CodePipelineName`: đặt tên cho pipeline, ví dụ `DeployToCloudFormationService`.
2. `StackName`: nhập tên CloudFormation Stack, ví dụ `GameHub`.
3. `TemplatePath`: nhập đường dẫn tới file YAML cấu hình trong repository, ví dụ `backend/codepipeline.yaml`.
4. `OutputFileName`: đặt tên file đầu ra, ví dụ `output.json`.

##### 4. Phân quyền và hoàn tất khởi tạo

![Ảnh 5](/images/5-Workshop/5.8-Pipeline-console-setup/anh5.png)

1. Cuộn xuống mục `CloudFormationResourcePermissions` để xem các quyền mặc định được cấp cho CloudFormation.
2. `RetentionPolicy`: chọn hành vi khi stack bị xóa, ví dụ `Delete`.
3. Kiểm tra lại toàn bộ thông tin trong mục `Preview`.
4. Nhấn `Create pipeline from template` ở góc dưới cùng bên phải.

#### Kết quả mong đợi

Sau khi tạo xong, CodePipeline sẽ tự động chạy quy trình build và deploy mỗi khi có thay đổi code được push lên nhánh `V1` trên GitHub.

#### Lưu ý quan trọng

- Hãy đảm bảo repository name và branch name đúng với dự án thật của bạn.
- Nếu pipeline chưa chạy ngay lập tức, hãy đợi vài phút để AWS hoàn tất quá trình khởi tạo.

