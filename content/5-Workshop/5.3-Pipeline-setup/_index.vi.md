---
title : "Khởi tạo Pipeline CI/CD"
date: 2026-07-12
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Mục tiêu

Trong phần này, bạn sẽ khởi tạo cấu hình pipeline ban đầu cho backend GameHub bằng AWS SAM và AWS CodePipeline. Bước này tạo nền tảng cho quy trình build, deploy và quản lý môi trường Dev/Prod trong workshop.

#### Bước 1: Khởi tạo Pipeline

1. Mở Terminal tại thư mục gốc của dự án.
2. Chạy lệnh sau để bắt đầu quá trình khởi tạo pipeline:
```bash
sam pipeline init --bootstrap
```
3. Khi hệ thống hiện các câu hỏi, hãy chọn các tùy chọn sau:
- `Select a pipeline template`: chọn `1` (AWS Quick Start Pipeline Templates)
- `Select CI/CD system`: chọn `5` (AWS CodePipeline)
- `Which pipeline template would you like to use?`: chọn `2` (Two-stage pipeline)
- `Do you want to go through stage setup process now?`: nhập `y` (Yes)

> Note: Bước này sẽ tạo cấu hình pipeline ban đầu, bao gồm các file template và các tài nguyên bootstrap cần thiết để triển khai ứng dụng trên AWS.

#### Bước 2: Cấu hình Stage Dev

Sau khi chọn `y`, AWS SAM sẽ bắt đầu thiết lập stage đầu tiên cho môi trường phát triển.

1. `Stage configuration name`: nhập `dev`
2. `Select a credential source`: chọn `2` (default named profile)
3. `Enter the region`: nhập `ap-southeast-1` hoặc khu vực AWS bạn đang dùng
4. Nếu được hỏi về profile, nhập `gamehub`
5. Khi gặp các câu hỏi về ARN, IAM role, artifact bucket hoặc các tài nguyên liên quan, hãy nhấn `Enter` để SAM tự tạo giá trị mặc định
6. `Does your application contain any IMAGE type Lambda functions?`: nhập `n`

> Note: Nếu bạn chưa chắc chắn về thông tin cần nhập, hãy chọn giá trị mặc định bằng cách nhấn Enter để tiến trình tiếp tục.

#### Bước 3: Cấu hình Stage Prod

Sau khi stage Dev được hoàn tất, hệ thống sẽ tiếp tục hỗ trợ bạn cấu hình stage thứ hai cho môi trường production.

1. `Stage configuration name`: nhập `prod`
2. `Select a credential source`: chọn cách tương tự như ở stage Dev
3. `Enter the region`: chọn cùng region với Dev hoặc region khác nếu bạn muốn tách môi trường vận hành

#### Bước 4: Kiểm tra kết quả khởi tạo

Sau khi quy trình hoàn tất, hãy kiểm tra thư mục pipeline bằng lệnh sau:
```bash
ls pipeline
```

Bạn nên thấy các file quan trọng sau:
- `pipeline/samconfig.toml`
- `pipeline/codepipeline.yaml`
- `buildspec_deploy.yml`

#### Kết quả mong đợi

- Pipeline đã được khởi tạo thành công bằng AWS SAM.
- Các file cấu hình pipeline đã xuất hiện trong thư mục `pipeline`.
- Bạn đã sẵn sàng cho các bước cấu hình tiếp theo như liên kết GitHub, thiết lập stage và triển khai ứng dụng.

#### Ghi chú

- `sam pipeline init --bootstrap` sẽ tạo các tài nguyên bootstrap như S3 artifact bucket.
- `samconfig.toml` lưu trữ thông tin về stage, profile và cấu hình triển khai.
- Bạn có thể chỉnh sửa file này sau khi khởi tạo nếu cần tùy chỉnh cho môi trường của mình.

![Ảnh 1](/images/5-Workshop/5.3-Pipeline-setup/anh1.png)

![Ảnh 2](/images/5-Workshop/5.3-Pipeline-setup/anh2.png)

